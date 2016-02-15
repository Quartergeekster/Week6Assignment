##SEF034 Assignment 2
##Word analysing program by Robert Roe
##150409241

import OS
import sys
import random

def Menu():
	print ("""\t\tWelcome to Word Play
		\n\n\tSelect an option:\n
		1. Enter Word\n
		2. Check letter occurences\n
		3. Is Palindrome?\n
		4. Anagram\n
		5. Quit\n\n""")
	try:
		choice = int(input("Enter choice: "))
		return choice
	except ValueError:
		print("Number not valid")


def getWord():
	Word = str(input("Enter your word: "))
	return Word
	

def main():
	InputWord = ""
	choice = Menu()
	while(choice != 5):
		if(choice == 1):
			InputWord = getWord()
		elif(choice == 2):
			CheckLetterOccurences(InputWord)
		elif(choice == 3):
			CheckIsPalindrome(InputWord)
		elif(choice == 4):
			GenerateAnagram(InputWord)
		else:
			print("That was not an option.")
		choice = Menu()
	sys.exit()
