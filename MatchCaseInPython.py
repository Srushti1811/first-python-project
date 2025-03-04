x=int(input("Enter the value of x : "))
# x is a varible to match

match x:
    #if x is 0
    case 0:
        print("x is Zero")
    case 4:
        print("case is 4")

    case _ if x != 90 :
        print(x," is not 90")
    case _ if x == 60 :
        print(x, " is equal to 80")

    case _ :
        print(x)
