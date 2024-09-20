import React from 'react';
import Map from './map.jsx';
import Analysis from './visualAnalysis.js';

const Dashboard = ({ onLogout }) => {
  const handleLogout = () => {
    onLogout();
    window.location.href = 'http://localhost:5000/login';
  };
  return (
    <div className="sidebar">
      <nav>
        <ul>
          <li><h1>ACCIWATCH</h1></li>
          <li><a href="#analysis">Analysis</a></li>
          <li><a href="#upload">Upload</a></li>
          <li><a href="#model">Model</a></li>
          <li><a href="#help">Help</a></li>
          <li><a onClick={handleLogout}>Logout</a></li>
        </ul>
      </nav>
      <div className="map-container">
        <Map />
      </div>
      <Analysis />
    </div>
  );
};

export default Dashboard;
