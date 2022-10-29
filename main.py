UserName = input("Please enter your name : ")
question = input("Hello dear " + UserName +"\n Text what you would like to get help for : ")

if question.find("can't find") >= 0:
    whatYouCanNotFind = input("Tell me what you can not find? : ")
    if whatYouCanNotFind.find("phone") >= 0:
        answer1 = input("Did you check your room?(Yes or No) : ")
        if answer1.find("yes") >= 0:
            answer1_1 = input("Did you check your pockets? (yes or no)")
            if answer1_1.find("yes") >= 0:
                answer1_2 = input("did you find it? : ")
                if answer1_2.find("yes") >= 0:
                    print("Well done!")
                else :
                    print("Good Luck buddy! ")
            elif answer1_1.find("no") >= 0:
                answer1_7 = input("did you find it? : ")
                if answer1_7.find("yes") >= 0:
                    print("Well done!")
                else:
                    print("Sorry that's all I can do \n Good Luck buddy! ")

        elif answer1.find("no") >= 0:
            answer1_3 = input("Go check your room! \n Did you find it? (yes or no)")
            if answer1_3.find("yes")>=0:
                print("Well done!")
            elif answer1_3.find("no")>=0:
                answer1_4 = input("Did you check your pockets? (Yes or no): ")
                if answer1_4.find("yes") >= 0 :
                    answer1_5 = input("Did you find it? : (Yes or no)")
                    if answer1_5.find("yes")>=0:
                        print("Well done!")
                    elif answer1_5.find("no")>=0 :
                        print("good luck on your mission soldier!")
                elif answer1_4.find("no")>=0:
                    answer1_6 = input("Go check your pockets! \n Did you find it? (yes or no)")
                    if answer1_6.find("yes")>=0:
                        print("Well done!")
                    elif answer1_6.find("no") >=0:
                        print("good luck on your mission soldier!")
    elif whatYouCanNotFind.find("keys")>=0:
        answer2 = input("Did you check your room?(yes or no) : ")
        if answer2.find("yes") >= 0:
            answer2_1 = input("Did you check your pockets? (yes or no)")
            if answer2_1.find("yes") > 0:
                print("good luck buddy")
