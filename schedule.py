import schedule
import time

def morning():
    print("good morning")

def noon():
    print("good noon")

def evening():
    print("good evening")

def task1():
    print("task1 was initiated")
def task2():
    print("task2")
def task3():
    print("task3")

evening()

#schedule.every().day.at("23:18").do(task1)
#schedule.every().day.at("23:19").do(task2)
#schedule.every().day.at("23:20").do(task3)
#schedule.every(1).minutes.do(morning)
#schedule.every(10).seconds.do(noon)

while True:
    schedule.run_pending()
    time.sleep(1)
