> # Noob4 - Master
> > Noob - 200pts
> 
> By using the right tools one can see all the way into the real depth of the fabric of space!
> 
> To enter you will need to connect through `ssh`.
> The username for this trial is `master`.  
> The server name is `sparkly-unicorn.td.org.uit.no`.   
> The password for master is the flag from the `knight` challenge.
> 
> 
> Tips: ssh master@sparkly-unicorn.td.org.uit.no
> 
> Tips: The structure is deep, but not endless

## Writeup

The flag is located in a flat.txt file within the deepest nested directory.  
Extract flag with:  


```cat $(find . -name "flag.txt")```

    
```
Flag: UitHack22{recursive(recursive(recursive(recursive)))}
```