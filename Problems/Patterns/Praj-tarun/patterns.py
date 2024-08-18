def pattern_1(n):
    i=0
    while i<n:
        j=0
        while j<n:
            print('*',end='')
            j+=1
        print()
        i+=1

def main(): 
    pattern_1(5)



if __name__ == "__main__":
    main()