#include <stdlib.h>
#include <string.h>
#include "caesar.h"

// Общая функция обработки, чтобы не дублировать код.
// Не используем глобальные переменные для потокобезопасности.
static char* process_text(const char* text, int shift) {
    if (text == NULL) return NULL;

    // Математический трюк для обработки отрицательных сдвигов и сдвигов > 26
    shift = shift % 26;
    if (shift < 0) {
        shift += 26;
    }

    int len = strlen(text);
    // Выделяем память под новую строку (+1 для нуль-терминатора)
    char* result = (char*)malloc(len + 1);
    if (result == NULL) return NULL;

    for (int i = 0; i < len; i++) {
        char c = text[i];
        // Обрабатываем только строчные латинские буквы
        if (c >= 'a' && c <= 'z') {
            result[i] = 'a' + (c - 'a' + shift) % 26;
        } else {
            // Остальные символы оставляем без изменений
            result[i] = c;
        }
    }
    result[len] = '\0';
    
    return result;
}

char* caesar_encrypt(const char* text, int shift) {
    return process_text(text, shift);
}

char* caesar_decrypt(const char* text, int shift) {
    // Дешифрование - это тот же сдвиг, но в обратную сторону
    return process_text(text, -shift);
}

// Функция для очистки выделенной памяти
void free_result(char* str) {
    if (str != NULL) {
        free(str);
    }
}
