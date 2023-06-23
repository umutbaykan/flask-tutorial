import { NavLink } from "react-router-dom"
import propTypes from 'prop-types';


const NavButton = ({to, text}) => {
  return (
    <NavLink to={to} className="navbutton" key={to}>{text}</NavLink>
  )
}

NavButton.propTypes = { to: propTypes.string, text: propTypes.string}


export default NavButton;