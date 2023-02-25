from Notelist import Notelist


class UI:

    def __init__(self, my_notelist) -> None:
        self.flag = True
        self.notelist: Notelist = my_notelist

    def input_number(self):
        flag = True
        while flag:
            answer = input("Введите номер заметки: ")
            if answer.isdigit():
                flag = False
                return int(answer)

    def print_main_menu(self):
        print("1. Добавить заметку\n"
              "2. Изменить заметку\n"
              "3. Удалить заметку\n"
              "4. Прочитать заметку по id\n"
              "5. Прочитать все заметки\n"
              # "6. Поиск заметки"
              "0. Выход\n")

    def add_note(self):
        heading = input("Введите заголовок заметки: ")
        body = input("Введите ткст заметки: ")
        self.notelist.add_note(heading, body)
        print()

    def edit_note(self):
        note_id = self.input_number()
        print(self.notelist.read_note(note_id))
        if note_id in self.notelist.notes.keys():
            print("1 - Изменить заголовок\n"
                  "2 - Изменить тело заметки\n"
                  "3 - Дополнить тело заметки\n")
            action = input("Введите команду: ")
            match action:
                case "1":
                    heading = input("Введите новый заголовок: ")
                    self.notelist.change_note_heading(note_id, heading)
                case "2":
                    body = input("Введите новый текст заметки: ")
                    self.notelist.change_note_body(note_id, body)
                case "3":
                    adding = input("Введите текст, которым вы хотите дополнить заметку: ")
                    self.notelist.add_note_body(note_id, adding)

    def delete_note(self):
        note_id = self.input_number()
        self.notelist.delete_note(note_id)

    def read_note(self):
        note_id = self.input_number()
        print("---------------------\n" + self.notelist.read_note(note_id) + "\n---------------------")

    def read_all_notes(self):
        for note_id in self.notelist.notes.keys():
            print("---------------------\n" + self.notelist.read_note(note_id) + "\n---------------------")

    def run(self):
        print("Добро пожаловать в Самые лучшие заметки!\n")
        while self.flag:
            self.print_main_menu()
            choise = input("Введите номер команды: ")
            match choise:
                case "1":
                    self.add_note()
                case "2":
                    self.edit_note()
                case "3":
                    self.delete_note()
                case "4":
                    self.read_note()
                case "5":
                    self.read_all_notes()
                # case "6": pass
                case "0":
                    self.flag = False
