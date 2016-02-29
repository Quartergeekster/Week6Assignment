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
		print("")
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

def CheckLetterOccurences(Word, WordList):
	for i in range(0, len(WordList)):
		LetterCount = Word.count(WordList[i])
		print(WordList[i] + " occurs " + str(LetterCount) + " times")



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

def CheckAnagram(Word1, WordList):
	print("Enter a word to compare to your original")
	Word2 = getWord()
	WordList2 = SplitWord(Word2)
	WordList.sort()
	WordList2.sort()
	if(WordList == WordList2):
		print(Word1 + " is an anagram of " + Word2)
	else:
		print(Word1 + " is not an anagram of " + Word2)
		print("")


def main():
	InputWord = ""
	choice = Menu()
	try:
		while(choice != 5):
			if(choice == 1):
				InputWord = getWord()
				print("Your word was " + InputWord)
				WordList = SplitWord(InputWord)
			elif(choice == 2):
				CheckLetterOccurences(InputWord, WordList)
			elif(choice == 3):
				CheckIsPalindrome(InputWord, WordList)
			elif(choice == 4):
				CheckAnagram(InputWord, WordList)
			else:
				print("That was not an option.")
			choice = Menu()
	except UnboundLocalError:
		print("Word has not been assigned")
		choice = Menu()
		sys.exit()

main()
