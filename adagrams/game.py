import random 
import string
import copy


LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    
    letters_list = []

    for char, frequency in LETTER_POOL.items():
        letters_list.extend([char] * frequency)


    hand = []
    for i in range(10):
        randomLetter = random.choice(letters_list)
        hand.append(randomLetter)
        letters_list.remove(randomLetter)
    

    #*********
    #YET TO SEE IF FREQUENCY IS LESS THAN THE LETTER POOL
    return hand
    

def uses_available_letters(word, letter_bank):
    # the purpose of this function is to check if the letters in the user input
    # are in present in our current hand.

    # access our hand
    list_copy = copy.deepcopy(letter_bank)

    # letters_in_list_flag == True

    for letter in word.upper():
        if letter in list_copy:
            list_copy.remove(letter)
        else:
            return False

    return True



def score_word(word):
    #find out what is best to store letter/point. 
    score_chart = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, 
        "N": 1, "R": 1, "S": 1, "T": 1, "D": 2,"G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10}
    print(type(score_chart))

    score = 0
    # 
    for letter in word:
        for key,value in score_chart.items():
        

    pass

def get_highest_word_score(word_list):
    pass