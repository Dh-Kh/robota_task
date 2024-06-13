from redis import Redis
from rq_scheduler import Scheduler
from .scraper.robota import SeleniumRobota
from .database.storage import DatabaseRobota

def container() -> None:
    s = SeleniumRobota()
    amount = s.parser("https://robota.ua/", "junior")
    d = DatabaseRobota()
    d.execute_task(amount)

scheduler = Scheduler(connection=Redis())

job = scheduler.cron(
    cron_string="0 * * * *",  
    func=container,
    repeat=None  
)

if __name__ == "__main__":
    scheduler.run()