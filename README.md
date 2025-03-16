Personal Library Manager

📖 About the Project

The Personal Library Manager is a command-line application that allows users to manage their personal book collection. With this tool, users can add, remove, search, and display books while also tracking their reading progress. The library data is saved persistently using JSON file handling to ensure that books remain stored even after the program is closed.

🛠 Features

➕ Add a book: Users can add new books by entering the title, author, publication year, genre, and read status.

🗑️ Remove a book: Users can remove a book from the library, with a confirmation step for unread books.

🔍 Search for books: Books can be searched by title or author.

📚 Display all books: Shows all books stored in the library along with details such as author, publication year, genre, and read status.

📊 View library statistics: Displays the total number of books and the percentage of books read.

🚪 Persistent storage: Uses JSON file handling to save and load books from a file (library.txt).

📂 Project Structure

|-- library.txt       # JSON file storing the book data
|-- library_manager.py  # Python script for managing the library

🚀 How to Run the Project

Prerequisites

Install Python 3.x on your system.

Running the Program

Clone the repository:

git clone https://github.com/your-username/personal-library-manager.git
cd personal-library-manager

Run the script:

python library_manager.py

📜 How It Works

The program loads the existing book data from library.txt.

The user is presented with a menu to choose an action.

The selected operation is performed (adding, removing, searching, displaying books, or viewing statistics).

The updated library is saved back to library.txt before exiting.

💾 Data Storage

The library data is stored in library.txt using JSON format.

Each book entry has the following structure:

[
  {
    "title": "Book Title",
    "author": "Author Name",
    "publication_year": 2024,
    "genre": "Fiction",
    "read_status": true
  }
]

🎯 Example Usage

🎉 Welcome to your Personal Library Manager!
1️⃣  ➕ Add a book
2️⃣  🗑️  Remove a book
3️⃣  🔍 Search for a book
4️⃣  📚 Display all books
5️⃣  📈 Display statistics
6️⃣  🚪 Exit and Save
Enter your choice (1-6): 1
Enter book name: The Alchemist
Enter writer name: Paulo Coelho
Enter publication year: 1988
Enter genre: Fiction
Have you read it? (yes/no): yes

✅ Book added successfully!

🛠 Technologies Used

Python (for implementing the functionality)

JSON (for storing and retrieving data persistently)

📌 Future Enhancements

Add a feature to update book details.

Implement a category-wise listing of books.

Create a graphical user interface (GUI) using Tkinter or PyQt.

Export book lists to a CSV file.

🤝 Contributing

If you'd like to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m "Add new feature").

Push to the branch (git push origin feature-branch).

Open a pull request.

📞 Contact

If you have any questions, feel free to reach out via GitHub Issues!

Happy coding! 🚀📚

