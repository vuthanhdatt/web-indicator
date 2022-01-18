import os
from dotenv import load_dotenv
from datetime import date
import telegram

from indicator import text


if __name__ == '__main__':
    
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    today = date.today()
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id='-1001453202586',text=text,parse_mode='Markdown')
    updates = bot.get_updates()



