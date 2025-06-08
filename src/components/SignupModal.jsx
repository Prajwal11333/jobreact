import React, { useState } from 'react';

const SignupModal = ({ closeModal }) => {
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    password: '',
    userType: 'jobseeker'
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
    console.log('Signup attempt:', formData);
    alert('Signup functionality will be implemented with backend integration');
    closeModal();
  };

  return (
    <div className="modal active">
      <div className="modal-content">
        <button className="modal-close" onClick={closeModal}>
          <i className="fas fa-times"></i>
        </button>
        <h2>Join AccessWork</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="signup-name">Full Name</label>
            <input
              type="text"
              id="signup-name"
              name="fullName"
              value={formData.fullName}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="signup-email">Email</label>
            <input
              type="email"
              id="signup-email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="signup-password">Password</label>
            <input
              type="password"
              id="signup-password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="user-type">I am a</label>
            <select
              id="user-type"
              name="userType"
              value={formData.userType}
              onChange={handleInputChange}
            >
              <option value="jobseeker">Job Seeker</option>
              <option value="employer">Employer</option>
            </select>
          </div>
          <button type="submit" className="btn primary-btn" style={{width: '100%', marginTop: '1rem'}}>
            <i className="fas fa-user-plus"></i>
            Create Account
          </button>
        </form>
        <p style={{textAlign: 'center', marginTop: '1rem'}}>
          Already have an account? <a href="#" style={{color: '#667eea'}}>Login here</a>
        </p>
      </div>
    </div>
  );
};

export default SignupModal;