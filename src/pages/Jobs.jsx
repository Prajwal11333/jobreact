import React, { useState, useEffect } from 'react';
import JobCard from '../components/JobCard';
import { sampleJobs } from '../data/sampleJobs';

const Jobs = () => {
  const [jobs, setJobs] = useState(sampleJobs);
  const [filters, setFilters] = useState({
    title: '',
    location: '',
    type: '',
    accessibility: ''
  });

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const filterJobs = () => {
    const filteredJobs = sampleJobs.filter(job => {
      const matchesTitle = job.title.toLowerCase().includes(filters.title.toLowerCase());
      const matchesLocation = filters.location === '' || job.location.toLowerCase().includes(filters.location.toLowerCase());
      const matchesType = filters.type === '' || job.type === filters.type;
      const matchesAccessibility = filters.accessibility === '' || job.accessibility.includes(filters.accessibility);
      
      return matchesTitle && matchesLocation && matchesType && matchesAccessibility;
    });
    
    setJobs(filteredJobs);
  };

  const applyForJob = (jobId) => {
    const job = sampleJobs.find(j => j.id === jobId);
    alert(`Application started for: ${job.title} at ${job.company}\n\nYou'll be redirected to the application page.`);
  };

  const saveJob = (jobId) => {
    const job = sampleJobs.find(j => j.id === jobId);
    alert(`Job saved: ${job.title} at ${job.company}\n\nYou can view saved jobs in your profile.`);
  };

  useEffect(() => {
    filterJobs();
  }, [filters]);

  return (
    <div className="page-section active">
      <div className="page-content">
        <div className="jobs-header">
          <h1>Find Your Perfect Job</h1>
          <p>Discover inclusive opportunities that match your skills and accessibility needs</p>
        </div>

        <div className="jobs-filters">
          <div className="filter-row">
            <div className="form-group">
              <label htmlFor="filter-title">Job Title</label>
              <input
                type="text"
                id="filter-title"
                name="title"
                placeholder="Search jobs..."
                value={filters.title}
                onChange={handleFilterChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="filter-location">Location</label>
              <select
                id="filter-location"
                name="location"
                value={filters.location}
                onChange={handleFilterChange}
              >
                <option value="">All Locations</option>
                <option value="remote">Remote</option>
                <option value="bangalore">Bangalore</option>
                <option value="mumbai">Mumbai</option>
                <option value="delhi">Delhi</option>
                <option value="pune">Pune</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="filter-type">Job Type</label>
              <select
                id="filter-type"
                name="type"
                value={filters.type}
                onChange={handleFilterChange}
              >
                <option value="">All Types</option>
                <option value="full-time">Full Time</option>
                <option value="part-time">Part Time</option>
                <option value="contract">Contract</option>
                <option value="freelance">Freelance</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="filter-accessibility">Accessibility</label>
              <select
                id="filter-accessibility"
                name="accessibility"
                value={filters.accessibility}
                onChange={handleFilterChange}
              >
                <option value="">All Jobs</option>
                <option value="wheelchair-accessible">Wheelchair Accessible</option>
                <option value="hearing-support">Hearing Support</option>
                <option value="vision-support">Vision Support</option>
                <option value="remote-friendly">Remote Friendly</option>
              </select>
            </div>
          </div>
          <button className="btn primary-btn" onClick={filterJobs}>
            <i className="fas fa-filter"></i>
            Apply Filters
          </button>
        </div>

        <div id="jobs-container">
          {jobs.length === 0 ? (
            <div className="no-jobs" style={{textAlign: 'center', padding: '2rem', background: 'white', borderRadius: '15px', boxShadow: '0 5px 20px rgba(0,0,0,0.08)'}}>
              <i className="fas fa-search" style={{fontSize: '3rem', color: '#667eea', marginBottom: '1rem'}}></i>
              <h3>No jobs found matching your criteria</h3>
              <p>Try adjusting your filters or search terms</p>
            </div>
          ) : (
            jobs.map(job => (
              <JobCard
                key={job.id}
                job={job}
                onApply={applyForJob}
                onSave={saveJob}
              />
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default Jobs;