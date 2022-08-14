from flask import Flask, request
from flask_cors import CORS
from taskDAO import TaskDAO
from note import Note, asdict

if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)

    dao = TaskDAO("todos")

    @app.get('/notes')
    def get_notes():
        result = dao.select_note()
        status = result['status']
        if status['number'] == 200:
            response = result['value']
            result = [asdict(Note.from_array(note)) for note in response]
            return {'status': status, 'data': result}
        else:
            result = "Not found"
        return result

    @app.route('/note/new', methods=['GET', 'POST'])
    def create_note():
        args = dict(request.args)
        result = dao.insert_note(Note.from_array(
            [value for _, value in args.items()]))
        status = result['status']
        if status['number'] == 200:
            response = result['value']
            result = [asdict(note) for note in response]
            return {'status': status, 'data': result}
        else:
            return "Not Found"

    @app.delete('/note/delete/<note_id>')
    def delete_note(note_id):
        result = dao.delete_note(note_id)
        return result

    @app.get('/note/<note_id>')
    def get_note(note_id):
        result = dao.select_note(note_id)
        status = result['status']
        if status['number'] == 200:
            response = result['value']
            result = [asdict(Note.from_array(note)) for note in response]
            return {'status': status, 'data': result}
        else:
            result = "Not found"
        return result

    app.run(debug=True)
