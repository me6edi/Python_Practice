books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
print("Now the top book is",books[-1])

books.pop()
print("Now the top book is",books[-1])

books.pop()
if not books:
    print("No books left")