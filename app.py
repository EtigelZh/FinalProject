# импорт объекта для создания приложения

from flask import Flask
# создание экземпляра объекта приложения
app = Flask(__name__)
# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"A4Q8z\n\xec]/'
# здесь необходимо указать все контроллеры страниц
# закомментировать еще не реализованные
import controllers.index
import controllers.new_product
import controllers.search