class StringUtils:
    """
    Класс с полезными утилитами для обработки строк.
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход строку, возвращает ее же,
        у которой первая буква стала заглавной.
        Пример: "skypro" -> "Skypro"
        """
        if not string:
            return string
        return string.upper() + string[1:]

    def trim(self, string: str) -> str:
        """
        Принимает на вход строку, удаляет лишние пробелы в начале.
        Пример: "   skypro" -> "skypro"
        """
        if not string:
            return string
        return string.lstrip()

    def to_list(self, string: str, delimeter=",") -> list[str]:
        """
        Принимает на вход строку с разделителем,
        возвращает список строк.
        Пример: "a,b,c,d" -> ["a", "b", "c", "d"]
        """
        if self.is_empty(string):
            return []
        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка содержит искомый символ,
        и False - если не содержит.
        Пример: utils.contains("Skypro", "k") -> True
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки.
        Пример: utils.delete_symbol("Skypro", "k") -> "Sypro"
        """
        if self.contains(string, symbol):
            return string.replace(symbol, "")
        return string

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка начинается с заданного символа,
        и False - если нет.
        Пример: utils.starts_with("Skypro", "S") -> True
        """
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка заканчивается на заданный символ,
        и False - если нет.
        Пример: utils.end_with("Skypro", "o") -> True
        """
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """
        Возвращает True, если строка пустая или состоит
        только из пробелов, и False - если нет.
        Пример: utils.is_empty("") -> True
        """
        if string is None:
            return True
        return string.strip() == ""

    def list_to_string(self, lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку
        с указанным разделителем.
        Пример: utils.list_to_string(["a", "b"]) -> "a, b"
        """
        if not lst:
            return ""
        return joiner.join(map(str, lst))
