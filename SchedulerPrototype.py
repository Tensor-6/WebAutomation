#scheduler tester
import Scheduler as s
sch = s.Scheduler()
def task():
    print("sucess testertask")
sch.schedule_task('sunday', '13:1', 2,'seconds',task)
print("sucess posttask")