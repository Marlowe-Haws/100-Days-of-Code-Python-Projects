from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
        	output_text += char
    print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    while True:
        direction = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'q' to quit: ").lower()
        if direction == "q":
            print("Goodbye!")
            exit()
        elif direction != "encode" and direction != "decode":
            print("Please enter 'encode', 'decode', or 'q' only.")
            continue
        else:
            break
            
    text = input("Type your message: ").lower()

    while True:
        shift = input("Type the shift number: ")
        try:
            shift = int(shift)
        except ValueError:
            print("Please enter integers only.")
            continue
        break

    shift = int(shift)
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
