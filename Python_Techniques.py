        # DONT' RUN THE FILE, BECAUSE IT WILL GIVE YOU AN ERROR
        # Or if you correct it, you will need a powerplant to run this file

"""
OWNER - CREATED AND MODIFIED BY ROLAND MÁRTON 
"""

'''
##################################### BOOKMARK ###################################
1) Shutil funkció - Ha középre igazítani akarsz dolgokat akkor lehet ezt csinálni
2) Window kompatibilis terminál törlés 
3) Weblink importálása
4) Időkésleltetés beállítása
5) Quit function
6) Sys, ha azt akarjuk például hogy lépjen ki a terminál 
7) How to split a file into a list in Python
8) Playsound telepítés
9) Custom welcome message
10) AI random választ egyet a táblán
11) Enumerate használata
12) Merging two dictionaries 
13) Zip használata
14) Random generátorok 
15) Print akármekkora board, koordináta kereső, set_random_letter 
16) Game Inventory 
17) Kép megnyitás 
18) Színkódok használata
19) format function
20) Dictionary functions
21) String module, ascii_upper/lowercase, abc betűi
22) Regular expressions - validátor példa, move validátor
23) Dedent használata, leading whitespace levágása each line
24) Table print (for ERP for example)
25) Timed printing
26) Str-ből lista
27) Random szám lista generátor list comphrenesionnal
28) Creating Dicts with lists and for loop
29) random randint vs randrange difference & random.choices()
30) end parameter in print
31) How to make a list of keys from a dictionary
32) Arguments in functions (Positional,Default, Variable length etc)
33) Difference between list() and split() (str --> list) & list --> str with join
34) List creation problem with range, how range creates for example (0,5) or (1,6)
35) Creating dict from a sentence, and check how many letters does it have. How many A, how many B etc
36) Dictionary key sorting

#################################################################################

                                DATA STRUCTURE CHANGES
1) str --> list
2) list --> str
3) integer --> list_of_integer
4) list_of_integer --> integer
5) list_of_str --> list_of_int
6) list_of_int --> list_of_str
7) From 2 lists to dictionary
'''


# 1) Shutil funkció - Ha középre igazítani akarsz dolgokat akkor lehet ezt csinálni
import shutil
import subprocess


def middle():
    return shutil.get_terminal_size().columns

print("Mi a neved te vadállat?".center(middle()))
input(" " * (int(middle() / 2)))

"------------------------------------------------------------"
# 2) Window kompatibilis terminál törlés 

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

"------------------------------------------------------------"
# 3) Weblink importálása

import webbrowser            

webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

"------------------------------------------------------------"
# 4) Időkésleltetés beállítása

import time

time.sleep(5)

"------------------------------------------------------------"
# 5) Quit function

"quit()"

"------------------------------------------------------------"
# 6) Sys, ha azt akarjuk például hogy lépjen ki a terminál 

import sys

"sys.exit()"

# Mikor meghívjuk a python cmp.py 1 2 3 4 -t a terminálban az egy listát csinál
print("This is the name of the program:", sys.argv[0])  # >>> cmp.py
  
print("Argument List:", str(sys.argv))  # >>> ['cmp.py', '1', '2', '3', '4']

print("Number of elements including the name of the program:",  # >>> 5
       len(sys.argv))
print("Number of elements excluding the name of the program:",  # >>> 4
      (len(sys.argv)-1))

##############################
add = 0.0
  
# Getting the length of command # python3 add.py 3.14 2.89 4.44
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += float(sys.argv[i])
  
print ("the sum is :", add) # the sum is 10.47
"------------------------------------------------------------"
# 7) How to split a file into a list in Python
 
with open('.secret_list/list.txt', 'r') as file:
    menu = file.read().splitlines()

'vagy' 

f = open('myfile.txt')
file_as_list = f.readlines()
for line in file_as_list:       # Emiatt vissza adja minden sorát, de alapvetően csak az elsőt adja vissza a readline
  print(line)

