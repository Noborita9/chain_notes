from attrs import asdict
import psycopg2
from status import Status
from note import Note
from user import User


class TaskDAO():
    def __init__(self, db_name: str) -> None:
        self.conn = psycopg2.connect(
            database=db_name, user="postgres", password="", host="127.0.0.1", port="5432")
        self.cur = self.conn.cursor()

    def insert_note(self, note: Note):
        try:
            query = "INSERT INTO todos(title, content) VALUES (%s, %s) RETURNING id;"
            self.cur.execute(query, (note.title, note.content))
            last_id = self.cur.fetchall()[0][0]
            self.conn.commit()
            note = Note.from_array([last_id, note.title, note.content])
            return {"status": asdict(Status.from_code("OK")), "value": [note]}
        except Exception as e:
            raise e

    def insert_user(self, user: User):
        try:
            query = "INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s);"
        except Exception as e:
            raise e

    def select_note(self, id: int = 0):
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
    dao = TaskDAO("todos")
    result = dao.select_note()
    if result:
        print(result["value"])

    # conn = psycopg2.connect(database="todos", user="postgres", password="", host="127.0.0.1" ,port="5432")
    # cur = conn.cursor()
    # cur.execute("INSERT INTO todos(title, content) VALUES('first test', 'passed');")
    # conn.commit()
    # cur.execute("SELECT * FROM todos;")
    # row = cur.fetchall()
    # print(row)
    # conn.close()
