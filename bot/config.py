import os


class Config:

    API_ID = "18991521"
    API_HASH = "0c1086e0013e5f6633ad3b4bae13238b"
    BOT_TOKEN = "6856735851:AAGcLvCpc4XY187gr5DtGp4B58rBy_ClBFs"
    SESSION_NAME = "SS_Gen"
    LOG_CHANNEL = -1002146220863
    DATABASE_URL = "mongodb+srv://amelieclubb:amelieclubb0@amelieclubb.xpzmwav.mongodb.net/?retryWrites=true&w=majority&appName=amelieclubb"
    AUTH_USERS = "1633416742"
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 15))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 2))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
