# Solution for UMASS's CTF steg challenge "warandpieces"

from itertools import permutations 
import binascii 

def guess():

    possible_choices = ["0010", "0110", "1000", "1001", "1010", "1100", "1110", "1111", "0000"]
    
    a = "0101" # white soldier crouching left with rifle
    b = "0100" # black soldier waving with rifle
    c = "1101" # white soldier waving with rifle
    d = "1011" # white soldier aiming right with rifle
    e = "0011" # black soldier aiming left with pistol
    f = "0001" # black soldier aiming right with rifle
    g = "0111" # black soldier crouching left with rifle
    h = "" # white soldier aiming left with pistol
    i = "" # white soldier with rifle and handgun
    j = "" # white soldier crouching right with rifle
    k = "" # black soldier crouching right with rifle
    l = "" # black soldier facing backwards
    
    unknown_soldiers = [h,i,j,k,l]
    
    perms = permutations(possible_choices, 5) 
    
    n = 0
    
    for perm in list(perms):
        
        (h,i,j,k,l) = perm
        #print (perm)
        
        string = a + a + b + c + b + f + a + e + \
             a + e + g + d + i + j + i + i + \
             i + j + a + k + g + b + e + h + \
             g + i + a + k + g + e + e + h + \
             i + j + i + l + e + b + g + e + \
             g + c
             
        hexStr = hex(int(string, 2))
        #print(hexStr[2:])
        
        output = binascii.unhexlify(hexStr[2:])
        
        try:
            strOutput = output.decode("ascii")
        except UnicodeDecodeError:
            pass
        else:

            if strOutput.isascii() and strOutput.isprintable() and "_" in strOutput:
                print(strOutput)
                n += 1
            
    # with open('possibilities.txt', 'w') as file:
        # file.write(strOutput)
                
    print ("total possible flags:" + str(n))
    
   
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
    
if __name__ == "__main__":
    guess()