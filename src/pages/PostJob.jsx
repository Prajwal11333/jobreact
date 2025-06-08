import React, { useState } from 'react';

const PostJob = ({ showPage }) => {
  const [formData, setFormData] = useState({
    companyName: '',
    jobPosition: '',
    jobLocation: '',
    employmentType: '',
    jobDescription: '',
    accessibilityFeatures: [],
    salaryRange: '',
    contactEmail: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleCheckboxChange = (e) => {
    const { value, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      accessibilityFeatures: checked
        ? [...prev.accessibilityFeatures, value]
        : prev.accessibilityFeatures.filter(feature => feature !== value)
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Job posted successfully! It will be visible after approval.');
    showPage('jobs');
  };

  return (
    <div className="page-section active">
      <div className="page-content">
        <div className="jobs-header">
          <h1>Post an Inclusive Job</h1>
          <p>Create opportunities that welcome talent from all backgrounds</p>
        </div>

        <div className="search-container">
          <form id="post-job-form" onSubmit={handleSubmit}>
            <div className="filter-row">
              <div className="form-group">
                <label htmlFor="company-name">Company Name *</label>
                <input
                  type="text"
                  id="company-name"
                  name="companyName"
                  value={formData.companyName}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="job-position">Job Title *</label>
                <input
                  type="text"
                  id="job-position"
                  name="jobPosition"
                  value={formData.jobPosition}
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>
            
            <div className="filter-row">
              <div className="form-group">
                <label htmlFor="job-location">Location *</label>
                <input
                  type="text"
                  id="job-location"
                  name="jobLocation"
                  placeholder="e.g. Bangalore, Remote"
                  value={formData.jobLocation}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="employment-type">Employment Type *</label>
                <select
                  id="employment-type"
                  name="employmentType"
                  value={formData.employmentType}
                  onChange={handleInputChange}
                  required
                >
                  <option value="">Select Type</option>
                  <option value="full-time">Full Time</option>
                  <option value="part-time">Part Time</option>
                  <option value="contract">Contract</option>
                  <option value="freelance">Freelance</option>
                </select>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="job-desc">Job Description *</label>
              <textarea
                id="job-desc"
                name="jobDescription"
                rows="6"
                placeholder="Describe the role, responsibilities, and requirements..."
                value={formData.jobDescription}
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

            <div className="form-group">
              <label htmlFor="accessibility-features">Accessibility Features</label>
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                gap: '1rem',
                marginTop: '0.5rem'
              }}>
                {[
                  { value: 'wheelchair-accessible', label: 'Wheelchair Accessible' },
                  { value: 'hearing-support', label: 'Hearing Support Available' },
                  { value: 'vision-support', label: 'Vision Support Available' },
                  { value: 'flexible-hours', label: 'Flexible Working Hours' },
                  { value: 'remote-work', label: 'Remote Work Options' },
                  { value: 'assistive-tech', label: 'Assistive Technology Provided' }
                ].map((feature) => (
                  <label
                    key={feature.value}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '0.5rem'
                    }}
                  >
                    <input
                      type="checkbox"
                      value={feature.value}
                      checked={formData.accessibilityFeatures.includes(feature.value)}
                      onChange={handleCheckboxChange}
                    />
                    {feature.label}
                  </label>
                ))}
              </div>
            </div>

            <div className="filter-row">
              <div className="form-group">
                <label htmlFor="salary-range">Salary Range</label>
                <input
                  type="text"
                  id="salary-range"
                  name="salaryRange"
                  placeholder="e.g. ₹5,00,000 - ₹8,00,000"
                  value={formData.salaryRange}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label htmlFor="contact-email">Contact Email *</label>
                <input
                  type="email"
                  id="contact-email"
                  name="contactEmail"
                  value={formData.contactEmail}
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>

            <button type="submit" className="btn primary-btn" style={{marginTop: '1rem'}}>
              <i className="fas fa-paper-plane"></i>
              Post Job
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default PostJob;