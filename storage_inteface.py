from storage import EventStorage


class EventStorageInterface:
    def __init__(self):
        self.storage = EventStorage()

    def add_event(self, date, title, text):
        event = {'date': date, 'title': title, 'text': text}
        self.storage.add_event(event)
        return event

    def get_events(self):
        return self.storage.get_events()

    def get_event(self, event_id):
        return self.storage.get_event(event_id)

    def update_event(self, event_id, date=None, title=None, text=None):
        updated_event = {}
        if date:
            updated_event['date'] = date
        if title:
            updated_event['title'] = title
        if text:
            updated_event['text'] = text
        return self.storage.update_event(event_id, updated_event)

    def delete_event(self, event_id):
        return self.storage.delete_event(event_id)
