# 🎓 Student ERP System

A command-line **Student ERP (Enterprise Resource Planning) System** built in Python for managing student records, subject marks, averages, and topper information.

The project focuses on **Object-Oriented Programming (OOP)**, **JSON file handling**, **exception handling**, and a structured **terminal-based user interface**.

---

## ✨ Features

✔ Add new student records  
✔ Store student information locally using JSON format  
✔ Calculate student average marks automatically  
✔ View all saved student records  
✔ Find and display the topper student  
✔ Input validation for IDs, names, and marks  
✔ Handles missing or empty files safely  
✔ Structured terminal UI with formatted output

---

## 🛠 Technologies Used

- **Python 3.x**
- **Object-Oriented Programming (OOP)**
- **JSON Data Handling**
- **Exception Handling**
- **File Handling**
- **CLI / Terminal UI Design**

---

## 📚 Libraries Used

This project uses only Python built-in libraries.

| Library | Purpose |
|----------|----------|
| `json` | Store and retrieve student records in JSON format |

No external dependencies are required.

---

## 📂 Project Structure

```text
Student-ERP-System/
│── student_erp.py
│── erp.txt
└── README.md
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone <your-repository-link>
```

Move into the project directory:

```bash
cd Student-ERP-System
```

Run the program:

```bash
python student_erp.py
```

---

## 📋 Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add Student |
| 2 | View All Students |
| 3 | View Topper Student |
| 4 | Exit Program |

---

## 📊 Subjects Included

The system currently manages marks for:

- IOT
- Maths
- OS
- DSA
- C Programming

Average marks are calculated automatically from these subjects.

---

## 💾 Data Storage

Student records are stored locally inside:

```text
erp.txt
```

Data is saved using **JSON line-by-line storage format**.

Example:

```json
{
  "name": "Amarnath",
  "id": 101,
  "marks": [85, 90, 78, 88, 92],
  "average": 86.6
}
```

---

## ⚠ Error Handling & Validation

The program safely handles:

- Invalid numeric input
- Invalid student names
- Missing storage files
- Empty student records
- Incorrect menu choices

---

## 🔮 Future Improvements

Planned improvements for future versions:

- [ ] Student search by ID
- [ ] Student record update feature
- [ ] Delete student record option
- [ ] Subject-wise topper analysis
- [ ] Grade calculation system
- [ ] CSV / Database storage support
- [ ] GUI version using Tkinter / CustomTkinter
- [ ] Authentication / Admin login system

---

## 👨‍💻 Developed By

**Amarnath Rastogi**

Core logic, functionality, project structure, and implementation were independently developed by **Amarnath**.

**Claude AI (Anthropic)** was used only for **terminal UI implementation, formatting, and interface styling assistance**.
