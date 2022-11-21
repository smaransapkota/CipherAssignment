def encrypt(name,depth):
    encrypted_text=''
    if int(len(name)/depth)!=len(name)/depth:
        cel=(int(len(name)/depth))+1
        if cel*depth==len(name):
            for i in range(len(name)):
                if(i==len(name)-1):
                    encrypted_text+=name[i]
                    break
                encrypted_text+=name[(i+(depth-1)*i)%(len(name)-1)]
        else:
            add_alpha=['#' for i in range((cel*depth)%len(name))]
            name+=''.join(add_alpha)
            print(name)
            for i in range(len(name)):
                if(i==len(name)-1):
                    encrypted_text+=name[i]
                    break
                encrypted_text+=name[(i+(depth-1)*i)%(len(name)-1)]
    else:
        for i in range(len(name)):
                if(i==len(name)-1):
                    encrypted_text+=name[i]
                    break
                encrypted_text+=name[(i+(depth-1)*i)%(len(name)-1)]


    return encrypted_text

def decrypt(string,depth):
    decrypted_text=''
    celling=int((len(string)/depth))
    for i in range(len(string)):
        if(i==len(string)-1):
            decrypted_text+=string[i]
            break
        decrypted_text+=string[(i+(celling-1)*i)%(len(string)-1)]
    return decrypted_text

if __name__ == "__main__":
    name="SMARANSAPKOTA"
    depth=int(input("Enter the depth"))
    encoded=encrypt(name,depth)
    print(encoded)
    print(decrypt(encoded,depth))
    