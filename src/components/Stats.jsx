import React from 'react';

const Stats = () => {
  const stats = [
    {
      number: '10,000+',
      label: 'Job Seekers Helped'
    },
    {
      number: '500+',
      label: 'Partner Companies'
    },
    {
      number: '2,500+',
      label: 'Successful Placements'
    },
    {
      number: '95%',
      label: 'Satisfaction Rate'
    }
  ];

  return (
    <section className="stats">
      <div className="container">
        <div className="stats-grid">
          {stats.map((stat, index) => (
            <div key={index} className="stat-item">
              <h3>{stat.number}</h3>
              <p>{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Stats;