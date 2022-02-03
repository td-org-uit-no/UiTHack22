> # Ephemeral
> You are on a nighttime mission to infiltrate the secret Empire facility known as Re-Al-Phagby G, and rescue the brave programmers imprisoned within.
> However, a numeric keypad lock blocks your way! While nobody is around, the Empire has introduced countermeasures to stop people from simply trying every password.
> Can you still break in?
> Hint 1. We know we only have to try numbers for the password. Try different numbers - do you notice any differences?
> Hint 2. Look closer at the supposed countermeasure to stop bruteforcing - when does it actually trigger?

Thankfully, the Empire's lack of linting has introduced a timing oracle into the `secure_compare` function. Instead of
```
for (size_t i = 0; i < PASSWORD_MAX_LENGTH; i++)
    {
        if(input[i] != key[i]) 
        {
            // Since this password is wrong,
            // delay for a bit to stop Rebels from bruteforcing passwords.
            sleep(BRUTEFORCE_PENALTY);
            // We can stop comparing since the password is wrong.
            return 0;
        }
```

what is actually happening is

```
for (size_t i = 0; i < PASSWORD_MAX_LENGTH; i++)
    {
        if(input[i] != key[i]) 
        {

            // We can stop comparing since the password is wrong.
            return 0;
        }
        sleep(BRUTEFORCE_PENALTY);
```

so every correct digit of the password introduces another second-long delay in `secure_compare`. By testing digits in order, and noting when the delay triggers, you can discover the password `1138`.

Entering the password `1138` reveals the flag, `UiTHack22{the-timing-oracle-of-delphi}`.