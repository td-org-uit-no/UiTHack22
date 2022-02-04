> # Noob5 - Jedi
> > Noob  - 250pts
> 
> So you have made it here. Don't get too confident, there are still tasks to be challenged. Use the force to retrieve the flag. 
> 
> To enter you will need to connect through `ssh`.
> The username for this trial is `jedi`.  
> The server name is `sparkly-unicorn.td.org.uit.no`.  
> The password for jedi is the flag from the `master` challenge.
> 
> Tips: `ssh jedi@sparkly-unicorn.td.org.uit.no`  
> Tips: First glance can fool you
> 

## Writeup

src/flag.txt is a disguised zipped file. Uncompress the "txt" file to recieve another disguised file and read its contents. 

Example solution: 
`unzip -p flag.txt | less`

```
UiTHack22{Don’t call me a mindless philosopher, you overweight glob of grease! -C-3PO}
```