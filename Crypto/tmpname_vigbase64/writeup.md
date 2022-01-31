># Master Vigndu
>> Crypto - 150pts
>
>Master Windu is leading the the 7th Sky Corpse in an >epic space 
>battle against the Separatists. Suddenly he is hit in the rear of his ship. 
>He gets a look of the ships shooting at him. It is the SLAVE I and he is transfering 
>a message. 
>
>
>[Message](./message.txt)

## Writeup

Notice that the second crypted text contains a "=" that should indicate a base64.
"SLAVE" is the only word that is exclaimed. Notice also how "Mace Vigndu" is not his name and Vigenere is a way to chiper text. Use SLAVE as key and then base64 on the 
cipher outputed.

```
UiTHack22{I_Know_Your_Name_Is_Master_Windu!}