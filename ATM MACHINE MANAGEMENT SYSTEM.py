a={'kaniska':'1456','nayaki':'1234','priyanka':'1245','poorani':'1109'}b=['kaniska','nayaki','priyanka','poorani']c={'1456':15000,'1234':5000,'1245':30000,'1109':5500}c_name=input("Enter your name:")c_pass=input("Enter your password:")for i in range(0,len(b)):    if c_name==b[i] and a[b[i]]==c_pass:        print("The total amount in your account:",c[a[b[i]]])        print('''         1.Deposite         2.withdraw         3.mini_statement         4.exit         ''')        amount=c[a[b[i]]]        option= int(input("select your option:") )       

 if option ==1:
    print("you can deposite the money below 50000")dep= int(input("Enter the amount"))amount+=depprint (" Total amount:", amount)
 elif option==2:print("you can withdraw the money below the 50000") withd= int(input("Enter the amount:")) amount -= withd print("Total amount:", amount)
 elif option ==3: print("=======ATM=======") print("Username:", b[i]) print("Total amount:", amount) print("Thanks for visiting") print("==================")
else: print("please enter correct logins") 

