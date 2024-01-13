import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import {viteSingleFile} from "vite-plugin-singlefile";



export default defineConfig({

    plugins: [
      vue(),
      viteSingleFile(),
    ],
    server: {
    proxy: {
      '/api': {
        target: 'https://keybattler.poslam.ru', // Replace with your backend API URL
        changeOrigin: true
      }
    }
  }

})
