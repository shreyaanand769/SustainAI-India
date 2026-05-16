export type DistrictRisk = {
  district: string;
  state: string;
  lat: number;
  lon: number;
  heat: number;
  water: number;
  aqi: number;
  flood: number;
  agriculture: number;
  population: number;
  sustainability: number;
  trend: 'improving' | 'stable' | 'deteriorating';
};

export const districtRisks: DistrictRisk[] = [
  { district: 'Bengaluru Urban', state: 'Karnataka', lat: 12.97, lon: 77.59, heat: 76, water: 91, aqi: 62, flood: 39, agriculture: 44, population: 88, sustainability: 48, trend: 'deteriorating' },
  { district: 'Mumbai City', state: 'Maharashtra', lat: 19.07, lon: 72.87, heat: 73, water: 55, aqi: 70, flood: 84, agriculture: 21, population: 93, sustainability: 52, trend: 'stable' },
  { district: 'New Delhi', state: 'Delhi', lat: 28.61, lon: 77.20, heat: 86, water: 74, aqi: 95, flood: 42, agriculture: 18, population: 91, sustainability: 38, trend: 'deteriorating' },
  { district: 'Chennai', state: 'Tamil Nadu', lat: 13.08, lon: 80.27, heat: 82, water: 87, aqi: 58, flood: 76, agriculture: 31, population: 81, sustainability: 45, trend: 'deteriorating' },
  { district: 'Pune', state: 'Maharashtra', lat: 18.52, lon: 73.85, heat: 69, water: 67, aqi: 61, flood: 46, agriculture: 49, population: 75, sustainability: 59, trend: 'stable' },
  { district: 'Kutch', state: 'Gujarat', lat: 23.73, lon: 69.85, heat: 88, water: 89, aqi: 43, flood: 31, agriculture: 73, population: 39, sustainability: 54, trend: 'stable' },
  { district: 'Kamrup Metro', state: 'Assam', lat: 26.14, lon: 91.73, heat: 58, water: 38, aqi: 51, flood: 88, agriculture: 66, population: 64, sustainability: 61, trend: 'deteriorating' },
  { district: 'Indore', state: 'Madhya Pradesh', lat: 22.71, lon: 75.85, heat: 72, water: 63, aqi: 52, flood: 24, agriculture: 57, population: 66, sustainability: 68, trend: 'improving' }
];

export const riskTimeline = [
  { horizon: 'Now', heat: 71, water: 68, aqi: 64, agriculture: 52 },
  { horizon: '1M', heat: 75, water: 71, aqi: 66, agriculture: 54 },
  { horizon: '6M', heat: 79, water: 76, aqi: 69, agriculture: 59 },
  { horizon: '1Y', heat: 81, water: 78, aqi: 70, agriculture: 61 },
  { horizon: '5Y', heat: 87, water: 84, aqi: 74, agriculture: 69 },
  { horizon: '10Y', heat: 92, water: 88, aqi: 78, agriculture: 74 }
];

export const interventions = [
  { name: 'Urban cool-roof + heat shelter grid', domain: 'Heat', impact: 91, cost: '₹1,240 cr', roi: '2.8x', carbon: '1.1 MtCO₂e', speed: '9 months' },
  { name: 'Managed aquifer recharge and lake revival', domain: 'Water', impact: 94, cost: '₹2,850 cr', roi: '3.6x', carbon: '0.3 MtCO₂e', speed: '24 months' },
  { name: 'AI precision irrigation for stressed mandals', domain: 'Agriculture', impact: 83, cost: '₹980 cr', roi: '4.1x', carbon: '0.6 MtCO₂e', speed: '12 months' },
  { name: 'Flood zoning + sponge-city corridors', domain: 'Flood', impact: 88, cost: '₹3,400 cr', roi: '2.2x', carbon: '0.9 MtCO₂e', speed: '36 months' }
];

export const causalNodes = [
  ['Groundwater collapse', 'Borewell over-extraction', 0.92],
  ['Groundwater collapse', 'Lake encroachment', 0.81],
  ['Urban heat island', 'Construction density', 0.86],
  ['Urban heat island', 'Tree cover loss', 0.78],
  ['AQI crisis', 'Transport emissions', 0.74],
  ['AQI crisis', 'Construction dust', 0.67],
  ['Flood risk', 'Drainage capacity gap', 0.89]
];
