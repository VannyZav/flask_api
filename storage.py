class EventStorage:
    def __init__(self):
        self.events = []
        self.id_counter = 1

    def add_event(self, event):
        event['id'] = self.id_counter
        self.events.append(event)
        self.id_counter += 1

    def get_events(self):
        return self.events

    def get_event(self, event_id):
        for event in self.events:
            if event['id'] == event_id:
                return event
        return None

    def update_event(self, event_id, new_event):
        for event in self.events:
            if event['id'] == event_id:
                event.update(new_event)
                return True
        return False

    def delete_event(self, event_id):
        for event in self.events:
            if event['id'] == event_id:
                self.events.remove(event)
                return True
        return False



