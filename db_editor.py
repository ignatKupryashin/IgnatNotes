import csv
from datetime import datetime

from Note import Note
from Notelist import Notelist


def encode_note(my_note: Note):
    return {"note_id": my_note.note_id, "heading": my_note.heading, "body": my_note.body,
            "date_created": my_note.date_created, "date_edited": my_note.date_edited}


def save(path, data: Notelist):
    with open(path, "w", newline='') as file:
        fieldnames = ["note_id", "heading", "body", "date_created", "date_edited"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for key in data.notes.keys():
            writer.writerow(encode_note(data.get_note(key)))


def load(path, data: Notelist) -> None:
    with open(path, "r", newline="") as file:
        fieldnames = ["note_id", "heading", "body", "date_created", "date_edited"]
        reader = csv.DictReader(file)
        for row in reader:
            datetime.strptime(row['date_created'], '%Y-%m-%d %H:%M:%S.%f')
            data.import_note(int(row['note_id']),
                             row['heading'],
                             row['body'],
                             datetime.strptime(row['date_created'], '%Y-%m-%d %H:%M:%S.%f'),
                             datetime.strptime(row['date_edited'], '%Y-%m-%d %H:%M:%S.%f'))



