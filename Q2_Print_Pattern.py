

ans="yes"
while ans!="n":
    n=input("Enter a albhabet")


    if n=="a":
        star = int(input("Enter a numbe of lines you want to print *"))
        print(n,end=" ")
        for i in range(star+1):
            print("*"*i)

    elif n=="b":
        num = int(input("Enter odd number for printing a correct diamond"))

        space = num // 2  # 7 divide by 2 willl give you 3

        print(n)

        for i in range(1, num + 1, 2):
            print(" " * space, end="")
            print("*" * i)
            space = space - 1

        space = 1
        for i in range(num - 2, 0, -2):
            print(" " * space, end="")
            print("*" * i)
            space = space + 1





