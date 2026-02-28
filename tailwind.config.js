/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/*.py',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          50: '#e8ebf0',
          100: '#c5cdd9',
          200: '#9eadc1',
          300: '#778da9',
          400: '#5a7496',
          500: '#3d5b83',
          600: '#2e4a72',
          700: '#1f3860',
          800: '#1a2946',
          900: '#111c30',
        },
        gold: {
          50: '#fef8e7',
          100: '#fdedc4',
          200: '#fbe19d',
          300: '#f9d576',
          400: '#f7cb57',
          500: '#e8a021',
          600: '#d4891a',
          700: '#b97213',
          800: '#9e5c0c',
          900: '#7a4508',
        },
      },
    },
  },
  plugins: [],
}