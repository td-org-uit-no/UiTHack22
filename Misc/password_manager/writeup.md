> # Password manager
> > Misc - 100 pts
> 
> Han Solo and Chewbacka is flying the Milenium Falcon through space.  
> Out of nowhere the Falcon stops!!!! 
> -"WHAT IS HAPPENING" yells Han  
> -"Rrrrrrr-ghghghghgh" answers Chewbacca.  
> -"Yeah, you are right! It is probably that" says Han.  
> -"Rrrr-ghghg-rrrr" Chewbacca snares!  
> -"I will fix it fast, don't worry!"  
> The computer on the falcon does a self test and the result is that   
> the computer needs to reset.  
> -"SHIT! I dont remember the password!"  
> -"ghghgh-rrrr!"  
> -"Thats right I have a note for that"  
> Han Solo pulls up the note and looks shocked. He does not remember  
> anything about the password and he needs your help!  
> 

## Writeup

The note that Han Solo pulls out is a simple list. 
However  the list is very long and tidious and it 
would take a long time to go trough it manually. It looks like
it only contains symbols and numbers, but it the flag is hidden in the list
as the only letters there. A simple script that parses the list is therefore
a nice way to solve this task. It is also important to remember the structure 
of the flag when the letters are recovered. 

```
Flag: UiTHack22{Luke_would_Have_remembered_The_Password}
```