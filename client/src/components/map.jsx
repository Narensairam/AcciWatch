import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import CustomDropdown from './Dropdown.jsx';
import './map.css';
import 'leaflet/dist/leaflet.css';

const Map = () => {
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    const fetchMarkers = async () => {
        try {
            const response = await fetch('http://localhost:5000/get_cluster');
            if (!response.ok) {
                throw new Error('Failed to fetch markers');
            }
            const data = await response.json();
            const formattedMarkers = data.map(marker => ({
                lat: marker.Latitude,
                lng: marker.Longitude,
                title: `Color: ${marker.color}`
            }));
            setMarkers(formattedMarkers);
        } catch (error) {
            console.error('Error fetching markers:', error);
        }
    };

    fetchMarkers();
}, []);

    return (
        <div style={{ border: '2px solid black', margin: '5px', position: 'relative', overflow:'hidden' }}>
          <input
          type="text"
          placeholder="Search..."
          style={{
          width: '30vw',
          position: 'absolute',
          top: '10px',
          left: '10px',
          zIndex: '1',
          padding: '10px',
          }}
        />
   <div className="dropdown-container">
    <CustomDropdown />
   </div>
            <MapContainer
                center={[12.9716, 76.6423]} 
                zoom={9}
                style={{ height: 'calc(100vh - 20px)' }}
                attributionControl={false}
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {markers.map((marker, index) => (
                    <Marker key={index} position={[marker.lat, marker.lng]}>
                        <Popup>{marker.title}</Popup>
                    </Marker>
                ))}
            </MapContainer>
        </div>
    );
};

export default Map;
