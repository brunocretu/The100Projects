#Check if Palindrome
#Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

def main():
    while True:

        isPalindrome = True

        word = input("Enter a word and I'll tell you if it is a Palindrome (it reads the same forwards as backwards): ")

        if len(word.split()) != 1:
        	word = input('Please input a single word: ')

        for i in range(int(len(word)/2)):
            if word[i] == word[-i-1]:
                continue
            else:
                isPalindrome = False
                break

        if isPalindrome:
            print('The word "' + word + '" is a Palindrome')
            print('____________________________')
            loop = input('Do you wish to try another word? (Y|N):')
            if loop == 'N' or loop == 'no' or loop == 'n' or loop == 'No':
            	break
        else:
            print('The word "' + word + '" is not a Palindrome')
            print('____________________________')
            loop = input('Do you wish to try another word? (Y|N):')
            if loop == 'N' or loop == 'no' or loop == 'n' or loop == 'No':
            	break

if __name__ == '__main__':
    main()
