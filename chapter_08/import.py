import greeters


while True:
    print("\nPlease tell me your name:")
    print("Press q to quit at any time")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")   
    if l_name == 'q':
        break
    formatted_name = greeters.get_formatted_name(f_name, l_name)

print(f"\nHello, {formatted_name}")

from greeters import get_formatted_name


while True:
    print("\nPlease tell me your name:")
    print("Press q to quit at any time")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")   
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)

print(f"\nHello, {formatted_name}")

from greeters import get_formatted_name as gff


while True:
    print("\nPlease tell me your name:")
    print("Press q to quit at any time")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")   
    if l_name == 'q':
        break
    formatted_name = gff(f_name, l_name)

print(f"\nHello, {formatted_name}")

import greeters as fn


while True:
    print("\nPlease tell me your name:")
    print("Press q to quit at any time")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")   
    if l_name == 'q':
        break
    formatted_name = fn.get_formatted_name(f_name, l_name)

print(f"\nHello, {formatted_name}")

from greeters import *


while True:
    print("\nPlease tell me your name:")
    print("Press q to quit at any time")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")   
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)

print(f"\nHello, {formatted_name}")