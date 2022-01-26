#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
 
#define PASSWORD_HASH_LENGTH 32

// By Imperial decree, all identification must supply a passphrase which
// hashes to the following digest. Just include it in the binary,
// the Rebels can't possibly bruteforce the entire 54-letter passphrase...
uint8_t PASSWORD_HASH[PASSWORD_HASH_LENGTH] = {
    0x1c, 0x00, 0x31, 0xe8, 0xc2, 0x0f, 0xbd, 0x87, 0x84, 0x54, 0xe0, 0x7a, 0xb0, 0x95, 0x23, 0x95,
    0x3b, 0x08, 0x7e, 0x93, 0xe0, 0x4d, 0x09, 0x83, 0x4d, 0xd8, 0x0f, 0x83, 0xea, 0xa8, 0x6e, 0xbd
    };

uint8_t HASH_PRIME[PASSWORD_HASH_LENGTH] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x63
    };

uint8_t HASH_BASIS[PASSWORD_HASH_LENGTH] = {
    0xdd, 0x26, 0x8d, 0xbc, 0xaa, 0xc5, 0x50, 0x36, 0x2d, 0x98, 0xc3, 0x84, 0xc4, 0xe5, 0x76, 0xcc, 
    0xc8, 0xb1, 0x53, 0x68, 0x47, 0xb6, 0xbb, 0xb3, 0x10, 0x23, 0xb4, 0xc8, 0xca, 0xee, 0x05, 0x35 
    };


void hash_password(uint8_t *input, uint8_t *dst) {
    for(int i = 0; i < PASSWORD_HASH_LENGTH; i++) {
        dst[i] = HASH_BASIS[i];
    }

    uint8_t tmp[PASSWORD_HASH_LENGTH];
    for (int i = 0; i < strlen(input); i++)
    {
        memset(tmp, 0x0, sizeof(uint8_t) * PASSWORD_HASH_LENGTH);
        for(int j = 0; j < PASSWORD_HASH_LENGTH; j++){
            for(int l = 1; l < PASSWORD_HASH_LENGTH; l++){
                tmp[l-1] = tmp[l];
            }
            tmp[PASSWORD_HASH_LENGTH - 1] = 0x0;

            uint16_t carry = 0;
            for(int k = PASSWORD_HASH_LENGTH - 1; k >= 0; k--){
                carry += (uint16_t)(tmp[k]) + (uint16_t)(dst[k]) * (uint16_t)HASH_PRIME[j];
                tmp[k] = (carry & 0xff);
                carry >>= 8;
            }
        }

        for(int j = PASSWORD_HASH_LENGTH - 1; j >= 0; j--){
            dst[j] = tmp[j];
        }

        dst[PASSWORD_HASH_LENGTH - 1] ^= input[i];
    }
}

int main(int argc, char *argv[]) {
    if(argc < 2) {
        printf("I'm going to need to see some identification.\n");
        printf("Error: must provide a password as the second argument.\n");
        return 1;
    }

    char input_hash[PASSWORD_HASH_LENGTH];
    hash_password(argv[1], &input_hash[0]);

    // Use strncmp to stop the pesky Rebels from trying to overflow our buffers.
    if(strncmp(input_hash, PASSWORD_HASH, PASSWORD_HASH_LENGTH) == 0) {
        printf("These aren't the droids we are looking for.\n");
        char *flag = getenv("MINDTRICK_FLAG");
        if(flag != NULL) {
            printf("The flag is %s", flag);
        }
    } else {
        printf("This ID is forged, after them!\n");
        printf("Error: input did not match the hash.\n");
    }
    return 0;
}