# py-project
def calc (x,y,op):
    if op == '1':
        return x + y
    if op == '2':
        return x - y
    if op == '3':
        return x * y
    if op == '4':
        if y == 0:
           return" Error! Division by zero."
        return x / y 
    
while True:
    print("select operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.divide")

    op = input(" Enter choice (1/2/3/4):")
    if op in ('1','2','3','4'):
        try:
            a = float(input("Enter first number:"))
            b = float(input("Enter second number:"))
            print("result:",calc (a,b,op))
        except:
            print("Invalid input")
        if input("Next calculation?(yes/no):") == "no":
            break
        else:
            print("invalid choice")


