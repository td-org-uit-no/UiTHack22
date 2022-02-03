># Meet Jabba the Hutt
>> Web - 200pts
>
>Only Mr. Jabba and a special few have access to the secret key. Good luck. 
>
>The website is located at: `link`
>
>Files: 
>[source code](./scr/)

## Writeup
With a keen eye, you can see that after every submission of a username, the tokens on the site alteres. It is the username encoded with base64, which gives an indication that it's the correct username you need to have, or be able to bypass the token all together to create a logged in session. Using Jabba's full name as the username, or injecting the base64 encoded version of his name into the token gives you a valid session, and you can move over to see the flag. 

The flag yields: `UiTHack22{special_token_for_a_special_gangsterboss}`
