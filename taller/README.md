# Taller de programación UNTDF 2025

Descripción
-----------
Esta carpeta contiene la configuración mínima y material práctico para ejecutar ejemplos en Python que complementan los apuntes teóricos del curso. Está pensada principalmente para trabajar con notebooks (Jupyter) ubicados en las subcarpetas correspondientes, y también incluye pequeños scripts de ejemplo.

Estado del entorno
------------------
El proyecto fue inicializado con `uv`. `uv` utiliza `venv` internamente para crear un entorno virtual aislado. Si estás viendo este README en la consola, significa que tu entorno Python está correctamente seteado para ejecutar los ejemplos.

Python
------
Este material está orientado a Python 3.14. Se recomienda usar esa versión cuando sea posible para evitar incompatibilidades.

Cómo usar el entorno (breve)
----------------------------
Estas son dos formas habituales de trabajar con el entorno del proyecto. Suponemos que ya tenés `uv` instalado si querés usar la primera opción.

- Usando `uv` (si lo tenés instalado):
	- Crear/actualizar el entorno y ejecutar comandos dentro del mismo: `uv run <comando>`.
	- Por ejemplo, para ejecutar el main desde el entorno: `uv run python main.py`.

- Manualmente con `venv` (alternativa):
	- Crear el entorno virtual: `python3 -m venv .venv`
	- Activarlo: `source .venv/bin/activate`
	- Instalar dependencias (si existen): `python -m pip install -r requirements.txt` o usar `pyproject.toml` según tu flujo.
	- Ejecutar el script o notebook: `python main.py` o abrir los notebooks con Jupyter.

Estructura relevante
--------------------
- `src/datasets/` — contiene datos utilizados en los ejemplos, por ejemplo `indicadores-provinciales.csv`.
- `src/ejemplos/` — notebooks y ejemplos prácticos (por ejemplo `intro pandas.ipynb`).
- `main.py` — script simple que muestra este README cuando se ejecuta.

Notas finales
------------
Los notebooks dentro de `src/ejemplos/` son el lugar recomendado para realizar ejercicios y experimentos; contienen ejemplos más extensos y prácticos que los apuntes teóricos. Si necesitás ayuda con la activación del entorno o con `uv`, decímelo y te doy comandos más específicos según tu sistema.


