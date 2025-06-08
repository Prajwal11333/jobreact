import React, { useState } from 'react';

const Navbar = ({ currentPage, showPage, openModal }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  const handleNavClick = (page) => {
    showPage(page);
    setMobileMenuOpen(false);
    window.scrollTo(0, 0);
  };

  return (
    <nav className="navbar" id="navbar">
      <div className="nav-container">
        <a 
          href="#" 
          className="logo" 
          onClick={(e) => { e.preventDefault(); handleNavClick('main'); }}
        >
          <i className="fas fa-universal-access"></i>
          AccessWork
        </a>
        <ul className={`nav-menu ${mobileMenuOpen ? 'mobile-open' : ''}`}>
          <li>
            <a 
              href="#" 
              onClick={(e) => { e.preventDefault(); handleNavClick('jobs'); }}
              className={currentPage === 'jobs' ? 'active' : ''}
            >
              Find Jobs
            </a>
          </li>
          <li>
            <a 
              href="#" 
              onClick={(e) => { e.preventDefault(); handleNavClick('post-job'); }}
              className={currentPage === 'post-job' ? 'active' : ''}
            >
              Post Job
            </a>
          </li>
          <li>
            <a 
              href="#" 
              onClick={(e) => { e.preventDefault(); handleNavClick('resources'); }}
              className={currentPage === 'resources' ? 'active' : ''}
            >
              Resources
            </a>
          </li>
          <li>
            <a 
              href="#" 
              onClick={(e) => { e.preventDefault(); handleNavClick('about'); }}
              className={currentPage === 'about' ? 'active' : ''}
            >
              About
            </a>
          </li>
          <li>
            <a 
              href="#" 
              onClick={(e) => { e.preventDefault(); handleNavClick('contact'); }}
              className={currentPage === 'contact' ? 'active' : ''}
            >
              Contact
            </a>
          </li>
        </ul>
        <div className="nav-buttons">
          <a 
            href="#" 
            className="nav-btn login-btn" 
            onClick={(e) => { e.preventDefault(); openModal('loginModal'); }}
          >
            Login
          </a>
          <a 
            href="#" 
            className="nav-btn signup-btn" 
            onClick={(e) => { e.preventDefault(); openModal('signupModal'); }}
          >
            Sign Up
          </a>
        </div>
        <button className="mobile-menu-btn" onClick={toggleMobileMenu}>
          <i className="fas fa-bars"></i>
        </button>
      </div>
    </nav>
  );
};

export default Navbar;