#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "caesar.h"


static int mod(int a, int b) {
    int r = a % b;
    return r < 0 ? r + b : r;
}


static char* process_text(const char* text, int shift) {
    if (text == NULL) {
        return NULL;
    }


    size_t len = strlen(text);
    char* result = (char*)malloc(len + 1);
    if (result == NULL) {
        return NULL; // Ошибка выделения памяти
    }

    for (size_t i = 0; i < len; i++) {
        char c = text[i];
        

        if (c >= 'a' && c <= 'z') {
           
            int pos = c - 'a';
            int new_pos = mod(pos + shift, 26);
            result[i] = 'a' + new_pos;
        } else {

            result[i] = c;
        }
    }
    
    result[len] = '\0';
    return result;
}

extern char* caesar_encrypt(const char* text, int shift) {
    // Шифрование — это просто сдвиг вперед
    return process_text(text, shift);
}

extern char* caesar_decrypt(const char* text, int shift) {
    // Дешифрование — это сдвиг назад (отрицательный сдвиг)
    return process_text(text, -shift);
}


extern void free_string(char* str) {
    if (str != NULL) {
        free(str);
    }
}
