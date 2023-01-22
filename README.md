[![Actions Status](https://github.com/dmi-sm/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/dmi-sm/python-project-50/actions)
[![Makefile CI](https://github.com/dmi-sm/python-project-50/actions/workflows/makefile.yml/badge.svg)](https://github.com/dmi-sm/python-project-50/actions/workflows/makefile.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/2db18b56974b4c063ee7/maintainability)](https://codeclimate.com/github/dmi-sm/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2db18b56974b4c063ee7/test_coverage)](https://codeclimate.com/github/dmi-sm/python-project-50/test_coverage)

# Generate Difference
Вычислитель отличий – консольная утилита, для сравнения двух структур данных, поиска различий между ними и вывода их в различный форматах. 

### Поддерживаемые форматы файлов:
- json
- yaml/yml

### Доступные форматы вывода:
- stylish (по умолчанию)
- plain
- json

# Установка
Для установки загрузите проект, убедитесь, что находитесь в корневой директории проекта, запустите команду `make package-install`.
```bash
$make package-install
```

# Запуск
Для запуска воспользуйтесь командой `gendiff`, при необходимости выберите формат, и укажите пути к файлам.
```bash
$gendiff [-f] [--format] <file_path> <file_path>
```
### Пример вывода в формате по умолчанию: stylish
[![asciicast](https://asciinema.org/a/tgaJRurUYnUgceQ6jePp7vZEr.svg)](https://asciinema.org/a/tgaJRurUYnUgceQ6jePp7vZEr)
[![asciicast](https://asciinema.org/a/rbZr9CJQesoIUws7jA9PW9QDu.svg)](https://asciinema.org/a/rbZr9CJQesoIUws7jA9PW9QDu)

### Сравнение вложенных структур и ввывод в формате по умолчанию: stylish
[![asciicast](https://asciinema.org/a/COzZWhnst5lEkc13fNXICpZBx.svg)](https://asciinema.org/a/COzZWhnst5lEkc13fNXICpZBx)
[![asciicast](https://asciinema.org/a/ABuYAn06yzg1Pc5DWEnensmXH.svg)](https://asciinema.org/a/ABuYAn06yzg1Pc5DWEnensmXH)

### Сравнение вложенных структур и ввывод в формате plain
[![asciicast](https://asciinema.org/a/dfBvFlWvohRIl54jYgZ6gcYDK.svg)](https://asciinema.org/a/dfBvFlWvohRIl54jYgZ6gcYDK)

### Сравнение вложенных структур и ввывод в формате json
[![asciicast](https://asciinema.org/a/wZ2jXto9gw7xPCeqWXjC0nIb0.svg)](https://asciinema.org/a/wZ2jXto9gw7xPCeqWXjC0nIb0)