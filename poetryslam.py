#import random module
import random

#greeting the user
print('Welcome to the Poetry Slam!')
print('Choose to read the poem in style 1, 2, 3, or 4!')
poem_choice = input('How should we read the poem today? ')
def greeting(poem_choice):
    if poem_choice == '1':
        get_file_line(poem_choice)
    elif poem_choice == '2':
        lines_printed_backwards(poem_choice)
    elif poem_choice == '3':
        lines_printed_random(poem_choice)
    elif poem_choice == '4':
        lines_printed_custom(poem_choice)
    else:
        print('Please choose an option 1-4')

#function to print the poem normally to console
def get_file_line(poem_choice):
    filename = 'poem.txt'
    infile = open(filename, 'r')
    for line in infile:
        print(line, end='')

#function to print lines backwards
def lines_printed_backwards(poem_choice):
    lines_list = [
        '1 "Smart" by Shel Silverstein', 
        '2 My dad gave me one dollar bill', 
        "3 Cause I'm his smartest son,", 
        '4 And I swapped it for two shiny quarters', 
        "5 'Cause two is more then one!", 
        '6 And then I took the quarters', 
        '7 And traded them to Lou', 
        "8 For three dimes-- I guess he didn't know", 
        '9 That three is more than two!', 
        '10 Just then, along came old blind Bates', 
        "11 And just 'cause he can't see", 
        '12 He gave me four nickels for my three dimes,', 
        '13 And four is more than three!', 
        '14 And I took the nickels to Hiram Coombs', 
        '15 Down at the seed-feed store,',   
        '16 And the fool gave me five pennies for them,', 
        '17 And five is more than four!', 
        '18 And I went and showed my dad,', 
        '19 And he got red in the cheeks', 
        '20 And closed his eyes and shook his head--', 
        '21 Too proud of me to speak!'
    ]
    for i in reversed(lines_list):
        print(i)

#function to print lines at random
def lines_printed_random(poem_choice):
    lines_list = [
        '"Smart" by Shel Silverstein', 
        'My dad gave me one dollar bill', 
        "Cause I'm his smartest son,", 
        'And I swapped it for two shiny quarters', 
        "'Cause two is more then one!", 
        'And then I took the quarters', 
        'And traded them to Lou', 
        "For three dimes-- I guess he didn't know", 
        'That three is more than two!', 
        'Just then, along came old blind Bates', 
        "And just 'cause he can't see", 
        'He gave me four nickels for my three dimes,', 
        'And four is more than three!', 
        'And I took the nickels to Hiram Coombs', 
        'Down at the seed-feed store,',   
        'And the fool gave me five pennies for them,', 
        'And five is more than four!', 
        'And I went and showed my dad,', 
        'And he got red in the cheeks', 
        'And closed his eyes and shook his head--', 
        'Too proud of me to speak!'
    ]
    for i in lines_list:
        random.shuffle(lines_list)
        print(i)

#function to print in alphabetical order
def lines_printed_custom(poem_choice):
    lines_list = [
        '"Smart" by Shel Silverstein', 
        'My dad gave me one dollar bill', 
        "Cause I'm his smartest son,", 
        'And I swapped it for two shiny quarters', 
        "'Cause two is more then one!", 
        'And then I took the quarters', 
        'And traded them to Lou', 
        "For three dimes-- I guess he didn't know", 
        'That three is more than two!', 
        'Just then, along came old blind Bates', 
        "And just 'cause he can't see", 
        'He gave me four nickels for my three dimes,', 
        'And four is more than three!', 
        'And I took the nickels to Hiram Coombs', 
        'Down at the seed-feed store,',   
        'And the fool gave me five pennies for them,', 
        'And five is more than four!', 
        'And I went and showed my dad,', 
        'And he got red in the cheeks', 
        'And closed his eyes and shook his head--', 
        'Too proud of me to speak!'
    ]
    for i in sorted(lines_list):
        print(i)
greeting(poem_choice)
    