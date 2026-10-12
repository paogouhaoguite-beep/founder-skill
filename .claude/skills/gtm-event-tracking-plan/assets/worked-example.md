# Synthetic data-layer plan
Business action: basket successfully updated by the commerce API.

```javascript
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({ecommerce: null});
window.dataLayer.push({event: 'cart_add_confirmed', ecommerce: {currency: 'USD', value: 30, items: [{item_id: 'DEMO-BLUE', price: 30, quantity: 1}]}});
```
Map the custom trigger to the appropriate GA4 ecommerce event. A failed API response must not emit it; the UI click alone is insufficient.

## Acceptance scenarios
1. Double click causes one successful API addition. Event cardinality follows the actual confirmed action, not two raw clicks.
2. Consent is denied then granted. Preview against the documented consent behavior; do not silently replay all past events or override the user's choice.
