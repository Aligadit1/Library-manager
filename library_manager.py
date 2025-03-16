import json
# funtion to load all the books from the file library.txt
def load_library():
    # make a global variable to use it all over the code
    global library
    # trying to load the data in read mode
    try:
        with open("library.txt","r") as file:
            library = json.load(file)
            # if any error occurs the library will be empty
    except (FileNotFoundError,json.JSONDecodeError):
        library = []        
# calling the function in start to load the library   
load_library()       

# function to save all the data in library.txt file
def save_library():
    # opening the library.txt in write mode
    with open("library.txt","w") as file:
        # using json format to add books as dictionary in a list
        json.dump(library,file,indent=4)

"""➕ Function to add a new book to the library"""
def adding_book():
    book_name = input("Enter book name: ")
    writer_name = input("Enter writer name: ")
    
    # 🔍 Check if the book already exists in the library
    for book in library:
        if "".join(book_name.lower().strip().split()) == "".join(book["title"].lower().strip().split()) and "".join(writer_name.lower().strip().split()) == "".join(book["author"].lower().strip().split()) :
            print(f"\n Book with name {' '.join(book_name.title().split())} by {' '.join(writer_name.title().split())} already exists ❌")
            return  # Exit function if book exists
    
    # 📅 Ensure publication year is a valid number
    while True:
        publication_year = input("Enter publication year: ").strip()
        if publication_year.isdigit():
            publication_year = int(publication_year)
            break
        else:
            print("⚠️  Invalid input! Please type a valid year.")
    
    genre = input("Enter genre: ")
    
    # 📖 Validate read status input
    while True:
        read_status = input("Have you read it? (yes/no): ").strip().lower()
        if read_status in ["yes","no","y","n"]:
            if read_status in ["yes","y"]:
                read_status = True
            else:
                read_status = False    
            break
        else:
            print("⚠️  Invalid input! Please type 'yes' or 'no'.")
    
    # 🆕 Create a new book dictionary
    new_book = {
        "title":book_name,
        "author":writer_name,
        "publication_year":publication_year,
        "genre":genre,
        "read_status":read_status,
    }
    
    library.append(new_book)  # 📥 Add book to library
    save_library()
    print("\n✅ Book added successfully!") 

"""❌ Function to remove a book from the library"""
def remove_book():
    if not library:
        print("\n🚫 No books in the library")
    else:
        title_to_remove = "".join(input("Enter the title of the book to remove: ").strip().lower().split())
        author_to_remove = "".join(input("Enter the author of the book to remove: ").strip().lower().split())
        found = False
        for book in library:
            if "".join(book["title"].lower().strip().split()) == title_to_remove and "".join(book["author"].lower().strip().split()) == author_to_remove:
                found = True
                readable_status = "Unread"
                if book["read_status"] == True:
                    readable_status = "Read"
            
                print(f"\n📖 Name : {book['title'].title()}\n✍️  Author : {book['author'].title()}\n📅 Published year : {book['publication_year']}\n📚 Genre : {book['genre'].capitalize()}\n📌 Status : {readable_status}")
            
                # ⚠️ Confirm deletion for unread books
                if book["read_status"] == False:
                    while True:
                        removing_confirmation = input("You have not read this book yet. Are you sure you want to delete it? (yes/no): ").strip().lower()
                        if removing_confirmation in ["yes","no","y","n"]:
                            break
                        else:
                            print("⚠️  Invalid input! Please type 'yes' or 'no'.")
                    if removing_confirmation in ["yes","y"]:
                        library.remove(book)
                        print("\n✅ Book removed successfully")
                        save_library()
                        break
                    else:
                        print("\n🚫 Book removal cancelled")    
                else:
                    library.remove(book)
                    print("\n✅ Book removed successfully")
                    save_library()
                    break
        if not found:
            print("\n❌ Book not found") 

"""🔍 Function to search for a book by title"""
def search_book():
    if not library:
        print("\n🚫 No books in the library")
    else:    
        print("\n🔍 Search by: \n1️⃣  Title\n2️⃣  Author")
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            title_to_search = "".join(input("Enter the book name you want to search: ").strip().lower().split())
            for book in library:
                if "".join(book["title"].strip().lower().split()) == title_to_search:
                    readable_status = "Unread"
                    if book["read_status"] == True:
                        readable_status = "Read"
                    print(f"\n📖 Name : {book['title'].title()}\n✍️  Author : {book['author'].title()}\n📅 Published year : {book['publication_year']}\n📚 Genre : {book['genre'].capitalize()}\n📌 Status : {readable_status}")
                    break
            else:
                print("\n❌ Book not found.")
        elif choice == "2":
            author_to_search="".join(input("Enter authors name: ").strip().lower().split())
            found_books = [book for book in library if "".join(book["author"].strip().lower().split()) == author_to_search ]
            if found_books:
                print("\n📚 Books by this author:")
                for index, book in enumerate(found_books, start=1):
                    readable_status = "Unread"
                    if book["read_status"] == True:
                        readable_status = "Read"
                    print(f"\n{index}. 📖 Name : {book['title'].title()}\n   ✍️  Author : {book['author'].title()}\n   📅 Published year : {book['publication_year']}\n   📚 Genre : {book['genre'].capitalize()}\n   📌 Status : {readable_status}")
            else:
                print("\n❌ No books found by this author.")
        else:
            print("\n⚠️  Invalid choice! Please enter 1 or 2.")  

"""📚 Function to display all books in the library"""
def all_books():
    if not library:
        print("\n🚫 No books in the library")
    else:
        print("\n📖 Current books in the library")    
        for index, book in enumerate(library,start=1):
            readable_status = "Unread"
            if book["read_status"] == True:
                readable_status = "Read"
            print(f"\n{index}. 📖 Name : {book['title'].title()}\n   ✍️ Author : {book['author'].title()}\n   📅 Published year : {book['publication_year']}\n   📚 Genre : {book['genre'].capitalize()}\n   📌 Status : {readable_status}")

"""📊 Function to show statistics about the library"""
def statistics():
    total_books = len(library)
    books_read = sum(1 for book in library if book["read_status"])
    
    print("\n📊 Statistics of your library")
    if total_books == 0:
        print("📚 Total books = 0")
        print("📖 Books read = 0.00%")
        return
    if books_read == 0:
        print(f"📚 Total books = {total_books}")
        print("📖 Books read = 0.00%")
        return
    print(f"📚 Total books = {total_books}")
    print(f"📖 Percentage Read = {(books_read/total_books)*100:.2f}%")

# 🎯 Main menu loop
while True:
    print("\n🎉 Welcome to your Personal Library Manager!")
    print("1️⃣  ➕ Add a book ")
    print("2️⃣  🗑️  Remove a book")
    print("3️⃣  🔍 Search for a book")
    print("4️⃣  📚 Display all books")
    print("5️⃣  📈 Display statistics")
    print("6️⃣  🚪 Exit and Save")
    
    user_choice = input("Enter your choice (1-6): ")
    
    if user_choice == "1":
        adding_book()
    elif user_choice == "2":
        remove_book()
    elif user_choice == "3":
        search_book()
    elif user_choice == "4":
        all_books()
    elif user_choice == "5":
        statistics()
    elif user_choice == "6":
        save_library()
        print("Library saved to file. 👋Goodbye!")
        break  # Exit the loop
    else:
        print("\n⚠️  Invalid choice, please enter a number between 1 and 6.")
