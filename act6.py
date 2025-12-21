print("age check about vote")
age=(int(input("enter ur age:")))
if age<0:
    print("invalied age")
elif age<18:
    print("ur a minor")
    print("u can not vote")
elif age>18 and  age < 60:
    print("ur an adult")
    print("can vote")
else:
    print("ur a senior")
    print("u can vote an have senior benefits")