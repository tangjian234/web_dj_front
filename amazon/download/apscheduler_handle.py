# runapscheduler.py

##### run stack_spider in different directory  
import sys
sys.path.append(r'c:/Local/Work/Web/web/tutorial/scrapyRT/stack/stack/spiders')
sys.path.append(r'C:/Local/Work/Python/PyLib/scrapy/download/download/spiders')

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
from quotes_spider import Download_Test,Download_Test_local

from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED

import os 
from pathlib import Path,PureWindowsPath 

# Start logger  
from log_lib import Logger
logger = Logger()

class scrapy_scheduler:
  
  '''
  <A class used to run crawl work in a python apscheduler, run once or periodicity 

  <Attributes> 
  ----------
  scheduler : TwistedScheduler
  process : CrawlerProcess
  job_complete_status : 
    dictionary for each task_id : task complete is true, not complete is false, 
  task_id :pk of task 

  <Methods>
  -------
  __init__(self) :
    Initialize scheduler,  
  job_completed(self,event):    
    Call back function after scrapping task is completed
  '''
  def __init__(self):
    '''
    Initialize scheduler,  
    kick start crawl process ,
    Set task_id(pk) to indicate which task is being run 
  
    '''
    ##### kick start the schedular : TwistedScheduler for network operation 
    self.scheduler = TwistedScheduler()

    self.scheduler.add_jobstore(DjangoJobStore(), "default")
    s= get_project_settings()
    #s['LOG_ENABLED'] =False 
    self.process = CrawlerProcess(s)
    #self.process.settings.set('LOG_ENABLED',False,priority='cmdline')
    self.scheduler.start()
    self.job_complete_status = {}
    self.task_id=""
 
  def job_completed(self,event):
      """ Call back function after scrapping task is completed 
      Args:
          <event (bool)>: exception or normal 
      """
      if event.exception:
        logger.worker.warning('The job crashed :(')
      else:
        logger.worker.warning(self.task_id+'The job finished ')
        # set job complete to true, will display complete in web interface 
        self.job_complete_status[self.task_id] = True

  def delete_old_job_executions(self,max_age=604_800):
      """This job deletes all apscheduler job executions older than `max_age` from the database."""
      DjangoJobExecution.objects.delete_old_job_executions(max_age)

  """ // MARK :  handle_scrapy_start"""
  def handle_scrapy_start(self,scrapy_data):
    """ Main function : 
      1. add crawl job to scheduler. 
      2. add listener to get call back function, when task is done
      
      Args:
          <scrapy_data>: data dictionary that contain task_id
    """
    try : 
      """ Set start and end time  """  
      start=datetime.now()
      end=start+ timedelta(seconds=32)
      #end=start+ timedelta(hours=10)
      
      """  Transfer parameter  """        
      #     use task_id to transfer pk 
      #     use asin_list to transfer list of asin input 
      self.task_id=scrapy_data['task_id']
      asin_list=scrapy_data['asin_list']
      
      """  Add listener   """  
      self.scheduler.add_listener(self.job_completed,  EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
      self.job_complete_status[self.task_id] = False

      """StackSpider    """          
      # add crawl job to scheduler. 
      
      ## StackSpider : run once now 
      #self.scheduler.add_job(self.process.crawl, args=[StackSpider,asin_list])
      
      ## StackSpider:  run periodicity 
      self.scheduler.add_job(self.process.crawl, 'interval', args=[StackSpider], seconds=20,next_run_time=datetime.now(),start_date = start,end_date=end )
      
      """ amazon_download   """  
      """ // MARK :  amazon_download :  run once now"""
      OUTPUT_DIR='C:/Local/Work/Python/PyLib/scrapy/download/result/'
      #  : amazon_download :  run once now       
      #self.scheduler.add_job(self.process.crawl, args=[Download_Test,asin_list,OUTPUT_DIR])            
      
      ## amazon_download : run periodicity 
      #self.scheduler.add_job(self.process.crawl, 'interval', args=[Download_Test], hours=1,
      #next_run_time=datetime.now(),start_date = start,end_date=end )
      
      """ Kick start the craw process    """  
      
      self.process.start(False) 
      #self.process.start(stop_after_crawl=True) 
    
    except ReactorAlreadyRunning:
      logger.worker.info("already run")

  def handle_scrapy_stop(self):
      """Not used , Deprecated : Stop the scheduler 
      // TODO : when and hwoto close down the schedular gracefully 
      """
      logger.worker.warning("Stopping scheduler...")
      self.process.stop()
      self.scheduler.shutdown() 
      logger.worker.warning("Scheduler shut down successfully!")


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