 names_list=["shiva","mahadeva","ishvara","maheshvara","linga","nataraja","pashupatinath","bhairava",
        "ardhanari","chandrashekhara","somaskanda","neelakantha","trilochan","kedarnatha"]
 bank_AC_nos=[1,2,3,4]#list of account numbers

 name=input("name")
 bank_AC_no=int(input("bank ac no"))


 if bank_AC_no in bank_AC_nos and name in names_list:
     print("continue")
 else:
     print("not a customer")
 banking_operations=["loan","credit"]
 print(banking_operations,"select the operation")
 operation=input("operation")
 if operation in banking_operations:
     print("continue") 
 else:
     print("Back to menu")


 if operation=="loan":

 
    
     loan_amt=int(input("enter how much amount are you taking as loan?"))
     proof=int(input("enter the value of your documents:"))
     if proof>=loan_amt:   
         print(f"Mr/Mrs {name} your bank account number is:{bank_AC_no} as per records your loan amount is : Rs.{loan_amt} ")
     else:
         print("your property is deficiency to take loan amount ")
 elif operation=="credit":
     if bank_AC_no==1 and name



def credit(mail,Amount):
        mail=input("enter your mail             ::")
        password=input("enter your password     ::")
        if mail in emails:
            authenticate=emails.get(mail)
            # print(authenticate,"password")
        if password==authenticate:
            print("logging in!!")
        
            index = list(emails.keys()).index(email)
            
            # print(index)

            amount = Amount[index]
            print(f"Amount associated with   {email}   : BAL....{amount}")
            amt_add=int(input("enter how much you are crediting?     ::"))
            updt=amount+amt_add
            
            print(f"after crediting      {amt_add}  total amount BAL...   {updt}   ")
        
def withdraw(emails,Amount):
        mail=input("enter your mail                ::")
        password=input("enter your password        ::")
        
        if email in emails:
            authenticate=emails.get(mail)
        if password==authenticate:
            print("Authenticating..........!!")
            index = list(emails.keys()).index(email)
            
            print(index)

            amount = Amount[index]
            print(f"Amount associated with    {email}    :BAL... {amount}")
            withdraw_amt=int(input("enter how much you are withdrawing?      ::"))
            if amount<withdraw_amt:
                  print("we cannot perform this action....\n insufficient of balnces....")
                  exit()
            updt=amount-withdraw_amt
            
            print(f"after withdrawing    {withdraw_amt}    total amount is     {updt}")
        
def transfer(emails,Amount):
     from_mail=input("enter sender mail         ::")
     from_pass=input("enter seneder password    ::")
     if from_mail in emails:
            authenticate=emails.get(from_mail)
     if from_pass==authenticate:
            print("Authenticating.............!!\n")
            
     To_mail=input("enter receiver mail          ::")
     To_pass=input("enter receiver password      ::")
     if To_mail in emails:
            authenticate=emails.get(To_mail)
     if To_pass==authenticate:
            print("Authenticating..........!!\n")
            amt_transfer=int(input(f"    {from_mail}    enter how much amt need to transfer for       {To_mail}"))
            
            index = list(emails.keys()).index(from_mail)
            # Amount=Amount[index]
            amount = Amount[index]
            if amt_transfer>amount:
                  print("we cannot perform this action....\n insufficient of balnces....")
                  exit()
            else:
                updt_amount=amount-amt_transfer
            
                print(f"Amount associated after transfering from    {from_mail}   : BAl..   {updt_amount}")
                
                index = list(emails.keys()).index(To_mail)
                amount = Amount[index]+amt_transfer
                print(f"Amount associated after crediting   {from_mail}   to   {To_mail}   : BAL...{   amount}")
def signup():
         print("please signup ....\n if you are a new user....")
         email_new=input("enter your mail")
         email_pass=input("set your password ..keep more than 8 chars with combination of capital,small,digits and symbols.....")
         length=len(email_pass)
         if length>=8:
           
            countsma=0
            countcap=0
            countdig=0
            countsymbol=0
            for i in email_pass:
                if i.islower():
                    countsma+=1
                if i.isupper():
                    countcap+=1
                elif i.isdigit():
                    countdig+=1
                else:
                    countsymbol+=1
         if countcap>=2 and countdig>=2 and countsma>2 and countsymbol>2:
                print("strong")
         elif countcap>=1 and countdig>=1 and countsma>1 and countsymbol>1:
                     print("medium")
         else:
                    print("weak")


         operation=input("welcome,,please select your operation 1.Credit1  2.Withdraw1  3.Transfer1   ::").lower()
         if operation=="credit1":
                print("we have no knowledge on DBMS so ...")
                
         elif operation=="withdraw1":
                print("we have no knowledge on DBMS so ...")
         elif operation=="transfer1":
                print("we have no knowledge on DBMS so ...")

#main function.......
print("WELCOME TO EBI((EMAIL BANK OF INDIA!!))\n\n")
emails={"1@g":"1","1905bhanuprakash@gmail.com":"bhanu@B1234","manojgelisam":"manoj@M123","yokshitha.com":"yokshitha@123"}
Amount=[123,2,3,4]
email=input(("enter your mail to login    ::"))
if email in emails:
    operation=input("welcome,,please select your operation 1.Credit  2.Withdraw  3.Transfer   ::").lower()
    if operation=="credit":
        credit(emails,Amount)
        
    elif operation=="withdraw":
        withdraw(emails,Amount)
    elif operation=="transfer":
         transfer(emails,Amount)
else:
         signup()     
         
