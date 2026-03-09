# Вводим константу - количество килобайт в одном мегабайте
KILOBYTES_IN_MEGABYTE = 1024
# Вводим константу - количество байт в одном килобайте
BYTES_IN_KILOBYTE = 1024

# Вводим исходные данные
volume_in_megabytes = 1.44
pages = 100
strokes = 50
symbols = 25
symbol_weight_in_bytes = 4

# Вычисление объема одной книги в байтах
volume_of_book_in_b = (symbol_weight_in_bytes * symbols * strokes * pages)

# Перевод объема одной книги из байтов в килобайты
volume_of_book_in_kb = volume_of_book_in_b / BYTES_IN_KILOBYTE
# Перевод объема одной книги из килобайтов в мегабайты
volume_of_book_in_mb = volume_of_book_in_kb / KILOBYTES_IN_MEGABYTE

# Находим количество книг, помещающихся на одной дискете
number_of_books = int(volume_in_megabytes // volume_of_book_in_mb)

print("Количество книг, помещающихся на дискету:", number_of_books)
