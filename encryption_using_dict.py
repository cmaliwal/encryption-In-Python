#simple Encryption :

letters = { 'a' : 'm', 'b' : 'd', 'c' : 'l', 'd' : 'x', 'e' : 'j', 'f' : 't', 'g' : 'u', 'h' : 'k', 'i' : 'z', 'j' : 'd', 'k' : 'o', 'l' : 'y', 'm' : 'i', 'n' : 'v', 'o' : 'p', 'p' : 'q', 'q' : 'f', 'r' : 'c', 's' : 'r', 't' : 'b', 'u' : 'j', 'v' : 'w', 'w' : 'n', 'x' : 'h', 'y' : 's', 'z' : 'a' }

message = raw_input ("Enter your message : ").lower()

encrypted = ""

for letter in message :
	if letter in letters:
		encrypted += letters[letter]	
	else:
		encrypted += letter
		
print (encrypted)	