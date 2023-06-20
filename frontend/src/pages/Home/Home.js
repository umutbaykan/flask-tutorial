import React from 'react';
import NavButton from '../../components/NavButton/NavButton';

const Home = () => {
  return (
  <>
  <h1>welcome home</h1>
  <NavButton to={'/signup'} text={'Sign Up'}/>
  <br></br>
  <NavButton to={'/login'} text={'Login'}/>
  </>
  )
}

export default Home