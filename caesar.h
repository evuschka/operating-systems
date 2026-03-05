просили в задании.
#ifndef CAESAR_H
#define CAESAR_H

// Объявляем функции с атрибутом extern для экспорта
extern char* caesar_encrypt(const char* text, int shift);
extern char* caesar_decrypt(const char* text, int shift);

// Вспомогательная функция для очистки памяти из Python,
// чтобы избежать утечек памяти (требование задания).
extern void free_result(char* str);

#endif
