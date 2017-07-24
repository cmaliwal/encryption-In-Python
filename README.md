# encryption-In-Python
Simple Python Encryption: How to Encrypt a Message

type1 :

	
letters = { 'a' : 'm', 'b' : 'd', 'c' : 'l', 'd' : 'x', 'e' : 'j', 'f' : 't', 'g' : 'u', 'h' : 'k', 'i' : 'z', 'j' : 'd', 'k' : 'o', 'l' : 'y', 'm' : 'i', 'n' : 'v', 'o' : 'p', 'p' : 'q', 'q' : 'f', 'r' : 'c', 's' : 'r', 't' : 'b', 'u' : 'j', 'v' : 'w', 'w' : 'n', 'x' : 'h', 'y' : 's', 'z' : 'a' }

message = raw_input ("Enter your message : ").lower()

encrypted = ""

for letter in message :
	if letter in letters:
		encrypted += letters[letter]	
	else:
		encrypted += letter
		
print (encrypted)	


type2 : encryption using ord() and char()

message = raw_input ("Enter a message to encrypt: ").upper()

encrypted = ""

for letter in message :
	if letter == " ":
		encrypted += " "
	else:
		encrypted += chr(ord(letter)+5)
		
print (encrypted)


type3: encryption using index location 

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 			0123456789				  25

message = raw_input ("Enter a message to encrypt: ").upper()

encrypted = ""

for letter in message :
	if letter == " ":
		encrypted += letter	
	elif ALPHABET.index(letter) + 5 > len(ALPHABET):
		encrypted += ALPHABET[ALPHABET.index(letter) + 5 - 26]
	else:
		encrypted += ALPHABET[ALPHABET.index(letter) + 5]
		
print (encrypted)
