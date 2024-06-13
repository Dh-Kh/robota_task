from redis import Redis
from datetime import datetime
from rq_scheduler import Scheduler
from scraper.robota import SeleniumRobota
from database.storage import DatabaseRobota

#issue not working periodic task
#also add periodic in Readme.md

def container() -> None:
    s = SeleniumRobota()
    amount = s.parser("https://robota.ua/", "junior")
    d = DatabaseRobota()
    d.execute_task(amount)


if __name__ == "__main__":
    
    scheduler = Scheduler(connection=Redis())
    
    #3600    
    
    job = scheduler.schedule(
        scheduled_time=datetime.utcnow(),
        func=container,
        interval=120,
        repeat=None  
    )
    

    scheduler.run()