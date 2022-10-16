"""
Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений
 одной строки в другой.

Пример:
                      c: 2
 or
"hello or world", "or" -> 2

"""

def count_substr(text, find):
    count = 0
    for i in range(len(text)):  # 0, len(text), len(or) ->2
        if text[i:i + len(find)] == find:
            count += 1
    return count


# print(f'"{text}", "{find}" -> {count}')

data_table = [
    ["hello or woror", "or", 3],
    ["aaaaaa", "aa", 5],
    ["abababa", "aba", 4]
]

for txt, sub_str, expected in data_table:  #  ["hello or woror", "or", 3]
    assert count_substr(txt, sub_str) == expected, f"expected {expected}"

