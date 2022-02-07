books = ['Seven Habits', 'How to influence people', 'First Things First']
print(books)
print('\nUsing loop to print:')
for i in books:
    print(i)

print('\nUsing in range:')
for i in range(0,len(books)):
    print(books[i])

print('\nAdding an element to a list:')
print('Add Dog Man to the list of Books')
books.append('Dog Man')
for i in range(0,len(books)):
    print(books[i])

print('\nErasing all elements in a list:')
books.clear()
for i in range(0,len(books)):
    print(books[i])

print('\nModifying an element in a list:')
print('Modifying the first element, from Seven Habits to Harry Potter')
books = ['Seven Habits', 'How to influence people', 'First Things First']
books[0] = 'Harry Potter'
for i in range(0,len(books)):
    print(books[i])

print('\nTake an element and store it in a variable using pop:')
print('Take element 1 and store it in a new variable fav_book')
fav_book = books.pop(1)
for i in range(0,len(books)):
    print(books[i])
print(f'\nMy favorite book:\n{fav_book}')

print('\nWithout a parameter, pop takes the last element:')
print("Let's put the favorite book back to Books list")
print('Append will put the fav_book as the last element in the list')
books.append(fav_book)
for i in range(0,len(books)):
    print(books[i])
last_book = books.pop()
print(f'\nI took {last_book} from the Books list')
