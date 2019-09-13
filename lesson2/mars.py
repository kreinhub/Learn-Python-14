import ephem


mars = ephem.Mars('2000/01/01')
const = ephem.constellation(mars)

print(const)