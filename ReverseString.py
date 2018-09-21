#String reverse
#Enter a string and the program will reverse it and print it out

def main():
	print('This script reverses any string you input')
	while True:
		string = input('String you wish to be reversed: ')

		revString = string[::-1]
		print('The reversed string is: ' + revString)

		print('___________________')

		loop = input('Do you wish to reverse any other string? (Y|N) ')

		if loop == 'N' or loop == 'no' or loop = 'No':
			break

if __name__ == '__main__':
	main()
