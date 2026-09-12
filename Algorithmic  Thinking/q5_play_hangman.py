""" Question 5: Hangman """
"""
Input: string
Output: interactive hangman game 
"""
def guesse_letter(guessed_letter):
    while True:
        letter=input("Which letter do you want to guess: ")
        if len(letter)==1:
            if letter not in guessed_letter:
                return letter
            else:
                print("You already guessed that letter! Pick a different letter.")
        else:
            print("Enter only one letter.")    
def update_cur_word(guesse_letters,word,cur_word):
    for i in range(len(word)):
        if word[i]==guesse_letters:
            cur_word=cur_word[:i]+guesse_letters+cur_word[i+1:]
    return cur_word        

def play_hangman(word):
    cur_word="_" * len(word)
    parts_left = 6
    guessed_letters=[]
    turn=0
    while ("_" in cur_word and parts_left !=0 ):
        print("Current word:" , cur_word)
        print("parts left" , parts_left)
        print("Letters guessed:", "," .join(guessed_letters))
        guesse_letters= guesse_letter(guessed_letters)
        if guesse_letters in word:
            print("Good Guess")
            cur_word=update_cur_word(guesse_letters,word,cur_word)
        else:
            print ("Wrong guess")
            parts_left-=1
        turn+=1
        guessed_letters.append(guesse_letters)
        print("----------------------")
    print("Final Word: ",cur_word)
    if parts_left !=0:
        print("You Won in ", turn," turns") 
    else:
        print("You lose in ", turn," turns")    

    return 


if __name__ == '__main__':
    play_hangman("programmimg")


""" Sample Hangman game in Python terminal:

Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 6
Letters guessed: 
Which letter do you want to guess: e
Not quite...
-----
Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e
Which letter do you want to guess: o
Good guess!
-----
Current word: _ _ o _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e, o
Which letter do you want to guess: i
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i _ _ 
Incorrect guesses left: 5
Letters guessed: e, o, i
Which letter do you want to guess: n
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i n _ 
Incorrect guesses left: 5
Letters guessed: e, o, i, n
Which letter do you want to guess: g
Good guess!
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 5
Letters guessed: e, o, i, n, g
Which letter do you want to guess: y
Not quite...
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y
Which letter do you want to guess: as
Please enter only one letter.
Which letter do you want to guess: a
Good guess!
-----
Current word: _ _ o g _ a _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a
Which letter do you want to guess: m
Good guess!
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a, m
Which letter do you want to guess: i
You already guessed that letter! Pick a different letter.
Which letter do you want to guess: t
Not quite...
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t
Which letter do you want to guess: r
Good guess!
-----
Current word: _ r o g r a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t, r
Which letter do you want to guess: p
Good guess!
-----
Final word: p r o g r a m m i n g 
You won in 11 turns.
"""