'vagy'
with open ('myfile.txt', 'r') as file:
    file_as_list = file.readlines()
    for line in file_as_list:
        print(line)

"------------------------------------------------------------"
# 8) Playsound telepítés

import sys, subprocess, os


def check_playsound():
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    return "playsound" in installed_packages

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def main():
    if check_playsound():
        #play()
        pass
    else:
        while True:
            clear()
            install_choice = input("This game needs additional resources...\n\nDo you want to proceed? (y/n) ")
            if install_choice == "y":
                clear()
                print("Installing...")
                time.sleep(1)
                install("playsound")
                print("Done!")
                time.sleep(2)
                clear()
                #play()
            elif install_choice == "n":
                print("Goodbye!")
                quit()


if __name__ == '__main__':
    main()

"------------------------------------------------------------"
# 9) Custom welcome message

def get_hello_message():
    name = input('What\'s your name?')
    if name != "":
        return(f'Hello, {name}!')
    else:
        return('Hello, World!')

"------------------------------------------------------------"
# 10) AI random választ egyet a táblán

import random 

def get_ai_move(board):
    """Returns the coordinates of a valid move for player on board."""
    dot = '.'
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    while board[row][col] != dot:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
        continue
    return (row, col)

def mark_AImove(board, player, row, col):
    if board[row][col] == '.':
        board[row][col] = player

"------------------------------------------------------------"
# 11) Enumerate használata

# enumerate function in loops
l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

'''
>>> (0, 'eat')
    (1, 'sleep')
    (2, 'repeat')
'''

# changing index and printing separately
for count,ele in enumerate(l1,100):
    print (count,ele)

"""
>>> 100 eat
    101 sleep
    102 repeat
"""

#getting desired output from tuple
for count,ele in enumerate(l1):
  print(count)
  print(ele)

"""
>>> 0
    eat
    1
    sleep
    2
    repeat
"""

"------------------------------------------------------------"
# 12) Merging two dictionaries 
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)
'''
>>> {'c': 4, 'a': 1, 'b'. 3}
'''

"------------------------------------------------------------"
# 13) Zip használata

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))

'''
>>> (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
'''

"------------------------------------------------------------"
# 14) Random generátorok 

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

'''
>>> cherry
'''

x = "WELCOME"

print(random.choice(x))

'''
>>> c
'''

print(random.randint(3, 9))  #returns a number between 3 and 9 (both included)

"------------------------------------------------------------"
# 15) Print akármekkora board, koordináta kereső, set_random_letter 

def get_board(length, fill_char):
    board = []
    for row_index in range(length):
        row = []
        for col_index in range(length):
            row.append(fill_char)
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(*row)

def get_letter_index(board, char):
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            if char == board[row_index][col_index]:
                return row_index, col_index

def set_random_letter(letter, board):
    board[random.randint(0, len(board)-1)][random.randint(0, len(board)-1)] = letter

def main():
    chars = "[đäđĐÄ]|Ä||d|"
    board = get_board(5, "?")
    for char in chars:
        set_random_letter(char, board)
    coordinates = get_letter_index(board, "d")
    print_board(board)
    print(coordinates)

"------------------------------------------------------------"
# 16) Game Inventory 

def get_inventory():
    return {"name": "Bela",
            "weapon": ["Axe"],
            "health": 3}

print("Weapons:", get_inventory()[1])           # >>> Key Error 1
print("Weapon:", get_inventory()["weapon"])     # >>> Axe

def get_weapon(inventory, weapon):
    for key, value in inventory.items():
        if key == "weapon":
            inventory["weapon"].append(weapon)
    print(inventory)

def main():
    print("----------------------------------------------------------------")
    inventory = get_inventory()
    get_weapon(inventory, "Sword")
    get_weapon(inventory, "Gun")

"------------------------------------------------------------"
# 17) Kép megnyitás 

from PIL import Image

