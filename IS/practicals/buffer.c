#include <stdio.h>
#include <string.h>

void vulnerable(const char *input) {
    char buffer[5];

    /*
     * Intentionally unsafe for the lab:
     * strcpy() does not check whether input fits in buffer.
     */
    strcpy(buffer, input);

    printf("You entered: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }

    vulnerable(argv[1]);
    printf("Program completed normally.\n");

    return 0;
}
