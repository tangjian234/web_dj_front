# runapscheduler.py
##### run stack_spider in different directory  
import sys
sys.path.append(r'c:/Local/Work/Web/web/tutorial/scrapyRT/stack/stack/spiders')
from datetime import datetime, timedelta
from runpy import run_path
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.twisted import TwistedScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import schedule
import time
import logging

from twisted.internet.error import ReactorAlreadyRunning
from stack_spider import StackSpider
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
 
class scrapy_scheduler:

  def __init__(self):
    ##### kick start the schedular
    self.scheduler = TwistedScheduler()
    self.scheduler.add_jobstore(DjangoJobStore(), "default")
    self.process = CrawlerProcess(get_project_settings())
    self.scheduler.start()

  def my_job(self):
      #  Your job processing logic here...
      print("My job")


  def delete_old_job_executions(self,max_age=604_800):
      """This job deletes all apscheduler job executions older than `max_age` from the database."""
      DjangoJobExecution.objects.delete_old_job_executions(max_age)
  
  def handle_scrapy_start(self):
    try : 
      start=datetime.now()
      end=start+ timedelta(seconds=32)
      ##### add_job
      self.scheduler.add_job(self.process.crawl, 'interval', args=[StackSpider], seconds=20,next_run_time=datetime.now(),start_date = start,end_date=end )
      self.process.start(False) 
    except ReactorAlreadyRunning:
      logger.info("already run")

  def handle_scrapy_stop(self):
      logger.info("Stopping scheduler...")
      self.process.stop()
      self.scheduler.shutdown() 
      logger.info("Scheduler shut down successfully!")
  

 
'''
def handle():
    #scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler = TwistedScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        my_job,
        trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        id="my_job",  # The `id` assigned to each job MUST be unique
        max_instances=1,
        replace_existing=True,
    ) 
    logger.info("Added job 'my_job'.")

    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler shut down successfully!")

'''