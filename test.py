import ctypes
import os
import sys

def main():
    # Поиск библиотек
    lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libcaesar.so')
    
    try:
        # Загрузка динамической библиотеки
        caesar_lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"Ошибка загрузки библиотеки: {e}")
        print("Возможно, вы забыли скомпилировать ее? Попробуйте запустить 'make'.")
        sys.exit(1)


    # Функция caesar_encrypt (шифрование)
    caesar_lib.caesar_encrypt.argtypes = [ctypes.c_char_p, ctypes.c_int]
    caesar_lib.caesar_encrypt.restype = ctypes.POINTER(ctypes.c_char)

    # Функция caesar_decrypt (дешифрование)
    caesar_lib.caesar_decrypt.argtypes = [ctypes.c_char_p, ctypes.c_int]
    caesar_lib.caesar_decrypt.restype = ctypes.POINTER(ctypes.c_char)

    # Функция free_string (освобождение памяти)
    caesar_lib.free_string.argtypes = [ctypes.POINTER(ctypes.c_char)]
    caesar_lib.free_string.restype = None

    original_text = "hello"
    shift = 3

    print(f"Оригинальный текст: {original_text}")
    print(f"Сдвиг: {shift}")

    # Шифрование
    b_text = original_text.encode('utf-8')
    enc_ptr = caesar_lib.caesar_encrypt(b_text, shift)
    
    # Конвертируем указатель обратно в строку Python
    encrypted_text = ctypes.cast(enc_ptr, ctypes.c_char_p).value.decode('utf-8')
    print(f"Зашифрованный текст: {encrypted_text}")

    # Дешифрование
    b_enc_text = encrypted_text.encode('utf-8')
    dec_ptr = caesar_lib.caesar_decrypt(b_enc_text, shift)
    
    decrypted_text = ctypes.cast(dec_ptr, ctypes.c_char_p).value.decode('utf-8')
    print(f"Расшифрованный текст: {decrypted_text}")


    if encrypted_text == "khoor" and decrypted_text == "hello":
        print("Тест пройден успешно!")
    else:
        print("Тест провален!")

    # Очистка памяти
    # Важно освободить память, выделенную внутри C (через malloc)
    caesar_lib.free_string(enc_ptr)
    caesar_lib.free_string(dec_ptr)

if __name__ == "__main__":
    main()
