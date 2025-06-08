import React, { useState } from 'react';

const QuickSearch = ({ showPage }) => {
  const [searchData, setSearchData] = useState({
    keywords: '',
    location: '',
    type: 'all'
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSearchData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSearch = (e) => {
    e.preventDefault();
    console.log('Searching with:', searchData);
    showPage('jobs');
  };

  return (
    <section className="quick-search">
      <div className="container">
        <div className="search-container">
          <form className="search-form" onSubmit={handleSearch}>
            <div className="form-group">
              <label htmlFor="search-keywords">What</label>
              <input
                type="text"
                id="search-keywords"
                name="keywords"
                placeholder="Job title, skills, company"
                value={searchData.keywords}
                onChange={handleInputChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="search-location">Where</label>
              <input
                type="text"
                id="search-location"
                name="location"
                placeholder="City, state, or remote"
                value={searchData.location}
                onChange={handleInputChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="search-type">Type</label>
              <select
                id="search-type"
                name="type"
                value={searchData.type}
                onChange={handleInputChange}
              >
                <option value="all">All Types</option>
                <option value="full-time">Full Time</option>
                <option value="part-time">Part Time</option>
                <option value="contract">Contract</option>
                <option value="remote">Remote</option>
              </select>
            </div>
            <button type="submit" className="search-btn">
              <i className="fas fa-search"></i>
              Search Jobs
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default QuickSearch;
