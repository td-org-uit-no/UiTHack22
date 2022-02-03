#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <unistd.h>
#include <sys/time.h>

#define PASSWORD_MAX_LENGTH 32
#define BRUTEFORCE_PENALTY 1

int secure_compare(char *input, char *key)
{
    for (size_t i = 0; i < PASSWORD_MAX_LENGTH; i++)
    {
        if(input[i] != key[i]) 
            // We can stop comparing since the password is wrong.
            return 0;
            // Since this password is wrong,
            // delay for a bit to stop Rebels from bruteforcing passwords.
            sleep(BRUTEFORCE_PENALTY);

        if(input[i] == '\0' && key[i] == '\0')
            // We're done comparing, the password is valid.
            return 1; 

        if (key[i] == '\0')
            // The key ended before the password.
            // The Stormtroopers probably just accidentally hit another key, let them in.
            return 1;

        if(input[i] == '\0')
            // The password is too short.
            return 0; 
    }
    return 1;
    
}

int main(int argc, char *argv[]){
    char *password = getenv("EPHEMERAL_PASSWORD");
    if(password == NULL) {
        printf("Error: our password is missing!");
        return 1;
    }


    char input[PASSWORD_MAX_LENGTH];

    printf("Welcome to the Imperial mainframe.\n");
    printf("Note: to ensure our stormtroopers are 1) capable of remembering the passwords and\n");
    printf("2) capable of entering the passwords with their bulky gloves, passwords have been\n");
    printf("restricted to numbers only. Don't think that we'll just let the Rebels try every\n");
    printf("password, though...\n");     

    int locked = 1;
    while(locked) {
        printf("Enter password: ");
        scanf("%31s", &input);

        time_t request_start, request_over;
        time(&request_start);
        if(secure_compare(input, password) == 1)
        {
            printf("Password accepted.\n");
            char *flag = getenv("EPHEMERAL_FLAG");
            if(flag != NULL) {
                printf("The flag is: %s\n", flag);
            }
            locked = 0;
        } else {
            printf("Wrong password.\n");
        }
        time(&request_over);
        double request_time = difftime(request_over, request_start); 
        printf("Request took %.2f seconds to process.\n", request_time);
    }
}