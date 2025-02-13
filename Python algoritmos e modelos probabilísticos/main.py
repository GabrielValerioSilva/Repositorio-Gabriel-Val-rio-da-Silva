import matplotlib.pyplot as plt

hospital_data = [
    {"hospital": "Hospital A", "tempo_espera": 45},
    {"hospital": "Hospital B", "tempo_espera": 30},
    {"hospital": "Hospital C", "tempo_espera": 60},
    {"hospital": "Hospital D", "tempo_espera": 20},
    {"hospital": "Hospital E", "tempo_espera": 50},
    {"hospital": "Hospital F", "tempo_espera": 25},
]

for i, hospital in enumerate(hospital_data):
    print(f"{i}. {hospital['hospital']} - {hospital['tempo_espera']}")
    
ordenado = sorted(hospital_data, key=lambda x: x["tempo_espera"], reverse=True)

print("-")

for i, hospital in enumerate(ordenado):
    print(f"{i}. {hospital['hospital']} - {hospital['tempo_espera']}")
    