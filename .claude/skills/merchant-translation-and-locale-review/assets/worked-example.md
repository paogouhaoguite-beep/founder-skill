# Synthetic worked example

Input: English care label for es-MX: “Hand wash only. Do not tumble dry. Capacity: 750 mL. Model: B-750.” Protected token B-750; capacity must not change.

Translation: “Lavar únicamente a mano. No secar en secadora. Capacidad: 750 mL. Modelo: B-750.”

Review table: “only”→“únicamente” preserved restriction; “Do not”→“No” preserved prohibition; 750 mL and B-750 unchanged. No Mexican-peso price or additional guarantee is introduced. Native review pending; print-layout inspection not run.

Boundary scenario 1: Source says “ships in 2 days” without explaining dispatch versus arrival. Flag ambiguity before choosing a target phrase that commits to delivery.
Boundary scenario 2: The source has [[order_id]] placeholders. Preserve exact tokens through chunking and reassembly; do not translate or remove them.
