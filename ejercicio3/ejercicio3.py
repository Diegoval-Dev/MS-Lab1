import pulp

model = pulp.LpProblem("Asignacion_de_autobuses", pulp.LpMinimize)

# Variables de decisión: número de autobuses que inician en cada turno (continuas, >= 0)
x = [pulp.LpVariable(f"x{i+1}", lowBound=0, cat="Continuous") for i in range(6)]

# Funcion objetivo: minimizar el total de autobuses
model += pulp.lpSum(x), "Total_de_autobuses"

# Restricciones de cobertura de turnos
model += x[0] + x[5] >= 4, "Turno_1"
model += x[0] + x[1] >= 8, "Turno_2"
model += x[1] + x[2] >= 10, "Turno_3"
model += x[2] + x[3] >= 7, "Turno_4"
model += x[3] + x[4] >= 12, "Turno_5"
model += x[4] + x[5] >= 4, "Turno_6"


model.solve()

print("Estado de la solucion:", pulp.LpStatus[model.status])
print("Valor optimo:", pulp.value(model.objective))

for i in range(6):
    print(f"x{i+1} (Turno {i+1}) = {x[i].varValue:.2f}")
