#timer looper
import schedule
import time
import datetime

class Scheduler:
    def __init__(self):
        self.job = None

    def perform_task(self):
        # Placeholder for the task code
        print(f"Task executed at {datetime.datetime.now()}")

    def schedule_task(self, day_of_week=None, time_of_day=None, interval=None, unit='seconds', task=None):
        if task is not None:
            self.perform_task = task

        if interval is not None:
            if unit == 'seconds':
                self.job = schedule.every(interval).seconds.do(self.perform_task)
            elif unit == 'minutes':
                self.job = schedule.every(interval).minutes.do(self.perform_task)
            elif unit == 'hours':
                self.job = schedule.every(interval).hours.do(self.perform_task)
            elif unit == 'days':
                self.job = schedule.every(interval).days.do(self.perform_task)
            elif unit == 'weeks':
                self.job = schedule.every(interval).weeks.do(self.perform_task)
        elif day_of_week is not None and time_of_day is not None:
            self.job = getattr(schedule.every(), day_of_week).at(time_of_day).do(self.perform_task)

        self.wait_until_next_run()

    def calculate_sleep_duration(self):
        now = datetime.datetime.now()
        next_run = schedule.next_run()
        sleep_duration = (next_run - now).total_seconds()
        return max(sleep_duration, 0)

    def wait_until_next_run(self):
        while True:
            schedule.run_pending()
            sleep_duration = self.calculate_sleep_duration()
            if sleep_duration > 0:
                time.sleep(sleep_duration)
            else:
                break