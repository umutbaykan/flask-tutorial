import React from 'react';
import {
  Routes,
  Route,
} from "react-router-dom";

import Home from './pages/Home/Home';
import Game from './pages/Game/Game';
import NotFound from './pages/NotFound/NotFound';


const App = () => {
    return (
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/game/:gameId' element={<Game/>}/>
          <Route path='*' element={<NotFound/>}/>
        </Routes>
    );
}

export default App;
