import React from 'react';

const CTA = ({ openModal }) => {
  return (
    <section className="cta">
      <div className="container">
        <div className="cta-content">
          <h2>Ready to Start Your Journey?</h2>
          <p>Join thousands of professionals who have found their perfect career match</p>
          <div className="hero-buttons">
            <button 
              className="btn secondary-btn" 
              onClick={() => openModal('signupModal')}
            >
              <i className="fas fa-user-plus"></i>
              Get Started
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CTA;