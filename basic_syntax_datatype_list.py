books = ['Seven Habits', 'How to influence people', 'First Things First']
print(books)
print('\nUsing loop to print:')
for i in books:
    print(i)

print('\nUsing in range:')
for i in range(0,len(books)):
    print(books[i])

print('\nAdding an element to the list')
print('Add Dog Man to the list of Books')
books.append('Dog Man')
for i in range(0,len(books)):
    print(books[i])
