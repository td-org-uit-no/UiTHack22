#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define buffsize 64

int main(int argc, char** argv)
{

    long n = 0;
    char input[buffsize];

    printf("Loading archive, please wait...\n");
    sleep(1);

    while (n == 0) {

        printf("What are you looking for? \n");
        gets(input);
        if (strcmp(input, "stardust") == 0 || (strcmp(input, "Stardust") == 0) || (strcmp(input, "star dust") == 0) || (strcmp(input, "Star dust") == 0)) {
            printf("Found file: project stardust. File contents are too large to read, please insert the disk-drive from the archive into the analysis station.\n");
        } else if ((strcmp(input, "darth plagueis") == 0) || (strcmp(input, "Darth Plagueis") == 0)) {
            printf("Found file: %s. Reading file: Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.\n", input);
        } else if (strcmp(input, "secret") == 0 || (strcmp(input, "flag") == 0)) {
            printf("Found Symlink: %s -> darth plagueis.\n", input);
        } else if ((strcmp(input, "deathstar") == 0) || (strcmp(input, "death star") == 0) || (strcmp(input, "Deathstar") == 0) || (strcmp(input, "Death star") == 0)) {
            printf("Found Symlink: %s -> stardust.\n", input);
        } else {
            printf("No matches found for %s\n", input);
        }

        memset(input, 0, buffsize);
    }

    printf("Error occured, exiting...\n");
    sleep(1);
    system("/bin/sh");
}