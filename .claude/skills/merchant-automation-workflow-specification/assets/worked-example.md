# Synthetic worked example

Input: Merchant wants a draft support task when a tracked parcel has no new scan for a merchant-defined interval. Event key orderID+shipmentID+ruleVersion; last scan and delivery status are authoritative inputs.

Flow: daily eligible read→exclude delivered/cancelled→compare scan age to configured interval→check existing open task→create or update a draft proposal→verify task ID. A duplicate trigger with the same key does not create another task. No customer email is sent.

Boundary scenario 1: Task creation times out. Read by stable key before retrying.
Boundary scenario 2: A late delivery event arrives after the stale-scan trigger. Re-read shipment status before creating the task and suppress if delivered.
