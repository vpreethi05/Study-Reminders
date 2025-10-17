import schedule
import time

def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger):
    """Schedule reminder delivery for each student at their preferred time."""
    for student in students_manager.get_students():
        reminder = reminder_generator(student['name'], student['course'])
        # Schedule for the preferred time (real use)
        schedule.every().day.at(student['preferred_time']).do(
            lambda s=student, r=reminder: (reminder_sender(s['email'], r), logger(s, r))
        )
        # Run immediately once for testing
        reminder_sender(student['email'], reminder)
        logger(student, reminder)

    print("Scheduler started (simulated for 30 seconds)...")
    start = time.time()
    while time.time() - start < 5:  # shorter for quick test
        schedule.run_pending()
        time.sleep(1)
    print("Scheduler stopped (test complete).")
