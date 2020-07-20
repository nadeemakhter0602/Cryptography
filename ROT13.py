import string
letters=string.ascii_letters
s_table=dict()
for i in range(len(letters)):
    s_table[letters[i]]=letters[(i+13)%len(letters)]
def enc(plaintext):
    ciphertext=''
    for i in plaintext:
        if i in letters:
            ciphertext=ciphertext+s_table[i]
        else:
            ciphertext=ciphertext+i
    return ciphertext
choice=input("You wanna Encrypt[0] or Decrypt[1]?\n")
if(choice=="0" or choice.lower=="encrypt"):
    plaintext=input("Enter text to encrypt : \n")
    print("Encrypted Text :")
    print(enc(plaintext))
elif(choice=="1" or choice.lower=="decrypt"):
    ciphertext=input("Enter text to decrypt : \n")
    print("Decrypted Text :")
    print(enc(ciphertext))
else:
    print("Invalid Choice Buddy, Bye.")
