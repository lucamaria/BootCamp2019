def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                   "digits differ by 2 or more: ")
    if len(step_1)!=3:
        raise ValueError("Your number needs to be a 3-digit number!")
    digit1=int(step_1)//100
    digit3=int(step_1)%10
    dif=abs(digit1-digit3)

    if dif <2:
        raise ValueError("The first and the last digit need to differ by two or more!")

    step_2 = input("Enter the reverse of the first number, obtained "
                   "by reading it backwards: ")
    reverse = step_1[len(step_1)-1:0:-1]+step_1[0]
    if reverse!=step_2:
        raise ValueError("This is not the reverse of your first number!")

    step_3 = input("Enter the positive difference of these numbers: ")

    if int(step_3)!=abs(int(step_1)-int(step_2)):
        raise ValueError("Please calculate the positive difference correctly!")

    step_4 = input("Enter the reverse of the previous result: ")
    reverse = step_3[len(step_3)-1:0:-1]+step_3[0]
    if  reverse!=step_4:
        raise ValueError("This is not the reverse of the previous result!")
    
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")
