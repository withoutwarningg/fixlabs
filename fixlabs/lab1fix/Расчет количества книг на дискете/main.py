diskette_capacity_mb = 1.44
book_pages = 100
lines_per_page = 50
chars_per_line = 25
char_size_bytes = 4

# Вычисляем информационный объем одной книги в байтах
book_capacity_bytes = book_pages * lines_per_page * chars_per_line * char_size_bytes

# Переводим информационный объем одной книги из байт в мегабайты
book_capacity_mb = book_capacity_bytes / (1024 * 1024)

# Вычисляем количество книг, которое можно разместить на дискете
num_books = diskette_capacity_mb / book_capacity_mb

print("Количество книг, помещающихся на дискету:", int(num_books))
