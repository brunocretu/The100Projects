#Count words
#Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

def main():
    print('This program counts the number of words in a string file.')
    print('1. Count the number of words in a string')
    print('2. Count the number of words in a text file')

    while True:
        wordDict = {}
        totalWords = 0

        mode = input('Please choose 1 or 2: ')
        if mode == '1':
            string = input('Please insert the string: ')
            for word in string.split(" "):
                word = word.lower().rstrip()
                if word not in wordDict.keys():
                    wordDict[word] = 1
                    totalWords += 1
                else:
                    wordDict[word] += 1
                    totalWords += 1
        if mode == '2':
            rawFile = input('Please name the file path: ')
            textFile = open(rawFile, 'r')

            for line in textFile:
                for word in line.split(" "):
                    word = word.lower().rstrip()
                    if word not in wordDict.keys():
                        wordDict[word] = 1
                        totalWords += 1
                    else:
                        wordDict[word] += 1
                        totalWords += 1
        print()
        print('The total word count is ' + str(totalWords) + ' and the count per word is:')
        for key in wordDict:
            print(" - " + key + ": " + str(wordDict[key]))

        print('____________________________')
        loop = input('Do you wish to try another sentence? (Y|N):')
        if loop == 'N' or loop == 'no' or loop == 'n' or loop == 'No':
        	break



if __name__ == '__main__':
    main()
