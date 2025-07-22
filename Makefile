install: #синхронизация зависимости
	uv sync
build: #Сборка пакета
	uv build
install: #Установка пакета
	uv tool install dist/*.whl
lint: #Проверка линтера
	uv run ruff check gendiff
