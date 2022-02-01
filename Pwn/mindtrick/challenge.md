# Jedi Mind Trick

You are deep in the city of Kra Emer, escorting a set of medical protocol droids to a local hospital, on a secret mission on behalf of the Distributed Interstellar Patient System (DIPS). 

However, you are suddenly accosted by a set of Imperial stormtroopers, asking to see your identification!

Can you pull off a Jedi mind trick of your own, and convince them to let you go?

Hint 1. The hash algorithm is weak, but there's a bigger weakness hiding here...

Hint 2. Take another look at the password hash comparison. What is it actually checking? Cppreference may be useful.

Hint 3. Take a look at the password hash, specifically the first two bytes: what happens if you use strncmp?