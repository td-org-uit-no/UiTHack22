> # Noob3 - Knight
> > Noob - 150pts
>
> Ahh, I see that you have succedded in passing all of your trials as a Padawan. As a Jedi Knight, you are expected to uphold the peace of the galaxy and the ideals of the Jedi Code. Conntinue your journey across the galaxy and perform heroic deeds, by finding what is _hidden_.
>
> To enter the trial you will need to connect through `ssh`.
> The username for this trial, is `knight`
> The server name is `sparkly-unicorn.td.org.uit.no`.
> The password for knight is the flag from the padawan challenge.
>
>
>
> Tips:
> `ssh knight@sparkly-unicorn.td.org.uit.no`
>
> Tips:
> Have you seen all of the list?

## Writeup
The flag directory is hidden as well as the flag.txt inside. The commands needed is `ls -la` to identify that there is a hidden directory, then `cd .flag`. you will need to identify the hidden text file as well, then you can use `cat .flag.txt` to read it.

```
UiTHack22{may_the_Force_be_with_you_Jedi_Knight}
```