from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
from study_reminders.scheduler import schedule_reminders

if __name__ == "__main__":
    manager = StudentsManager()
    schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)
