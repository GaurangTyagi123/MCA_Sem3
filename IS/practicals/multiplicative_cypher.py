def encrypt(original_string:str,key:int=0)->str :
    def get_pos(character:str,upper:bool=True):
        return ord(character) - ord('A') if upper else ord(character)- ord('a')
    if key < 0 or key > 25:
        return "invalid key"
    cyph:str = list(map(lambda x: chr(((get_pos(x)*key)%26) + ord('A')) if x.isupper() else chr(((get_pos(x,False)*key)%26) + ord('a')),original_string))
    return "".join(cyph)

def decrypt(cyph:str,key:int=0)->str:
    def get_pos(character:str,upper:bool=True):
        return ord(character) - ord('A') if upper else ord(character)- ord('a')
    def extended_euclidean(a,b):
        if(b == 0):
            return a,1,0
        gcd,x1,y1 = extended_euclidean(b,a%b)
        x = y1
        y = x1 - (a//b)*y1
        
        return gcd,x,y
    def modular_inverse(key,base=26):
        gcd,x,y = extended_euclidean(key,base)
        if gcd != 1:
            raise ValueError("modular inverse does not exist")
        return x%base
    
    if key < 0 or key > 25:
            return "invalid key"
    cyph:str = list(map(lambda x: chr(((get_pos(x)*modular_inverse(key))%26) + ord('A')) if x.isupper() else chr(((get_pos(x,False)*modular_inverse(key))%26) + ord('a')),cyph))
    return "".join(cyph)
    
    
    
if __name__ == "__main__":
    text:str = input("enter text: ")
    key:int = int(input("enter key: "))
    
    cyph:str = encrypt(text,key)
    print(f"ENCRYPTED TEXT : {cyph}")
    print(f"DECRYPTED TEXT : {decrypt(cyph,key)}")