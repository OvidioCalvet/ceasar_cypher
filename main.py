alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(encryption_type, original_text, shift_amount):

    result_text = ""

    if encryption_type == "decode":

        shift_amount *= -1

    for letter in original_text:

        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)

        result_text += alphabet[shifted_position]
    
    print(f"Here is your result: {result_text}")

ceasar(direction, text, shift)