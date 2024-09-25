import pyAesCrypt
import os


def decryption(file, password):
    buffer_size = 512 * 1024
    try:
        # Попытка расшифровать файл
        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            buffer_size
        )
        print(f"Файл \'{str(os.path.splitext(file)[0])}\' расшифрован")

        os.remove(file)
    except Exception as ex:
        print(f"Ошибка при расшифровке файла {file}: {ex}")


def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            decryption(path, password)
        else:
            walking_by_dirs(path, password)


if __name__ == '__main__':
    password = input("Введите пароль для расшифровки: ")
    walking_by_dirs("", password)
