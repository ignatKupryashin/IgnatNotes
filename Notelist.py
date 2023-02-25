import datetime

from Note import Note

class Notelist:
    """Класс записной книжки. Хранит состояние записной книжки,
    Достает заметки и пользуется интерфейсом каждой заметки"""

    max_id = 0
    notes: dict[int, Note] = dict()

    def __init__(self):
        print("Записная книжка создана")

    def refresh_max_id(self, new_max_id):
        """Обновляет max_id в записной книжке"""
        self.max_id = new_max_id

    def import_note(self, note_id, heading, body, date_created, date_edited):
        print(note_id)
        if note_id > self.max_id:
            self.max_id = note_id
        self.notes[note_id] = Note(note_id, heading, body, date_created, date_edited)

    def add_note(self, heading, body):
        self.max_id += 1
        print(self.max_id)
        self.notes[self.max_id] = Note(self.max_id, heading, body, datetime.datetime.now(), datetime.datetime.now())

    def change_note_body(self, note_id, body):
        self.notes[note_id].change_body(body)

    def add_note_body(self, note_id, body):
        self.notes[note_id].append(body)

    def change_note_heading(self, note_id, new_heading):
        self.notes[note_id].change_heading(new_heading)

    def delete_note(self, note_id):
        if note_id in self.notes.keys():
            del self.notes[note_id]

    def read_note(self, note_id) -> str:
        current_note = self.notes[note_id]
        note_string = "id: " + str(current_note.note_id) \
                      + "\nДата создания: " + current_note.date_created \
                      + "\nДата последнего изменения: " + current_note.date_created + "\n\n + " \
                      + current_note.heading + "\n\n" + current_note.body
        return current_note.heading + "\n\n" + current_note.body

    def filter_notes (self, note_id, heading, body) -> dict[int, Note]:
        answer = {}
        for Note in self.notes.values():
            if note_id == Note.note_id or Note.heading.find(heading) or Note.body.find(body):
                answer[Note.note_id] = Note
        return answer

    def get_note(self, note_id) -> Note:
        return self.notes[note_id]




