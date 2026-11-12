def count_bits(n:int):
    bits = 0
    
    while(n):
        bits += 1
        n >>= 1;  
    return bits



def crc(message,generator):
    message = int(message,2)
    generator = int(generator,2)
    
    message_length = count_bits(message)
    generator_length = count_bits(generator)
    
    if message_length < generator_length :
        raise ValueError("MESSAGE LENGTH TOO SHORT")
    
    remainder = message << (generator_length - 1)
    remainder_length = message_length + generator_length - 1
    
    while(remainder_length >= generator_length):
        remainder = remainder ^ (generator << (remainder_length - generator_length))
        remainder_length = count_bits(remainder)
        
    remainder = format(remainder,f'0{generator_length-1}b')
    message = format(message,'b')
    codeword = message + remainder
    
    return codeword    

def crc_check(codeword,generator):
    codeword = int(codeword,2)
    generator = int(generator,2)
    
    codeword_length = count_bits(codeword)
    generator_legnth = count_bits(generator)
    
    
    remainder = codeword
    remainder_length = codeword_length
    
    while(remainder_length >= generator_legnth):
        remainder = remainder ^ (generator << (remainder_length - generator_legnth))
        remainder_length = count_bits(remainder)
        
    return remainder == 0
    
def main():
    message = input("Enter message ")
    generator = input("Enter generator ")
    
    codeword = crc(message,generator)
    
    print(f"ORIGINAL MESSAGE: {message}")
    print(f"CODEWORD : {codeword}")
    
    # incorrect
    # print("CORRECT") if crc_check("1111",generator) else print("INCORRECT")
    
    # correct
    print("CORRECT") if crc_check(codeword,generator) else print("INCORRECT")
    
    
if __name__ == '__main__':
    main()