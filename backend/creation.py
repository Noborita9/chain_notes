import psycopg2 as sql

if __name__ == "__main__":
    conn = sql.connect(dbname="chained_notes", user="postgres",
                       password="", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    try:
        cur.execute(
            "CREATE TABLE notes (id_note uuid PRIMARY KEY, title VARCHAR(100), content VARCHAR(500));")

        cur.execute(
            "CREATE TABLE users (id_user uuid PRIMARY KEY, name VARCHAR(60), email VARCHAR(120), password VARCHAR(20));")

        cur.execute(
            "CREATE TABLE usernote (id_user uuid NOT NULL, id_note uuid NOT NULL, FOREIGN KEY (id_user) REFERENCES users(id_user), FOREIGN KEY (id_note) REFERENCES notes(id_note));")

        cur.execute("""CREATE TABLE chained(id_first uuid NOT NULL,
                    id_second uuid NOT NULL,
                    FOREIGN KEY(id_first) REFERENCES notes(id_note),
                    FOREIGN KEY(id_second) REFERENCES notes(id_note));
                    """)

        conn.commit()
    except Exception as e:
        raise e
