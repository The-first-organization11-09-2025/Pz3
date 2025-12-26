class ShiftKeyDescriptor:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get('_' + self.name)

    def __set__(self, obj, value):
        if type(value) != int:
            raise TypeError("Ключ шифра должен быть целым числом")
        obj.__dict__['_' + self.name] = value


class RussianCaesarCipher:

    shift = ShiftKeyDescriptor()

    def __init__(self, shift):
        self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.shift = shift

    def _process_char(self, char, direction):
        if 'а' <= char <= 'я':
            start = ord('а')
            index = ord(char) - start
            new_index = (index + direction * self.shift) % 33
            return chr(start + new_index)
        elif 'А' <= char <= 'Я':
            start = ord('А')
            index = ord(char) - start
            new_index = (index + direction * self.shift) % 33
            return chr(start + new_index)
        else:
            return char

    def encrypt(self, text):
        result = []
        for char in text:
            result.append(self._process_char(char, 1))
        return ''.join(result)

    def decrypt(self, text):
        result = []
        for char in text:
            result.append(self._process_char(char, -1))
        return ''.join(result)


if __name__ == "__main__":
    print("Шифр Цезаря")
    cipher = RussianCaesarCipher(5)
    print(f"Ключ шифра: {cipher.shift}")

    tests = "Жизнь - боль."

    encrypted = cipher.encrypt(tests)
    decrypted = cipher.decrypt(encrypted)
    print(f"'{tests}' шифровка '{encrypted}' дешифровка '{decrypted}'")


class AlphabetDescriptor:

    def __get__(self, obj, cls):
        return 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


class AtbashCipher:

    alphabet = AlphabetDescriptor()

    def encrypt(self, text):
        result = ''

        for char in text:
            if 'а' <= char <= 'я':
                pos = ord(char) - ord('а')
                new_pos = 31 - pos
                new_char = chr(ord('а') + new_pos)
                result += new_char

            elif 'А' <= char <= 'Я':
                pos = ord(char) - ord('А')
                new_pos = 31 - pos
                new_char = chr(ord('А') + new_pos)
                result += new_char

            else:
                result += char

        return result

    decrypt = encrypt


if __name__ == "__main__":
    cipher = AtbashCipher()

    print("Шифр Атабаш")

    text = "Скоро Новый Год!"
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)

    print(f"'{text}' шифровка '{encrypted}' дешифрока '{decrypted}'")
