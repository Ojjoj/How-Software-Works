def encrypt(key, message):
    encrypted = ""
    for column in range(key):
        encrypted += message[column::key]
    return encrypted


def decrypt(key, message):
    decrypted = [''] * len(message)
    i = 0
    for k in range(key):
        j = k
        while j < len(decrypted):
            decrypted[j] = message[i]
            j += key
            i += 1

    return ''.join(decrypted)


if __name__ == '__main__':
    message = 'cathylikeskeith'
    encrypted = encrypt(3, message)
    decrypted = decrypt(3, encrypted)

    print("Message :", message)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
