import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Home from './pages/home.jsx';
import Jobs from './pages/Jobs';
import PostJob from './pages/PostJob';
import Resources from './pages/Resources.jsx';
import About from './pages/About';
import Contact from './pages/Contact';
import Footer from './components/Footer';
import LoginModal from './components/LoginModal';
import SignupModal from './components/SignupModal';
import ComingSoonModal from './components/ComingSoonModal';

const App = () => {
  const [currentPage, setCurrentPage] = useState('main');
  const [activeModal, setActiveModal] = useState(null);

  const openModal = (modalId) => {
    setActiveModal(modalId);
  };

  const closeModal = () => {
    setActiveModal(null);
  };

  const renderPage = () => {
    switch (currentPage) {
      case 'main':
        return <Home showPage={setCurrentPage} openModal={openModal} />;
      case 'jobs':
        return <Jobs />;
      case 'post-job':
        return <PostJob showPage={setCurrentPage} />;
      case 'resources':
        return <Resources openModal={openModal} />;
      case 'about':
        return <About />;
      case 'contact':
        return <Contact />;
      default:
        return <Home showPage={setCurrentPage} openModal={openModal} />;
    }
  };

  return (
    <div className="App">
      <a href="#main-content" className="skip-link">Skip to main content</a>
      <Navbar 
        currentPage={currentPage} 
        showPage={setCurrentPage} 
        openModal={openModal} 
      />
      <main id="main-content">
        {renderPage()}
      </main>
      <Footer />
      
      {activeModal === 'loginModal' && (
        <LoginModal closeModal={closeModal} />
      )}
      {activeModal === 'signupModal' && (
        <SignupModal closeModal={closeModal} />
      )}
      {activeModal === 'comingSoonModal' && (
        <ComingSoonModal closeModal={closeModal} />
      )}
    </div>
  );
};

export default App;