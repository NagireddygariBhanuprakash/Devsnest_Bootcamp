print("                       📣Here is a game called HANGMAN📣                             ")
print()
host=input("enter the host👨‍🎤 name?🎙️::").upper()
print(f" 👋 | ˗ˏˋ ★ ˎˊ˗ WELCOME !!| Mr/mrs.'''{host}'''  ˗ˏˋ ★ ˎˊ˗ 👋its pleasure to host the GAME |")
print()
print()
name=input("🥷🥷🥷please enter your  player name🥷🥷🥷:: ").upper()
print()
print()
print(f" 👋 | ˗ˏˋ ★ ˎˊ˗ WELCOME !!| Mr/mrs.'''{name}'''  ˗ˏˋ ★ ˎˊ˗ 👋 |\n\n RULES FOR HANGMAN:: \n 1.One player thinks of a word and provides the number of letters in it as a clue \n 2.The other player then starts guessing letters one by one \n 3.For each correct guess, the letter is revealed in its corresponding position(s) in the word \n 4.For each incorrect guess, a body part of the hanging figure is drawn on the output screen \n 5.The 👨‍🎤👨‍🎤👨👨‍🎤{host}👨‍🎤👨‍🎤👨‍🎤 should treat an incorrect guess as if 🥷🥷🥷{name}🥷🥷🥷 guessed a wrong letter ")

shiva=["chandana","shiva","mahadeva","ishvara","maheshvara","linga","chandrashekhara","kedarnatha"]

print()
mood=input(f"Are you really 🤓interested🤓  to play🎮 game🎮 Mr/Mrs {name} after checking game rules❗❗❗:? yes to contine or any other key to exit::")
if mood=="yes":
     print(f"{name}! entered yes so continued ▶ have a  fun😎👍🤪")
else:
     print("you exited🔚 from game!!")
     exit()
len_word=len(shiva)#5 char 4
# print(len_word)
order=int(input(f"enter number from 0 to {len_word-1} to select a word?::"))#2

# order=int(input("enter number from 0 to ",len_word))

hangman_list=['''

 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

''',
'''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

''',
'''

+---+
  |   |
  O   |
 /|\  |
      |
      |
=========

''',
'''

+---+
  |   |
  O   |
 /|   |
      |
      |
=========

''',
'''

+---+
  |   |
  O   |
  |   |
      |
      |
=========

''',
'''

 +---+
  |   |
  O   |
      |
      |
      |
=========

''',
'''

 +---+
  |   |
      |
      |
      |
      |
=========

''',
]
selected_word=shiva[order]#kedarnatha
mylist=[" _ "]*len(selected_word)#length=10[' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ']
chances=6
print(mylist)               #[' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ']
gameover=False          #initially took false
while not gameover:     #not operator
    print("🚨📢🔔⚠️enter 'hint' to get hint But here is a condition so you loss one chance!!")
    print()
    print()
    guess=input("your guess?:").lower()#guess=K  --->changes to k and stored at1st blank
    if guess=="hint":
        print(f"Hello Mr/Mrs.{name}here is your clue is-->names of god shiva! 🛐🕉️🛕🙏ૐૐ")
    if guess in selected_word:#kedarnatha
        print("💥 🔑💥")
        print(f"correct answer Mr/Mrs{name}✅")
        print(hangman_list[chances])         #0123456789
        for pos in range(len(selected_word)):#kedarnatrha=0,9
            if selected_word[pos]==guess:#if selected word alphabet  =to user guessed alphabet#     k
                mylist[pos]=guess       #blank (my_list) guessed letter sits
              
        print(mylist)#['k', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ']
        if " _ " in mylist:
         print(f"Entered a correct letter 🤝🤝all the best for next guess Mr/Mrs{name} ")
        
    else:
        chances-=1          #chances=chances-1
        # print("🚨📢🔔⚠️enter 'hint' to get hint But here is a condition so you loss one chance!!")
        print(hangman_list[chances])
        print(chances,"chances left")
        print(mylist)#hint 
        if chances==1:
            print(f"Mr/Mrs{name} you have no chances if you guess wrong✘ once again you going to loss game😕😕 ")
        if chances==0:
            gameover=True
            print(f"👎🏼sorry to say this {name}lost game  better🤞🤞🤞 luck next time")
    if ' _ 'not in mylist:
             gameover=True
             print(f"🎊🎊🎊{name} you won🏆 game congrats!🎊🎊🎊")
             print()
             print(f"{name} is surprise🤩🎁🤩 for you click below link!🔗🔗🔗")
             print()
             print("https://youtu.be/72PWMeaStY0?si=kPq_SgRameevCsCZ")



  


# word_list = ["secret","hero"]
# len_word=len(word_list)
# order=int(input(f"enter number from 0 to {len_word-1} to select a word?::"))
# selected_word=word_list[order]#k
# guesses= ""
# turns = 10
# while turns>0:
#     failed = 0
#     for char in selected_word:
#         if char in guesses:
#             print(char,end ="")
#         else:
#             print("_ ",end="")
#             failed+=1
#     if failed == 0:
#         print("YOU WON")
#         break
#     guess = input("guess a character:")
#     guesses+=guess
#     if guess not in selected_word:
#         turns-=1
#         print("wrong")
#         print("You have",+turns,"more guesses")
#         if turns == 9:
#             print("---------")
#         elif turns == 8:
#             print("---------")
#             print("    0    ")
#         elif turns == 7:
#             print("---------")
#             print("    0    ")
#             print("    |    ")
#         elif turns == 6:
#             print("---------")
#             print("    0    ")
#             print("    |    ")
#             print("   /     ")
#         elif turns == 5:
#             print("---------")
#             print("    0    ")
#             print("    |    ")
#             print("   / \   ")
#         elif turns == 4:
#             print("---------")
#             print("  \ 0    ")
#             print("    |    ")
#             print("   / \   ")
#         elif turns == 3:
#             print("---------")
#             print("  \ 0 /  ")
#             print("    |    ")
#             print("   / \   ")
#         elif turns == 2:
#             print("---------")
#             print("    0/  ")
#             print("   /|    ")
#             print("   / \   ")
#         elif turns == 1:
#             print("---------")
#             print("    0   ")
#             print("   /|\  ")
#             print("   / \   ")
#         else:
#             print("YOU LOSE")