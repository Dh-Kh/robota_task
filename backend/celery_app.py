from celery import Celery
from celery.schedules import crontab
from celery.signals import beat_init
from scraper.robota import SeleniumRobota
from database.storage import DatabaseRobota
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

app = Celery("Worker", broker=REDIS_URL)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/2'),
        #crontab(minute="0", hour="*"),  
        container.s(),  
        name="scheduler"
    )

@app.task
def container() -> None:
    s = SeleniumRobota()
    amount = s.parser("https://robota.ua/", "junior")
    d = DatabaseRobota()
    d.execute_task(amount)
    print("Task is running!")
    
@beat_init.connect
def task_before_beat_starts(sender, **kwargs):
    container()
    print("First run!")


