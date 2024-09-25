import pyAesCrypt
import os

def encryption(file, password):
    buffer_size = 512 * 1024
    try:
        pyAesCrypt.encryptFile(
            str(file),
            str(file) + ".crp",
            password,
            buffer_size
        )

        print(f"Файл \' {str(os.path.splitext(file)[0])} \' зашифрован")

        os.remove(file)
    except Exception as ex:
        print(f"Ошибка при шифровке файла {file}: {ex}")

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        file_extension = os.path.splitext(path)[-1]
        try:
            if os.path.isfile(path):
                if file_extension != ".crp":
                    encryption(path, password)
                else:
                    walking_by_dirs(path, password)
        except Exception as ex:
            if str(ex).split('.')[-1][:-1] == 'crp':
                print("Пропускаем зашифрованый фаил")
            else:
                print(ex)

if __name__ == '__main__':
    password = input("Введите пароль для шифрования: ")
    walking_by_dirs("", password)