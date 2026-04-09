import matplotlib.pyplot as plt

# Tamaños de entrada
n = [10000, 100000, 500000]

# -------------------------
# DATASET UNIFORME ORDENADO
# -------------------------
uniform_lineal = [0.449763200012967, 4.281630999990739, 27.64504269999452]
uniform_binaria = [0.0005682000191882253, 0.0008865999989211559, 0.0011794000165537]
uniform_exponencial = [0.003553600050508976, 0.005264799925498664, 0.0063075999496504664]
uniform_interpolacion = [0.0005369000136852264, 0.0006067999638617039, 0.000722200027666986]

plt.figure(figsize=(9, 6))
plt.plot(n, uniform_lineal, marker='o', label='Lineal')
plt.plot(n, uniform_binaria, marker='o', label='Binaria')
plt.plot(n, uniform_exponencial, marker='o', label='Exponencial')
plt.plot(n, uniform_interpolacion, marker='o', label='Interpolación')
plt.xlabel("Tamaño n")
plt.ylabel("Tiempo promedio (ms/búsqueda)")
plt.title("Dataset uniforme ordenado")
plt.yscale("log")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.savefig("grafico_uniforme.png", dpi=300, bbox_inches="tight")

# -------------------------
# DATASET SESGADO ORDENADO
# -------------------------
biased_lineal = [0.4672782000852749, 8.241276900051162, 42.71225189999677]
biased_binaria = [0.00041610002517700195, 0.0008768000407144427, 0.000990699976682663]
biased_exponencial = [0.003019999945536256, 0.003796400036662817, 0.0035454999888315797]
biased_interpolacion = [0.07238160003907979, 0.21412610006518662, 0.16500319994520396]

plt.figure(figsize=(9, 6))
plt.plot(n, biased_lineal, marker='o', label='Lineal')
plt.plot(n, biased_binaria, marker='o', label='Binaria')
plt.plot(n, biased_exponencial, marker='o', label='Exponencial')
plt.plot(n, biased_interpolacion, marker='o', label='Interpolación')
plt.xlabel("Tamaño n")
plt.ylabel("Tiempo promedio (ms/búsqueda)")
plt.title("Dataset sesgado ordenado")
plt.yscale("log")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.savefig("grafico_sesgado.png", dpi=300, bbox_inches="tight")

# -------------------------
# DATASET DESORDENADO
# -------------------------
shuffled_lineal = [0.4374676999868825, 7.861508900066839, 39.209852400003]

plt.figure(figsize=(9, 6))
plt.plot(n, shuffled_lineal, marker='o', label='Lineal')
plt.xlabel("Tamaño n")
plt.ylabel("Tiempo promedio (ms/búsqueda)")
plt.title("Dataset desordenado")
plt.yscale("log")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.savefig("grafico_desordenado.png", dpi=300, bbox_inches="tight")

plt.show()