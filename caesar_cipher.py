import time,sys
encrypted_result=[]
decrypted_result=[]

def encrypt_caesar_cipher():
    '''
    DOCSTRING: Function to encrypt a given string using caesar cipher.
    \nINPUT: Any string.
    \nLOGIC: To encrypt, it uses the basic formula : (character + shift digits)
    \nOUTPUT: The encrypted string result.
    \n\nThis logic uses ASCII codes to convert the strings to integers. It uses Python's in-built ord() method.
    \nFirst, we convert the input string to lower-case (since upper-case has a different set of ASCII Codes). To normalise, we convert input strings to lowercase.
    \nThen,we get the number of digits that you want to shift. Then we read each letter in the word using a for loop.
    \nWe calculate the shift character using the formula : (character + shift digits).
    \nIf the values go more than the ASCII Code of 'z' (the last character in the alphabet,i.e. 122).
    \nIf it does, minus the value with 122 & add the result with 96 (If the letter crosses z, loop back from a).
    \nAppend it to the list
    \nElse, print the character value of the word using Python's inbuilt method chr().
    \nFinally, to print the string, join the individual characters of the list using join() and list comprehension for loop.
    \nClear the list at the end otherwise, retrying will keep appending all old results to the list continuously.
    '''
    global encrypted_result
    word = input("Enter a sentence to encrypt: ")
    word = word.lower()
    n = int(input("Enter the number of characters you want to shift: "))
    for w in range(len(word)):
        x = (ord(word[w]) + n)
        if x > 122:
            y = (x-122)+96
            encrypted_result.append(chr(y))
        elif ord(word[w]) == 32:
            y = 32
            encrypted_result.append(chr(y))
        else:
            encrypted_result.append(chr(x))
    print("\nThe encrypted result is",''.join([str(s) for s in encrypted_result]))
    encrypted_result.clear()
    retry()

def decrypt_caesar_cipher():
    '''
    DOCSTRING: Function to decrypt a given string using caesar cipher.
    \nINPUT: Any string.
    \nLOGIC: To decrypt, it uses the basic formula : (character + shift digits)
    \nOUTPUT: The decrypted string result.
    \n\nThis logic uses ASCII codes to convert the strings to integers. It uses Python's in-built ord() method.
    \nFirst, we convert the input string to lower-case (since upper-case has a different set of ASCII Codes). To normalise, we convert input strings to lowercase.
    \nThen,we get the number of digits that you want to shift. Then we read each letter in the word using a for loop.
    \nWe calculate the shift character using the formula : (character - shift digits).
    \nIf the values go more than the ASCII Code of 'a' (the first character in the alphabet,i.e. 96). First letter because we're going in reverse.
    \nIf it does, minus the value with 96 & add the result with 122 (If the letter crosses a, loop back from z).
    \nAppend it to the list
    \nElse, print the character value of the word using Python's inbuilt method chr().
    \nFinally, to print the string, join the individual characters of the list using join() and list comprehension for loop.
    \nClear the list at the end otherwise, retrying will keep appending all old results to the list continuously.
    '''
    global decrypted_result
    word = input("Enter a sentence to decrypt: ")
    word = word.lower()
    n = int(input("Enter the number of characters you want to shift: "))
    for w in range(len(word)):
        x = (ord(word[w]) - n)
        if x>=70 and x < 97:
            y = (x-96)+122
            decrypted_result.append(chr(y))
        elif ord(word[w]) == 32:
            decrypted_result.append(chr(32))
        else:
            decrypted_result.append(chr(x))
    decrypted_results = ''.join([str(s).capitalize() for s in decrypted_result])
    print("\nThe decrypted result is",decrypted_results.capitalize())
    decrypted_result.clear()
    retry()

def bruteforce_caesarcipher_decrypter():
    '''
    DOCSTRING: Function to decrypt a given string that's encrypted using caesar cipher 
    when you don't know the number of shift digits it has been encrypted with
    INPUT: Any string
    OUTPUT: All possible decrypted string results from which you can choose the right string
    '''
    global decrypted_result,n,word
    word = word.lower()
    for w in range(len(word)):
        x = (ord(word[w]) - n)
        if x>=70 and x < 97:
            y = (x-96)+122
            decrypted_result.append(chr(y))
        elif ord(word[w]) == 32:
            decrypted_result.append(chr(32))
        else:
            decrypted_result.append(chr(x))
    print("\nThe decrypted result is",''.join([str(s) for s in decrypted_result]))
    decrypted_result.clear()

def cipher_game():
    '''
    DOCSTRING: Function to accept the user's choice of what they want to do: Whether they want to encrypt a string
    or, decrypt a string encrypted string using Caesar's Cipher.
    INPUT: Numeral choice of 1 (or) 2.
    OUTPUT: Execution of Encryption program (or) Decryption program based on user's choice.
    '''
    global word,n
    choice = int(input("What do you want to do?\n1.Encrypt using Caesar Cipher\n2.Decrypt an encrypted Caesar Cipher\n3.Decrypt a Caesar cipher using brute force\n\nNOTE: Use option 3 to decrypt a Caesar Cipher if you don't know the number of shift digits needed to decrypt.\nThis option loops through 1-26 and gives you all results.\nYou can choose the result that makes sense,from all the results.\n\n"))
    if choice == 1:
        encrypt_caesar_cipher()
    elif choice ==2:
        decrypt_caesar_cipher()
    elif choice ==3:
        word=input("Enter a sentence to decrypt: ")
        for n in range(1,26):
            bruteforce_caesarcipher_decrypter()
        retry()
        

def retry():
    '''
    DOCSTRING: Function to accept user's choice whether they want to retry. If they do, it loops back to the main choice function.
    INPUT: 'y' or anything else
    OUTPUT: If 'y' then, loops back to main choice function - cipher_game() ; else, exits after waiting for 3 seconds
    '''
    ch=input("\nDo you want to try again?(y/n)\n")
    if ch == 'y':
        cipher_game()
    else:
        print("Exiting in 3 seconds...")
        time.sleep(3)
        sys.exit()

cipher_game()
