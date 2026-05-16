import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}', './lib/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        midnight: '#06111f',
        command: '#0b1b33',
        emeraldA: '#27f3a4',
        amberRisk: '#ff9f1c'
      },
      boxShadow: {
        glow: '0 0 40px rgba(39, 243, 164, 0.18)'
      }
    }
  },
  plugins: []
};
export default config;
