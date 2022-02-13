books = ['Seven Habits', 'How to influence people', 'First Things First', 'Predictably Irrational']
print('\nDel command with list comprehension')
del books[:]
for i in range(0,len(books)):
    print(books[i])

books = ['Seven Habits', 'How to influence people', 'First Things First', 'Predictably Irrational']
print('\nDel command with list comprehension [start:stop]')
del books[0:2]
for i in range(0,len(books)):
    print(books[i])

books = ['Seven Habits', 'How to influence people', 'First Things First', 'Predictably Irrational']
print('\nDel command with list comprehension [start:-stop]')
del books[0:-1]
for i in range(0,len(books)):
    print(books[i])

books = ['Seven Habits', 'How to influence people', 'First Things First', 'Predictably Irrational']
print('\nDel command with list comprehension [start:stop:step]') #blank [count] means up to the last element
del books[0::2]
for i in range(0,len(books)):
    print(books[i])

print('\nCreate a New List')
books = ['Seven Habits', 'How to influence people', 'First Things First', 'Predictably Irrational']
#use list comprehension to copy elements in a list and create a new list for the elements
#this way, you can delete the old list and the new one will not be affected
new_books = books[:]
#delete books list
del books[:]
#check what's inside the Books list
for i in range(0,len(books)):
    print(books[i])
#check what's inside the new_books
for i in range(0,len(new_books)):
    print(new_books[i])

print('\nCreate a New List with comprehension [start:stop:end')
books = ['Seven Habits', 'How to influence people', 'First Things First', 'Predictably Irrational']
new_books = books[0::2]
for i in range(0,len(new_books)):
    print(new_books[i])