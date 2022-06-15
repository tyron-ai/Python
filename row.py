#The program will print a sequence of 7 numbers, starting from that value.
#Each number must be printed using exactly two characters. 
#If the number takes two characters to print, e.g. 34 or -5, then just print it.
# If the number takes less than two characters to print, e.g. 0 or 9, then print a space in front of it.

def main():
    n=int(input('Enter the start number:\n'))
    if n > -1 and n < 10:
        print(' ', end='')
    print(n, end='')
    for i in range(n+1, n+7):
        print(' ', end='')
        if i > -1 and i < 10:
            print(' ', end='')
        print(i, end='')
    print()
main()
