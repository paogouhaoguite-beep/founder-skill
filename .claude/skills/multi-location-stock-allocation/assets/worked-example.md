# Synthetic worked example

All quantities, amounts, policies and company circumstances below are invented for arithmetic or decision review. They are not benchmarks.

## Inputs and timing

A has 80 available units and B has 10. Over the next two days, demand is A 20 and B 30. Neither location has other incoming stock. Transfer 20 units from A at the start of the period; they arrive at B at the end of day 2. Assume all stated demand occurs before that arrival and A fulfills its 20 units. The transfer is a movement within the network, not new supply. Units in transit remain part of network physical stock and are not yet available at B.

## Completed allocation comparison

| Scenario | A ending stock | B before transfer receipt | Treatment of B's unmet 20 units | B after receipt and settlement | Network ending physical stock |
|---|---:|---:|---|---:|---:|
| Retained backlog | 80 - 20 transferred - 20 fulfilled = 40 | 10 - 10 fulfilled = 0 | All 20 remain accepted backorders and are fulfilled immediately from the received transfer | 0 + 20 received - 20 backlog fulfilled = 0 | 40 |
| Lost sales | 40 | 0 | All 20 are lost demand; no orders, reservations or backlog remain | 0 + 20 received = 20 | 60 |

In the **retained-backlog scenario**, actual fulfilled units total 50: A 20 and B 30, including the delayed 20. Ending network stock is 90 - 50 = **40**. This assumes the delayed demand remains as orders and is fulfilled immediately upon receipt; B cannot meet those orders on time before arrival.

In the **lost-sales scenario**, only 30 units are actually sold and fulfilled: A 20 and B 10. Ending network stock is 90 - 30 = **60**. The other 20 units of demand do not consume inventory. Do not deduct forecast demand as though it were a completed sale, and do not infer which scenario applies without the merchant's backlog/cancellation evidence.

Neither scenario creates a 110-unit network. Both expose B's service gap before arrival. No transfer has been executed.

## Acceptance case 1 — supported inputs

Under the explicitly retained-backlog assumption, return A 40, B 0 and network 40 after the delayed 20 units are fulfilled. Under the lost-sales assumption, return A 40, B 20 and network 60. Show the pre-arrival service gap in both cases and distinguish demanded units from actual fulfillment.

## Acceptance case 2 — boundary or missing evidence

If source 80 is on-hand including 50 committed rather than available, recalculate from 30 available and never transfer committed units silently.

These cases specify expected behavior. Reading them or validating package syntax does not demonstrate live merchant acceptance.
