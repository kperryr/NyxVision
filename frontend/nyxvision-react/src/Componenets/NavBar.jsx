import { Link } from "react-router-dom";
import React from 'react';
import './NavBar.css';

 export default function NavBar(){
      return (
        <nav className="navbar">
            <div className="logo">NyxVision</div>
            <div className="links">
                <button>Logout</button>
            </div>
        </nav>
  );
}