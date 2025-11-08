# Taller de Programación — Temario

> Basado en los roadmaps de Python Developer y Data Analyst de roadmap.sh, con módulos añadidos de setup profesional, IDEs, Git/GitHub y un proyecto integrador aplicado a problemas reales de la carrera.

## Parte I — Camino Python Developer

### Módulo 1: Introducción a la programación
- **Tema 1.1:** ¿Qué es programar y para qué sirve?
- **Tema 1.2:** Paradigmas y tipos de lenguajes (imperativo, OOP, funcional; tipado estático vs. dinámico)
- **Tema 1.3:** El ecosistema Python en ingeniería (automatización, análisis, web, ciencia de datos)

### Módulo 2: Setup profesional del entorno
- **Tema 2.1:** Gestores de versiones y entornos: `pyenv` / `pyenv-win`, conda/mamba, `venv`, uv (entornos ultra-rápidos)
- **Tema 2.2:** Gestores de paquetes y proyectos: `pip`, uv, Poetry; `pyproject.toml` y lockfiles
- **Tema 2.3:** IDEs y productividad: VS Code (extensión Python), PyCharm (CE/Pro), depuración y linters
- **Tema 2.4:** Control de versiones y colaboración: Git básico, flujo con GitHub (repos, ramas, PRs)

### Módulo 3: Fundamentos de Python
- **Tema 3.1:** Sintaxis, variables y tipos de datos
- **Tema 3.2:** Estructuras de control (condicionales, bucles)
- **Tema 3.3:** Funciones, excepciones, módulos y paquetes
- **Tema 3.4:** Estándares de código (PEP 8), formateo y tipado con `typing`
- **Tema 3.5:** Introducción a clases y objetos (conceptos básicos de OOP, atributos, métodos, instancia de clases)
- **Tema 3.6:** Publicación de paquetes y módulos
- **Tema 3.7:** Estructura de carpetas, convenciones y buenas prácticas para organizar el código

### Módulo 4: Estructuras de datos y algoritmos básicos
- **Tema 4.1:** Listas, tuplas, sets, diccionarios
- **Tema 4.2:** Pilas, colas, heaps; nociones de árboles y grafos
- **Tema 4.3:** Funciones de orden superior, iteradores y generadores
- **Tema 4.4:** Recursión, funciones inmeditamente invocadas (IIFE) y currying
- **Tema 4.5:** Algoritmos fundamentales (búsqueda, ordenamiento)
- **Tema 4.6:** Complejidad (Big O) y buenas prácticas de rendimiento

### Módulo 5: Entradas/Salidas y conectividad
- **Tema 5.1:** Archivos (CSV, JSON, Excel) y paths
- **Tema 5.2:** Consumo de APIs (requests), autenticación básica
- **Tema 5.3:** Persistencia con SQLite/PostgreSQL (intro)

### Módulo 6: Calidad, pruebas y depuración
- **Tema 6.1:** Pruebas con `pytest` (fixtures, parametrización, coverage)
- **Tema 6.2:** Debugging en VS Code / PyCharm y logging
- **Tema 6.3:** Integración con GitHub (acciones básicas de CI)

### Módulo 7: Desarrollo web (opcional)
- **Tema 7.1:** Flask / FastAPI (rutas, controladores, validación)
- **Tema 7.2:** Django visión general (ORM, admin, templates)
- **Tema 7.3:** APIs REST para tableros y automatizaciones internas

### Módulo 8: Introducción práctica a ciencia de datos con Python
- **Tema 8.1:** NumPy y Pandas (series, dataframes, joins, groupby)
- **Tema 8.2:** Visualización con Matplotlib/Seaborn

## Parte II — Camino Data Analyst

### Módulo 9: Fundamentos del análisis de datos
- **Tema 9.1:** ¿Qué es Data Analytics?
- **Tema 9.2:** Tipos: descriptivo, diagnóstico, predictivo, prescriptivo
- **Tema 9.3:** Flujo de trabajo: recolección, limpieza, exploración, modelado ligero y comunicación

### Módulo 10: Excel para análisis
- **Tema 10.1:** Funciones clave y buenas prácticas de modelado
- **Tema 10.2:** Tablas dinámicas y gráficos
- **Tema 10.3:** Exportación/consumo desde Python

### Módulo 11: SQL esencial para analistas
- **Tema 11.1:** SELECT/FROM/WHERE, agregaciones y GROUP BY
- **Tema 11.2:** JOINs, subconsultas y CTEs
- **Tema 11.3:** Limpieza y validación (nulos, duplicados)

### Módulo 12: Python para análisis (intermedio)
- **Tema 12.1:** Pandas intermedio (reshape, ventanas, series de tiempo)
- **Tema 12.2:** Visualización y storytelling
- **Tema 12.3:** Introducción a estadística para decisiones (EDA, regresión lineal simple)

### Módulo 13: Recolección y gestión de datos
- **Tema 13.1:** Fuentes: bases de datos, CSV/Excel, APIs, scraping
- **Tema 13.2:** Limpieza avanzada (faltantes, duplicados, outliers)
- **Tema 13.3:** Versionado de datasets y notebooks; estructura de proyectos

### Módulo 14: Visualización y comunicación de insights
- **Tema 14.1:** Principios de visualización
- **Tema 14.2:** Herramientas BI (panorama: Power BI / Tableau)
- **Tema 14.3:** Dashboards y reportes ejecutivos; métricas y KPIs

