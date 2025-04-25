Python Sales Data BST Parser
This is a simple command-line project I built in Python to practice data parsing, file I/O, and implementing a Binary Search Tree (BST) from scratch. It loads sales-style data from a CSV file, inserts it into a BST, and allows users to search or display the entries through a menu interface.

The project includes structured OOP design with classes for bids, tree nodes, and the full BST, along with a clean CLI flow for interaction.

🔍 What It Does
✅ Load bids from a CSV file
🌳 Insert bids into a Binary Search Tree ordered by ID
📋 Display all bids in-order (sorted by ID)
🔎 Search bids by their ID
🧠 Input validation and clear feedback
💬 Command-line menu interface

🧰 Tech Stack
Python 3

CSV module

Object-Oriented Programming

CLI (no external packages)

📁 Project Structure
bash
Copy
Edit
Python-Sales-Data-BST-Parser/
├── main.py          # Main Python script with BST and menu
├── bids.csv         # Sample CSV file with sales data
└── README.md        # This file
🚀 How to Run
Clone the repository or download the files

bash
Copy
Edit
git clone https://github.com/Samuelr2112/Python-Sales-Data-BST-Parser.git
cd Python-Sales-Data-BST-Parser
Run the program

bash
Copy
Edit
python main.py
📄 Sample CSV Format
csv
Copy
Edit
bidId,title,fund,amount
1001,Office Supplies,General Fund,45.50
1002,Projector Rental,Tech Fund,200.00
1003,Conference Registration,Education Fund,150.75
✅ How the Menu Works
Load Bids from the CSV file

Display All Bids in-order using the BST

Search for a Bid by entering a specific ID

Exit the program

👋 Why I Built This
I wanted to improve my Python skills while revisiting core computer science concepts like Binary Search Trees and file parsing. This project helped me practice clean coding, recursion, and user input handling — and it’s something you can run easily without any dependencies or setup.

Feel free to test it out or build on it!

Let me know if you want me to update the README.md file in your repo directly.
