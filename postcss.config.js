// postcss.config.js
module.exports = {
  plugins: [
    require("postcss-import"), // Подключите postcss-import первым
    require("tailwindcss"),
    require("autoprefixer"),
    require("postcss-nested"),
    require("cssnano")({
      preset: "default",
    }),
  ],
};
