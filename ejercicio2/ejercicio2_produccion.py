# ejercicio2_produccion.py

import pulp

months = list(range(1,7))
demand     = {1:180, 2:250, 3:190, 4:140, 5:220, 6:250}
prod_cost  = {1:50, 2:45, 3:55, 4:52, 5:48, 6:50}
inv_cost   = {1:8,  2:10, 3:10, 4:10, 5:8,  6:8}
capacity   = 225

m = pulp.LpProblem("Produccion_MultiPeriodo", pulp.LpMinimize)
P = pulp.LpVariable.dicts('P', months, lowBound=0)
I = pulp.LpVariable.dicts('I', months, lowBound=0)

m += pulp.lpSum(prod_cost[t]*P[t] + inv_cost[t]*I[t] for t in months)

m += I[1] == P[1] - demand[1]
for t in months[1:]:
    m += I[t] == I[t-1] + P[t] - demand[t]

for t in months:
    m += P[t] <= capacity

m.solve(pulp.PULP_CBC_CMD(msg=False))

print("Mes | Demanda | Produc. | Invent. | Costo Prod | Costo Inv | Total Mes")
for t in months:
    prod = P[t].value()
    inv  = I[t].value()
    cp   = prod_cost[t]*prod
    ci   = inv_cost[t]*inv
    print(f"{t:>3} | {demand[t]:>7} | {prod:>7.1f} | {inv:>7.1f} |"
          f" {cp:>10.1f} | {ci:>9.1f} | {cp+ci:>10.1f}")

non_opt = sum(demand[t]*prod_cost[t] for t in months)
opt     = sum(prod_cost[t]*P[t].value() + inv_cost[t]*I[t].value() for t in months)
print("\nCosto Óptimo Total:     ", opt)
print("Costo Producción exacta:", non_opt)
print("Ahorro:                 ", non_opt - opt)
