📘 Study Reminders Automation – ACIT4420 Assignment 2

This project was developed as part of ACIT4420 – Problem Solving with Scripting at OsloMet (Oslo Metropolitan University).
It demonstrates how Python can be used to build an automated system that sends personalized study reminders to students using modular programming, scheduling, and file handling techniques.

🎯 Project Purpose

The main goal of this assignment is to design a modular Python package named study_reminders that can:

Manage student information (name, email, course, preferred reminder time)

Generate personalized study reminder messages

Simulate sending reminders via console output

Log each reminder with timestamps

Schedule daily reminder delivery using the schedule library

This project shows how scripting can automate routine communication tasks and demonstrates good software design practices such as modularity, logging, and data management.

🗂 Project Structure
ACIT4420_Assignment2/
│
├── main.py                     # Main script integrating all modules
├── students.json               # Dummy student data
├── setup.py                    # Setup file for package installation
├── test.py                     # Unit tests for modules
├── README.md                   # Main project documentation
│
├── study_reminders/            # Package folder
│   ├── __init__.py
│   ├── students.py
│   ├── students_manager.py
│   ├── reminder_generator.py
│   ├── reminder_sender.py
│   ├── logger.py
│   └── scheduler.py
│
├── reminder_log.txt            # Generated automatically after first run
│
├── Assignment2_Report.pdf      # Full report on implementation and reflection
└── Assignment2_SourceFile.ipynb  # Jupyter Notebook source for module execution



🚀 How to Run

Install the required library:

pip install schedule


Run the main program:

python main.py


Check:

Console output → to see simulated reminders

reminder_log.txt → to confirm logs were recorded

Alternatively, you can open and execute all modules interactively in
📓 ACIT4420_Assignment2.ipynb (Jupyter Notebook).

🧪 Testing (Optional)

Unit tests for each module are included in test.py.
You can run them using:

python -m unittest -v test.py


This verifies key functions like adding/removing students, generating reminders, and logging activities.

📄 Documentation and Report

A detailed technical description of each module, sample outputs, and test results is included in
📁 ACIT4420_Assignment2/README.md

The full written report (Introduction, Methods, Results, and Discussion) describing the program, workflow, and challenges is provided in
📄 Assignment2_Report.pdf inside the project folder.

🧩 Learning Outcomes

Through this assignment, I learned how to:

Structure a Python project into reusable modules

Use JSON for data storage

Implement logging for system traceability

Schedule automated tasks using the schedule library

Integrate and test different components in one working system

👤 Author

Name: Preethi Vijayakumar
Course: ACIT4420 – Problem Solving with Scripting
Institution: OsloMet – Oslo Metropolitan University

✅ This repository contains the complete code, Jupyter source, detailed report, and documentation for the automated study reminder system.
