# Выводим подстроки, которые входят в строку, полученную через STDIN

data = input("Введите данные для анализа:\n")
data_len = len(data)
repeating_length_min = input("Задайте минимальную длину строки для анализа совпадений:\n")
repeating_length_min = int(repeating_length_min)
repeating_pieces = []
longest_repeating_piece = ''
piece = ''
index_counter = 0
range_counter = 0

while range_counter != data_len - repeating_length_min:
    while index_counter <= data_len - repeating_length_min:
        for i in range(repeating_length_min + range_counter):
            piece += data[i]
        if piece in data:
            repeating_pieces.append(piece)
        piece = ''
        index_counter += 1
    index_counter = 0
    range_counter += 1

repeating_pieces.sort(key=len)
print(f'\nСамое короткое повторяющееся значение: {repeating_pieces[0]}')
print(f'\nСамое длинное повторяющееся значение: {repeating_pieces[-1]}')
print('\nТоп 10 самых коротких повторяющихся значений:')

for i in range(10):
    print(f'#{i}: {repeating_pieces[i]}')

repeating_pieces.reverse()
print('\nТоп 10 самых длинных повторяющихся значений:')

for i in range(10):
    print(f'#{i}: {repeating_pieces[i]}')
