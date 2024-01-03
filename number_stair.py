def pattern_1(rows):
    for i in range(1, rows+1):
        for j in range(i):
            print(i, end=" ")
        print("\r")


# Driver Code
        
def main():
    pattern_1(1000)


if __name__ == "__main__":
    main()