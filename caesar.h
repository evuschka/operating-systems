#ifndef CAESAR_H
#define CAESAR_H


extern char* caesar_encrypt(const char* text, int shift);
extern char* caesar_decrypt(const char* text, int shift);


extern void free_result(char* str);

#endif
