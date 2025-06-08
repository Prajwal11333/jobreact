import React from 'react';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>AccessWork</h3>
          <p>Creating inclusive opportunities for everyone. Building bridges between talented professionals and forward-thinking employers.</p>
        </div>
        <div className="footer-section">
          <h3>For Job Seekers</h3>
          <a href="#">Find Jobs</a>
          <a href="#">Resume Tools</a>
          <a href="#">Career Resources</a>
          <a href="#">Community Forum</a>
        </div>
        <div className="footer-section">
          <h3>For Employers</h3>
          <a href="#">Post Jobs</a>
          <a href="#">Diversity Guide</a>
          <a href="#">Accessibility Resources</a>
          <a href="#">Partner With Us</a>
        </div>
        <div className="footer-section">
          <h3>Support</h3>
          <a href="#">Help Center</a>
          <a href="#">Contact Us</a>
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; 2024 AccessWork. All rights reserved. Built with accessibility in mind.</p>
      </div>
    </footer>
  );
};

export default Footer;