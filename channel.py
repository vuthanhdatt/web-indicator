import os
from datetime import date

import telegram
from dotenv import load_dotenv

from indicator import texts

if __name__ == '__main__':
    
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    today = date.today()
    bot = telegram.Bot(token=TOKEN)
    for text in texts:
        bot.send_message(chat_id='-1001453202586',text=text,parse_mode='Markdown',disable_web_page_preview=True)
    updates = bot.get_updates()



