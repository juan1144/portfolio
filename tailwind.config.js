/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      colors: {
        light: {
          background: '#ffffff',
          backgroundOverlay: '#ffffffE6',
          primary: '#000000',
          secondary: '#0C111D',
          border: '#27272a',
          accent: '#14b8a6',
        },
        dark: {
          background: '#191919',
          backgroundOverlay: '#2a2a2acc',
          primary: '#ffffff',
          secondary: '#fbfbff',
          border: '#27272a',
          accent: '#14b8a6',
        },
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}
