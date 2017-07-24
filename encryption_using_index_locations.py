#encryption using index location 

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