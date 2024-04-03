# Отчет по второму ДЗ по БД SberTech 2024

## Установил Redis-Insight

После установки начал работать с данными, использовал датасет наполненный информацией по погоде в рпазличное время суток. JSON-файл весил около 60мб, поэтому тут не поместился. Далее, используя программу, которая прикреплена тут же, заполнил БД данными из JSON-а. Результат и время работы - прилагаю:

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/1.png)

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/2.png)

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/3.png)

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/4.png)

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/5.png)

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/6.png)

## Кластеризация

Дальше - интереснее. Начался процесс создания редис-кластера. Для начала я хотел создать 3 ноды, однако столкнулся с тем, что сам функционал redis-cli --cluster не позволяет создать кластер на меньше чем 6 нодах. Создав их и прописав каждой свой конфиг, я запустил redis-server на каждой, а после произвел процесс кластеризации, вследствии чего у меня получилось поставить кластер. Далее я проверил работоспособоность всей этой штуки при помощи ping-а, на что мне ответили PONG. Потом я отключил одну из нод и проверил, что все продолжает работать, так и оказалось.

![alt text](https://github.com/AndreyTkachik/db_sbertech_2024/blob/hw2/redis_hw/pics/7.png)
