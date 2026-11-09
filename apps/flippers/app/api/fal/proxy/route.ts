// Lets the browser upload files straight to fal's storage without seeing the
// API key. Restricted to the storage endpoints only: model calls always go
// through /api/generate, which validates them against the catalog.
import { createRouteHandler } from "@fal-ai/server-proxy/nextjs";

const STORAGE = "rest.fal.ai/storage/upload";
export const { GET, POST, PUT } = createRouteHandler({
  allowedUrlPatterns: [
    `${STORAGE}/initiate\\?storage_type=fal-cdn-v3`,
    `${STORAGE}/initiate-multipart\\?storage_type=fal-cdn-v3`,
    `${STORAGE}/complete-multipart\\?storage_type=fal-cdn-v3`,
  ],
  allowedEndpoints: ["storage/upload"],
  allowUnauthorizedRequests: true, // the app password (middleware.ts) guards this route
});
