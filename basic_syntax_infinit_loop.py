'''
loop until a condition is satisfied
'''
print ('Mom said "Budi, read all your books until you get them".')
print ('Budi did not understand the last book and read it repeatedly '
       'until total reads twice the number of the books')
number_of_books = 10
count_total_reads = 0
count_books_read_understood = 0

while count_total_reads < number_of_books * 2:
    count_total_reads = count_total_reads + 1
    if count_books_read_understood == number_of_books-1:
        print(f"Buku ke {count_books_read_understood + 1} was not clear")
    else:
        count_books_read_understood = count_books_read_understood + 1
        print(f'Book number {count_books_read_understood} had been read and understood')
print(f'Number of books that have been read and understood : {count_books_read_understood} books')
print(f'Budi said, "I could only get {count_books_read_understood} books"')
