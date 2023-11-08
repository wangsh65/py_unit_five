total=0
count=0
while True:
    ask_user= int(input("ask your number"))
    if ask_user == "q" or count>0:
        average=total/count
        print(average)

        break
    else:
        print("continuous")







