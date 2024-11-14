// postcss.config.js
module.exports = {
  plugins: [
    // Подключите postcss-import первым
    require("postcss-import"),
    require("tailwindcss"),
    require("autoprefixer"),
    require("postcss-nested"),
    require("cssnano")({
      preset: "default",
    }),
  ],
};
