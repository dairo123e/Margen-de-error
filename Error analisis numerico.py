import numpy as np

def calcular_errores():
    
    n = int(input("Ingrese la cantidad de datos a procesar: "))
    
    
    valor_verdadero = float(input("Ingrese el valor verdadero: "))
    
    
    datos = []
    
    
    for i in range(n):
        valor = float(input(f"Ingrese el dato {i+1}: "))
        datos.append(valor)
    
    
    datos = np.array(datos)
    
    
    valor_medio = np.mean(datos)
    
    
    errores_porcentuales = np.abs((datos - valor_verdadero) / valor_verdadero * 100)
    
    
    error_medio_porcentual = np.abs((valor_medio - valor_verdadero) / valor_verdadero * 100)
    
    
    print("\nResultados:")
    print("-" * 50)
    print(f"Valor verdadero: {valor_verdadero}")
    print(f"Valor promedio: {valor_medio}")
    print("\nErrores para cada medición:")
    
    for i, (dato, error) in enumerate(zip(datos, errores_porcentuales), 1):
        print(f"Dato {i}: {dato} - Porcentaje del margen de error: {error:.4f}%")
    
    print(f"\nPorcentaje del margen de error del valor promedio: {error_medio_porcentual:.4f}%")
    
    
    diferencias_absolutas = np.abs(datos - valor_verdadero)
    diferencia_media_absoluta = np.abs(valor_medio - valor_verdadero)
    
    print("\nValores absolutos de las diferencias:")
    for i, dif in enumerate(diferencias_absolutas, 1):
        print(f"Dato {i}: {dif:.4f}")
    
    print(f"Diferencia absoluta del valor promedio: {diferencia_media_absoluta:.4f}")

if __name__ == "__main__":
    print("Programa para calcular márgenes de error")
    print("-" * 50)
    calcular_errores()