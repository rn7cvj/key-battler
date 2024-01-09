import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default defineConfig({
  // base : path.resolve(__dirname , "./dist/"),
  plugins: [vue() ],
  server: {
    proxy: {
      '/api': {
        target: 'https://keybattler.poslam.ru', // Replace with your backend API URL
        changeOrigin: true
      }
    }
  }

})
