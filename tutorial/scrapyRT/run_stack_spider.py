import sys
import time
import schedule
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from apscheduler.schedulers.twisted import TwistedScheduler
from apscheduler.schedulers.background  import BackgroundScheduler
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from runpy import run_path
from datetime import datetime,timedelta
sys.path.append(r'c:/Local/Work/Web/web/tutorial/scrapyRT/stack/stack/spiders')
from stack_spider import StackSpider

settings = run_path(
    "C:/Local/Work/Web/web/tutorial/scrapyRT/stack/stack/spiders/stack_spider.py")

process = CrawlerProcess(get_project_settings())
#scheduler = TwistedScheduler()

scheduler = BackgroundScheduler()
start=datetime.now()
end=start+ timedelta(seconds=62)
scheduler.add_job(process.crawl, 'interval', args=[StackSpider], seconds=20,next_run_time=datetime.now(),start_date = start,end_date=end )
scheduler.start()
process.start(False)
