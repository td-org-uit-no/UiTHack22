> # Massacre aftermath
> > Rev-Eng - 400 pts
> 
> After the violent boarding of the CR90 corvette Tantive IV by Lord Vader, the commanders have instructed you to break into the rebel computer systems and access the flight logs.  
> Lord Vader is personally overseeing this process so you quickly find your way to a terminal by the docking bay.  
> In this terminal you are met with a login prompt, and not wanting to be cut in half you do your best to break past their encryption schemes.
> 
> [massacre_aftermath](./massacre_aftermath)
> 
> 
> Hint: Have you tried cutting it open?
> Hint: This seems very proprietary, must be flawed somehow...
> 
> 
> Files: [source code](./src/massacre_aftermath)
> 
> [Writeup](./writeup.md)


## Writeup

Reverse engineering the binary using tools such as radare or ghidra reveals that the code is "encrypting" the user input and comparing the result to a static array of ints.

The encrypt function uses rust iteratiors to perform a relatively simple operation:
for each letter, the output is the sum of all ascii values the previous letters, with the previous letter for the first letter being itself.

Inversing this function can be done in several ways:

A working rust decoder can be found [here](./src/massacre_aftermath/src/main.rs?plain=1#L58) and is implemented using the same techniques as the encrypt function.

Example pythonish pseudocode of this could be something like:

```py
res = ""
for c in s[1:].rev():
    res += chr(prev - c)
    prev = c

res += s[0] / 2
res = res.reverse()
```

```
Flag: UiTHack22{BrinG_tHE_Droid_to_my_father_ON_Alderaan}
```