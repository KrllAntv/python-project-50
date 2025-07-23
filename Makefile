install: #синхронизация зависимости
	uv sync
build: #Сборка пакета
	uv build
package-install: #Установка пакета
	uv tool install dist/*.whl
lint: #Проверка линтера
	uv run ruff check gendiff
test: #Запуск тестов
	uv run pytest
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml
check: test lint

