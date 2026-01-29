# 📂 Protected File Reader (Python)

A simple Python program that safely reads a file using exception handling (`try-except-finally`) to prevent crashes and handle common file-related errors.

---

## 🚀 Features

- Takes filename input from user  
- Reads and displays file content  
- Handles missing file errors  
- Handles permission access errors  
- Prevents empty filename input  
- Always executes cleanup message using `finally`  

---

## 🛠 Technologies Used

- Python 3  
- File Handling  
- Exception Handling (`try-except-finally`)  

---

## 📋 How It Works

1. User enters a file name  
2. Program checks if input is empty  
3. Program tries to open and read the file  
4. If an error occurs, it is handled gracefully  
5. Program prints **Operation Finished** every time  

---

## ▶ How To Run

1. Make sure Python is installed  
2. Save the program file (example: `file_reader.py`)  
3. Open terminal or command prompt  
4. Run the following command:

```bash
python file_reader.py
