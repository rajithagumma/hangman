import random
HANGMAN=['''
  +---+
  |   |
      |
      |
      |
      |
      |
========''','''
  +---+
  |   |
  o   |
      |
      |
      |
      |
========''','''
  +---+
  |   |
  o   |
  |   |
      |
      |
      |
========''','''
  +---+
  |   |
  o   |
 /|   |
      |
      |
      |
========''','''
  +---+
  |   |
  o   |
 /|\  |
      |
      |
      |
========''','''
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
      |
========''','''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
      |
========''']
list_of_words=["property","rights","child","year"]
name=input("enter your name:-")
print("welcome",name,"!")
print("try to guess the word in less than 6 attempts")
list_of_words=["property","rights","child","year"]
word=random.choice(list_of_words)
turns=6
guessmade=""
valid_entry=set("abcdefghijklmnopqrstuvwxyz")
list1=[]
while len(word)>0:
            main_word=""
            for letter in word:
                if letter in guessmade:
                    main_word=main_word+letter
                else:
                    main_word=main_word+"_ "
            if main_word==word:
                print(main_word)
                print("you won!!!!")
                break
            print("guess the words",main_word)
            guess=input()
            if guess   in list1:
                print("you already guessed that letter ")
            else:
                list1.append(guess)
                if guess in valid_entry:
                    guessmade=guessmade+guess
                else:
                    print("enter  valid character:")
                    guess=input()
                if guess not in word:
                    turns=turns-1
                    if turns==6:
                        print("6 turns left!!!")
                        print(HANGMAN[0])
                    if turns==5:
                        print("5 turns left")
                        print(HANGMAN[1])
                    if turns==4:
                        print("4 turns left")
                        print(HANGMAN[2])
                    if turns==3:
                        print("3 turns left")
                        print(HANGMAN[3])
                    if turns==2:
                        print("2 turns left")
                        print(HANGMAN[4])
                    if turns==1:
                        print("1 turns left")
                        print(HANGMAN[5])
                    if turns==0:
                        print("0 turns left")
                        print("you loose")
                        print("you let a good man die")
                        print(HANGMAN[6])
                        break














# words=["bear","pizza","washington","snake","sun","moon"]
# max_wrong=len(HANGMAN)-1
# word=random.choice(words)
# current_guess="-"*len(word)
# wrong_guess=0
# used_letters=[]
# print("welcome to hangman game")
# print("try guess the word")
# while wrong_guess<max_wrong and current_guess!=word:
#     guess=input("enter your letter guess:")
#     if  guess in used_letters:
#         print("you have already guessed that letter",guess)
#         guess=input("enter your letter guess:")
#     used_letters.append(guess)
#     if guess in word:
#         print("you have guessed correctly")
#         new_current_guess=""
#         for letter in range(len(word)):
#             if guess==word[letter]:
#                 new_current_guess+=guess
#             else:
#                 new_current_guess+="-"
#         current_guess=new_current_guess
#     else:
#         print("sorry that was not correct")
#         print(HANGMAN[wrong_guess])
#         print("you have used the following words",used_letters)
#         print("so far, the word is!",current_guess)
#         wrong_guess+=1
# if wrong_guess==max_wrong:
#     print(HANGMAN[wrong_guess])
#     print("you have been hanged")
#     print("the correct word is ",word)
# else:
#     print("you have won")
