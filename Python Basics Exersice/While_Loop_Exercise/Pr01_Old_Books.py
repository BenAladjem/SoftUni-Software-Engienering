book_name = input()
book_count = 0
found_book = False
current_book = input()
while not current_book=="No More Books":
    if current_book == book_name:
        found_book = True
        print("You checked %d books and found it."%(book_count))
        break

    book_count +=1
    current_book = input()
if not found_book:
    print("The book you search is not here!")
    print("You checked %d books."%(book_count))