import React, { useState, useEffect } from 'react';
import QuickSearch from '../components/QuickSearch';
import Features from '../components/Features';
import Stats from '../components/Stats';
import SuccessStories from '../components/SuccessStories';
import CTA from '../components/CTA';

const Home = ({ showPage, openModal }) => {
  return (
    <div className="page-section active">
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <h1>Inclusive Opportunities for Everyone</h1>
            <p>Connecting talented individuals with disabilities to meaningful careers and supportive employers</p>
            <div className="hero-buttons">
              <a 
                href="#" 
                className="btn primary-btn" 
                onClick={(e) => { e.preventDefault(); showPage('jobs'); }}
              >
                <i className="fas fa-search"></i>
                Find Jobs
              </a>
              <a 
                href="#" 
                className="btn secondary-btn" 
                onClick={(e) => { e.preventDefault(); showPage('post-job'); }}
              >
                <i className="fas fa-plus"></i>
                Post a Job
              </a>
            </div>
          </div>
        </div>
      </section>

      <QuickSearch showPage={showPage} />
      <Features />
      <Stats />
      <SuccessStories />
      <CTA openModal={openModal} />
    </div>
  );
};

export default Home;