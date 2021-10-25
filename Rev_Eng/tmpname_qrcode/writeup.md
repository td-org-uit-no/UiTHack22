

Solution:

When you read the qrcode you might notice it is base64 encoded.  
When you decode the b64 you might notice the words ELF in the output.  
This indicates the output is an executable so you need to store the contents in a file, give it exec permissions and run it.

```
zbarimg -q qrcode.png --raw | base64 -d > flag
chmod +x flag
./flag
```