import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
  optimizeDeps: {
    exclude: ['svelte', 'svelte/**'], // Exclude all Svelte internals
    esbuildOptions: {
      target: 'esnext' // Force modern format
    }
  },
  build: {
    commonjsOptions: {
      transformMixedEsModules: true // Handle mixed ESM/CJS
    }
  }
});