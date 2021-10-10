from typing import Callable

def get_longest_subsequence(lst: list[int], has_property: Callable) -> list[int]:
    """ Returneaza cea mai lunga secventa dintr-o lista, cu o anumita specificatie

        Args:
            lst (list[int]): Lista principala

        :return:
            list[int]: Cea mai lunga subsecventa cu specificatia ceruta
    """

    returned_subsequence = []
    max_length = 0

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            current_subsequence = lst[i:j+1]
            if len(current_subsequence) > max_length and has_property(current_subsequence):
                max_length = len(current_subsequence)
                returned_subsequence = current_subsequence

    return returned_subsequence


def get_longest_sorted_asc(arr):
    current_min_index = 0
    min_index = max_index = 0
    for current_max_index, i in enumerate(arr[1:]):
        if arr[current_max_index] > i or current_max_index + 2 == len(arr):
            if arr[current_max_index] < i:
                current_max_index += 1
            if max_index - min_index < current_max_index - current_min_index:
                min_index, max_index = current_min_index, current_max_index
            current_min_index = (current_max_index := current_max_index + 1)
    return arr[min_index: max_index + 1]

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 2, 3, 6, 1, 2, 3, 9, 18, 20]) == [1, 2, 3, 9, 18, 20]
    assert get_longest_sorted_asc([]) == []
    assert get_longest_sorted_asc([-7]) == [-7]
    assert get_longest_sorted_asc([9, 5, 4, 2]) == [9]

test_get_longest_sorted_asc()

def int_equal_to_fractional(n: float) -> bool:
    """
    Verifica daca partea intreaga a unui numar este egala cu parte sa fractionara
    Args:
        n (float): Numarul verificat
    :return:    bool: True daca partea intreaga este egala cu cea fractionara sau False in caz contrar
    """

    x=str(n).split('.')
    return x[0] == x[1]

def test_int_equal_to_fractional():
    assert int_equal_to_fractional(21.48) == False
    assert int_equal_to_fractional(0.0) == True
    assert int_equal_to_fractional(123.123) == True
    assert int_equal_to_fractional(73.10) == False

test_int_equal_to_fractional()

def are_int_equal_to_fractional(lst: list[float]) -> bool:
    """
    Verificam daca fiecare element al unei liste are partea intreaga egala cu parte fractionara

    Args:
            lst (list[float]): Lista verificata

    :return:
        bool: True daca fiecare element respecta conditia sau False in caz contrar
    """

    return len(list(filter(lambda x:not int_equal_to_fractional(x),lst)))==0


def test_are_int_equal_to_fractional():
    assert are_int_equal_to_fractional([23.23,12.12,7.7]) == True
    assert are_int_equal_to_fractional([]) == True
    assert are_int_equal_to_fractional([27.98,65.41,99.91,49.38]) == False
    assert are_int_equal_to_fractional([1.1]) == True

test_are_int_equal_to_fractional()

def get_longest_equal_int_real(lst: list[float]) -> list[float]:
    """
    Returneaza cea mai lunga subsecventa in care numerele au partea intreaga egala cu parte fractionara
    Args:
        lst (list[float]): Lista principala
    :return: list[float]: Subsecventa cu numere ce indeplinesc conditia
    """

    return get_longest_subsequence(lst, are_int_equal_to_fractional)

def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([]) == []
    assert get_longest_equal_int_real([1.1,7.7,18.6,12.0]) == [1.1,7.7]
    assert get_longest_equal_int_real([68.9,90.11,76.98]) == []

test_get_longest_equal_int_real()


def list_input():
    print("Introdu elementele listei separate printr-o virgula")
    lst = input("lista: ")
    lst = [float(x) for x in lst.split(",")]

    return lst


def main():
    shouldRun=True
    option = ''
    data = []


    while shouldRun:
        print(
            """     Ce doresti sa faci?
            1. Citire date
            2. Determinare cea mai lunga subsecventa din lista a numerelor ordonate crescator
            3. Determinare cea mai lunga subsecventa din lista a numerelor a caror parte intreaga este egala cu partea fractionara
            4. Iesire
            """)
        option = input("Optiune meniu:")

        if option == '1':
            data = list_input()
        elif option == '2':
            data = get_longest_sorted_asc(data)
            print(f"cea mai lunga subsecventa din lista a numerelor ordonate crescator e {data}")
        elif option == '3':
            data = get_longest_equal_int_real(data)
            print(f"Cea mai lunga subsecventa din lista a numerelor a caror parte intreaga este egala cu partea fractionara e {data}")
        elif option == '4':
            shouldRun=False

if __name__ == "__main__":
    main()