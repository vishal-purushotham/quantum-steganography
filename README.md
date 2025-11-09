# Quantum Steganography

A hybrid security protocol that combines **BB84 Quantum Key Distribution (QKD)** with **classical steganography** to securely encrypt and hide messages.

## Overview

This project demonstrates a two-layer security approach:

1. **Quantum Key Distribution (BB84 Protocol):** Alice and Bob generate a shared secret key using quantum mechanics principles. The security is guaranteed by the fundamental laws of quantum physics - any eavesdropping attempt would disturb the quantum states and be detected.

2. **Classical Steganography:** The quantum-generated key is used as a one-time pad to encrypt a secret message. The encrypted message is then hidden within normal-looking text by manipulating the case of letters.

## Features

- Modern implementation using **Qiskit 1.0+**
- BB84 protocol with quantum circuit simulation
- One-time pad encryption for perfect secrecy
- Steganographic encoding/decoding using letter case
- Complete end-to-end demonstration

## Prerequisites

- Python 3.8 or newer
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vishal-purushotham/quantum-steganography.git
cd quantum-steganography
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
quantum-steganography/
├── bb84_protocol.py      # BB84 Quantum Key Distribution implementation
├── steganography.py      # Classical encryption and steganography functions
├── main.py              # Main demonstration script
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Usage

Run the main demonstration:

```bash
python main.py
```

### What happens when you run it:

1. **Quantum Key Exchange:** Alice and Bob perform the BB84 protocol to generate a shared secret key
2. **Encryption:** Alice encrypts her message using the quantum key as a one-time pad
3. **Steganography:** The encrypted binary data is hidden in a carrier text by changing letter cases
4. **Transmission:** Bob receives the innocent-looking text
5. **Extraction:** Bob extracts the hidden binary message from the text
6. **Decryption:** Bob decrypts the message using his copy of the quantum key
7. **Verification:** The system verifies that the decrypted message matches the original

### Sample Output

```
--- Starting BB84 Protocol ---
Alice's initial bits: 011010...
Alice's chosen bases: 110010...
Bob's chosen bases:   010110...
Bob's measured bits:  010110...

Sifted key: 10110100...
--- BB84 Protocol Finished ---

--- Starting Classical Encryption & Steganography ---
Original secret message: 'Quantum is the future!'
Encrypted binary stream (first 64 bits): 0010100111110001...

Carrier text after hiding message:
'in ThE heART OF the BUStLINg CITY...'

Decrypted secret message: 'Quantum is the future!'
--- Process Complete ---

Verification successful: The original and decrypted messages match!
```

## How It Works

### BB84 Protocol

1. Alice generates random bits and randomly chooses measurement bases (Z or X)
2. Alice prepares qubits based on her bits and bases
3. Bob randomly chooses measurement bases and measures the qubits
4. Alice and Bob compare their bases (without revealing the bits)
5. They keep only the bits where their bases matched (sifting)
6. The result is a shared secret key

### Steganography

- **Encryption:** Each character of the message is XORed with bits from the quantum key
- **Encoding:** Each bit of the encrypted message is hidden in the carrier text:
  - `1` → uppercase letter
  - `0` → lowercase letter
- **Decoding:** Bob extracts bits from the text case and decrypts using the key

## Security Features

- **Quantum Security:** Any eavesdropping on the quantum channel would be detected due to quantum measurement disturbance
- **One-Time Pad:** Provides perfect secrecy when the key is truly random and used only once
- **Steganography:** Hides the existence of the encrypted message in plain sight

## Technical Details

- **Quantum Simulator:** Uses Qiskit's `AerSimulator` for quantum circuit simulation
- **Key Length:** Uses 300 qubits to generate approximately 150 bits of sifted key
- **Encryption:** XOR-based one-time pad with 8 bits per character

## Dependencies

- `qiskit>=1.0.0` - Quantum computing framework
- `qiskit-aer` - High-performance quantum circuit simulator
- `matplotlib` - Plotting library (for potential visualizations)
- `numpy` - Numerical computing library

## Limitations

- This is a **simulation** using classical computers - real quantum key distribution requires actual quantum hardware
- The carrier text must be long enough to hide the entire encrypted message
- In practice, additional error correction and privacy amplification would be needed

## Future Enhancements

- Add quantum channel noise simulation
- Implement error correction protocols
- Add privacy amplification
- Create visualization of the BB84 protocol
- Support for different steganography methods
- Real quantum hardware integration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## References

- [BB84 Protocol](https://en.wikipedia.org/wiki/BB84) - Original quantum key distribution protocol
- [Qiskit Documentation](https://qiskit.org/documentation/) - Quantum computing framework
- [One-Time Pad](https://en.wikipedia.org/wiki/One-time_pad) - Perfect encryption cipher

## Author

Created as a demonstration of quantum cryptography and steganography integration.

---

**Note:** This is an educational project demonstrating the concepts of quantum key distribution and steganography. For production use, additional security measures and real quantum hardware would be required.
