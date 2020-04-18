import time,sys
encrypted_result=[]
decrypted_result=[]

def caesar_cipher():
    '''
    DOCSTRING: Function to encrypt a given string using caesar cipher.
    INPUT: Any string.
    OUTPUT: The encrypted string result.
    '''
    global encrypted_result
    mystring=input("Enter a sentence to encrypt: ")
    for s in range(len(mystring)):
        ss=ord(mystring[s])+3
        encrypted_result.append(chr(ss))
    print("\nThe encrypted result is",''.join([str(x) for x in encrypted_result]))
    encrypted_result.clear()
    retry()

def rev_caesar_cipher():
    '''
    DOCSTRING: Function to decrypt a given string that's encrypted using caesar cipher.
    INPUT: Any string.
    OUTPUT: The decrypted string result.
    '''
    global decrypted_result
    newstring=input("Enter a sentence to decrypt: ")
    for s in range(len(newstring)):
        sss=ord(newstring[s])-3
        decrypted_result.append(chr(sss))
    print("\nThe decrypted result is ","".join([str(y) for y in decrypted_result]))
    decrypted_result.clear()
    retry()

def cipher_game():
    '''
    DOCSTRING: Function to accept the user's choice of what they want to do: Whether they want to encrypt a string
    or, decrypt a string encrypted string using Caesar's Cipher
    INPUT: Numeral choice of 1 (or) 2
    OUTPUT: Execution of Encryption program (or) Decryption program based on user's choice
    '''
    choice = int(input("What do you want to do?\n1.Encrypt using Caesar Cipher\n2.Decrypt an encrypted Caesar Cipher\n"))
    if choice == 1:
        caesar_cipher()
    elif choice ==2:
        rev_caesar_cipher()

def retry():
    ch=input("\nDo you want to try again?(y/n)\n")
    if ch == 'y':
        cipher_game()
    else:
        print("Exiting in 3 seconds...")
        time.sleep(3)
        sys.exit()

cipher_game()
