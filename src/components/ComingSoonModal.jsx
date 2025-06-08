import React from 'react';

const ComingSoonModal = ({ closeModal }) => {
  return (
    <div className="modal active">
      <div className="modal-content">
        <button className="modal-close" onClick={closeModal}>
          <i className="fas fa-times"></i>
        </button>
        <div style={{textAlign: 'center'}}>
          <i className="fas fa-rocket" style={{fontSize: '3rem', color: '#667eea', marginBottom: '1rem'}}></i>
          <h2>Coming Soon!</h2>
          <p>This feature is currently under development. We're working hard to bring you the best experience possible.</p>
          <p>Stay tuned for updates!</p>
          <button 
            className="btn primary-btn" 
            onClick={closeModal}
            style={{marginTop: '1rem'}}
          >
            Got it!
          </button>
        </div>
      </div>
    </div>
  );
};

export default ComingSoonModal;