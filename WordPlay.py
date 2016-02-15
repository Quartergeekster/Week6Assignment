##SEF034 Assignment 2
##Word analysing program by Robert Roe
##150409241



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
	except ValueError:
		print("Number not valid")

def main():
	choice = Menu()