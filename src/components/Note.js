import { React } from 'react'

import './Note.css'
const Note = (props) => {
  return (
    <li className='note' id={props.id}>
      <h1>{props.title}</h1>
      <p>{props.content}</p>
    </li>
  )
}

export default Note
