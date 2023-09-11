# flask_api
Техническое задание: Сервис для работы с Календарем.


Требования:


— API интерфейс CRUD — Добавление / Список / Чтение / Обновление / Удаление<br/>
— модель данных "Событие": ID, Дата, Заголовок, Текст<br/>
— локальное хранилище данных<br/>
— максимальная длина заголовка — 30 символов<br/>
— максимальная длина поля Текст — 200 символов<br/>
— нельзя добавить больше одного события в день<br/>
— API интерфейс: /api/v1/calendar/… (по аналогии с заметкой)<br/>
— формат данных: "ГГГГ-ММ-ДД|заголовок|текст" (по аналогии с заметкой)<br/>


# инструкция к API:
в коммандной строке перемещаемся в папки с проектом с помощью команды cd, например: "cd flask_api"


create event:<br/>
(в примере тестовые данные в теле запроса)<br/>
curl http://127.0.0.1:5000/api/v1/calendar/events -Method POST -ContentType 'application/json' -Body '{"date": "1976.09.21", "title": "Test curl", "text": "Hello from Curl"}'


read list of events:
curl http://127.0.0.1:5000/api/v1/calendar/events -Method GET


read event:
curl http://127.0.0.1:5000/api/v1/calendar/events/<int:event_id> -Method GET


update event:
curl http://127.0.0.1:5000/api/v1/calendar/events/<int:event_id> -Method PUT -ContentType 'application/json' -Body '{"date": "2023.09.22", "title": "test curl", "text": "Hello from updated message"}'


delete event:
curl http://127.0.0.1:5000/api/v1/calendar/events/<int:event_id> -Method DELETE

