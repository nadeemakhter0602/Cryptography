import string
letters=string.ascii_letters
letters=[i.upper() for i in letters]
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
choice=input("You wanna Encode[0] or Decode[1]?\n")
if(choice=="0" or choice.lower=="encrypt"):
    plaintext=input("Enter text to encode : \n").upper()
    print("Encoded Text :")
    print(enc(plaintext))
elif(choice=="1" or choice.lower=="decrypt"):
    ciphertext=input("Enter text to decode : \n").upper()
    print("Decoded Text :")
    print(enc(ciphertext))
else:
    print("Invalid Choice Buddy, Bye.")
