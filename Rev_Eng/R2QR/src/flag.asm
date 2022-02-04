
BITS 32
global _start

SECTION .data
	msg:	db 42h, 75h, 89h, 74h, 68h, 81h, 83h, 8bh, 52h, 52h, 9bh, 68h, 85h, 8ch, 70h, 7fh, 6dh, 85h, 7fh, 6fh, 82h, 69h, 7fh, 77h, 81h, 6eh, 9dh, 42h, 42
	len:	equ $-msg

SECTION .text

_start:
	mov ecx, msg
	mov	edx, len
	xor eax, eax

	_loop1:
		sub byte [ecx+eax], 20h

		inc eax
		cmp edx, eax
		jne _loop1

	mov	ebx,1
	mov	eax,4

	int	0x80
	mov	ebx,0
	mov	eax,1
	int	0x80
