"""
when execution happens we need to log all the information,execution,even the exception raised to some text file for this
purpose we need to logger.
"""
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # file name format
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)    # path
os.makedirs(logs_path,exist_ok=True)                   #if there is existing then also create


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