def print_image():
    myImage = Image.open("rickroll_4k.jpg");
    myImage.show();

"------------------------------------------------------------"
# 18) Színkódok használata

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

prCyan("Lajos")

def logo1():
        with open('image/menu_logo1.txt') as file:
            prYellow(file.read())

"------------------------------------------------------------"
# 19) format function

# using format option in a simple string
print("{}, A computer science portal for geeks."
      .format("GeeksforGeeks"))
 
# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))
 
# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))

'''
>>> GeeksforGeeks, A computer science portal for geeks.
    This article is written in Python
    Hello, I am  18 years old!
'''

# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))
 
# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
      .format("User", 19))
 
# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}"
      .format("one", "two", "three", "four"))

'''
>>> GeeksforGeeks, is a computer science portal for geeks
    Hi! My name is User and I am 19 years old
    This is one two three four
'''

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {1}, I'm {0}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

"""
>>> My name is John, I'm 36
    My name is 36, I'm John
    My name is John, I'm 36
"""
"------------------------------------------------------------"
# 20) Dictionary functions

dict = {
    "sajt" : 1,
    "trapista" : 2, "lapkasajt" : 3,
}

print(dict)                 # {'sajt':1 ,'trapista': 2, 'lapkasajt': 3}
print("----------------")

print(dict.items())         # dict_items([('sajt', 1), ('trapista', 2), ('lapkasajt', 3)])
print("---------------")

print(dict.get("sajt"))     # 1 
print("---------------")

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y) 
print(thisdict)             # {'key1':0, 'key2': 0, 'key3': 0}
print("---------------")

dict.update({"Feri" : 5})   # {'sajt':1 ,'trapista': 2, 'lapkasajt': 3, 'Feri': 5}
print(dict)
print("----------------")

print(dict.values())        # dict_values([1, 2, 3, 5])
print(dict.keys())          # dict_keys(['sajt', 'trapista', 'lapkasajt', 'Feri'])

"------------------------------------------------------------"
# 21) String module, ascii_upper/lowercase, abc betűi

import string 

row_letters = sorted(string.ascii_uppercase[0:10])  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(row_letters)
letters = string.ascii_lowercase                    # abcdefghijklmnopqrstuvwxyz
print(letters)
"------------------------------------------------------------"
# 22) Regular expressions - validátor példa, move validátor

import re

def validate_move(move):
    # Only accepts: Single letter at the beginning, number(s) at the end
    validation = "^[A-Za-z]\d+$"
    return re.search(validation, move) is not None

"------------------------------------------------------------"
#23) Dedent használata, leading whitespace levágása each line

from textwrap import dedent

score1 = 5
score2 = 10
do_you_rethrow_question = dedent(f'''
                Your safe score is {score1}
                Your score in this round is {score2}
                Do you want to throw the dice again? [stressful music in the background])
                ''')

"------------------------------------------------------------"
#24) Table print (for ERP for example)
def print_table(table):

    def print_data_line(stats: dict):
        return ('|'.join([f"{ stat : ^20}" for stat in stats.values()]))

    header = '|'.join([f"{ key : ^20}" for key in table[0].keys()])
    separator = '-'*len(header)

    clear()
    print(header.center(middle()))
    print(separator.center(middle()))
    for line in table:
        data_line = print_data_line(line)
        print(data_line.center(middle()))
    input('\npress ENTER to continue...')

"------------------------------------------------------------"
#25) Timed printing

def timed_printing(my_string):
    for character in my_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

"------------------------------------------------------------"
#26) Str-ből lista
txt = "welcome to the jungle"

x = txt.split()

print(x)

"""
>>> ['welcome', 'to', 'the', 'jungle']
"""

"-------------------------------------------------------------"
#27) Random szám lista generátor list comphrenesionnal

list_of_numbers = []
for index in range(9):
        list_of_numbers.append(random.randint(1,20))

# VS

