#using while
count_books=10
count_books_read = 0
print(f"There are {count_books} books")
print('Mom said, "Read all of your books!')

while count_books_read < count_books:
    count_books_read = count_books_read + 1
    print(f'reading book number {count_books_read}')
    print(f'Book number {count_books_read} has been read')
print(f'Total number of books have been read = {count_books_read}')