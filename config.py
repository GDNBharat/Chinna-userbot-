import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28362850")) #optional
API_HASH = getenv("API_HASH", "34f9cb93364db16fc45d003e4c81d97a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7588442909").split()))
OWNER_ID = int(getenv("OWNER_ID", "7588442909"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://vishalpandeynkp:Bal6Y6FZeQeoAoqV@cluster0.dzgwt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ALIVE_PIC = getenv("ALIVE_PIC", "")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP","-1002141779241")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GDNBharat/Chinna-userbot-")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGwyGIAEvzTBeHrzv9vZtRFnNZM2q0tEG-IVScMlkXd1SuXMAqAfsxOU2-DLuJfBMHfiNTX36oNhH_-IBfOk9irMEaaYYDy33MwoHM7K4d5G6OKllEpUH1Ih1LlFv6jVuMkSA9iQuD0XBPHdcpp7P5PMpWVtzmAZAz4B0bzcngvPmQzXpJmICG-O5gN-y0i_m-kiyhE2Fw88Tw3Eg8isBInnuFfFbl1dty-x_xhunDpPM9UY-V8-XEoCsAH1KZXYF495vmComYtJh0Vlu8TUIglaL-hB2AkvV0uJyIJs70X5FVI9-A5c4VOXYnSS5birPvE5-v_6mcWntsefMKBkB4q_SpmmwAAAAHETnMdAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
