// import React from 'react';

// const Resources = ({ openModal }) => {
//   const resources = [
//     {
//       icon: 'fas fa-file-alt',
//       title: 'Resume Builder',
//       description: 'Create professional resumes that highlight your skills and accommodations',
//       buttonText: 'Use Tool',
//       buttonIcon: 'fas fa-external-link-alt'
//     },
//     {
//       icon: 'fas fa-comments',
//       title: 'Interview Prep',
//       description: 'Practice common interview questions and learn to discuss accommodations',
//       buttonText: 'Start Practice',
//       buttonIcon: 'fas fa-play'
//     },
//     {
//       icon: 'fas fa-graduation-cap',
//       title: 'Skill Courses',
//       description: 'Free online courses to develop in-demand professional skills',
//       buttonText: 'Browse Courses',
//       buttonIcon: 'fas fa-book-open'
//     },
//     {
//       icon: 'fas fa-network-wired',
//       title: 'Mentorship Program',
//       description: 'Connect with experienced professionals in your field',
//       buttonText: 'Find Mentor',
//       buttonIcon: 'fas fa-user-friends'
//     },
//     {
//       icon: 'fas fa-briefcase',
//       title: 'Career Guidance',
//       description: 'One-on-one sessions with career counselors',
//       buttonText: 'Book Session',
//       buttonIcon: 'fas fa-calendar-alt'
//     },
//     {
//       icon: 'fas fa-users',
//       title: 'Community Forum',
//       description: 'Connect with peers and share experiences',
//       buttonText: 'Join Forum',
//       buttonIcon: 'fas fa-comment-dots'
//     }
//   ];

//   return (
//     <div className="page-section active">
//       <div className="page-content">
//         <div className="jobs-header">
//           <h1>Career Resources</h1>
//           <p>Tools and guides to help you succeed in your career journey</p>
//         </div>

//         <div className="feature-grid">
//           {resources.map((resource, index) => (
//             <div key={index} className="feature-card">
//               <i className={`${resource.icon} feature-icon`}></i>
//               <h3>{resource.title}</h3>
//               <p>{resource.description}</p>
//               <button
//                 className="btn primary-btn"
//                 onClick={() => openModal('comingSoonModal')}
//               >
//                 <i className={resource.buttonIcon}></i>
//                 {resource.buttonText}
//               </button>
//             </div>
//           ))}
//         </div>
//       </div>
//     </div>
//   );
// };

// export default Resources;



import React from 'react';

const Resources = ({ openModal }) => {
  const handleResumeBuilder = async () => {
    try {
      // Check if Flask server is running
      const response = await fetch('http://localhost:5000/api/resume-builder');
      const data = await response.json();
      
      if (data.success) {
        // Open resume builder in new tab
        window.open('http://localhost:5000/resume', '_blank');
      } else {
        // Fallback to modal if server is not running
        openModal('comingSoonModal');
      }
    } catch (error) {
      console.error('Flask server not running:', error);
      // Show error message or fallback
      alert('Resume Builder service is currently unavailable. Please make sure the Flask server is running on port 5000.');
    }
  };

  const resources = [
    {
      icon: 'fas fa-file-alt',
      title: 'Resume Builder',
      description: 'Create professional resumes that highlight your skills and accommodations',
      buttonText: 'Use Tool',
      buttonIcon: 'fas fa-external-link-alt',
      action: handleResumeBuilder // Special action for resume builder
    },
    {
      icon: 'fas fa-comments',
      title: 'Interview Prep',
      description: 'Practice common interview questions and learn to discuss accommodations',
      buttonText: 'Start Practice',
      buttonIcon: 'fas fa-play',
      action: () => openModal('comingSoonModal')
    },
    {
      icon: 'fas fa-graduation-cap',
      title: 'Skill Courses',
      description: 'Free online courses to develop in-demand professional skills',
      buttonText: 'Browse Courses',
      buttonIcon: 'fas fa-book-open',
      action: () => openModal('comingSoonModal')
    },
    {
      icon: 'fas fa-network-wired',
      title: 'Mentorship Program',
      description: 'Connect with experienced professionals in your field',
      buttonText: 'Find Mentor',
      buttonIcon: 'fas fa-user-friends',
      action: () => openModal('comingSoonModal')
    },
    {
      icon: 'fas fa-briefcase',
      title: 'Career Guidance',
      description: 'One-on-one sessions with career counselors',
      buttonText: 'Book Session',
      buttonIcon: 'fas fa-calendar-alt',
      action: () => openModal('comingSoonModal')
    },
    {
      icon: 'fas fa-users',
      title: 'Community Forum',
      description: 'Connect with peers and share experiences',
      buttonText: 'Join Forum',
      buttonIcon: 'fas fa-comment-dots',
      action: () => openModal('comingSoonModal')
    }
  ];

  return (
    <div className="page-section active">
      <div className="page-content">
        <div className="jobs-header">
          <h1>Career Resources</h1>
          <p>Tools and guides to help you succeed in your career journey</p>
        </div>

        <div className="feature-grid">
          {resources.map((resource, index) => (
            <div key={index} className="feature-card">
              <i className={`${resource.icon} feature-icon`}></i>
              <h3>{resource.title}</h3>
              <p>{resource.description}</p>
              <button
                className="btn primary-btn"
                onClick={resource.action}
              >
                <i className={resource.buttonIcon}></i>
                {resource.buttonText}
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Resources;