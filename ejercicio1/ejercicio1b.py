import pulp

def main():
    prob = pulp.LpProblem("Ejercicio1b", pulp.LpMaximize)

    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)
    x3 = pulp.LpVariable("x3", lowBound=0)
    x4 = pulp.LpVariable("x4", lowBound=0)

    prob += x1 + x2 + 3*x3 + 2*x4, "Z"

    prob += x1 + 2*x2 - 3*x3 + 5*x4 <= 4, "R1"
    prob += 5*x1 - 2*x2         + 6*x4 <= 8, "R2"
    prob += 2*x1 + 3*x2 - 2*x3 + 3*x4 <= 3, "R3"
    prob += -x1        +   x3 + 2*x4 <= 0, "R4"

    prob.solve(pulp.PULP_CBC_CMD(msg=True))

    print(f"Estado: {pulp.LpStatus[prob.status]}")
    print(f"Z óptimo = {pulp.value(prob.objective)}")
    print(f"x1 = {x1.value()}")
    print(f"x2 = {x2.value()}")
    print(f"x3 = {x3.value()}")
    print(f"x4 = {x4.value()}")

if __name__ == "__main__":
    main()