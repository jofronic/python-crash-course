def make_shirt(text, size='large'):
    """This function summarize the size and words on the shirts"""
    print(f"The size of this shirt is {size.title()} and they wrote on it '{text.capitalize()}'.")
make_shirt('I love Python')
make_shirt(size='medium', text='i love Python')
make_shirt(size='small', text='i love Python')