// src/components/JobCard.jsx
import React from 'react';

const JobCard = ({ job, onApply, onSave }) => {
  const getAccessibilityIcon = (feature) => {
    const icons = {
      'wheelchair-accessible': 'fas fa-wheelchair',
      'hearing-support': 'fas fa-assistive-listening-systems',
      'vision-support': 'fas fa-eye',
      'remote-friendly': 'fas fa-home',
      'flexible-hours': 'fas fa-clock',
      'assistive-tech': 'fas fa-desktop'
    };
    return icons[feature] || 'fas fa-check';
  };

  const formatSalary = (salary) => {
    if (!salary) return 'Salary not disclosed';
    return salary;
  };

  return (
    <div className="job-card">
      <div className="job-header">
        <div>
          <h3 className="job-title">{job.title}</h3>
          <div className="job-company">{job.company}</div>
        </div>
        <div className="job-salary" style={{ textAlign: 'right', color: '#28a745', fontWeight: '600' }}>
          {formatSalary(job.salary)}
        </div>
      </div>

      <div className="job-meta">
        <span className="job-tag">
          <i className="fas fa-map-marker-alt"></i> {job.location}
        </span>
        <span className="job-tag">
          <i className="fas fa-briefcase"></i> {job.type.replace('-', ' ').toUpperCase()}
        </span>
        <span className="job-tag">
          <i className="fas fa-calendar-alt"></i> {job.postedDate}
        </span>
      </div>

      {job.accessibility && job.accessibility.length > 0 && (
        <div className="accessibility-features">
          {job.accessibility.map((feature, index) => (
            <span 
              key={index} 
              className={`accessibility-indicator ${feature}`}
              title={feature.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}
            >
              <i className={getAccessibilityIcon(feature)}></i>
              {feature.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}
            </span>
          ))}
        </div>
      )}

      <div className="job-description">
        {job.description}
      </div>

      {job.requirements && (
        <div className="job-requirements" style={{ marginBottom: '1rem' }}>
          <strong>Key Requirements:</strong>
          <ul style={{ marginTop: '0.5rem', paddingLeft: '1.5rem' }}>
            {job.requirements.slice(0, 3).map((req, index) => (
              <li key={index} style={{ marginBottom: '0.25rem', color: '#666' }}>{req}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="job-actions">
        <button 
          className="apply-btn"
          onClick={() => onApply(job.id)}
        >
          <i className="fas fa-paper-plane"></i>
          Apply Now
        </button>
        <button 
          className="save-btn"
          onClick={() => onSave(job.id)}
        >
          <i className="fas fa-bookmark"></i>
          Save Job
        </button>
      </div>
    </div>
  );
};

export default JobCard;