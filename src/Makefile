TARGET = lib/biolink.so
C_SRC_DIR = c
OBJ_DIR = obj
CC = gcc

CFLAGS = -fPIC -fstack-protector-all -W -Wall -Wextra -Wunused -Wcast-align -Werror -pedantic -pedantic-errors -Wfloat-equal -Wpointer-arith -Wformat-security -Wmissing-format-attribute -Wformat=1 -Wwrite-strings -Wno-long-long -std=gnu99 -Wstrict-prototypes -Wmissing-prototypes -Wmissing-declarations -Wold-style-definition -Wdeclaration-after-statement -Wbad-function-cast -Wnested-externs -O3 -I$(C_SRC_DIR)
LDFLAGS = -shared
LIBS = -lm

SRC_FILES := $(wildcard $(C_SRC_DIR)/*.c)
OBJ_FILES := $(patsubst $(C_SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(SRC_FILES))


all: $(TARGET)

$(TARGET): $(OBJ_FILES)
	$(CC) $(LDFLAGS) $^ -o $@ $(LIBS)

$(OBJ_DIR)/%.o: $(C_SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR)/* $(TARGET)

.PHONY: clean

