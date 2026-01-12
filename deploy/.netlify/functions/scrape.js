const fetch = require('node-fetch');

exports.handler = async (event, context) => {
  try {
    const response = await fetch('https://www.insecam.org/api/v1/cameras');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();

    // Assuming the API returns an array of camera objects
    // Transform to match our markers format if needed
    const markers = data.map(camera => ({
      id: camera.id || 'unknown',
      country: camera.country || 'Unknown',
      country_code: camera.country_code || 'XX',
      region: camera.region || 'Unknown',
      city: camera.city || 'Unknown',
      zip: camera.zip || '00000',
      timezone: camera.timezone || '+00:00',
      manufacturer: camera.manufacturer || 'Unknown',
      lat: parseFloat(camera.lat) || 0,
      lng: parseFloat(camera.lng) || 0,
      stream: camera.stream || ''
    }));

    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
      },
      body: JSON.stringify(markers)
    };
  } catch (error) {
    console.error('Error fetching cameras:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Failed to fetch cameras' })
    };
  }
};