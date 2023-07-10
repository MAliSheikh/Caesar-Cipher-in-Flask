alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True


def shift_encrypt(text, shift_amount):
    encrypted_text = ""
    for letter in text:
        if letter in alphabets: 
            position = alphabets.index(letter)
            new_position = position + shift_amount
            encrypted_text += alphabets[new_position]
        else:
            encrypted_text += letter
    print(f"The Shift Cipher encoded text is '{encrypted_text}'")

def shift_decrypt(text, shift_amount):
    decrypted_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position - shift_amount
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += letter
    print(f"The Shift Cipher decoded text is '{decrypted_text}'")

def ceaser_encrpyt(text):
    encrypted_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position + 3
            encrypted_text += alphabets[new_position]
        else:
            encrypted_text += letter

    print(f"The Ceaser Cipher encoded text is '{encrypted_text}'")

def ceaser_decrypt(text):
    decrypted_text = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position - 3
            decrypted_text += alphabets[new_position]
        else:
            decrypted_text += letter

    print(f"The Ceaser Cipher decoded text is '{decrypted_text}'")


while should_continue:

    option = input("type 'ceaser' for Ceaser Cipher, type 'shift' for Shift Cipher: \n")

    if option == 'ceaser':
        direction = input("type 'encode' to encrypt, type 'decode' to decrypt: \n")
        text = input("Please enter your message: \n").lower()
        if direction == 'encode':
            ceaser_encrpyt(text)
        elif direction == 'decode':
            ceaser_decrypt(text)
        else:
            print("Invalid input")
            print("Please enter a valid option")

    elif option == 'shift':
        direction = input("type 'encode' to encrypt, type 'decode' to decrypt: \n")
        text = input("Please enter your message: \n").lower()
        shift = int(input("Enter the shift amount: \n"))

        if direction == 'encode':
            shift_encrypt(text=text, shift_amount=shift)
        elif direction == 'decode':
            shift_decrypt(text=text, shift_amount=shift)
        else:
            print("Invalid input")
            print("Please enter a valid option")
    
    else:
        print("Invalid input")
        print("Please enter a valid option")

    again = input("Type any key to continue. type 'Q / q' to close the program.  \n").lower()

    if again == 'q':
        should_continue = False
        
