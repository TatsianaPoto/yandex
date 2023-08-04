def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}
    
    # Подсчитываем частоту каждого символа в первой строке
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Уменьшаем частоту каждого символа во второй строке
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # Проверяем, что все частоты стали равны нулю
    for count in char_count.values():
        if count != 0:
            return False

    return True

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()

    result = 1 if are_anagrams(str1, str2) else 0
    print(result)