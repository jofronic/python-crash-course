#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd


def money_to_float(value) -> float:
    if pd.isna(value):
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip()
    if not s:
        return 0.0
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg = True
        s = s[1:-1]
    s = s.replace("$", "").replace(",", "").strip()
    try:
        num = float(s)
    except ValueError:
        return 0.0
    return -num if neg else num


def normalize_text(value: str) -> str:
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def parse_dates(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce")


def build_reference_key(source_file: str, row_num_1_based: int) -> str:
    return f"{source_file}:row {row_num_1_based}"


def detect_transfer(description: str) -> str:
    desc = description.upper()
    transfer_terms = [
        "TRANSFER", "XFER", "ALLOTMENT", "ZELLE", "VENMO", "CASH APP",
        "PAYPAL *TRANSFER", "FROM SAVINGS", "TO SAVINGS", "ACH CREDIT",
        "ACH DEBIT", "ONLINE TRANSFER", "INTERNAL TRANSFER", "INST XFER"
    ]
    return "Y" if any(term in desc for term in transfer_terms) else "N"


def classify_scope(account: str) -> str:
    mapping = {
        "Axos": "Business_SoleProp",
        "Novo": "Business_Partnership",
        "USAA": "Personal",
        "Chase": "Personal",
        "Navy Federal": "Personal",
    }
    return mapping.get(account, "Review")


def classify_transaction(description: str, account: str):
    desc = description.upper()

    if detect_transfer(description) == "Y":
        return ("Transfer", "Internal Transfer", "Non-taxable transfer", "Transfer")

    if "DFAS-CLEVELANDPPD" in desc or "ALLOTMENT" in desc:
        return ("Transfer", "Owner Contribution", "Owner contribution", "Transfer")

    if any(term in desc for term in ["DISTROKID", "STRIPE", "PAYPAL", "SQUARE INC", "SQ *"]):
        if account in {"Axos", "Novo"}:
            return ("Business Income", "Client / Platform Receipt", "Schedule C income review", "Business Income")

    if "GOOGLE *WORKSPACE" in desc or "WORKSPACE" in desc:
        return ("Business Expense", "Business Email / Productivity", "Schedule C expense", "Office / Software")
    if "GOOGLE ONE" in desc:
        return ("Business Expense", "Cloud Storage", "Schedule C expense", "Office / Software")
    if re.search(r"\bGOOGLE\b", desc):
        return ("Business Expense", "Google Service", "Schedule C expense", "Office / Software")
    if "AMAZON WEB SERVICES" in desc or "AWS" in desc:
        return ("Business Expense", "Cloud Computing", "Schedule C expense", "Office / Software")
    if "ADOBE" in desc:
        return ("Business Expense", "Creative Software", "Schedule C expense", "Office / Software")
    if "CANVA" in desc:
        return ("Business Expense", "Design Software", "Schedule C expense", "Office / Software")
    if "DROPBOX" in desc:
        return ("Business Expense", "Cloud Storage", "Schedule C expense", "Office / Software")
    if "SPREAKER" in desc:
        return ("Business Expense", "Podcast Hosting", "Schedule C expense", "Office / Software")
    if "GODADDY" in desc or "SQUARESPACE" in desc or "BLUEHOST" in desc:
        return ("Business Expense", "Hosting / Domain", "Schedule C expense", "Office / Software")

    if "TUTORIALS DOJO" in desc or "UDEMY" in desc:
        return ("Business Expense", "Professional Education", "Schedule C expense", "Education")

    if "GOOGLE *FI" in desc or "GOOGLE FI" in desc:
        return ("Business Expense", "Phone", "Schedule C expense", "Utilities")
    if "VERIZON" in desc:
        return ("Business Expense", "Internet / Phone", "Schedule C expense", "Utilities")

    if "UBER" in desc or "LYFT" in desc:
        return ("Transportation", "Rideshare", "Personal", "Transportation")
    if any(term in desc for term in ["WHOLEFDS", "WHOLE FOODS", "TRADER JOE", "STOP & SHOP", "TARGET", "AMAZON MKT", "AMAZON.COM"]):
        return ("Personal Expense", "Shopping / Groceries", "Personal", "Shopping")
    if "MORTGAGE" in desc or "MT BANK" in desc or "M&T" in desc:
        return ("Housing", "Mortgage", "Personal", "Housing")

    if account in {"Axos", "Novo"}:
        return ("Business Expense", "Other Business Expense", "Review", "Other Business")
    return ("Personal Expense", "Uncategorized", "Review", "Miscellaneous")


def parse_usaa(path: Path, year: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["TxnDate"] = parse_dates(df["Date"])
    df = df[df["TxnDate"].dt.year == year].copy()
    if df.empty:
        return pd.DataFrame()
    df["Amount"] = df["Amount"].apply(money_to_float)
    df["Description"] = df["Description"].apply(normalize_text)
    return pd.DataFrame({
        "TxnDate": df["TxnDate"].dt.date.astype(str),
        "Month": df["TxnDate"].dt.strftime("%Y-%m"),
        "Account": "USAA",
        "Bank": "USAA",
        "Description": df["Description"],
        "Amount": df["Amount"],
        "BankCategory": df.get("Category", "").astype(str),
        "SourceFile": path.name,
        "SourceRow": df.index + 2,
    })


def parse_chase(path: Path, year: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["TxnDate"] = parse_dates(df["Posting Date"])
    df = df[df["TxnDate"].dt.year == year].copy()
    if df.empty:
        return pd.DataFrame()
    df["Amount"] = df["Amount"].apply(money_to_float)
    df["Description"] = df["Description"].apply(normalize_text)
    return pd.DataFrame({
        "TxnDate": df["TxnDate"].dt.date.astype(str),
        "Month": df["TxnDate"].dt.strftime("%Y-%m"),
        "Account": "Chase",
        "Bank": "Chase",
        "Description": df["Description"],
        "Amount": df["Amount"],
        "BankCategory": df.get("Type", "").astype(str),
        "SourceFile": path.name,
        "SourceRow": df.index + 2,
    })


def parse_navy_federal(path: Path, year: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["TxnDate"] = parse_dates(df["Posting Date"])
    df = df[df["TxnDate"].dt.year == year].copy()
    if df.empty:
        return pd.DataFrame()
    df["Amount"] = df["Amount"].apply(money_to_float)
    indicator = df["Credit Debit Indicator"].astype(str).str.upper()
    debit_mask = indicator.str.contains("DEBIT", na=False)
    credit_mask = indicator.str.contains("CREDIT", na=False)
    df.loc[debit_mask, "Amount"] = -df.loc[debit_mask, "Amount"].abs()
    df.loc[credit_mask, "Amount"] = df.loc[credit_mask, "Amount"].abs()
    desc_col = "Reference" if "Reference" in df.columns else df.columns[0]
    df["Description"] = df[desc_col].apply(normalize_text)
    return pd.DataFrame({
        "TxnDate": df["TxnDate"].dt.date.astype(str),
        "Month": df["TxnDate"].dt.strftime("%Y-%m"),
        "Account": "Navy Federal",
        "Bank": "Navy Federal",
        "Description": df["Description"],
        "Amount": df["Amount"],
        "BankCategory": df.get("type", "").astype(str),
        "SourceFile": path.name,
        "SourceRow": df.index + 2,
    })


def parse_axos(path: Path, year: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    df["TxnDate"] = parse_dates(df["Date"])
    df = df[df["TxnDate"].dt.year == year].copy()
    if df.empty:
        return pd.DataFrame()
    df["Amount Debit"] = df.get("Amount Debit", 0).apply(money_to_float)
    df["Amount Credit"] = df.get("Amount Credit", 0).apply(money_to_float)
    df["Amount"] = df["Amount Credit"] - df["Amount Debit"]
    df["Description"] = df["Description"].apply(normalize_text)
    return pd.DataFrame({
        "TxnDate": df["TxnDate"].dt.date.astype(str),
        "Month": df["TxnDate"].dt.strftime("%Y-%m"),
        "Account": "Axos",
        "Bank": "Axos",
        "Description": df["Description"],
        "Amount": df["Amount"],
        "BankCategory": df.get("Transaction Type", "").astype(str),
        "SourceFile": path.name,
        "SourceRow": df.index + 2,
    })


def parse_novo(path: Path, year: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    df["TxnDate"] = parse_dates(df["Date"])
    df = df[df["TxnDate"].dt.year == year].copy()
    if df.empty:
        return pd.DataFrame()
    df["Amount"] = df["Amount"].apply(money_to_float)
    df["Description"] = df["Description"].apply(normalize_text)
    return pd.DataFrame({
        "TxnDate": df["TxnDate"].dt.date.astype(str),
        "Month": df["TxnDate"].dt.strftime("%Y-%m"),
        "Account": "Novo",
        "Bank": "Novo",
        "Description": df["Description"],
        "Amount": df["Amount"],
        "BankCategory": df.get("Category", "").astype(str),
        "SourceFile": path.name,
        "SourceRow": df.index + 2,
    })


def dedupe_chase_union(df: pd.DataFrame) -> pd.DataFrame:
    chase = df[df["Account"] == "Chase"].copy()
    other = df[df["Account"] != "Chase"].copy()
    if chase.empty:
        return df
    chase["DedupKey"] = (
        chase["TxnDate"].astype(str) + "|" +
        chase["Description"].astype(str).str.upper() + "|" +
        chase["Amount"].round(2).astype(str)
    )
    chase = chase.drop_duplicates(subset=["DedupKey"]).drop(columns=["DedupKey"])
    return pd.concat([other, chase], ignore_index=True)


def enrich(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["FlowDirection"] = df["Amount"].apply(lambda x: "Income" if x > 0 else "Expense")
    df["TransferFlag"] = df["Description"].apply(detect_transfer)
    df["Scope"] = df["Account"].apply(classify_scope)
    classified = df.apply(lambda r: classify_transaction(r["Description"], r["Account"]), axis=1, result_type="expand")
    classified.columns = ["MasterCategory", "Subcategory", "TaxLabel", "BudgetCategory"]
    df = pd.concat([df, classified], axis=1)
    df["ReferenceKey"] = df.apply(lambda r: build_reference_key(r["SourceFile"], int(r["SourceRow"])), axis=1)
    return df


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    grp = df.groupby("Account", dropna=False)["Amount"].agg(
        money_in=lambda s: s[s > 0].sum(),
        money_out=lambda s: -s[s < 0].sum(),
        net="sum",
        rows="count",
    ).reset_index()
    return grp.sort_values("Account")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--year", type=int, default=2025)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_frames = []
    for path in sorted(input_dir.iterdir()):
        name = path.name.lower()
        try:
            if name.startswith("usaa") and path.suffix.lower() == ".csv":
                all_frames.append(parse_usaa(path, args.year))
            elif name.startswith("chase") and path.suffix.lower() == ".csv":
                all_frames.append(parse_chase(path, args.year))
            elif "navy_federal" in name and path.suffix.lower() == ".csv":
                all_frames.append(parse_navy_federal(path, args.year))
            elif name.startswith("axos") and path.suffix.lower() == ".csv":
                all_frames.append(parse_axos(path, args.year))
            elif name.startswith("novo_") and path.suffix.lower() == ".csv":
                all_frames.append(parse_novo(path, args.year))
        except Exception as exc:
            print(f"Skipped {path.name}: {exc}")

    frames = [f for f in all_frames if not f.empty]
    if not frames:
        raise SystemExit("No supported files found.")

    combined = pd.concat(frames, ignore_index=True)
    combined = dedupe_chase_union(combined)
    combined = enrich(combined)
    combined["TxnDate_dt"] = pd.to_datetime(combined["TxnDate"], errors="coerce")
    combined = combined.sort_values(["TxnDate_dt", "Account", "Description", "Amount"]).drop(columns=["TxnDate_dt"])

    transactions_path = output_dir / f"transactions_{args.year}_clean.csv"
    summary_path = output_dir / f"account_summary_{args.year}.csv"
    combined.to_csv(transactions_path, index=False)
    summarize(combined).to_csv(summary_path, index=False)

    print(f"Wrote: {transactions_path}")
    print(f"Wrote: {summary_path}")


if __name__ == "__main__":
    main()