list_of_numbers = [random.randrange(1, 20) for _ in range(9)]

"-------------------------------------------------------------"

#28) Creating Dicts with lists and for loop
fruit_number = [1,2,3,4,5]
list_of_fruits = ["apple", "banana", "peach", "watermelon", "lemon"]

grocery_list = {}
for index in range(len(fruit_number)):
    grocery_list[fruit_number[index]] = list_of_fruits[index]
print(grocery_list)

"-------------------------------------------------------------"
#29) random randint vs randrange difference & random.choices()

import random 

# 3 parameter - randrange(start, stop, step)    -> = x and < y (!!!)
# 2 parameter - randint (start, stop)           -> = x and <= y 

# Using randrange() to generate numbers from 50-100
# skipping 5
print ("Random number from 50-100 skip 5 is : ",end="")
print (random.randrange(50,100,5))      # one number
"""
>>> Random number from 50-100 skip 5 is : 90

"""
print(random.randint(3, 9))
"""
>>> 5
"""
##########################################################
mylist = ["geeks", "for", "python"]
  
print(random.choices(mylist, weights = [10, 1, 1], k = 5))

# first parameter = sequence is a mandatory parameter that can be a list, tuple, or string.
# weights = possibility % 
# k = how many choices

"""
>>> ['geeks', 'geeks', 'geeks', 'for', 'for']
"""

"-------------------------------------------------------------"
#30 end parameter in print

# used to append any string at the end of the output of the print statement
# By default, the print method ends with a newline. WIth end = "" 
# #it will append a space instead a new_line

print("Welcome to" , end = ' ') 
print("GeeksforGeeks", end = ' ')

"""
>>> Welcome to GeeksforGeeks
"""

print("Python" , end = '@') 
print("GeeksforGeeks")

"""
>>> Python@GeeksforGeeks
"""

print("Welcome to") 
print("GeeksforGeeks")

"""
>>> Welcome to
GeeksforGeeks
"""

"-------------------------------------------------------------"
#31 How to make a list of keys from a dictionary

fruits = [
{ 'name' : 'apple', 'price' : 20 },
{ 'name' : 'avocado', 'price' : 10},
{ 'name' : 'orange' , 'price' : 5}
]

fruit_names = []
for fruit in fruits:
	fruit_names.append(fruit['name'])
print(fruit_names)

"""
>>> ['apple', 'avocado', 'orange']
"""

# Make a list comprehension from the dict with words starting with 'a' 
print([fruit['name'] for fruit in fruits if fruit ['name'][0] == 'a'])

"""
>>> ['apple', 'avocado']
"""

"-------------------------------------------------------------"
#32 Arguments in functions (Positional,Default, Variable length etc)

# Positional arg
def sum(a,b):
    return a,b

sum(5,6)

"""
>>> 5,6
"""

# Default arg
def sum(a = 5, b = 7):
    return a, b

sum()
sum(5,6)

"""
>>> 5 
7
>>> 5 
6
"""

# Variable length
def sum(a, *b):
    return a,b

sum(5,6,7,8)
"""
>>> 5
(6,7,8) # tuple
"""

def sum(a, **b):
    return a,b

sum(5, six = 6)

"""
>>> 5
six 6 
"""

"-------------------------------------------------------------"
#33) Difference between list() and split() (str --> list) & list --> str with join

string = "Peter Jackson"

print(string)
print(list(string))		#List of str elements (letters)
print(string.split())	#List of str elements (words)

var = string.split()		

print("".join(var))		#the string again but without space

"""
>>> Peter Jackson
['P', 'e', 't', 'e', 'r', ' ', 'J', 'a', 'c', 'k', 's', 'o', 'n']
['Peter', 'Jackson']
PeterJackson
"""

"-------------------------------------------------------------"
#34) List creation problem with range, how range creates for example (0,5) or (1,6)

print(range(1,8))
print(range(0,8))
print(range(len("jóska")))

new_list = []
for index in range(8):
	new_list.append(index)
