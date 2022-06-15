#Starting from n, the program will print out every 7th number in the range n to n+41.
#Each number will appear on a new line.
#Numbers are printed using a field width of 2 and are right-justified
def main():
    n = int(input('Enter a number:\n'))
    
    for i in range(n, n+42, 7):
        if i > -1 and i < 10:
            print(' ', end='')
            print(i)
        else:
            print(i)
main()
