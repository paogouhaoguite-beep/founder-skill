# Synthetic worked example

Synthetic bundle A needs 2 units X and 1Y; bundle B needs 1X and 2Y. Eligible X=10,Y=8. Standalone capacities A=min(5,8)=5 and B=min(10,4)=4, but **5A+4B is impossible** (X14,Y13). A merchant priority of 3A first consumes X6,Y3; remaining X4,Y5 supports 2B. Final 3A+2B consumes X8,Y7, leaving X2,Y1.

| Proposal | X need | Y need | Decision |
|---|---:|---:|---|
|5A+4B|14|13|reject shortages 4X/5Y|
|3A+2B|8|7|feasible under supplied priority|

## Boundary case 1

Y8 consists of 4 at each of two locations and no transfer/assembly path. Recompute each location separately; pooled capacity is not a delivery promise.

## Boundary case 2

Parent bundle stock 5 is preassembled from components already deducted. Do not reserve component units a second time for selling that finished stock.
