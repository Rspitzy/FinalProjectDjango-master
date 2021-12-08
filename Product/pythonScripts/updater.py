from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .spider import ScrapeProduct


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ScrapeProduct, 'interval', minutes=15, replace_existing=True)
    scheduler.start()
