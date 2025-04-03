import os

def list_directory(path="."):
    """Возвращает список файлов и папок в указанной директории."""
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return f"Ошибка: Папка '{path}' не найдена."
    except PermissionError:
        return f"Ошибка: Нет прав доступа к папке '{path}'."
    except OSError as e:
        return f"Ошибка: {e}"

def create_directory(path):
    """Создает новую директорию."""
    try:
        os.makedirs(path, exist_ok=False)
        return f"Папка '{path}' успешно создана."
    except FileExistsError:
        return f"Ошибка: Папка '{path}' уже существует."
    except PermissionError:
        return f"Ошибка: Нет прав на создание папки в указанном месте."
    except OSError as e:
        return f"Ошибка: {e}"

def change_directory(path):
    """Изменяет текущую рабочую директорию."""
    try:
        os.chdir(path)
        return f"Текущая директория изменена на: {os.getcwd()}"
    except FileNotFoundError:
        return f"Ошибка: Папка '{path}' не найдена."
    except PermissionError:
        return f"Ошибка: Нет прав доступа к папке '{path}'."
    except OSError as e:
        return f"Ошибка: {e}"
