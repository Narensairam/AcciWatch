import React from 'react';
import Dropdown from 'react-bootstrap/Dropdown';

function CustomDropdown() {
  return (
    <Dropdown>
      <Dropdown.Toggle variant="secondary" id="dropdown-basic">
        Filters
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item>
        Severity
        </Dropdown.Item>
        <Dropdown.Item>Density</Dropdown.Item>
        
      </Dropdown.Menu>
    </Dropdown>
  );
}

export default CustomDropdown;
