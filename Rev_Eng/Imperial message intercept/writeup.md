> # Imperial message intercept
> > Rev-Eng - 200pt
>
> The rebels have infiltrated an imperial cruiser and extracted a crucial part of their encryption system.  
> You have been recruited to help them reverse engineer the code and use it to decrypt their covert communications.  
> Based on inside knowledge you also know that the first letters are always the same in these messages.
>
> The following message was just intercepted by a communications satelite, can you use the encryption code to decipher the message?
>
> ```
> 77 74 6A 6E 52 15 6F 79 09 42 21 4D 78 31 4B 6C 43 03 0C 79 45 42 0F 1E 20 27 45 57 16 70 7B 4D 57 3A 6E 2C 04 41 58 21 31 43 53 43 23 2C 4A 11
> ```
> Files: [source code](./scr)


## Writeup

Upon inspecting the source code you discover that the encryption algorithm uses xor with random outputs based on a key to produce its output.
We also see that the maximum value the key can have is 0xFFFFFF or 2^28.
We also know that the first 10 letters of the flag will always be "UiTHack22{" so we can use this to verify if our solution is correct.
Based on this we can create a function as such that will bruteforce the solution based on the input.

This can also be found in [this file](./src/solve.c).

```c
void solve(char* encrypted) {
    int N = strlen(encrypted);
    char* tmp = malloc(sizeof(char) * N);
    char* template = "UiTHack22{";

    for (long i = 0; i < (1 << 28); i++) {
        strcpy(tmp, encrypted);
        encrypt(tmp, i, N);
        if (strncmp(tmp, template, 10) == 0) {
            printf("key: %ld flag: %s\n", i, tmp);
            break;
        }
    }
    free(tmp);
}
```

This will result in finding the following flag, encrypted with the key 256089778.

```
UiTHack22{there_is_a_ReBel_BaSe_on_HOth__ENGage}
```