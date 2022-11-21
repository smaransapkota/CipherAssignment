
def encrypt(key,string,alphabets):
    encrypted_arr=[]
    for i in range(len(key)):
        sum_alphabets=(alphabets.index(string[i])+alphabets.index(key[i]))%26
        encrypted_arr.append(alphabets[sum_alphabets])

    return "".join(encrypted_arr)

def decrypt(key,string,alphabets):
    decrypted_arr=[]
    for i in range(len(key)):
        sub_alphabets=(alphabets.index(string[i])-alphabets.index(key[i]))%26
        decrypted_arr.append(alphabets[sub_alphabets])

    return "".join(decrypted_arr)
    

if __name__ == "__main__":
    alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    name="SMARANSAPKOTA"
    key=input("Enter the key: ")
    if len(key)!=len(name):
        print("key length should be equal to length of name.")
    else:
        encrypted_name=encrypt(key,name,alphabets)
        print(encrypted_name)
        print(decrypt(key,encrypted_name,alphabets))

   
    

    

