// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html", // Укажите путь к вашим шаблонам
    "./blog/templates/**/*.html",
    "./news/templates/**/*.html",
    "./blog/static/**/*.css", // Укажите путь к файлам blog.css
    "./news/static/**/*.css", // Укажите путь к файлам blog.css
    "./src/**/*.css", // Укажите путь к CSS-файлам
    './src/**/*.vue'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
