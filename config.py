import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "29063710"))
    API_HASH = os.environ.get("API_HASH", "86a28f873f227e3289af91fa88931511")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6302772060:AAGtWrE5ZAP426-hbCB21YDdefC3BHy_4uk")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
