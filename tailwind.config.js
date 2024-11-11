// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html", // Укажите путь к вашим шаблонам
    "./main/templates/**/*.html", // Если шаблоны лежат в приложениях
    "./blog/templates/**/*.html",
    "./news/templates/**/*.html",
    "./blog/static/**/*.css", // Укажите путь к файлам blog.css
    "./news/static/**/*.css", // Укажите путь к файлам blog.css
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
