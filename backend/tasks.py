from celery import Celery
from celery.signals import beat_init
from scraper.robota import SeleniumRobota
from database.storage import DatabaseRobota

app = Celery("tasks")

app.config_from_object('celeryconfig')

@app.task(acks_late=True)
def container() -> None:
    s = SeleniumRobota()
    amount = s.parser("https://robota.ua/", "junior")
    d = DatabaseRobota()
    d.execute_task(amount)
   
@beat_init.connect
def task_before_beat_starts(sender, **kwargs):
    container()