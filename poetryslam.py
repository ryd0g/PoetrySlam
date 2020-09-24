#function to print the poem to console
def get_file_line():
    filename = 'poem.txt'
    infile = open(filename, 'r')
    for line in infile:
        print(line, end='')

#function to print lines backwards
def lines_printed_backwards():
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