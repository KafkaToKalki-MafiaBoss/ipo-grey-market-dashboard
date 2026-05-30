from zoneinfo import ZoneInfo
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pipeline
import logging

ist=ZoneInfo("Asia/Kolkata")

scheduler=BlockingScheduler(timezone=ist)

# trigger=CronTrigger.from_crontab("0 10-17/2,19 * * *")

# scheduler.add_job(pipeline.run_pipeline,trigger=trigger)
scheduler.add_job(pipeline.run_pipeline)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

scheduler.start()