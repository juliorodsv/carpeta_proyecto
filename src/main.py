import sys
import time
import os

def main():
    print("¡Hola! El script principal está funcionando correctamente. 🚀")
    print("-" * 50)

    # Medición de tiempo de ejecución (ideal para procesos de datos o scripts de respaldo)
    tiempo_inicio = time.time()

    # Muestra la ruta exacta del intérprete de Python
    print(f"Ruta del intérprete actual: {sys.executable}")

    # Comprobación del entorno virtual
    if "venv" in sys.executable:
        print("✅ ¡Excelente! Estás ejecutando el script usando tu entorno virtual (venv).")
    else:
        print("⚠️ Atención: Estás usando el Python global del sistema, no el venv.")

    print("-" * 50)
    print(f"Directorio de trabajo actual: {os.getcwd()}")

    tiempo_fin = time.time()
    print(f"⏱️ Tiempo de ejecución del script: {tiempo_fin - tiempo_inicio:.4f} segundos.")

if __name__ == "__main__":
    main()
