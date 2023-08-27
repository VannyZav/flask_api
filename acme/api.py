from flask import Flask, request
import model
import logic


app = Flask(__name__)

_event_logic = logic.EventLogic()


class ApiException(Exception):
    pass


def from_raw(raw_event: str) -> model.Event:
    parts = raw_event.split('|')
    if len(parts) == 3:
        event = model.Event
        event.id = None
        event.date = parts[0]
        event.header = parts[1]
        event.text = parts[2]
        return event
    elif len(parts) == 4:
        event = model.Event
        event.id = parts[0]
        event.date = parts[1]
        event.header = parts[2]
        event.text = parts[3]
        return event
    else:
        raise ApiException(f'invalid RAW event data {raw_event}')


def to_raw(event: model.Event) -> str:
    if event.id is None:
        return f"{event.date}|{event.header}|{event.text}"
    else:
        return f"{event.id}|{event.date}|{event.header}|{event.text}"


API_root = "/api/v1/"
Calendar_api_root = API_root + "/calendar"


@app.route(Calendar_api_root + "/", methods=["POST"])
def create():
    try:
        data = request.get_data().decode('utf-8')
        event = from_raw(data)
        _id = _event_logic.create(event)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with {ex}", 404


@app.route(Calendar_api_root + "/", methods=["GET"])
def list():
    try:
        events = _event_logic.list()
        raw_events = ""
        for event in events:
            raw_events += to_raw(event) + '\n'
        return raw_events, 200
    except Exception as ex:
        return f"failed to LIST with {ex}", 404


@app.route(Calendar_api_root + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        event = _event_logic.read(_id)
        raw_event = to_raw(event)
        return raw_event, 200
    except Exception as ex:
        return f"failed to READ with {ex}", 404


@app.route(Calendar_api_root + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = request.get_data().decode('utf-8')
        event = from_raw(data)
        _event_logic.update(_id, event)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with {ex}", 404


@app.route(Calendar_api_root + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with {ex}", 404
