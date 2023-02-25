import db_editor
from Notelist import Notelist
from UI import UI
from db_editor import *
from pathlib import Path

db_path = "db.csv"
notelist: Notelist = Notelist()

if Path(db_path).exists():
     db_editor.load(db_path, notelist)

ui: UI = UI(notelist)
ui.run()
db_editor.save(db_path, notelist)


