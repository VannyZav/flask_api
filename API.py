from flask import Flask, jsonify, request
from storage_inteface import EventStorageInterface

app = Flask(__name__)


storage_interface = EventStorageInterface()

max_title_length = 30
max_text_length = 200
max_events_per_day = 1


def validate_event_data(date, title, text):
    if len(title) > max_title_length or len(text) > max_text_length:
        return False, 'Превышена максимальная длина заголовка или текста'

    daily_events = [event for event in storage_interface.get_events() if event['date'] == date]
    if len(daily_events) >= max_events_per_day:
        return False, 'Можно добавить только одно событие в день'

    return True, ''


@app.route('/api/v1/calendar/events', methods=['GET'])
def get_events():
    events = storage_interface.get_events()
    return jsonify(events)


@app.route('/api/v1/calendar/events', methods=['POST'])
def add_event():
    data = request.get_json()
    date = data['date']
    title = data['title']
    text = data['text']

    valid, error_message = validate_event_data(date, title, text)

    if not valid:
        return jsonify({'message': error_message}), 400

    event = storage_interface.add_event(date, title, text)
    return jsonify(event), 201


@app.route('/api/v1/calendar/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = storage_interface.get_event(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404
    return jsonify(event)


@app.route('/api/v1/calendar/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    date = data.get('date')
    title = data.get('title')
    text = data.get('text')

    valid, error_message = validate_event_data(date, title, text)

    if not valid:
        return jsonify({'message': error_message}), 400

    if not storage_interface.update_event(event_id, date=date, title=title, text=text):
        return jsonify({'message': 'Event not found'}), 404
    return jsonify({'message': 'Event updated'})


@app.route('/api/v1/calendar/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    if not storage_interface.delete_event(event_id):
        return jsonify({'message': 'Event not found'}), 404
    return jsonify({'message': 'Event deleted'})


if __name__ == '__main__':
    app.run()
