install: # установить зависимости
	poetry install

gendiff: # запустить сценарий
	poetry run gendiff

build: # собрать пакет
	poetry build

publish: # отладить публикацию, чтобы не добавлять пакет в каталог PyPI
	poetry publish --dry-run

package-install: # установить пакет в окружение пользователя
	python3 -m pip install --user dist/*.whl

package-reinstall: # переустановить пакет
	python3 -m pip install --upgrade --force-reinstall dist/*.whl

lint: # запустить проверку линтером
	poetry run flake8 gendiff

tests: # запустить тестирование
	poetry run pytest

package-uninstall: # удалить пакет из окружения пользователя
	python3 -m pip uninstall dist/*.whl