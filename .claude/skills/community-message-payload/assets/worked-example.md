# Worked example

All names, inputs and results below are synthetic.

Input: synthetic Telegram chat -100123; approved message “The cotton tote is back in stock. $24 USD.”; no link supplied; HTML mode; no send authorization.

Preview: The cotton tote is back in stock. $24 USD.
```json
{"chat_id":"-100123","text":"The cotton tote is back in stock. $24 USD.","parse_mode":"HTML"}
```
Payload parses as JSON; no link or @everyone was invented. Status: prepared, not sent; schema not checked against live API; message_id unavailable. For Discord text-only, corresponding draft is `{"content":"The cotton tote is back in stock. $24 USD.","allowed_mentions":{"parse":[]}}`; its destination belongs to the separately approved webhook, not a Telegram chat ID.

## Acceptance scenarios

1. The message contains “<soft> & durable” in Telegram HTML mode. Render literal text as “&lt;soft&gt; &amp; durable” rather than unintended tags.

2. The send request times out. Do not retry blindly or call it delivered; inspect readback where available and report unresolved status.
