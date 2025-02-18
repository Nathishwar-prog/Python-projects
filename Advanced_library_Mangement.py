#Author : Nathishwar
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, member_id, contact_info):
        self.name = name
        self.member_id = member_id
        self.contact_info = contact_info
        self.borrowed_books = []
        self.fines = 0.0

    def borrow_book(self, book, due_date):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append({"book": book, "due_date": due_date})
            print(f"{self.name} borrowed '{book.title}' (Due: {due_date})")
        else:
            print(f"'{book.title}' is not available for borrowing.")

    def return_book(self, book):
        for borrowed in self.borrowed_books:
            if borrowed["book"] == book:
                book.is_available = True
                self.borrowed_books.remove(borrowed)
                self.calculate_fine(borrowed["due_date"])
                print(f"{self.name} returned '{book.title}'")
                return
        print(f"'{book.title}' was not borrowed by {self.name}.")

    def calculate_fine(self, due_date):
        if datetime.now() > due_date:
            days_late = (datetime.now() - due_date).days
            fine = days_late * 0.50  # $0.50 per day late
            self.fines += fine
            print(f"{self.name} has a fine of ${fine:.2f} for late return.")
        else:
            print(f"{self.name} returned the book on time. No fine.")

    def pay_fine(self, amount):
        if amount <= self.fines:
            self.fines -= amount
            print(f"{self.name} paid ${amount:.2f}. Remaining fines: ${self.fines:.2f}")
        else:
            print(f"Amount exceeds the fine. {self.name}'s fine is ${self.fines:.2f}")

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}, Contact: {self.contact_info})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added {member} to the library.")

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == book.isbn:
                results.append(book)
        return results

    def borrow_book(self, member_id, isbn, due_date):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        if member and book:
            member.borrow_book(book, due_date)
            self.transactions.append({
                "type": "borrow",
                "member": member.name,
                "book": book.title,
                "date": datetime.now()
            })
        else:
            print("Member or book not found.")

    def return_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        if member and book:
            member.return_book(book)
            self.transactions.append({
                "type": "return",
                "member": member.name,
                "book": book.title,
                "date": datetime.now()
            })
        else:
            print("Member or book not found.")

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction['type'].capitalize()}: {transaction['member']} - '{transaction['book']}' on {transaction['date']}")

# Example usage
library = Library()

# Adding books
book1 = Book("Python Programming", "John Doe", "123456")
book2 = Book("Advanced Python", "Jane Smith", "654321")
library.add_book(book1)
library.add_book(book2)

# Adding members
member1 = Member("Alice", "M001", "alice@example.com")
member2 = Member("Bob", "M002", "bob@example.com")
library.add_member(member1)
library.add_member(member2)

# Borrowing books
due_date = datetime.now() + timedelta(days=14)
library.borrow_book("M001", "123456", due_date)
library.borrow_book("M002", "654321", due_date)

# Returning books
library.return_book("M001", "123456")
library.return_book("M002", "654321")

# Listing transactions
library.list_transactions()

# Searching for books
results = library.search_books("Python")
for book in results:
    print(book)
