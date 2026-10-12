# Synthetic synonym failure
Ten search sessions contain "waterproof pouch"; only a water-resistant pouch exists. A global synonym would create misleading matches. Proposed result: explain no waterproof match, display the water-resistant item only with its limitation. Separately, "cord bag" can map to "cable organizer" when catalog use cases support it.

## Acceptance scenarios
1. Logs count 30 searches from 10 sessions. Report event and session denominators separately.
2. A synonym improves one query but breaks a size-specific query. Include that counterexample in replay and narrow the rule before publication.
