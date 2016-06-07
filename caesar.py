import sys

def encrypt(message, shift):
	arr = list(message)
	var = ''.join([shiftLetter(x, shift) for x in arr])
	print(var)
	return var
	
def decrypt(message, shift):
	return encrypt(message, -shift)

def shiftLetter(let, shift):
	ilet = ord(let)
	tmp = 0
	if ilet in list(range(65, 90)):
		tmp = (ilet - 65 + shift) % 26
        let = chr(65 + tmp)
	if ilet in list(range(97, 122)):
		tmp = (ilet - 97 + shift) % 26
        let = chr(97 + tmp)
	return let

def main():
	shift = 3 if len(sys.argv) < 4 else int(sys.argv[3]) 
	if sys.argv[2] == "e":
		encrypt(sys.argv[1], shift)
	else:
		decrypt(sys.argv[1], shift)

###

if __name__ == "__main__":
	main()
