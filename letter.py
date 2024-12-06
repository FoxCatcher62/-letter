
from dotenv import load_dotenv
import smtplib
import os 
email_to = "ares.preobrazhenskiy@yandex.ru"
email_from = "ares.preobrazhenskiy@mail.ru"
topic = "Приглашение!"
text = f"""\
From: {email_from}
To: {email_to}
Subject: "Приглашение!"
Content-Type: text/plain; charset="UTF-8";
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно сdd
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
website = "https://dvmn.org/profession-ref-program/ares.preobrazhenskiy/VWkbS/"
friend_name = "Дима"
my_name = "Артем"

text = text.replace("%website%",website)
text = text.replace("%friend_name%", friend_name)
text = text.replace("%my_name%", my_name)
text = text.encode("UTF-8")

load_dotenv("pas.env")
MY_LOGIN = os.getenv("MY_LOGIN")
MY_PASS = os.getenv("MY_PASS")

server = smtplib.SMTP_SSL("smtp.mail.ru:465")
server.login(MY_LOGIN, MY_PASS)
server.sendmail(email_from, email_to, text)
server.quit()
