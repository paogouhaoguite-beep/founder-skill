# Synthetic worked example

Synthetic day:120 tickets ×10 active minutes=1200 minutes. Three agents scheduled 480 each, supplied shrinkage 25%, fully ramped →3×480×0.75=1080 productive minutes. Gap 120 minutes or 12 average tickets. A fourth new agent at 50% ramp adds 480×0.75×0.5=180 minutes, total 1260; arithmetic headroom 60 minutes, **not an SLA guarantee**. Peak 160 tickets need 1600 minutes, gap 340 even with the new agent. Decision table: base—schedule the trained half-ramp agent if available; peak—request 340 minutes qualified surge or an approved backlog plan.

## Boundary case 1

The same agent supports email and chat concurrently but no effective concurrency data exists. Do not allocate 480 productive minutes to each channel; report shared capacity unresolved.

## Boundary case 2

One specialist is absent and only they can resolve safety complaints. Total team spare minutes do not solve that skill gap; route to named qualified backup.
