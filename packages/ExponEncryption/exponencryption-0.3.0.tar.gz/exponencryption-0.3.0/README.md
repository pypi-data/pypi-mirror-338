# ExponEncryption

A secure Python library for string encryption using an exponential encryption algorithm.

## Installation

You can install ExponEncryption using pip:

```bash
pip install ExponEncryption
```

## Features

- Secure string encryption using exponential encryption algorithm
- Password-based encryption
- Easy-to-use API
- Flask-based web interface for interactive use

## Usage

### As a Library

```python
from ExponEncryption import ExponEncryption

# Create an instance of the encryption class
encryptor = ExponEncryption()

# Encrypt a message
message = "Hello, World!"
password = "your_secret_password"
encrypted_text, key = encryptor.encrypt(message, password)

# Decrypt the message
decrypted_text = encryptor.decrypt(encrypted_text, key, password)
print(decrypted_text)  # Output: Hello, World!
```



## Security Notes

- Keep your encryption password secure
- Never share your encryption key
- Store encrypted data and keys separately
- Use strong passwords for better security

## Requirements

- Python 3.6 or higher

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

