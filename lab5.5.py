# FILE: 2252__AAhmed_Lab05_CoderDecoder.py
# NAME: Encoder/Decoder
# AUTHOR(s): ABDIRAHMAN ahmed
# DATE: 11/5/2024

#Correction LAB 


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = list(alphabet)

def encode_message(message):
    encoded = []
    for char in message:
        if char.isalpha():
            position = alphabet_list.index(char.lower()) + 1
            encoded.append(str(position))
        else:
            encoded.append(char)
    return "-".join(encoded)

def decode_message(code):
    decoded = []
    parts = code.split("-")
    for part in parts:
        if part.isdigit():
            position = int(part) - 1
            letter = alphabet_list[position]
            decoded.append(letter)
        else:
            decoded.append(part)
    return "".join(decoded)

print("Welcome to the Coder/Decoder Program!")
print("Choose an option:")
print("1. Encode a message")
print("2. Decode a message")
choice = input("Enter 1 or 2: ")

if choice == "1":
    message = input("Enter the message to encode: ")
    print("Encoded message:", encode_message(message))
elif choice == "2":
    code = input("Enter the code to decode: ")
    print("Decoded message:", decode_message(code))
else:
    print("Invalid choice. Please enter 1 or 2.")