import ephem


# mars = ephem.Mars('2000/01/01')
# const = ephem.constellation(mars)

date = "'2019-09-15'"
planet_name = "Mars"
cmd = f"ephem.{planet_name}({date})"
#print(cmd)
result = eval(cmd)
print(result)

#print(const)