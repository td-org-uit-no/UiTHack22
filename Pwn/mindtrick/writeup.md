> # Jedi Mind Trick
> > Pwn - 300 pts
> 
> You are deep in the city of Kra Emer, escorting a set of medical protocol droids to a local hospital, on a secret mission on behalf of the Distributed Interstellar Patient System (DIPS). 
> 
> However, you are suddenly accosted by a set of Imperial stormtroopers, asking to see your identification!
> 
> Can you pull off a Jedi mind trick of your own, and convince them to let you go?
> 
> Hint 1. The hash algorithm is weak, but there's a bigger weakness hiding here...
> 
> Hint 2. Take another look at the password hash comparison. What is it actually checking? Cppreference may be useful.
> 
> Hint 3. Take a look at the password hash, specifically the first two bytes: what happens if you use strncmp?


## Writeup

The Empire has fallen for the age old trap of rolling their own cryptography: 
the hash is not cryptographic - specifically, it is the 256-bit version of FNV-1 https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function

At this point you may try to bruteforce the entire hash, but there is a simpler way - note that the hash isn't being compared with memcmp, but with strncmp (https://en.cppreference.com/w/c/string/byte/strncmp). The hashes are not being compared as byte arrays, but as null-terminated strings!

This means that the input and expected hash are only compared until the first null byte. Since the Empire managed to put a null byte in the second byte of the password hash, any hash with `0x1c 0x00` as the first two bytes will qualify. This makes it very easy to find a hash collision (as in `solution.c`): for instance, `28488aaaaaaaaaaaaaaaaaaaaaaaaa` will qualify.

Entering a hash which collides gives us the flag,  
`UiTHack22{not-a-tale-the-jedi-would-tell-you}`

(The full passphrase is "0ItIsNotATaleTheJediWouldTellYouTheTaleOfDarthPlagueis".)