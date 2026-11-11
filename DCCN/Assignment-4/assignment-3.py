def bits_count(data):
    bits = 0

    while data > 0:
        bits += 1
        data >>= 1

    return bits


def crc(message, generator):
    msg = int(message, 2)
    gen = int(generator, 2)

    msg_len = bits_count(msg)
    gen_len = bits_count(gen)

    if msg_len < gen_len:
        print("Error: generator has to be less long than message")
        return ""

    rem = msg << (gen_len - 1)
    rem_len = msg_len + gen_len - 1

    while rem_len >= gen_len:
        rem = rem ^ (gen << (rem_len - gen_len))
        rem_len = bits_count(rem)

    print(f"\nRemainder: {rem:b}\n")

    codeword = ""

    for i in range(msg_len - 1, -1, -1):
        codeword += '1' if (msg & 1) else '0'
        msg >>= 1

    return codeword


def main():
    message = input("Enter message: ")
    generator = input("Enter generator: ")

    codeword = crc(message, generator)

    print(f"Sender codeword: {codeword}")


if __name__ == "__main__":
    main()