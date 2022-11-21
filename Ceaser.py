alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name="SMARANSAPKOTA"
shift=int(input("Enter the Shift Value"))


def Encrypted():
    encrypted=''
    for letter in name.upper():
        letters_index=alphabets.index(letter)
        encrypt_letter_index=(letters_index+shift)%26
        encrypted+=alphabets[encrypt_letter_index]
        
    return encrypted

def Decrypted():
    decrypted=''
    for letter in Encrypted():
        letters_index=alphabets.index(letter)
        encrypt_letter_index=(letters_index-shift)%26
        decrypted+=alphabets[encrypt_letter_index]
        

    return decrypted
print(Encrypted())
print(Decrypted())


