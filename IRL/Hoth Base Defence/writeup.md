> # Hoth Base Defence
> > IRL - 200pts  
> You are stationed on the new rebel base on Hoth, and are regularly sent out to check on suspicious activities around the base permimeter.
> Whenever the base detects nearby activity you are sent out to investigate and report back.
> 
> Just now the base has detected an anomaly at the following coordinates:
> 
> `69.683250, 18.972639`
> 
> Investigate and report back.
> 
> <img src="https://i.gifer.com/90GZ.gif" width="400" height="400" />
> 

## Writeup

By finding the IRL clues the following flag can be created.

The initial clue is a set of coordinates that lead to the location of the first card.
The first card contains the first part of the flag and coordinates to the next clue.

The second clue is also a set of coordinates that lead to the second card.
This card contains the second part of the flag and the next clue.
This is the sharepoi id of a room on mazemap, and leads to the final clue.

The final clue contains a ceasar cipher with the final part of the flag shifted 5 times.

Flag:
```
UiTHack22{we_have_the_deathstar_schematics_on_disk}
```
