alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def s_encrypt():
    plaintext = 'hello'
    operation = 'decrypt'
    shift_amount= 4
    
    if operation == "encrypt":
        encrypted_text = ""
        for letter in plaintext:
          if letter in alphabets: 
            position = alphabets.index(letter)
            new_position = position + shift_amount
            encrypted_text += alphabets[new_position]
          else:
            encrypted_text += letter
            return (f"The Shift Cipher encoded text is '{encrypted_text}'")

    elif operation == "decrypt":
        decrypted_text = ""
        for letter in plaintext:
          if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position - shift_amount
            decrypted_text += alphabets[new_position]
          else:
            decrypted_text += letter
            return (f"The Shift Cipher decoded text is '{decrypted_text}'")

print(s_encrypt())