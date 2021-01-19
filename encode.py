from dicktionary import MorseCode


def encode_to_morse(text: str) -> str:
	global MorseCode
	result = ''
	for char in text:
		if char in MorseCode:
			result += MorseCode[char]
		else:
			result += char
	return result
