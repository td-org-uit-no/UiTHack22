
CFLAGS= -Os -nostartfiles -m32 -static -Wl,-n,-N

all: flag

encode: flag
	base64 flag | qrencode -l L -o "../flag.png" 


flag: flag.asm Makefile
	nasm -f elf32 flag.asm
	clang -o flag flag.o $(CFLAGS)
	strip -s flag
	
clean:
	rm flag flag.o
