import React from 'react';

const SuccessStories = () => {
  const stories = [
    {
      quote: "AccessWork helped me find a remote position that perfectly accommodates my mobility needs. The application process was transparent and inclusive from day one.",
      author: "Sarah M., Software Developer"
    },
    {
      quote: "As a deaf professional, I struggled to find employers who truly understood accessibility. Through AccessWork, I found a company that values my contributions.",
      author: "David R., Marketing Specialist"
    },
    {
      quote: "The platform's detailed accessibility information saved me time and helped me focus on opportunities that were genuinely suitable for my needs.",
      author: "Maria L., Data Analyst"
    }
  ];

  return (
    <section className="success-stories">
      <div className="container">
        <h2>Success Stories</h2>
        <div className="story-grid">
          {stories.map((story, index) => (
            <div key={index} className="story-card">
              <blockquote>{story.quote}</blockquote>
              <div className="story-author">{story.author}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default SuccessStories;