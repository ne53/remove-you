import schedule
from time import sleep
import main
main.run()
def task():
    main.run()
schedule.every(1).minutes.do(task)
while True:
    schedule.run_pending()
    sleep(1)