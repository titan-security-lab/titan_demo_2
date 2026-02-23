#include <string.h>
#include <stdio.h>

/*
 * VULNERABLE: Buffer Overflow - CWE-120
 * Attacker can overflow buffer with long input
 */
void copy_user_input(char *user_data) {
    char buffer[64];
    
    // No bounds checking - buffer overflow!
    strcpy(buffer, user_data);
    
    printf("Copied: %s\n", buffer);
}
