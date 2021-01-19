def decode_from_morse(code: str) -> str:
	global MorseCode
	buffer = ""
	result = ""
	for char in code:
		buffer += code
		if buffer in MorseCode:
			result += MorseCode[buffer]
			buffer = ""
	return result
