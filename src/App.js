import './App.css';

import NoteList from './components/NoteList'
import NoteCreate from './components/NoteCreate'
function App() {
  return (
    <div className="App">
      <NoteCreate />
      <NoteList />
    </div>
  );
}

export default App;
