import { Link } from "react-router-dom";
// import { useContext } from 'react';
import classes from './MainNavigation.module.css';
import React from 'react';

// import FavoritesContext from '../../store/favorites-context';

function MainNavigation() {
  
  // const favoritesCtx = useContext(FavoritesContext);
  return(
    <header className={classes.header}>
      <div className={classes.logo}>Receipt App</div>
      <nav>
        <ul>
          <li>
            <Link to="/">How To Use</Link>
          </li>
          <li>
            <Link to="/new-image">Upload</Link>
          </li>
          <li>
            <Link to="/history">
              History
              {/* <span className={classes.badge}>{favoritesCtx.totalFavorites}</span> */}
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;