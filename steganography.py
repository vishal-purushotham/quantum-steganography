# steganography.py

def encrypt_onetimepad(key, message):
    """
    Encrypts a message using a one-time pad (XOR operation).
    The key is repeated if it's shorter than the message.
    """
    encrypted_bits = ""
    for i, char in enumerate(message):
        message_bit = format(ord(char), '08b') # Convert character to 8-bit binary
        
        encrypted_char_bits = ""
        for j in range(8):
            key_bit = key[(i * 8 + j) % len(key)]
            xor_result = int(key_bit) ^ int(message_bit[j])
            encrypted_char_bits += str(xor_result)
        encrypted_bits += encrypted_char_bits
    return encrypted_bits


def stega_encoder(binary_message, carrier_text):
    """
    Encodes a binary message into a carrier text by changing letter case.
    """
    encoded_text = ""
    bit_index = 0
    
    for char in carrier_text:
        if bit_index < len(binary_message) and char.isalpha():
            if binary_message[bit_index] == '1':
                encoded_text += char.upper()
            else: # bit is '0'
                encoded_text += char.lower()
            bit_index += 1
        else:
            encoded_text += char
            
    if bit_index < len(binary_message):
        print("Warning: Carrier text was not long enough to hide the full message.")

    return encoded_text


def stega_decoder(encoded_text, key_length_bits):
    """
    Decodes a binary message from a steganographically encoded text.
    """
    decoded_bits = ""
    for char in encoded_text:
        if len(decoded_bits) >= key_length_bits:
            break
        if char.isalpha():
            if char.isupper():
                decoded_bits += '1'
            else:
                decoded_bits += '0'
    return decoded_bits


def decrypt_onetimepad(key, encrypted_bits):
    """
    Decrypts a message using a one-time pad (XOR operation).
    """
    decrypted_message = ""
    for i in range(0, len(encrypted_bits), 8):
        encrypted_char_bits = encrypted_bits[i:i+8]
        if len(encrypted_char_bits) < 8:
            continue

        decrypted_char_bits = ""
        for j in range(8):
            key_bit = key[(i+j) % len(key)]
            xor_result = int(key_bit) ^ int(encrypted_char_bits[j])
            decrypted_char_bits += str(xor_result)
            
        decrypted_char_code = int(decrypted_char_bits, 2)
        decrypted_message += chr(decrypted_char_code)

    return decrypted_message
