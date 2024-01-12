import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# gerando uma massa de dados:
x, y = make_regression(n_samples=200, n_features=1, noise=30)

# criação do modelo:
modelo = LinearRegression()

# treinando o modelo:
modelo.fit(x, y)

# mostrando o gráfico:
plt.scatter(x, y)
plt.plot(x, modelo.predict(x), color='red', linewidth=3)
plt.show()