print(new_list)

new_list = []
for index in range(1,8):
	new_list.append(index)
print(new_list)

"""
>>> range(1, 8)
range(0, 8)
range(0, 5)
[0, 1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
"""
# List index starts from 0 
# Range starts from 0 - so if you want a 1-7 list you need range(1,8)

"-------------------------------------------------------------"
#35) Creating dict from a sentence, and check how many letters does it have. How many A, how many B etc

def create_dictionary(word = "The quick brown fox jumps over the lazy dog."):
    elements = {}
    index = 0
    for cha in word.lower():
        if word[index].isalpha():
            if cha not in elements.keys():
                elements[cha] = word.count(cha)		# This makes the 't' : 1 etc
        index += 1
    return elements

print(create_dictionary())

"""
>>> {'t': 1, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 
'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 
's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
"""

"-------------------------------------------------------------"
#36) Dictionary key sorting

dictionary = {'t': 1, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1,  'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}

def sort_keys(elements):
    keys = elements.keys()
    return sorted(keys)

keys = sort_keys(dictionary)

print(keys)

#///////////////////////////////////////////// ITS THE SAME

k = list(dictionary.keys())
for i in range(len(k) - 1):
    for j in range(len(k) - i - 1):
        if k[j] > k[j + 1]:
            k[j], k[j + 1] = k[j + 1], k[j]
print(k)


#################################################################################

                                #DATA STRUCTURE CHANGES

#1) str --> list

string_var = "sajt"
var = string_var.split()        #If you use list() you will get ["s","a","j","t"]
print(var)
"""
>>> ["sajt"]
"""

"-------------------------------------------------------------"
#2) list --> str

string_var = "sajt"
var  = string_var.split()
print("".join(var))
"""
>>> sajt
"""

"-------------------------------------------------------------"
#3) integer --> list_of_integer

list_of_strings = list(str(123))
print(list_of_strings)
"""
>>> ['1','2','3']
"""

"-------------------------------------------------------------"
#4) list_of_integer --> integer

list_of_strings = list(str(123)) # or you have a str_list = ['1','2','3']
int_var = int("".join(list_of_strings))
"""
>>> 123
"""

"-------------------------------------------------------------"
#5) list_of_str --> list_of_int

list_of_string = ['1','2','3']
print(list(map(int, list_of_string)))   
# map() collects the elements, object type, so you need list()

"""
>>> [1,2,3]
"""

empty_list = []
for index in list_of_string:
    empty_list.append(int(index))
print(empty_list)

"""
>>> [1,2,3]
"""
"-------------------------------------------------------------"
#6) list_of_int --> list_of_str

list_of_int = [1,2,3]
print(list(map(str,list_of_int)))
"""
>>> ['1','2','3']
"""

empty_list = []
for index in list_of_int:
    empty_list.append(str(index))
print(empty_list)
"""
>>> ['1','2','3']
"""
"-------------------------------------------------------------"
#7) From 2 lists to dictionary

list_of_fruits = ["apple", "banana", "peach", "watermelon", "lemon"]
fruit_number = [1,2,3,4,5]

"""
or you can generate a list 1-5 with this 

fruit_number = []
for number in range(1,6):        # range() won't show the 6th 
    fruit_number.append(number)
print(fruit_number)
"""

grocery_list = {}
for index in range(len(fruit_number)):      # It doesn't matter you need only the length
    grocery_list[fruit_number[index]] = list_of_fruits[index]
print(grocery_list)

"""
>>> {1: 'apple', 2: 'banana', 3: 'peach', 4: 'watermelon', 5: 'lemon'}
"""

"""
If the fruit_number is [1,2,3,4] but the list_of fruits has 5 elements it will give you a 4 key pair dict
{1: 'apple', 2: 'banana', 3: 'peach', 4: 'watermelon', 5}

You have to use len, because range needs az integer, you can't use list and it can't be out of index
"""
