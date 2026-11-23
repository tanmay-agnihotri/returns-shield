// Backend URL. Set VITE_API_URL in Vercel (or a local .env file) to point
// the frontend at the deployed backend; falls back to the local dev server.
export const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
