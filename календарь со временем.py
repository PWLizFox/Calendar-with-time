import calendar
import datetime
import time
# Делаем красивое название календаря :)
print("-----------------------------------------------------\n"
      "                     Календарь\n"
      "-----------------------------------------------------")
# Узнаём какая текущая дата и время
now = datetime.datetime.now()
# Рисуем колендарь с текущим месяцем и годом
print(calendar.month(now.year, now.month))
print("-----------------------------------------------------")

while True:
      # Получаем текущее время
      current_time = datetime.datetime.now().strftime("%H:%M:%S")
      # Очищаем строку (используем \r для возврата курсора)
      print("\rТекущее время -> ", current_time, end='')
      # Ждем 1 секунду
      time.sleep(1)
