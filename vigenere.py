from sys import argv
import re

def crypt(mList, kList, sign):
	messageLen = len(mList)
	keyLen = len(kList)
	codeList = list(range(messageLen))

	for cur in range(messageLen):
		codeList[cur] = addLetters(mList[cur], kList[cur % keyLen], sign)

	print ''.join(codeList)

def addLetters(mLet, kLet, sign):
	val = (ord(mLet) - 65) + sign * (ord(kLet) - 65)
	val %= 26
	return chr(val + 65)

def validateInput(ans):
	while(ans != 'e' and ans != 'd'):
		ans = raw_input("Invalid. Encrypt (e) or Decrypt (d)\n>")
	return ans

def main():
	regex = re.compile('[^a-zA-Z]')
	mList = list(regex.sub('', argv[1]).upper())
	kList = list(regex.sub('', argv[2]).upper())
	ans = validateInput(raw_input("Encrypt (e) or Decrypt (d)\n>").lower())
	sign = 1 if ans == 'e' else -1
	crypt(argv[1], argv[2], sign)

if __name__ == "__main__":
	main()
