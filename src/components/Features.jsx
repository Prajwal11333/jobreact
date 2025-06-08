import React from 'react';

const Features = () => {
  const features = [
    {
      icon: 'fas fa-universal-access',
      title: 'Accessibility First',
      description: 'Every job posting includes detailed accessibility information and accommodation options to help you make informed decisions.'
    },
    {
      icon: 'fas fa-handshake',
      title: 'Inclusive Employers',
      description: 'We partner with companies committed to diversity and inclusion, ensuring genuine opportunities for all candidates.'
    },
    {
      icon: 'fas fa-users',
      title: 'Supportive Community',
      description: 'Connect with peers, mentors, and professionals who understand your journey and can provide valuable guidance.'
    },
    {
      icon: 'fas fa-tools',
      title: 'Career Tools',
      description: 'Access specialized resume builders, interview prep, and career guidance tailored for professionals with disabilities.'
    },
    {
      icon: 'fas fa-shield-alt',
      title: 'Privacy Protected',
      description: 'Your personal information and accommodation needs are kept confidential and shared only with your consent.'
    },
    {
      icon: 'fas fa-rocket',
      title: 'Career Growth',
      description: 'Find not just jobs, but career paths with companies that invest in your professional development and advancement.'
    }
  ];

  return (
    <section className="features">
      <div className="container">
        <h2>Why Choose AccessWork?</h2>
        <div className="feature-grid">
          {features.map((feature, index) => (
            <div key={index} className="feature-card">
              <i className={`${feature.icon} feature-icon`}></i>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;