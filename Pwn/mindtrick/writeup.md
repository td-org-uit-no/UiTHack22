The Empire has fallen for the age old trap of rolling their own cryptography: 
the hash is not cryptographic - specifically, it is the 256-bit version of FNV-1 https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function

At this point you may try to bruteforce the entire hash, but there is a simpler way - note that the hash isn't being compared with memcmp, but with strncmp (https://en.cppreference.com/w/c/string/byte/strncmp). The hashes are not being compared as byte arrays, but as null-terminated strings!

This means that the input and expected hash are only compared until the first null byte. Since the Empire managed to put a null byte in the second byte of the password hash, any hash with `0x1c 0x00` as the first two bytes will qualify. This makes it very easy to find a hash collision (as in `solution.c`): for instance, `28488aaaaaaaaaaaaaaaaaaaaaaaaa` will qualify.

(The full passphrase is "0ItIsNotATaleTheJediWouldTellYouTheTaleOfDarthPlagueis".)