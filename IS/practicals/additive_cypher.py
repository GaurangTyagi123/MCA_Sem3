def encrypt(original_string:str,key:int=0)->str :
    def get_pos(character:str,upper:bool=True):
        return ord(character) - ord('A') if upper else ord(character)- ord('a')
    if key < 0 or key > 25:
        return "invalid key"
    cyph:str = list(map(lambda x: chr(((get_pos(x)+key)%26) + ord('A')) if x.isupper() else chr(((get_pos(x,False)+key)%26) + ord('a')),original_string))
    return "".join(cyph)

def decrypt(cyph:str,key:int=0)->str:
    def get_pos(character:str,upper:bool=True):
        return ord(character) - ord('A') if upper else ord(character)- ord('a')
    if key < 0 or key > 25:
        return "invalid key"
    cyph:str = list(map(lambda x: chr(((get_pos(x)-key)%26) + ord('A')) if x.isupper() else chr(((get_pos(x,False)-key)%26) + ord('a')),cyph))
    return "".join(cyph)
    
if __name__ == "__main__":
    text:str = input("enter text: ")
    key:int = int(input("enter key: "))
    
    cyph:str = encrypt(text,key)
    print(f"ENCRYPTED TEXT : {cyph}")
    print(f"DECRYPTED TEXT : {decrypt(cyph,key)}")