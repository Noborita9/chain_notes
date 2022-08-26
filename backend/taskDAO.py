from attrs import asdict
import psycopg2
from status import Status
from note import Note
from user import User
import uuid


class TaskDAO():
    def __init__(self, db_name: str) -> None:
        self.conn = psycopg2.connect(
            database=db_name, user="postgres", password="", host="127.0.0.1", port="5432")
        self.cur = self.conn.cursor()

    def insert_note(self, note: Note, user: User):
        try:
            note_query = "INSERT INTO notes(title, content) VALUES (%s, %s) RETURNING id;"
            self.cur.execute(
                note_query, (note.title, note.content))
            last_id = self.cur.fetchall()[0][0]
            usernote_query = "INSTER INTO usernote (id_note, id_user) VALUES (%s, %s);"
            self.cur.execute(usernote_query, (note.id_note, ))
            self.conn.commit()
            note = Note.from_array([last_id, note.title, note.content])
            return {"status": asdict(Status.from_code("OK")), "value": [note]}

        except Exception as e:
            raise e

    def insert_user(self, user: User):
        try:
            # TODO: Implement Checker before
            query = "INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s);"
            self.cur.execute(
                query, (user.id_user, user.name, user.email, user.password))
            self.conn.commit()
            return {"status": asdict(Status.from_code("OK")), "value": user}

        except psycopg2.Error as e:
            raise e

    def select_note(self, id_user: uuid.UUID, id_note: int = 0):
        try:
            if id:
                query = f"SELECT * FROM todos WHERE id={id}"
            else:
                query = "SELECT * FROM todos"

            self.cur.execute(query)
            row = self.cur.fetchall()
            return {"status": asdict(Status.from_code("OK")), "value": row}
        except Exception as e:
            raise e

    def delete_note(self, id: int):
        try:
            query = f"DELETE FROM todos WHERE id={id}"
            self.cur.execute(query)
            self.conn.commit()
            return {"status": asdict(Status.from_code("OK")), "value": []}
        except Exception as e:
            raise e


if __name__ == "__main__":
    dao = TaskDAO("chained_notes")
    # result = dao.select_note()
    # if result:
    #     print(result["value"])

    # conn = psycopg2.connect(database="todos", user="postgres", password="", host="127.0.0.1" ,port="5432")
    # cur = conn.cursor()
    # cur.execute("INSERT INTO todos(title, content) VALUES('first test', 'passed');")
    # conn.commit()
    # cur.execute("SELECT * FROM todos;")
    # row = cur.fetchall()
    # print(row)
    # conn.close()
