import axios from 'axios'

class NoteService {
  async getNotes(userId) {
    let retorno = null
    const res = await axios({
      method: 'GET',
      url: 'http://127.0.0.1:5000/notes',
      headers: {
        Accept: 'application/json',
      },
    })
      .then((res) => {
        console.log(res)
        retorno = res.data.data
      })
      .catch(() => {
        return null
      })
    return retorno
  }
  async createNote(params) {
    let retorno = null
    const { title, content } = params
    const res = await axios({
      method: 'POST',
      url: 'http://127.0.0.1:5000/note/new',
      params: {
        title: title,
        content: content,
      },
      headers: {
        Accept: 'application/json',
      },
    })
      .then((res) => {
        retorno = res.data
      })
      .catch(() => {
        return null
      })
    return retorno
  }
}

const noteService = new NoteService()

export default noteService
