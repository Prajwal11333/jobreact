// src/pages/Contact.jsx
import React, { useState } from 'react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
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
    console.log('Contact form submitted:', formData);
    alert('Thank you for your message! We\'ll get back to you within 24 hours.');
    setFormData({ name: '', email: '', subject: '', message: '' });
  };

  return (
    <div className="page-section active">
      <div className="page-content">
        <div className="jobs-header">
          <h1>Contact Us</h1>
          <p>We're here to help you succeed</p>
        </div>

        <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem'}}>
          <div className="search-container">
            <h3 style={{marginBottom: '1rem'}}>Get in Touch</h3>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="contact-name">Name</label>
                <input
                  type="text"
                  id="contact-name"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="contact-email">Email</label>
                <input
                  type="email"
                  id="contact-email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="contact-subject">Subject</label>
                <select
                  id="contact-subject"
                  name="subject"
                  value={formData.subject}
                  onChange={handleInputChange}
                  required
                >
                  <option value="">Select a topic</option>
                  <option value="job-seeker-support">Job Seeker Support</option>
                  <option value="employer-inquiry">Employer Inquiry</option>
                  <option value="technical-issue">Technical Issue</option>
                  <option value="accessibility-concern">Accessibility Concern</option>
                  <option value="partnership">Partnership Opportunity</option>
                  <option value="other">Other</option>
                </select>
              </div>
              <div className="form-group">
                <label htmlFor="contact-message">Message</label>
                <textarea
                  id="contact-message"
                  name="message"
                  rows="5"
                  value={formData.message}
                  onChange={handleInputChange}
                  required
                  style={{
                    width: '100%',
                    padding: '1rem',
                    border: '2px solid #e1e5e9',
                    borderRadius: '12px',
                    fontFamily: 'inherit',
                    resize: 'vertical'
                  }}
                />
              </div>
              <button type="submit" className="btn primary-btn">
                <i className="fas fa-paper-plane"></i>
                Send Message
              </button>
            </form>
          </div>

          <div className="feature-card">
            <h3>Other Ways to Reach Us</h3>
            <div style={{textAlign: 'left'}}>
              <div style={{marginBottom: '1.5rem'}}>
                <i className="fas fa-envelope" style={{color: '#667eea', marginRight: '0.5rem'}}></i>
                <strong>Email:</strong> support@accesswork.com
              </div>
              <div style={{marginBottom: '1.5rem'}}>
                <i className="fas fa-phone" style={{color: '#667eea', marginRight: '0.5rem'}}></i>
                <strong>Phone:</strong> +91-80-1234-5678
              </div>
              <div style={{marginBottom: '1.5rem'}}>
                <i className="fas fa-map-marker-alt" style={{color: '#667eea', marginRight: '0.5rem'}}></i>
                <strong>Address:</strong> 123 Innovation Street, Tech Park, Bangalore, Karnataka 560001
              </div>
              <div style={{marginBottom: '1.5rem'}}>
                <i className="fas fa-clock" style={{color: '#667eea', marginRight: '0.5rem'}}></i>
                <strong>Support Hours:</strong> Monday - Friday, 9 AM - 6 PM IST
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
