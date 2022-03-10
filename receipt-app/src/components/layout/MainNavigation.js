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
            <Link to="/">All Meetup</Link>
          </li>
          <li>
            <Link to="/history">
              My Favorites
              {/* <span className={classes.badge}>{favoritesCtx.totalFavorites}</span> */}
            </Link>
          </li>
          <li>
            <Link to="/new-image">New Meetup</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;