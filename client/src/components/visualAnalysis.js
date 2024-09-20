import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Chart as ChartJS} from 'chart.js/auto';
import {Bar, Doughnut, Line} from 'react-chartjs-2'

import revenueData from "./data/revenueData.json";
import sourceData from "./data/sourceData.json";
import severity from "./data/severity.json"

function Analysis() {
  return (
    <div className='container'>
      <div className='row mb-2'>
        <div className='col-5 border border-dark me-2'>
        <Doughnut
          data={{
            labels: severity.map((data) => data.label),
            
            datasets: [
              {
                label: "Count",
                data: severity.map((data) => data.value),
                backgroundColor: [
                  "rgba(43, 63, 229, 0.8)",
                  "rgba(250, 192, 19, 0.8)",
                  "rgba(253, 155, 150, 0.8)",
                  "rgba(250, 192, 140, 0.8)"
                ],
                borderColor: [
                  "rgba(43, 63, 229, 0.8)",
                  "rgba(250, 192, 19, 0.8)",
                  "rgba(253, 135, 135, 0.8)",
                  "rgba(250, 192, 135, 0.8)"
                ],
              },
            ],
          }}
          options={{
            plugins: {
              title: {
                text: "Severity",
              },
            },
          }}
        />
        </div>
        <div className='col-5 border border-dark'><h1>Filters Come here</h1></div>
      </div>
      <div className='row'>
        <div className='col-5 border border-dark me-2'>
        <Bar
          data={{
            labels: sourceData.map((data) => data.label),
            datasets: [
              {
                label: "Count",
                data: sourceData.map((data) => data.value),
                backgroundColor: [
                  "rgba(43, 63, 229, 0.8)",
                  "rgba(250, 192, 19, 0.8)",
                  "rgba(253, 135, 135, 0.8)",
                ],
                borderRadius: 5,
              },
            ],
          }}
          options={{
            plugins: {
              title: {
                text: "Revenue Source",
              },
            },
          }}
        />
        </div>
        <div className='col-5 border border-dark'>
        <Line
          data={{
            labels: sourceData.map((data) => data.label),
            datasets: [
              {
                label: "Weather",
                data: sourceData.map((data) => data.revenue),
                backgroundColor: "#064FF0",
                borderColor: "#064FF0",
              },
              {
                label: "severity",
                data: sourceData.map((data) => data.cost),
                backgroundColor: "#FF3030",
                borderColor: "#FF3030",
              },
            ],
          }}
          options={{
            elements: {
              line: {
                tension: 0.5,
              },
            },
            plugins: {
              title: {
                text: "Monthly Revenue & Cost",
              },
            },
          }}
        />
        </div>
      </div>
    </div>
  );
}

export default Analysis;