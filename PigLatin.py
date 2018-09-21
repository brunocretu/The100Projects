#Pig Latin
#Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield ananabay).

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def main():
	print('Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield ananabay)')
	
	print()
	while True:
		word = input('What word do you wish to input? ')
		if len(word.split()) != 1:
			word = input('Please input a single word: ')

		if word[0] in vowels:
			output = word + 'yay OR ' + word + 'way'
		elif word[0] in consonants and word[1] in consonants:
			output = word[2:] + word[:2] + 'ay'
		else:
			output = word[1:] + word[0] + 'ay'

		print(output)

		print('____________________________')
		loop = input('Do you wish to play with another word? (Y|N) ')
		if loop == 'N' or loop == 'no' or loop == 'n' or loop == 'No':
			break		


if __name__ == '__main__':
	main()
