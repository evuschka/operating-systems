CC = gcc
CFLAGS = -Wall -Wextra -pedantic -fPIC
LDFLAGS = -shared
LIB_NAME = libcaesar.so
SRC = caesar.c
OBJ = caesar.o

.PHONY: all make install test clean

all: $(LIB_NAME)

make: all

$(LIB_NAME): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

install: $(LIB_NAME)
	# Требуются права суперпользователя (sudo make install)
	install -m 755 $(LIB_NAME) /usr/local/lib/
	ldconfig /usr/local/lib/ || true

test: $(LIB_NAME)
	python3 test.py

clean:
	rm -f $(OBJ) $(LIB_NAME)
