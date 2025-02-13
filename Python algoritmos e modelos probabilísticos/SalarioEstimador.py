import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

df = pd.read_csv('Salary_Data.csv')
df.head()

x = df['YearsExperience'].values
y = df['Salary'].values

X_train, X_test , y_train, y_test = train_test_split(x, y, train_size=0.7)

X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

lr = LinearRegression()
lr.fit(X_train, y_train)

predict_test = lr.predict(X_test)
predict_train = lr.predict(X_train)

anos_experiencia = 15

salario_previsto = lr.predict([[anos_experiencia]])
print(f"Salário previsto para 15 anos de experiência: R$ {salario_previsto[0][0]:,.2f}")

plt.scatter(x,y)
plt.plot(X_test,predict_test,color = 'orange')
plt.plot(X_train,predict_train,color = 'orange')
plt.xlabel('Anos de Experiencia')
plt.ylabel('Salario')
plt.show()

