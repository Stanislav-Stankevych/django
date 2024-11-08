// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html", // Укажите путь к вашим шаблонам
    "./main/templates/**/*.html", // Если шаблоны лежат в приложениях
    "./blog/templates/**/*.html",
    "./news/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
