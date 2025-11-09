# main.py

from bb84_protocol import perform_bb84
from steganography import (
    encrypt_onetimepad, 
    stega_encoder, 
    stega_decoder,
    decrypt_onetimepad
)

def main():
    # --- Configuration ---
    NUM_QUBITS = 300  # More qubits for a longer, more secure key
    SECRET_MESSAGE = "Quantum is the future!"
    CARRIER_TEXT = (
        "In the heart of the bustling city, where skyscrapers kissed the clouds and "
        "the rhythm of life beat like a relentless drum, there lived a quiet watchmaker "
        "named Elias. His shop, a tiny nook nestled between a loud cafe and a modern "
        "art gallery, was a relic of a bygone era. The air inside smelled of aged wood, "
        "polished brass, and the faint, metallic scent of time itself. Elias was a master "
        "of his craft, his fingers, though wrinkled, moved with the precision of a surgeon, "
        "coaxing life back into forgotten timepieces."
    )

    # --- 1. Quantum Key Exchange ---
    # Alice and Bob generate a secure shared key using the BB84 protocol.
    shared_key = perform_bb84(num_qubits=NUM_QUBITS)

    # Ensure the key is long enough for the message
    if len(shared_key) < len(SECRET_MESSAGE) * 8:
        print("\n!!! Warning: Sifted key is too short for a secure one-time pad. Rerunning protocol. !!!\n")
        main() # Rerun the entire process
        return

    # --- 2. Classical Encryption ---
    # Alice encrypts her secret message using the shared key as a one-time pad.
    print("--- Starting Classical Encryption & Steganography ---")
    print(f"Original secret message: '{SECRET_MESSAGE}'")
    encrypted_binary_message = encrypt_onetimepad(shared_key, SECRET_MESSAGE)
    print(f"Encrypted binary stream (first 64 bits): {encrypted_binary_message[:64]}...")

    # --- 3. Steganography Encoding ---
    # Alice hides the encrypted binary message within the carrier text.
    steganographic_text = stega_encoder(encrypted_binary_message, CARRIER_TEXT)
    print(f"\nCarrier text after hiding message:\n'{steganographic_text}'\n")

    # --- Communication happens here: Bob receives the steganographic_text ---
    
    # --- 4. Steganography Decoding ---
    # Bob receives the text and extracts the hidden binary message.
    # He knows the expected length of the binary message (8 bits per character).
    message_length_in_bits = len(SECRET_MESSAGE) * 8
    extracted_binary_message = stega_decoder(steganographic_text, message_length_in_bits)
    print(f"Bob extracted binary stream (first 64 bits): {extracted_binary_message[:64]}...")

    # --- 5. Classical Decryption ---
    # Bob uses his copy of the shared key to decrypt the binary message.
    decrypted_message = decrypt_onetimepad(shared_key, extracted_binary_message)
    print(f"\nDecrypted secret message: '{decrypted_message}'")
    print("--- Process Complete ---")

    # --- Verification ---
    assert SECRET_MESSAGE == decrypted_message
    print("\nVerification successful: The original and decrypted messages match!")

if __name__ == '__main__':
    main()
