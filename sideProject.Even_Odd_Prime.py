# Detecting whether the input is a prime, odd or even number ?!
# Obaid Nadeem
# Python 3.8

def main():

    def prime():
    
        # user_input = int(input("N: "))
    
        for i in range (2, user_input):
        
            check = user_input % i
            if check == 0:
                print("Prime: False")
                exit()
            elif i == user_input - 1 :
                print("Prime: True")
    
    
    def odd():
    
        # user_input = int(input("N: "))
    
        check = user_input % 2
    
        if check == 0:
            print("ODD: True")
        else:
            print("ODD: False")
    
    
    def even():
    
        # user_input = int(input("N: "))
    
        check = user_input % 2
    
        if check != 0:
            print("even: True")
        else:
            print("even: False")
    




    print("\n ******* CHECK ODD , EVEN AND PRIME PROPERTY OF A NUMBER *******")
    user_input = int(input("Enter a number: "))

    odd()
    even()
    prime()

main()