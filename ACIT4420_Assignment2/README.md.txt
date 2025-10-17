README.md — Study Reminders Automation
# study_reminders

A Python package that automates personalized study reminders for students.  
This project was developed as part of **ACIT4420 – Problem Solving with Scripting (Assignment II)** at **OsloMet**.

---

##  Project Purpose

The goal of this project is to design a modular Python package that automatically generates, sends, and logs personalized study reminders for students.  
It demonstrates **file handling**, **modular programming**, **scheduling**, and **automation techniques** using Python.

---

##  Features

- Manage a list of students with names, emails, courses, and reminder times.
- Generate personalized study reminder messages automatically.
- Simulate sending reminders via console output.
- Log all reminders with timestamps in a text file.
- Schedule reminders based on preferred times using the `schedule` library.
- Modular design: each module handles a specific part of the process.

---

##  Project Structure



ACIT4420_Assignment2/
│
├── main.py
├── students.json
├── README.md
├── setup.py
├── reminder_log.txt
│
└── study_reminders/
├── init.py
├── students.py
├── students_manager.py
├── reminder_generator.py
├── reminder_sender.py
├── logger.py
└── scheduler.py


---

##  Installation

### 1. Install dependencies
Make sure you have Python 3.x installed, then run:

```bash
pip install schedule

2. Clone or extract the project

Place the study_reminders folder and all files inside a directory such as:

C:\Users\<yourname>\ACIT4420_Assignment2

3. Run the program

From your terminal or Jupyter Notebook, navigate to the folder and run:

python main.py

 How It Works

The program reads student data from students.json.

For each student, it creates a personalized study reminder message.

The reminder is "sent" by printing it in the console.

The system logs every reminder with a timestamp to reminder_log.txt.

The scheduling module (schedule) simulates automatic daily reminder delivery (in this project, it runs for 30 seconds for testing).

 Example Output
Sending reminder to alice@example.com: Hi Alice, remember to review Python Scripting materials before the deadline!
Sending reminder to bob@example.com: Hi Bob, remember to review Data Science materials before the deadline!
Sending reminder to charlie@example.com: Hi Charlie, remember to review AI Basics materials before the deadline!
Scheduler started (simulated for 30 seconds)...
Scheduler stopped (test complete).

 Modules Overview
Module	Description
students.py	Basic management of student lists.
students_manager.py	Handles student data stored in JSON format.
reminder_generator.py	Creates personalized reminder messages.
reminder_sender.py	Simulates sending reminders (console output).
logger.py	Logs reminders to a file with timestamps.
scheduler.py	Automates daily reminder scheduling using the schedule library.
main.py	Integrates all modules into one automation process.
 Logging

All reminders are logged automatically in reminder_log.txt, including student name, timestamp, and message content.
This ensures traceability and provides evidence that the reminders were generated and processed.

Testing

Unit tests are provided in test.py to verify the core functionality of each module.

To run the tests:

python -m unittest test.py


Or for verbose mode:

python -m unittest -v test.py


 These tests check:

Adding and removing students

Generating reminders

Sending reminders (simulated)

Logging reminder details

Reading/writing student data

If everything is correct, you will see:

.....
----------------------------------------------------------------------
Ran 5 tests in 0.5s

OK


-----------------------

Execute:

To test the package quickly:

Run python main.py.

Check the console for reminder messages.

Open reminder_log.txt to confirm logs were written correctly.

