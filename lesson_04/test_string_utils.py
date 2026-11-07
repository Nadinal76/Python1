import pytest
from string_utils import StringUtils

utils = StringUtils()


# ================= 1. Тесты для capitalize() =================
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_already_capitalized():
    assert utils.capitalize("Skypro") == "Skypro"


def test_capitalize_numbers():
    assert utils.capitalize("123") == "123"


def test_capitalize_empty():
    assert utils.capitalize("") == ""


def test_capitalize_whitespace():
    assert utils.capitalize(" ") == " "


# ================= 2. Тесты для trim() =================
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_trim_with_spaces_inside():
    assert utils.trim("   sky pro   ") == "sky pro   "


def test_trim_empty():
    assert utils.trim("") == ""


# ================= 3. Тесты для to_list() =================
def test_to_list_positive():
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]


def test_to_list_custom_delimeter():
    assert utils.to_list("a:b:c", delimeter=":") == ["a", "b", "c"]


def test_to_list_empty():
    assert utils.to_list("") == []


# ================= 4. Тесты для contains() =================
def test_contains_true():
    assert utils.contains("Skypro", "k") is True


def test_contains_false():
    assert utils.contains("Skypro", "z") is False


# ================= 5. Тесты для delete_symbol() =================
def test_delete_symbol_positive():
    assert utils.delete_symbol("Skypro", "k") == "Sypro"


def test_delete_symbol_multiple():
    assert utils.delete_symbol("スカイプロ", "カ") == "スイプロ"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("Skypro", "z") == "Skypro"


# ================= 6. Тесты для starts_with() =================
def test_starts_with_true():
    assert utils.starts_with("Skypro", "S") is True


def test_starts_with_false():
    assert utils.starts_with("Skypro", "s") is False


# ================= 7. Тесты для end_with() =================
def test_end_with_true():
    assert utils.end_with("Skypro", "o") is True


def test_end_with_false():
    assert utils.end_with("Skypro", "O") is False


# ================= 8. Тесты для is_empty() =================
def test_is_empty_true():
    assert utils.is_empty("") is True


def test_is_empty_with_spaces():
    assert utils.is_empty("   ") is True


def test_is_empty_false():
    assert utils.is_empty("Skypro") is False


# ================= 9. Тесты для list_to_string() =================
def test_list_to_string_positive():
    assert utils.list_to_string(["a", "b"]) == "a, b"


def test_list_to_string_custom_joiner():
    assert utils.list_to_string(["a", "b"], joiner="-") == "a-b"


def test_list_to_string_empty():
    assert utils.list_to_string([]) == ""


# Используем pytest в фиктивном тесте, чтобы убрать
# ошибку неиспользуемого импорта (длина строки < 79)
def test_unused_import_fix():
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0
