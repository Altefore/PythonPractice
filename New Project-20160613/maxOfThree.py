# practice

def max_of_three(first, second, third):
    if first > second:
        if first > third:
            return first
        else:
            return third
    else:
        if second > third:
            return second
        else:
            return third
            
def main():
    first = input("please enter 3 numbers \n")
    second = input()
    third = input()
    
    print("the largest number is %d" % max_of_three(first, second, third))
    
    
if __name__ == "__main__":
    main()
