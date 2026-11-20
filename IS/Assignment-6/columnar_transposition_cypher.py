
def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()

    cols = len(key)
    rows = (len(plaintext) + cols - 1) // cols

    # Pad plaintext if required
    plaintext = plaintext.ljust(rows * cols, 'X')

    # Arrange plaintext row-wise
    matrix = [
        plaintext[i:i + cols]
        for i in range(0, len(plaintext), cols)
    ]

    # Determine column reading order
    order = sorted(range(cols), key=lambda i: (key[i], i))

    ciphertext = ""

    # Read columns according to sorted key
    for col in order:
        for row in range(rows):
            ciphertext += matrix[row][col]

    return ciphertext


def decrypt(ciphertext, key):
    key = key.upper()
    cols = len(key)
    rows = len(ciphertext) // cols

    # Determine column reading order
    order = sorted(range(cols), key=lambda i: (key[i], i))

    # Create empty matrix
    matrix = [[''] * cols for _ in range(rows)]

    index = 0

    # Fill columns according to key order
    for col in order:
        for row in range(rows):
            matrix[row][col] = ciphertext[index]
            index += 1

    # Read matrix row-wise
    plaintext = ''.join(
        matrix[row][col]
        for row in range(rows)
        for col in range(cols)
    )

    return plaintext.rstrip('X')


# Example
plaintext = "Gaurang Tyagi"
key = "watcher"

ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Decrypted:", decrypted)
