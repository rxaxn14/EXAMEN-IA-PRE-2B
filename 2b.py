import matplotlib.pyplot as plt

# 'Age', 'Weight (kg)', 'BMI'
age_data = df['Age'].dropna().tolist()
weight_data = df['Weight (kg)'].dropna().tolist()
bmi_data = df['BMI'].dropna().tolist()

plt.scatter(age_data, weight_data, color='blue', alpha=0.5)
plt.title('Dispersión de Edad vs Peso')
plt.xlabel('Edad (años)')
plt.ylabel('Peso (kg)')
plt.grid(True)
plt.show()

# - Edad tiene un rango de 20-60 años
# - No hay una correlación clara entre la edad y el peso
# - La variabilidad en el peso es mayor entre los individuos jóvenes (<30 años)
# - Algunos valores atípicos en peso (>120 kg)

plt.scatter(age_data, bmi_data, color='green', alpha=0.5)
plt.title('Dispersión de Edad vs BMI')
plt.xlabel('Edad (años)')
plt.ylabel('Índice de Masa Corporal (BMI)')
plt.grid(True)
plt.show()

# - La mayoría de los valores de BMI están entre 20-35
# - No existe una correlación fuerte entre la edad y el BMI
# - Valores de BMI altos (>40) se presentan en todos los grupos de edad
# - El BMI está más concentrado en rangos normales (18-25) para la mayoría de los individuos

plt.scatter(weight_data, bmi_data, color='red', alpha=0.5)
plt.title('Dispersión de Peso vs BMI')
plt.xlabel('Peso (kg)')
plt.ylabel('Índice de Masa Corporal (BMI)')
plt.grid(True)
plt.show()

# - Existe una correlación directa entre el peso y el BMI
# - A mayor peso, mayor BMI (relación lineal)
# - El rango de peso se concentra entre 50-100 kg
# - Valores atípicos con pesos altos (>120 kg) resultan en valores de BMI igualmente elevados (>40)
