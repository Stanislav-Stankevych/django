// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  
  build: {
    outDir: 'static/js', // Каталог для выходных файлов
    rollupOptions: {
      input: './src/js/main.js', // Входной файл
      output: {
        entryFileNames: '[name].js', // Убираем хеши в именах файлов
        chunkFileNames: '[name].js', // Убираем хеши в чанках
        assetFileNames: '[name].[ext]', // Убираем хеши для ассетов
      },
    },
  },

});
