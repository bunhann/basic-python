def pattern_1(rows):
    for i in range(1, rows+1):
        for j in range(i):
            print(i, end=" ")
        print("\r")


# Driver Code
        
def main():
    pattern_1(8)
    pattern_2("Hello World")


# pattern_2
    
def pattern_2(your_text):
    x=0
    for i in your_text:
        x = x + 1
        print(your_text[0:x])
    for i in your_text:
        x = x-1
        print(your_text[0:x])



if __name__ == "__main__":
    main()