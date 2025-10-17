import unittest
import os
from study_reminders.students import Students
from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder

class TestStudyReminders(unittest.TestCase):

    def setUp(self):
        # Setup temporary test data
        self.manager = StudentsManager()
        self.students = [
            {"name": "Alice", "email": "alice@example.com", "course": "Python Scripting", "preferred_time": "08:00"},
            {"name": "Bob", "email": "bob@example.com", "course": "Data Science", "preferred_time": "09:00"}
        ]
        # Clean up old log file if exists
        if os.path.exists("reminder_log.txt"):
            os.remove("reminder_log.txt")

    # ---------- Students.py ----------
    def test_students_add_and_remove(self):
        students = Students()
        students.add_student("Alice", "alice@example.com", "Python")
        self.assertEqual(len(students.get_students()), 1)
        students.remove_student("Alice")
        self.assertEqual(len(students.get_students()), 0)

    # ---------- StudentsManager.py ----------
    def test_students_manager_load_and_save(self):
        self.manager.add_student("TestUser", "test@example.com", "AI", "10:00")
        data = self.manager.get_students()
        self.assertTrue(any(s['name'] == "TestUser" for s in data))

    # ---------- ReminderGenerator.py ----------
    def test_reminder_generator(self):
        msg = generate_reminder("Alice", "Python")
        self.assertIn("Alice", msg)
        self.assertIn("Python", msg)

    # ---------- ReminderSender.py ----------
    def test_reminder_sender(self):
        try:
            send_reminder("test@example.com", "Reminder message")
        except Exception as e:
            self.fail(f"send_reminder raised Exception unexpectedly: {e}")

    # ---------- Logger.py ----------
    def test_logger_creates_file(self):
        student = {"name": "Alice", "email": "alice@example.com", "course": "Python"}
        log_reminder(student, "This is a test reminder")
        self.assertTrue(os.path.exists("reminder_log.txt"))

if __name__ == "__main__":
    unittest.main()
