##SEF034 Assignment 2
##Word analysing program by Robert Roe
##150409241

import os
import sys
import random

def Menu():
	print ("""\t\tWelcome to Word Play
		\n\tSelect an option:
		1. Enter Word
		2. Check letter occurences
		3. Is Palindrome?
		4. Anagram
		5. Quit\n\n""")
	try:
		choice = int(input("Enter choice: "))
		return choice
	except ValueError:
		print("Number not valid")


def getWord():
	Word = str(input("Enter your word: "))
	Word = Word.lower()
	return Word
	
def SplitWord(Word):
	WordList = list(Word)
	return WordList

def CheckLetterOccurences(Word):
	pass

def CheckIsPalindrome(Word, WordList):
        IsPalindrome = True
        N = len(WordList)
        for i in range(0,int((N/2)), 1):
                if(Word[i] == Word[N-i-1]):
                        IsPalindrome = True
                else:
                        IsPalindrome = False
        if(IsPalindrome):
                print(Word + " is a palindrome")
        else:
                print(Word + " is not a palindrome")

def GenerateAnagram(Word):
	pass

def main():
	InputWord = ""
	choice = Menu()
	while(choice != 5):
		if(choice == 1):
			InputWord = getWord()
			print("Your word was " + InputWord)
			WordList = SplitWord(InputWord)
		elif(choice == 2):
			CheckLetterOccurences(InputWord)
		elif(choice == 3):
			CheckIsPalindrome(InputWord, WordList)
		elif(choice == 4):
			GenerateAnagram(InputWord)
		else:
			print("That was not an option.")
		choice = Menu()
	sys.exit()
