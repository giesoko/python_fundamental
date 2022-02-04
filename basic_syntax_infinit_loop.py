'''
loop until a condition is satisfied
'''
print ('Mom said "Budi, read all your books until you get them".')
print ('Budi did not understand the last book and read it repeatedly '
       'until total reads twice the number of the books')
count_books = 10
count_reads = 0
count_understood = 0

while count_reads < count_books * 2:
    count_reads = count_reads + 1
    if count_understood == count_books-1:
        print(f"Buku ke {count_understood + 1} was not clear")
    else:
        count_understood = count_understood + 1
        print(f'Book number {count_understood} had been read and understood')
print(f'Number of books that have been read and understood : {count_understood} books')
print(f'Budi said, "I could only get {count_understood} books"')
