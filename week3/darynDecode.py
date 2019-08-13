def convert_char(char,key):
    letter = ord(char)
    letter += key
    if letter > 122:
        letter = ((letter - 122) + 96)
    return chr(letter)
    
def decode_char(char,key):
    letter = ord(char)
    letter -= key
    if letter < 97:
        letter = ((letter - 97) + 123)
    return chr(letter)

def convert_message(message,key):
    message = message.split()
    codeword = []
    for word in message:
        currentword = ''
        for char in word:
            currentword += convert_char(char,key)
        codeword.append(currentword)
    return ' '.join(codeword)
    
def decode_message(message,key):
    message = message.split()
    codeword = []
    for word in message:
        currentword = ''
        for char in word:
            currentword += decode_char(char,key)
        codeword.append(currentword)
    return ' '.join(codeword)
    
    
message = 'I Love My Wife'.lower()
key = 16

coded_message = convert_message(message,key)
print(coded_message, ':[coded message]')

# decoded_message = decode_message(coded_message,key)
# print(decoded_message, ':[decoded message]')
