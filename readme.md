![Новая задача](./images/ChatBotTelegram.jpg)

# **"Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot."**
___
## **Задача "Ещё больше выбора":**
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
1. С текстом 'Рассчитать норму калорий' и callback_data='calories'
2. С текстом 'Формулы расчёта' и callback_data='formulas'

Создайте новую функцию main_menu(message), которая:
1. Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
2. Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'

Создайте новую функцию get_formulas(call), которая:
1. Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
2. Будет присылать сообщение с формулой [Миффлина-Сан Жеора](https://www.calc.ru/Formula-Mifflinasan-Zheora.html).

Измените функцию set_age и декоратор для неё:
1. Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
2. Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.

По итогу получится следующий алгоритм:
1. Вводится команда /start
2. На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
3. В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
4. По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
5. По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
