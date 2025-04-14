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
          primary: '#262629',
          secondary: '#6c6c75',
          border: '#27272a',
          accent: '#14b8a6',
        },
        dark: {
          background: '#191919',
          backgroundOverlay: '#2a2a2acc',
          primary: '#f3f3f4',
          secondary: '#93939c',
          border: '#27272a',
          accent: '#14b8a6',
        },
      },
    },
  },
  darkMode: 'class',
  plugins: [],
}
