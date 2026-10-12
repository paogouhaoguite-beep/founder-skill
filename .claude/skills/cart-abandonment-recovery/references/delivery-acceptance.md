# Delivery example and acceptance

Illustrative flow, not a fixed schedule: eligible abandoned checkout → consent/suppression check → merchant-selected delay → reminder with actual cart link → purchase/opt-out exit. Supply the complete subject, preview, body and CTA, followed by an optional help or incentive message only when justified. If cart-link injection is unsupported, mark the flow not activation-ready; do not replace it with a fake checkout URL.

Acceptance: each message is finished; trigger, delay, audience, exit and discount rules are explicit; dynamic fields correspond to actual provider capabilities; no unsupported urgency; saved enabled/disabled state read back if configured. Without a provider, deliver a setup-ready draft with field requirements and say it is not active.
