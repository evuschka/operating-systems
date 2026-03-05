CC = gcc
CFLAGS = -Wall -Wextra -pedantic -fPIC
LDFLAGS = -shared

LIBRARY = libcaesar.so
SRC = caesar.c
OBJ = $(SRC:.c=.o)

.PHONY: all install test clean

all: $(LIBRARY)

$(LIBRARY): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

install: $(LIBRARY)
	# Установка в системную директорию требует прав суперпользователя (sudo)
	sudo cp $(LIBRARY) /usr/local/lib/
	sudo chmod 755 /usr/local/lib/$(LIBRARY)
	# ldconfig обновляет кэш системных библиотек, чтобы Python ее увидел
	sudo ldconfig

test:
	python3 test.py

clean:
	rm -f $(OBJ) $(LIBRARY)
