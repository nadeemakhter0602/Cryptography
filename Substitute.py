import string
letters=string.ascii_letters
letters=[i.upper() for i in letters]
print(letters)
def generate_table(key):
    s_table=dict()
    for i in range(len(letters)):
        s_table[letters[i]]=letters[(i+key)%len(letters)]
    return s_table
def denc(ciphertext,s_table):
    plaintext=''
    for i in ciphertext:
        if i in letters:
            plaintext=plaintext+s_table[i]
        else:
            plaintext=plaintext+i
    return plaintext
ciphertext=input("Enter text to Encode/Decode : \n").upper()
print("Substituting with all keys 1 through 25....")
for key in range(1,26):
    print("Trying",key,"as substitution cipher key :")
    print(denc(ciphertext,generate_table(key)))
