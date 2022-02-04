> # Murder mystery
> > Misc - 200 pts
> 
> We are trapped on a spaceship, but there is an impostor among us.  
> We have recovered the ship logs and now we only need to decode them to find the murderer.  
> Can you help us decode the logs?
> 
> [logs](./logs.txt)

## Writeup

The log is written in the esoteric [Among us](https://esolangs.org/wiki/Among_Us) language.  
The language specification can be found on the website, as well as a link to a [c++](https://github.com/toc8730/amonguscpp/blob/main/amongus.h) header file to compile the language.  
This header is missing the BROWN operator but that can be implemented as such: 
```
#define BROWN brown
void brown() {accumulator1 = stack.top(); }
```
To decode the output add the "log" to a .c file as shown in the solution file.  
Note that the EMERGENCY MEETING AND VOTED operators implement the main function and are not part of the core language.

The solution.c file can be compiled and tested as such:  
`g++ solution.c -o solution && ./solution`

```
Flag: UiTHack22{Impostor_SuS}
```
