#encryption using ord() and char()

message = raw_input ("Enter a message to encrypt: ").upper()

encrypted = ""

for letter in message :
	if letter == " ":
		encrypted += " "
	else:
		encrypted += chr(ord(letter)+5)
		
print (encrypted)