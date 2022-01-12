
flag3 = "schematics_on_disk}"

o = ""

for c in flag3:
    if c == '}' or c == '_':
        o += c
    else:
        i = ord(c)
        o += chr(i + 5)

print(o)