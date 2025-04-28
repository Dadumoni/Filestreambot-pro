# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20845715'))
    API_HASH = str(getenv('API_HASH', '72b3a12322c4edeb6c35fe91376aae84'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '7842987186:AAEdA2sWb7p_1NbLSMLeoH8NNTIxxTb53CY'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002523820446'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "7340459339").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', ''))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    
    # Fix FQDN and URL generation
    if ON_HEROKU:
        FQDN = str(getenv('FQDN', APP_NAME + '.herokuapp.com'))
    else:
        FQDN = str(getenv('FQDN', f'{BIND_ADRESS}:{PORT}'))
    
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://dadumoni05:WM6DGoujTAmrAIO4@cluster0.3wcnpfx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))  # Changed to None
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
