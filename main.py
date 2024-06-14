#Modelo de Cadena de Markov para predecir el clima

# Importamos la librería numpy para generar números aleatorios
import numpy as np
import matplotlib.pyplot as plt
import time

# Definimos la matriz de transición o de probabilidad de transición
matriz_transicion = { #La cadena de Markov cuenta con dos estados: Soleado y Nublado
    "Soleado ☀": {"Soleado ☀": 0.9, "Nublado ☁": 0.1}, 
    "Nublado ☁": {"Soleado ☀": 0.2, "Nublado ☁": 0.8},
}
# Definimos el nombre de los estados de la cadena de Markov para el clima
nombre_transicion:list[str] = ["Soleado ☀", "Nublado ☁"]

# Graficas de la cantidad de dias soleados y nublados
def Graph(dias: list[str]) -> None: 
  #Contamos la cantidad de dias soleados y nublados
  dias_soleados = dias.count("Soleado ☀")
  dias_nublados = dias.count("Nublado ☁")
  #Graficamos la cantidad de dias soleados y nublados
  fig, ax = plt.subplots()
  ax.bar(["Soleado ☀", "Nublado ☁"], [dias_soleados, dias_nublados], color=['#FFD700', '#A9A9A9'])
  ax.set_ylabel('Cantidad de días')
  ax.set_title('Días soleados y nublados')
  plt.show()
   


def Markov(dias: int) -> list[str]:
    # Inicializamos el estado actual y la lista de climas 
    clima_actual:str = nombre_transicion[np.random.choice(len(nombre_transicion))] #Elegimos que el clima sea aleatorio
    # clima_actual:str = nombre_transicion[0] #Elegimos que el clima sea Soleado
    # clima_actual:str = nombre_transicion[1] #Elegimos que el clima sea Nublado

    # Lista con el resultado de la prediccion de los climas
    lista_climas:list[str] = [clima_actual]
    
    # Hacemos un ciclo para predecir el clima de los próximos días
    for dia in range(dias - 1):  # Restamos 1 porque el primer día ya lo tenemos 
        # Determinamos el clima del día siguiente basado en la probabilidad de transición de la matriz 
        prediccion:str = np.random.choice(nombre_transicion, p=[matriz_transicion[clima_actual].get(state, 0) for state in nombre_transicion])
        # Actualizamos el estado actual y agregamos el clima a la lista
        clima_actual = prediccion
        lista_climas.append(clima_actual)

    # Se retorna una lista con la prediccion de los climas y la cantidad de dias soleados y nublados
    return lista_climas

def main() -> None: #Función principal
  try:
    # Definimos el número de días a predecir
    dias_simulacion:int = int(input("\n¿Cuántos días quieres predecir el clima?: "))
    # Predecimos el clima de los próximos días
    climas = Markov(dias_simulacion)
    # Imprimimos la lista de climas
    print(f"\n>>> Después de {dias_simulacion} días, el clima estará: {climas[-1]}")
    print("\n{:<8} {:<15}".format("Día", "Clima"))
    print("-" * 20)
    for dia, clima in enumerate(climas):
      time.sleep(0.015)
      print("{:<8} {:<15}".format(dia + 1, clima))
    #Graficamos la cantidad de dias soleados y nublados
    Graph(climas)
    
  
  except ValueError:
    print("\nPor favor, introduce un número válido.")
    main()
  except Exception as e:
    print(f"\nOcurrió un error: {e}")
    main()
 
if __name__ == '__main__':
  main()