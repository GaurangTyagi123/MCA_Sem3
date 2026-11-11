def bits_count(data):
    bits = 0

    while data > 0:
        bits += 1
        data >>= 1

    return bits


def crc_check(codeword, generator):
    cdw = int(codeword, 2)
    gen = int(generator, 2)

    cdw_len = bits_count(cdw)
    gen_len = bits_count(gen)

    if cdw_len < (2 * gen_len):
        print("Error: codeword has to be twice as long as generator")
        return False

    rem = cdw
    rem_len = cdw_len

    while rem_len >= gen_len:
        rem = rem ^ (gen << (rem_len - gen_len))
        rem_len = bits_count(rem)

    return rem == 0


def main():
    codeword = input("Enter codeword: ")
    generator = input("Enter generator: ")

    correct = crc_check(codeword, generator)

    print(f"Received message has {'no ' if correct else ''}error")


if __name__ == "__main__":
    main()