import React from 'react';

const About = () => {
  return (
    <div className="page-section active">
      <div className="page-content">
        <div className="jobs-header">
          <h1>About AccessWork</h1>
          <p>Bridging the gap between talent and opportunity</p>
        </div>

        <div className="feature-grid">
          <div className="feature-card">
            <i className="fas fa-heart feature-icon"></i>
            <h3>Our Mission</h3>
            <p>To create a world where every professional, regardless of ability, has equal access to meaningful career opportunities. We believe that diversity drives innovation and that inclusion makes us all stronger.</p>
          </div>
          
          <div className="feature-card">
            <i className="fas fa-eye feature-icon"></i>
            <h3>Our Vision</h3>
            <p>A future where accessibility is the norm, not the exception. Where employers actively seek diverse talent and job seekers can find opportunities that truly fit their needs and aspirations.</p>
          </div>
          
          <div className="feature-card">
            <i className="fas fa-users feature-icon"></i>
            <h3>Our Values</h3>
            <p>Inclusion, Accessibility, Dignity, Empowerment, and Innovation. These values guide every decision we make and every feature we build on our platform.</p>
          </div>
        </div>

        <div className="search-container" style={{marginTop: '3rem'}}>
          <h2 style={{textAlign: 'center', marginBottom: '2rem'}}>Our Story</h2>
          <p style={{lineHeight: '1.8', fontSize: '1.1rem', color: '#666'}}>
            AccessWork was founded in 2023 with a simple yet powerful idea: that everyone deserves the chance to build a meaningful career. Our founders, a diverse team of professionals with and without disabilities, recognized the barriers that existed in traditional job searching and decided to create something better.
          </p>
          <p style={{lineHeight: '1.8', fontSize: '1.1rem', color: '#666', marginTop: '1rem'}}>
            Today, we're proud to be India's leading inclusive job platform, connecting thousands of talented professionals with forward-thinking employers who value diversity and inclusion. Our platform goes beyond just job listings – we provide the tools, resources, and community support needed for career success.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;