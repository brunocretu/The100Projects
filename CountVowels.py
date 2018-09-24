#Count Vowels
#Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

vowels = 'aeiouAEIOU'

def main():

    while True:
        countA = 0
        countE = 0
        countI = 0
        countO = 0
        countU = 0
        countTotal = 0

        string = input("Enter a string and I'll tell you how many vowels there are and how many of each: ")

        for i in string:
            if i in vowels:
                countTotal += 1

                if i == 'a' or i == 'A':
                    countA += 1
                elif i == 'e' or i == 'E':
                    countE += 1
                elif i == 'i' or i == 'I':
                    countI += 1
                elif i == 'o' or i == 'O':
                    countO += 1
                else:
                    countU += 1

        print('String "' + string + '" contains ' + str(countTotal) + ' vowels:')
        print(' - a: ' + str(countA))
        print(' - e: ' + str(countE))
        print(' - i: ' + str(countI))
        print(' - o: ' + str(countO))
        print(' - u: ' + str(countU))

        print('____________________________')
        loop = input('Do you wish to try another sentence? (Y|N):')
        if loop == 'N' or loop == 'no' or loop == 'n' or loop == 'No':
        	break

if __name__ == '__main__':
    main()
