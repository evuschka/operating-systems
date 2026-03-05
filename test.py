import ctypes
import sys
import os

def main():
    # Загружаем динамическую библиотеку
    try:
        # Ищем библиотеку в текущей папке или в системной (если уже был make install)
        lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libcaesar.so')
        if not os.path.exists(lib_path):
            lib_path = 'libcaesar.so'
            
        caesar_lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print(f"Ошибка загрузки библиотеки: {e}")
        print("Убедитесь, что вы выполнили 'make' или 'make install'")
        sys.exit(1)

    # Настраиваем типы аргументов и возвращаемых значений для C-функций
    # Используем POINTER, чтобы не потерять адрес в памяти и потом очистить её
    caesar_lib.caesar_encrypt.argtypes = [ctypes.c_char_p, ctypes.c_int]
    caesar_lib.caesar_encrypt.restype = ctypes.POINTER(ctypes.c_char)

    caesar_lib.caesar_decrypt.argtypes = [ctypes.c_char_p, ctypes.c_int]
    caesar_lib.caesar_decrypt.restype = ctypes.POINTER(ctypes.c_char)

    caesar_lib.free_result.argtypes = [ctypes.POINTER(ctypes.c_char)]
    caesar_lib.free_result.restype = None

    original_text = b"hello"
    shift = 3

    print(f"Оригинальный текст: '{original_text.decode('utf-8')}', сдвиг: {shift}")

    # --- ШИФРОВАНИЕ ---
    enc_ptr = caesar_lib.caesar_encrypt(original_text, shift)
    if not enc_ptr:
        print("Ошибка памяти при шифровании!")
        sys.exit(1)
        
    encrypted_text = ctypes.cast(enc_ptr, ctypes.c_char_p).value.decode('utf-8')
    print(f"Зашифровано: '{encrypted_text}'")

    # --- ДЕШИФРОВАНИЕ ---
    dec_ptr = caesar_lib.caesar_decrypt(encrypted_text.encode('utf-8'), shift)
    decrypted_text = ctypes.cast(dec_ptr, ctypes.c_char_p).value.decode('utf-8')
    print(f"Расшифровано: '{decrypted_text}'")

    # Освобождаем память, выделенную в C (предотвращаем утечки памяти)
    caesar_lib.free_result(enc_ptr)
    caesar_lib.free_result(dec_ptr)

    # Проверка на соответствие заданию
    if encrypted_text == "khoor" and decrypted_text == "hello":
        print("УСПЕХ: Тест пройден корректно!")
    else:
        print("ОШИБКА: Тест провален.")

if __name__ == "__main__":
    main()
