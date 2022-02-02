'''
There are two repetition in python:
1. for, used when the number of repetition is defined. E.g. Read this book 10 times.
2. while, used when the number of repetition is not defined. E.g. Read this book until you understand.
'''
# using for
count_books = 10
print(f"There are {count_books} books")
print('Mom said, "Read all of your books!')
count_books_read = 0
for count_books_read in range(1, count_books + 1):
    print(f'Reading book number {count_books_read}')
    print(f'Book number {count_books_read} has been read')
print(f'Total number of books have been read = {count_books_read}')
