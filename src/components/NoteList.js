import { React, useEffect, useState } from 'react'

import './NoteList.css'
import Note from './Note'
import noteService from '../modules/NoteService'

const NoteList = () => {
  const [notes, setNotes] = useState([])
  useEffect(() => {
    noteService.getNotes().then((res) => {
      setNotes(res)
    })
  }, [])
  return (
    <ul className='note_list'>
      {notes.map((note) => {
        return (
          <Note
            key={note.id}
            id={note.id}
            title={note.title}
            content={note.content}
          />
        )
      })}
    </ul>
  )
}

export default NoteList
