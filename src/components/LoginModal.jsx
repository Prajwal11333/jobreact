import React, { useState } from 'react';

const LoginModal = ({ closeModal }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Login attempt:', formData);
    alert('Login functionality will be implemented with backend integration');
    closeModal();
  };

  return (
    <div className="modal active">
      <div className="modal-content">
        <button className="modal-close" onClick={closeModal}>
          <i className="fas fa-times"></i>
        </button>
        <h2>Welcome Back</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="login-email">Email</label>
            <input
              type="email"
              id="login-email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="login-password">Password</label>
            <input
              type="password"
              id="login-password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              required
            />
          </div>
          <button type="submit" className="btn primary-btn" style={{width: '100%', marginTop: '1rem'}}>
            <i className="fas fa-sign-in-alt"></i>
            Login
          </button>
        </form>
        <p style={{textAlign: 'center', marginTop: '1rem'}}>
          Don't have an account? <a href="#" style={{color: '#667eea'}}>Sign up here</a>
        </p>
      </div>
    </div>
  );
};

export default LoginModal;