## Parte III — Proyecto integrador (problema real)

### Módulo 15: Aplicación práctica guiada
- **Tema 15.1:** Definición del caso (traído por estudiantes o propuesto por la cátedra: producción, logística, costos, calidad, mantenimiento)
- **Tema 15.2:** Diseño de la solución: backlog, criterios de aceptación, plan de datos
- **Tema 15.3:** Implementación incremental (Git/GitHub):
  - Setup del repo, ramas e issues
  - Ingesta y limpieza (Pandas/SQL)
  - Análisis y visualización (Excel/Matplotlib/Seaborn)
  - Entrega técnica (`notebook`/script + `README`) y entrega ejecutiva (informe 1–3 páginas)
- **Tema 15.4:** Retro y mejora continua (code review, métricas de calidad, siguientes pasos)

## Referencias (consultada / sugerida)

- Roadmap.sh — Python Developer y PDF asociado.
- Roadmap.sh — Data Analyst y PDF asociado.


## Recursos adicionales
//TODO


# 🧩 Guía para Contribuir al Repositorio del Taller Python

El objetivo es mantener un entorno colaborativo, ordenado y didáctico, fomentando el aporte de la comunidad.

---

## 🧱 Tipos de Contribuciones

Existen **dos tipos principales** de aportes:

---

### 1️⃣ Contribuciones Complementarias

Incluyen aportes que **amplían o complementan** el contenido original del taller:

- Ejercicios adicionales o variantes de los existentes
- Nuevos temas o subtemas
- Ejemplos mejorados o aplicados a casos reales
- Aplicaciones prácticas específicas
- Implementaciones o módulos de código complementarios

📂 **Ubicación:**

```
contribuciones/
  ├── modulo_1/
  ├── modulo_2/
  ├── modulo_3/
  ├── modulo_4/
  ├── modulo_5/
  └── ejercicios_integradores/
```

📘 **Formato recomendado:**

- Preferentemente un único archivo `.md` con:
  - Breve introducción teórica
  - Explicación paso a paso
  - Bloques de código comentados
  - Resultados esperados o salida del programa
- Si el aporte requiere código Python más extenso o modular:
  - Crear una carpeta con nombre descriptivo (`modelo_lineal/`, `clasificacion_ml/`, etc.)
  - Incluir dentro:
    ```
    ├── README.md
    ├── main.py
    ├── utils.py (opcional)
    └── pyproject.toml / requirements.txt
    ```
  - El archivo `README.md` debe contener:
    - Descripción teórica y objetivo
    - Ejemplo de uso
    - Dependencias y método de instalación
    - Notas o recomendaciones

Ejemplo mínimo:

```markdown
# Ejemplo de Optimización Numérica

Este módulo muestra cómo resolver un sistema de ecuaciones lineales mediante `numpy.linalg`.

## Uso
```bash
python main.py
```

## Dependencias
- numpy

Instalación:
```bash
pip install -r requirements.txt
```


---

### 2️⃣ Correcciones, Actualizaciones o Mejoras de los Apuntes

Estas contribuciones modifican los **apuntes principales** del taller.
Pueden ser:

- Corrección de errores tipográficos o de código
- Mejoras de redacción o formato
- Actualización de ejemplos o librerías
- Inclusión de nuevos recursos o enlaces

📘 **Procedimiento:**

1. Hacer un *fork* del repositorio
2. Crear una rama descriptiva, por ejemplo:
   ```
   fix/modulo3-condicionales
   update/modulo5-optimizacion
   enhance/modulo4-grafos
   ```
3. Realizar los cambios necesarios
4. Enviar un **Pull Request (PR)**, usando la plantilla correspondiente:
   - `mejoras_apuntes.md`
   - `correccion_errores.md`
   - `contribucion_complementaria.md`
5. Asegurarse de incluir una descripción clara, motivación y pruebas del cambio.

---

## 🧾 Plantillas de Pull Request

Las plantillas se encuentran en la carpeta:

```
.github/PULL_REQUEST_TEMPLATE/
```

Cada una corresponde a un tipo distinto de contribución (ver ejemplos en esa carpeta).

---

## 🧰 Buenas Prácticas Generales

- Nombrar archivos y carpetas en **minúsculas** y con guiones bajos.
- Respetar el formato Markdown y los títulos existentes.
- Código en Python siguiendo **PEP8**.
- Incluir un `requirements.txt` o `pyproject.toml` si hay dependencias.
- Verificar ejecución con **Python ≥ 3.10**.
- Preferir dependencias estándar o ampliamente disponibles.
- No incluir datos binarios, pesados o con licencias no libres.

---

## 🧩 En resumen

| Tipo de Contribución | Ubicación | Forma | Requiere PR |
|-----------------------|------------|--------|--------------|
| Ejercicio o ejemplo complementario | `/contribuciones/modulo_X/` o `/contribuciones/ejercicios_integradores/` | `.md` o carpeta con código y README | ✅ |
| Corrección o mejora de apuntes | `/modulo_X/tema_X.X_...md` | Edición directa + PR | ✅ |

---

**💡 Tu aporte ayuda a mejorar el Taller Python.**
Cada contribución amplía las oportunidades de aprendizaje de toda la comunidad.
¡Gracias por participar! 🐍

