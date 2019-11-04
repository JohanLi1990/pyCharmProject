#we need the alphabet because we convert letters into numerical values to be able to use
#mathematical operations (note we encrypt the spaces as well)

#The Vigenere Algo
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(text, key, enc=True):
    text = text.upper()
    key = key.upper()
    processed_text = ''
    key_index = 0
    if enc:
        print("encrypting " + text)
    else:
        print("decrypting " + text)

    for chars in text:
        if enc:
            index = (ALPHABET.find(chars) +
                     ALPHABET.find(key[key_index])) % len(ALPHABET)
        else:
            index = (ALPHABET.find(chars) -
                     ALPHABET.find(key[key_index])) % len(ALPHABET)

        processed_text += ALPHABET[index]
        key_index += 1
        if key_index == len(key):
            key_index = 0

    return processed_text


if __name__ == '__main__':
    print("program starts:..... \n")
    output = vigenere_encrypt("I am lichenyang", "CYLI")
    print("encrypted text: "+ output)
    print(vigenere_encrypt(output, "CYLI", False))

