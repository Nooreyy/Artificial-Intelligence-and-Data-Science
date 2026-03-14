'''You are designing a mini library system.
Use a dictionary to store books. Key = book ID, Value = another dictionary with keys: title, author, available (True/False).
Add 3 books to the system.
Borrow one book (mark available=False).
Return one book (mark available=True).
Print the status of all books.
Use a set to store borrowed_user_ids to make sure a user doesn’t borrow the same book twice.'''

# create a dictionary to store books
print("***Library System***")
library = {
    1: {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'available': True},
    2: {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': True},
    3: {'title': '1984', 'author': 'George Orwell', 'available': True}
}
print("Books in the library:")

for book_id, book_info in library.items():
    print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")

# borrow one book (mark available=False)
print("\n***Borrowing a book (ID: 1)***")
library[1]['available'] = False

# return one book (mark available=True)
print("\n***Returning a book (ID: 2)***")
library[2]['available'] = True

# print the status of all books
print("\n***Updated Library Status***")
for book_id, book_info in library.items():
    print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")

# use a set to store borrowed_user_ids
print("\n***Borrowed User IDs***")
borrowed_user_ids = set()
user_id = 'user123'
# check if the user has already borrowed the book
if user_id in borrowed_user_ids:
    print(f"{user_id} has already borrowed a book.")
else:
    borrowed_user_ids.add(user_id)
    print(f"{user_id} has borrowed a book.")

# trying to borrow the same book again
if user_id in borrowed_user_ids:
    print(f"{user_id} has already borrowed a book.")
else:
    borrowed_user_ids.add(user_id)
    print(f"{user_id} has borrowed a book.")
    