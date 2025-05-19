class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.is_borrowed = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Genre: {self.genre}"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")

class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre, sub_genre):
        super().__init__(title, author, publication_year, genre)
        self.sub_genre = sub_genre

    def __str__(self):
        return f"{super().__str__()}, Sub-Genre: {self.sub_genre}"

    def describe_setting(self):
        print(f"The fictional world of '{self.title}'...")

class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, genre, topic):
        super().__init__(title, author, publication_year, genre)
        self.topic = topic

    def __str__(self):
        return f"{super().__str__()}, Topic: {self.topic}"

    def summarize_topic(self):
        print(f"'{self.title}' provides insights into {self.topic}.")

# Creating instances
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction")
fiction_book = FictionBook("Pride and Prejudice", "Jane Austen", 1813, "Fiction", "Romance")
non_fiction_book = NonFictionBook("Sapiens", "Yuval Noah Harari", 2011, "Non-Fiction", "History")

print(book1)
print(fiction_book)
print(non_fiction_book)

book1.borrow()
book1.return_book()
fiction_book.describe_setting()
non_fiction_book.summarize_topic()
