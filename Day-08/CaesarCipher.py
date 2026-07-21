import art
print(art.logo)

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


should_continue = True


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "encode":
                shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) - shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("type 'yes' to restart and 'no' to exit:\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")


    