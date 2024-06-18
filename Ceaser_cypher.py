def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for i in range(len(text)):
        char = text[i]

        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Add any non-alphabet characters unchanged
        else:
            result += char

    return result

# Get user choice
mode = input("Do you want to encrypt or decrypt? ").strip().lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
else:
    # Get input from the user
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    # Call the caesar_cipher function
    result_text = caesar_cipher(text, shift, mode)

    # Display the result
    if mode == "encrypt":
        print("Encrypted text:", result_text)
    else:
        print("Decrypted text:", result_text)
