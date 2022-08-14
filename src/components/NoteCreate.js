import { React } from 'react'

import noteService, { NoteService } from '../modules/NoteService'

const NoteCreate = () => {

  const createNote = () => {
    noteService.createNote({
      title: document.getElementById('title').value,
      content: document.getElementById('content').value,
    })
  }

  return (
    <div>
      <input id='title' placeholder='title' />
      <input id='content' placeholder='content' />
      <button onClick={createNote} >Create!</button>
    </div>
  )
}

export default NoteCreate
