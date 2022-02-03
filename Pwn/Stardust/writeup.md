> # Stardust
> > Pwn - 100 pts
> 
> Rebel forces have infiltrated the imperial base on on Sarif and are looking for the deathstar plans.  
> They are unfortunately hidden somewhere in the system and you only have access to this stardust program.  
> Can you find the plans hidden somewhere in the program?
> 
> Hint: Are there any ways you can manipulate the program?
> 
> Hint 2: Can you break it somehow?
> 


## Writeup

The program is designed poorly and is vulnerable to buffer overflow attacks.  
Simply enter a string longer than 64 characters and you gain access to a shell.  
Using this shell you can locate the flag.txt file and read it to find the flag.

```
UiTHack22{The_Deathstar_Will_Be_Beutiful_but_Flawed}
```