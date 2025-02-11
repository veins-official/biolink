# Проект: Кластеризация с использованием C и Python

## Описание

Этот проект представляет собой реализацию алгоритма кластеризации, написанного на языке C, с интеграцией в Python для обработки и визуализации данных. Основная идея заключается в том, чтобы объединить производительность и эффективность C с удобством и гибкостью Python.

## Структура проекта

```
biolink/
├── data
│   └── mnist.gz
├── docs
│   └── README.md
├── requirements.txt
└── src
    ├── c
    │   ├── matrix_functions.c
    │   └── matrix_functions.h
    ├── lib
    │   └── biolink.so
    ├── Makefile
    ├── obj
    │   └── matrix_functions.o
    └── python
        ├── biolink.py
        ├── main.py
        └── parser.py
```

## Инструкции по установке и запуску

1. **Создание виртуального окружения**
	```bash
	python -m venv .venv
	```

2. **Запуск виртуального окружения**
	```bash
	source .venv/bin/activate
	```

3. **Загрузка зависимостей**
	```bash
	pip install -r requirements.txt
	```
	
4. **Компиляция**
	```bash
	make -C src
	```

5. **Запуск кода**
	```bash
	python src/python/main.py
	```
	
6. **Сохранение зависимостей**
	```bash
	pip freeze > requirements.txt
	```
	
7. **Деактивация виртуального окружения**
	```bash
	deactivate
	```

