import random
print("						˗ˏˋ ★ ˎˊ˗ 💢♣  🇼​​ 🇪 ​​🇱 ​​🇨​​ 🇴 ​​🇲​​ 🇪​ ​🇹​​ 🇴​ 💰💰​🇲​​ 🇪​​ 🇪​​ 🇱 ​​🇴 ​ ​🇪 ​​🇻 ​​🇦 ​​🇷 ​​🇺​ ​ 🇰 ​​🇴 ​​🇹 ​​🇪​ ​🇸 ​​🇭 ​​🇼 ​​🇦​ ​🇷 ​​🇺 ​​🇩 ​​🇺   💰💰 \n			​")
host=input("please enter 💜🎃  Ｈ𝐨𝐬𝓉  ☆👊 name?::").upper()
player=input("please enter the player name?::👨🏻‍💼👨🏻‍💼👨🏻‍💼::").capitalize()

print(f"lets welcome our host 🤗👨🏻‍💼👨🏻‍💼👨🏻‍💼 Mr/Mrs{host}👨🏻‍💼👨🏻‍💼👨🏻‍💼 and our player 👨🏻‍💼👨🏻‍💼👨🏻‍💼Mr/Mrs.{player}👨🏻‍💼👨🏻‍💼👨🏻‍💼..!🤗\n \n")
dict={"1...Which animal is known as the 'Ship of the Desert":"camel","2...How many days are there in a year?":"365","3...What is the National song of India?":"vandematharam","4...Name the National Reptile of India?":"kobra"}
keys=list(dict.keys())
length_keys=len(keys)
print("RULES>>>>>>for game")
options=["a.camel  b.cow   c.horse   d.dog \n",
         "a.365  b.364   c.365.25    d.265  \n",
         "a.vandematharam    b.janaganamana    c.teluguthalli    d.bharatsalam  \n",
         "a.mountainadder   b.kobra  c.casmo  d.Nagaina"
         ]

correct_options=["a","a","a","b"]
print("here are ",length_keys,"questions first question carries 250000 rupees and last question carries 10000000rupess..! \n\n")
print("no lifespans,except quit ..if you quit the amount you won for last question's is to be taken...!\n \n")
mood=input("if interested '''𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲'''else enter 𝗲𝘅𝗶𝘁 to quit the game..")
if mood=="exit":
        exit()
else:
        print("𝗰𝗼𝗻𝘁𝗶𝗻𝘂𝗲to game 🤞🤞𝗮𝗹𝗹 𝘁𝗵𝗲 𝗯𝗲𝘀𝘁")

order=0
# question_no=keys[order]
prize_money=0
quit=False
# print(length_keys-1,"1234567890-")
    
while not quit:
        if length_keys==0:
                print("you won!!!")
                quit=True
                break
       
        question_no=keys[order]
        options1=options[order]
        print("here is your question \n",question_no,"\n\n")
        print(options1)
        ans=correct_options[order]
        # print(ans)
        mylist=" _ "*len(ans)
        print(mylist)
        answer=input("enter the answer of your question?:\n \n").lower()
        
        if answer==ans:
           print("correct answer \n")
           cashprize=(order+1)*250000
           print(cashprize,"won by",player)
        #    print(f"prize_money={10000}")
        #    print(f"☆👊 {player}☆👊  won {prize_money}💰💰​💰💰​\n")
           order+=1
           length_keys-=1
          
        
          
        elif answer=="quit" or answer=="Quit":
                        quit=True
                        print("you quit game! \n \n")
        
        else:
                print("incorreect answer!")
                quit=True

cashprize=order*250000
print(f"GAME OVER! you won {cashprize}  rupees\n \n")
 
print("https://youtu.be/72PWMeaStY0?si=kPq_SgRameevCsCZ")
