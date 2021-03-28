## Steganography - War and Pieces

I saw the hint that its nothing to do with EXIF data and just old school steg, so i began looking at the image carefully.

I remembered that flags start with UMASS{ and end with } 
So i thought it could be possible that each soldier represented a byte or 4 bits.

It would make sense to start reading from top left going right.
Looking at the image, i noticed the last two soldiers in the first row, and first two soldiers in the second row were the same. 
They correspond to the letters (SS from UMASS) so i knew i was on the right track.

First letter is U = 85 in decimal = 0101 0101 binary 

I started writing it all down in notepad but I couldn't solve it by hand because the flag didn't make sense...

After figuring out half the soldiers values, i was left with unknown ones that could be either 0000, 1000, 1010, 1100, 1110... 
I knew that the flag almost always contains character _ as well.
So i wrote a python script to permute the possible choices left for me. It outputted 420 results (hehe) and I looked for the one that made the most sense in "english".

flag: UMASS{lfl_t0v_s0lj4s}