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
	try: ##Tries to get a numeric input
		_choice = int(input("Enter choice: "))
		print("")
		return _choice
	except ValueError: ##if the input is not a number, this will catch the error
		print("Number not valid")

def getWord():
	_Word = str(input("Enter your word: ")) ##Inputs word
	_Word = _Word.lower() ##Converts to lowercase
	return _Word

def SplitWord(Word): ##Splits word into a list
	_WordList = list(Word)
	return _WordList

def CheckLetterOccurences(Word, WordList):
	_LetterToFind = str(input("\nEnter a letter to find: "))
	_Counter = 0
	for i in range(0, len(WordList)):
		if(_LetterToFind == WordList[i]):
			_Counter +=1
	print(_LetterToFind + " occurs " + str(_Counter) + " time(s)")

def CheckIsPalindrome(Word, WordList):
	IsPalindrome = True ##Defaults Is Palindrome to True
	N = len(WordList)
	for i in range(0,int((N/2)), 1): ##For each letter in half of the word
		if(Word[i] == Word[N-i-1]): ##If letter x places from the front is the same as the letter x places from the back
			IsPalindrome = True ##Continues being true
		else: ##If the above is not the case
			IsPalindrome = False ##Palindrome is no longer true
	if(IsPalindrome):
		print(Word + " is a palindrome")
	else:
		print(Word + " is not a palindrome")

def CheckAnagram(Word1, WordList):
	print("Enter a word to compare to your original")
	_Word2 = getWord()
	_WordList2 = SplitWord(_Word2)
	if(len(WordList) == len(_WordList2)):##Could be anagram
		for i in range(0, len(WordList)): ## Checks for each letter in Word1
			if(WordList[i] in _WordList2): ##If the letter is in word 2
				_WordList2.remove(WordList[i]) ##Remove from Word2
		if(len(_WordList2)==0): ##If Word2List length is zero, all letters have been removed, therefore is an anagram
			print(Word1 + " is an anagram of " + _Word2 + "\n")
		else:
			print(Word1 + " is not an anagram of " + _Word2 + "\n")
	else:
		print(Word1 + " is not an anagram of " + _Word2)
		print("")


def main():
	InputWord = ""
	if(InputWord == ""):
		print("\t\tWelcome to WordPlay\n")
		InputWord = getWord()
		WordList = SplitWord(InputWord)
	choice = Menu()
	try: ##Tries to run functions
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
	except UnboundLocalError: ##If a variable hasn't been assigned, this catches the error
		print("Word has not been assigned")
		choice = Menu()
	print("System exit")
	sys.exit()

main()
