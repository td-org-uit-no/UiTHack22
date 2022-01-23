#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>


void encrypt(char* val, int seed, int n) {
    srand(seed);
    for (int i = 0; i < n; i++) {
        int r = rand() % (CHAR_MAX);
        val[i] = (val[i] ^ r);
    }
}

void solve(char* encrypted) {
    int N = strlen(encrypted);
    char* tmp = malloc(sizeof(char) * N);
    char* template = "UiTHack22{";

    for (long i = 0; i < (1 << 28); i++) {
        strcpy(tmp, encrypted);
        encrypt(tmp, i, N);
        if (strncmp(tmp, template, 10) == 0) {
            printf("key: %ld flag: %s\n", i, tmp);
            break;
        }
    }
    free(tmp);
}

int main(int argc, char *argv[]) {
    long N, key;
    char* flag;
    if (argc == 3) {
        N = strlen(argv[1]);
        key = strtol(argv[2], NULL, 10) & 0xFFFFFFF;
        flag = malloc(sizeof(char) * N);
        sprintf(flag, "%s", argv[1]);
    } else {
        printf("Invalid arguments for encryption, exiting\n");
        exit(1);
    }
    
    printf("Encrypting message %s[%ld] with key %ld\n", flag, N, key);

    char* enc = malloc(sizeof(char) * N);
    strcpy(enc, flag);

    encrypt(enc, key, N);
    printf("Encrypted: \n");
    for (int i = 0; i < N; i++) {
        printf("%02X ", enc[i]);
    }
    printf("\n");

    solve(enc);

    free(enc);
    free(flag);
}