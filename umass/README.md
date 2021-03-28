## Steganography - War and Pieces

![original image](clue.jpg)

I saw the hint that its nothing to do with EXIF data and just old school steg, so i began looking at the image carefully.

I remembered that flags start with UMASS{ and end with } 
So i thought it could be possible that each soldier represented a byte or 4 bits.

It would make sense to start reading from top left going right.
Looking at the image, i noticed the last two soldiers in the first row, and first two soldiers in the second row were the same. 
They correspond to the letters (SS from UMASS) so i knew i was on the right track.

First letter is U = 85 in decimal = 0101 0101 binary 

I started writing it all down in notepad but I couldn't solve it by hand because the flag didn't make sense...

![wip](progress.jpg)

After figuring out half the soldiers values, i was left with unknown ones that could be either 0000, 1000, 1010, 1100, 1110... 
I knew that the flag almost always contains character _ as well.
So i wrote a python script to permute the possible choices left for me. It outputted 420 results (hehe) and I looked for the one that made the most sense in "english".

```python
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
        
        string = a + a + b + c + b + f + a + e + \
             a + e + g + d + i + j + i + i + \
             i + j + a + k + g + b + e + h + \
             g + i + a + k + g + e + e + h + \
             i + j + i + l + e + b + g + e + \
             g + c
             
        hexStr = hex(int(string, 2))
        output = binascii.unhexlify(hexStr[2:])
        
        try:
            strOutput = output.decode("ascii")
        except UnicodeDecodeError:
            pass
        else:
            if strOutput.isascii() and strOutput.isprintable() and "_" in strOutput:
                print(strOutput)
                n += 1     
    print ("total possible flags:" + str(n))
    
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
    
if __name__ == "__main__":
    guess()
```
flag: UMASS{lfl_t0v_s0lj4s}
