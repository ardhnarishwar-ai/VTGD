import { defineConfig } from 'vite';

// Vite config for a plain static frontend (no framework).
export default defineConfig({
  root: '.',
  base: './',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: 'index.html'
    }
  },
  server: {
    port: 5173,
    open: false
  },
  preview: {
    port: 4173
  }
});
