from bs4 import BeautifulSoup
import requests
import logging
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:  # Перевіряємо, чи успішний HTTP-запит
    soup = BeautifulSoup(response.text, features="html.parser")
    # Створюємо об'єкт BeautifulSoup для обробки HTML-вмісту
       # Знаходимо всі посилання на сторінку ринків Bitcoin
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
    res = soup_list[0].find("span")  # Знаходимо перше посилання та отримуємо елемент span всередині нього
class Text:
    def __init__ (self):
        self.print = res
    def printer(self):
        print(self.print)
text = Text()
text.printer()
logging.basicConfig(level=logging.DEBUG,filename="final-project.log",filemode="w",format="we have next logging message:%(asctime)s:%(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
