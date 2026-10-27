import sys


def main():
  print("¡Hola! El script principal está funcionando correctamente. 🚀")
  print("-" * 50)

  # Muestra la ruta exacta del intérprete de Python que está ejecutando este script
  print(f"Ruta del intérprete actual: {sys.executable}")

  # Una comprobación visual para saber si estás en el venv
  if "venv" in sys.executable:
    print(
        "✅ ¡Excelente! Estás ejecutando el script usando tu entorno virtual"
        " (venv)."
    )
  else:
    print(
        "⚠️ Atención: Estás usando el Python global del sistema, no el venv."
    )

print("Versión del script: 1.1.0 (Entorno de Desarrollo) 🧪")

if __name__ == "__main__":
  main()
