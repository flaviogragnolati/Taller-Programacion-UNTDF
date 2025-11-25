# 🧾 Resumen práctico de la notación `[]`, `.loc` y `.iloc` en **pandas**

> Guía rápida (con ejemplos) para usar los corchetes `[]`, `.loc` y `.iloc` en **DataFrames** y **Series**: selección de columnas, filtrado de filas, *groupby*, asignaciones y patrones seguros.

---

## 1) Idea general

En pandas, `[]` sirve para **dos cosas principales**:

1) **Seleccionar columnas**  
- `df["col"]` → `Series`  
- `df[["col1","col2"]]` → `DataFrame`

2) **Filtrar filas con una máscara booleana**  
- `df[df["col"] > 0]` → `DataFrame` con las filas que cumplen

> Nota: Para *indexado por etiquetas/posiciones* es preferible **`.loc`** / **`.iloc`**. La notación `[]` es más concisa, ideal para selección de columnas y filtros simples.

---

## 2) Dataset de ejemplo

```python
import pandas as pd

df = pd.DataFrame({
    "cliente": ["A", "B", "A", "C", "B", "A"],
    "segmento": ["retail", "retail", "corporativo", "retail", "corporativo", "retail"],
    "ventas": [1200, 800, 3000, 450, 2100, 700],
    "unidades": [10, 7, 25, 4, 18, 6],
    "fecha": pd.to_datetime(["2025-01-01","2025-01-02","2025-01-05","2025-01-05","2025-01-09","2025-01-10"])
})
```

---

## 3) Selección de **columnas** con `[]`

### 3.1 Una columna → `Series`
```python
df["ventas"]
```

### 3.2 Varias columnas → `DataFrame`
```python
df[["cliente", "ventas", "unidades"]]
```

### 3.3 Seleccionar columnas por lista dinámica
```python
cols = ["cliente", "segmento"]
df[cols]
```

> Buen patrón: preparar `cols` antes y luego pasar la lista a `[]`.

---

## 4) **Filtrado de filas** con `[]` (máscara booleana)

### 4.1 Condición simple
```python
df[df["ventas"] > 1000]
```

### 4.2 Varias condiciones (usar `&` / `|` y paréntesis)
```python
df[(df["ventas"] > 1000) & (df["segmento"] == "retail")]
```

### 4.3 pertenencia con `.isin`
```python
df[df["cliente"].isin(["A", "C"])]
```

### 4.4 texto con `.str`
```python
df[df["segmento"].str.contains("ret", case=False)]
```

### 4.5 fechas con `.dt`
```python
df[df["fecha"].dt.day >= 5]
```

---

## 5) **Slicing** con `[]` (filas por rango posicional)

> Aunque funciona, para posiciones explícitas se recomienda `.iloc`.

```python
df[1:4]      # filas 1,2,3
df[:3]       # primeras 3
df[-2:]      # últimas 2
```

---

## 6) **Asignación** y `SettingWithCopy`

- Con `[]` puedes **crear columnas**:
```python
df["precio_promedio"] = df["ventas"] / df["unidades"]
```

- Para **asignaciones condicionadas**, utiliza máscara y **`.loc`** para evitar *SettingWithCopyWarning*:
```python
mask = df["segmento"] == "retail"
df.loc[mask, "bonificacion"] = 0.05
```

> Regla de oro: si filtras filas y luego asignas, usa `df.loc[mask, "col"] = ...` (no `df[mask]["col"] = ...`).

---

## 7) `groupby` + `[]`: seleccionar columnas para agregación

`[]` es muy útil para **elegir qué columnas agregás** después del `groupby`:

### 7.1 Agregación simple sobre una columna
```python
df.groupby("cliente")["ventas"].sum()
```

### 7.2 Agregar **varias columnas** de una vez
```python
df.groupby("cliente")[["ventas","unidades"]].sum()
```

### 7.3 Agregaciones múltiples por columna (con `agg`)
```python
df.groupby("segmento")["ventas"].agg(["sum", "mean", "max"])
```

### 7.4 Agregaciones diferentes por columna
```python
df.groupby("cliente")[["ventas","unidades"]].agg({"ventas":"sum", "unidades":"mean"})
```

---

## 8) Patrones comunes con `[]`

### 8.1 *Columns-first* (columna, luego operación)
```python
# media de ventas para clientes A/C
df[df["cliente"].isin(["A","C"])]["ventas"].mean()

# top-3 ventas de segmento retail
df[df["segmento"]=="retail"]["ventas"].nlargest(3)
```

### 8.2 Seleccionar columnas tras filtrar filas
```python
df[df["ventas"] > 1000][["cliente","ventas","segmento"]]
```

### 8.3 Filtrar y ordenar (ordenar no usa `[]`, pero combina bien)
```python
df[df["ventas"] > 1000][["cliente","ventas"]].sort_values("ventas", ascending=False)
```

---

## 9) Trucos útiles

### 9.1 Filtrar por tipo de dato (y luego `[]`)
```python
num_cols = df.select_dtypes(include="number").columns
df[num_cols].head()
```

### 9.2 Seleccionar columnas por patrón en el nombre
```python
ventas_cols = [c for c in df.columns if "vent" in c]
df[ventas_cols]
```

### 9.3 Evitar cadenas largas con `query`/`eval` (alternativa a `[]`)
```python
# Alternativa legible al filtro con operadores
df.query("ventas > 1000 and segmento == 'retail'")[["cliente","ventas"]]
```

---

## 10) Anti-patrones a evitar con `[]`

- ❌ `df[mask]["col"] = valor` → puede disparar **SettingWithCopyWarning**  
  ✅ `df.loc[mask, "col"] = valor`

- ❌ `df["col"]` cuando esperás **DataFrame** (y luego falla una operación esperada)  
  ✅ `df[["col"]]` si necesitás DataFrame

- ❌ Cadenas muy largas de `[]` que dificultan leer  
  ✅ Romper en pasos intermedios (variables `mask`, `cols`)

---

## 11) Mini-recetario

```python
# 1) Columnas
df["col"]                      # Series
df[["c1","c2"]]                # DataFrame

# 2) Filtros
df[df["ventas"] > 1000]
df[df["cliente"].isin(["A","B"])]
df[df["segmento"].str.startswith("ret")]
df[df["fecha"].dt.month == 1]

# 3) Slice de filas
df[:5]; df[-3:]

# 4) Nueva columna y asignaciones seguras
df["ratio"] = df["ventas"] / df["unidades"]
mask = df["segmento"].eq("corporativo")
df.loc[mask, "tag"] = "corp"

# 5) groupby + [] (selección de columnas)
df.groupby("cliente")["ventas"].sum()
df.groupby("cliente")[["ventas","unidades"]].agg({"ventas":"sum","unidades":"mean"})

# 6) Seleccionar columnas por dtype o patrón
num_cols = df.select_dtypes("number").columns
df[num_cols]

cols = [c for c in df.columns if c.endswith("s")]
df[cols]
```

---

## 12) Cuándo preferir `.loc` / `.iloc`

- **`.loc[filas, columnas]`**: por **etiquetas**.  
  Ej.: `df.loc[df["ventas"]>1000, ["cliente","ventas"]]`

- **`.iloc[filas, columnas]`**: por **posiciones**.  
  Ej.: `df.iloc[:3, [0,2]]`

Usá `[]` para lo **rápido y legible** (columnas/filtros simples); `loc/iloc` para **precisión** y **asignaciones seguras**.

---

## 13) Ejemplo integrador

**Objetivo**: para ventas de **segmento retail** en enero 2025, calcular ventas totales y unidades promedio por cliente, quedarnos con el *top 2*.

```python
mask = (df["segmento"].eq("retail")) & (df["fecha"].dt.month.eq(1))
cols = ["cliente", "ventas", "unidades"]

res = (
    df[mask][cols]                                  # 1) filtro con [] + selección de columnas
      .groupby("cliente")[["ventas","unidades"]]    # 2) groupby + [] para columnas a agregar
      .agg({"ventas":"sum", "unidades":"mean"})     # 3) agregaciones distintas
      .sort_values("ventas", ascending=False)       # 4) ordenar
      .head(2)                                      # 5) top 2
)
print(res)
```

---

## 14) Reglas rápidas (cheatsheet)

- `df["col"]` → Series | `df[["c1","c2"]]` → DataFrame  
- `df[mask]` filtra **filas** con máscara booleana  
- **Asignaciones** después de filtrar → `df.loc[mask, "col"] = ...`  
- `groupby(...)[cols].agg(...)` para elegir columnas a agregar  
- Para **etiquetas/posiciones** exactas → preferir `.loc` / `.iloc`

---

## 15) Indexado explícito con `.loc` y `.iloc`

> Reglas rápidas:
- **`.loc[filas, columnas]`** → **por etiqueta** (index/column names). Los **slices por etiqueta son inclusivos** en el tope.
- **`.iloc[filas, columnas]`** → **por posición entera** (0..n-1). Los **slices por posición son exclusivos** en el tope, como en Python.

### 15.1 Selección básica

```python
# Por etiqueta (loc)
df.loc[0, "ventas"]                # celda (fila con etiqueta 0, col 'ventas')
df.loc[0:2, ["cliente", "ventas"]] # filas 0..2 (INCLUYE 2), 2 columnas

# Por posición (iloc)
df.iloc[0, 2]          # celda (fila 0, col 2)
df.iloc[0:3, [0, 2]]   # filas 0..2 (EXCLUYE 3), columnas por índice [0,2]
```

### 15.2 Máscaras booleanas (muy común)

```python
mask = (df["segmento"] == "retail") & (df["ventas"] > 1000)

# Filtrar y elegir columnas (loc)
df.loc[mask, ["cliente", "ventas", "segmento"]]

# Asignaciones seguras (evita SettingWithCopy)
df.loc[mask, "bonificacion"] = 0.05

# Con iloc (menos común para máscaras; se usa cuando ya tenés posiciones)
pos = (df["ventas"] > 1000).to_numpy().nonzero()[0]
df.iloc[pos, df.columns.get_indexer(["cliente", "ventas"])]
```

### 15.3 Slices por **etiqueta** vs **posición**

```python
# Si el índice es de fechas o etiquetas no numéricas, loc brilla:
df = df.set_index("fecha").sort_index()

# Rango por FECHAS (loc incluye el final)
df.loc["2025-01-02":"2025-01-09", ["cliente", "ventas"]]

# El mismo rango por POSICIONES (iloc, exclusivo en tope)
df.iloc[1:5, [df.columns.get_loc("cliente"), df.columns.get_loc("ventas")]]
```

### 15.4 Listas de etiquetas/posiciones y orden arbitrario

```python
# loc con etiquetas de fila y columna específicas
filas = [pd.Timestamp("2025-01-10"), pd.Timestamp("2025-01-01")]
cols  = ["cliente", "unidades"]
df.loc[filas, cols]

# iloc con posiciones (el orden lo definís vos)
df.iloc[[5, 0], [0, 3]]  # filas 5 y 0, columnas 0 y 3
```

### 15.5 Selecciones condicionales por columnas múltiples

```python
# Quedarnos con filas retail y devolver 2 columnas
df.loc[df["segmento"].eq("retail"), ["cliente", "ventas"]]

# Múltiples condiciones: agrupar SIEMPRE con paréntesis
df.loc[(df["ventas"] > 1000) & (df["unidades"] >= 6), ["cliente", "ventas", "unidades"]]
```

### 15.6 Asignaciones vectorizadas y rellenos

```python
# Nueva columna con operación vectorizada
df.loc[:, "precio_promedio"] = df["ventas"] / df["unidades"]

# Asignación condicional a varias columnas
mask = df["cliente"].eq("A")
df.loc[mask, ["segmento", "unidades"]] = ["preferente", 99]

# Rellenar valores faltantes por selección
faltantes = df["unidades"].isna()
df.loc[faltantes, "unidades"] = df.loc[faltantes, "unidades"].fillna(0)
```

### 15.7 Ordenar + seleccionar (patrón limpio)

```python
top = (
    df.sort_values(["segmento", "ventas"], ascending=[True, False])
      .loc[:, ["segmento", "cliente", "ventas"]]
      .groupby("segmento")
      .head(3)
)
```

### 15.8 `.loc` con **MultiIndex** (intro)

```python
# Supongamos índice jerárquico (segmento, cliente)
df2 = df.set_index(["segmento", "cliente"]).sort_index()

# Selección por primer nivel
df2.loc["retail"]

# Selección por tupla de niveles
df2.loc[("retail", "A"), "ventas"]

# Rango por etiqueta en primer nivel (incluye extremos)
df2.loc["corporativo":"retail", ["ventas", "unidades"]]
```

### 15.9 `.iloc` con pasos y negativos (técnicas posicionales)

```python
# Cada 2 filas de las primeras 6 y columnas 0..2
df.iloc[0:6:2, 0:3]

# Últimas 3 filas y últimas 2 columnas
df.iloc[-3:, -2:]
```

### 15.10 Selección condicional por **fila** completa o **columna** completa

```python
# Fila completa por etiqueta/posición
df.loc["2025-01-05"]         # requiere tener índice de fechas
df.iloc[3]                    # cuarta fila completa

# Columna completa por etiqueta/posición
df.loc[:, "ventas"]
df.iloc[:, 2]
```

### 15.11 Comparativa rápida

| Tarea | `[]` | `.loc` | `.iloc` |
|---|---|---|---|
| Seleccionar **1 columna** | `df["c"]` | `df.loc[:, "c"]` | `df.iloc[:, idx]` |
| Seleccionar **N columnas** | `df[["c1","c2"]]` | `df.loc[:, ["c1","c2"]]` | `df.iloc[:, [i1,i2]]` |
| Filtrar **filas** | `df[mask]` | `df.loc[mask, :]` | `df.iloc[posiciones, :]` |
| Asignar condicional | ⚠️ (no recomendado) | ✅ `df.loc[mask,"c"]=...` | ✅ si conocés posiciones |
| Rango por **etiqueta** | — | ✅ inclusivo | — |
| Rango por **posición** | ✅ `df[i:j]` (solo filas) | — | ✅ exclusivo (clásico Python) |

> Recomendación:  
> - Usa `[]` para selección rápida de columnas o filtros simples.  
> - Usa **`.loc`** para máscaras, etiquetas, asignaciones seguras y trabajo con índices (fechas, MultiIndex).  
> - Usa **`.iloc`** para posiciones puras, *slicing* posicional y manipulación por índices numéricos.

---

## 16) Recetas prácticas con `.loc` / `.iloc`

### 16.1 “Filtro por mes y top-n por cliente”

```python
# Índice por fecha para aprovechar loc por rango
dfi = df.set_index("fecha").sort_index()
enero = dfi.loc("2025-01-01":"2025-01-31")  # alternativa: dfi.loc["2025-01-01":"2025-01-31"]

mask = enero["segmento"].eq("retail")
cols = ["cliente", "ventas", "unidades"]

res = (
    enero.loc[mask, cols]
         .groupby("cliente")[["ventas", "unidades"]]
         .agg({"ventas": "sum", "unidades": "mean"})
         .sort_values("ventas", ascending=False)
         .head(3)
)
```

### 16.2 “Asignar etiquetas por cuantiles” (posicional + loc)

```python
# Ordenar por ventas y cortar por posiciones
ordered = df.sort_values("ventas", ascending=False).reset_index(drop=True)
n = len(ordered)
top_cut = int(n * 0.2)

ordered.loc[:top_cut-1, "tier"] = "TOP"
ordered.loc[top_cut:, "tier"]   = "REST"

# Selección equivalente con iloc para ver subconjuntos
top_view  = ordered.iloc[:top_cut, :]
rest_view = ordered.iloc[top_cut:, :]
```

### 16.3 “Seleccionar columnas por patrón y asignar” (loc)

```python
metric_cols = [c for c in df.columns if c in ("ventas","unidades")]
df.loc[:, metric_cols] = df.loc[:, metric_cols].fillna(0).clip(lower=0)
```

### 16.4 “Ventanas posicionales móviles” (iloc + rolling manual)

```python
# Media de ventas en ventanas de 3 filas, saltando 1
means = []
for i in range(0, len(df)-2, 1):
    window = df.iloc[i:i+3, df.columns.get_loc("ventas")]
    means.append(window.mean())
```

---

## 17) Errores comunes y cómo evitarlos

- **SettingWithCopyWarning**:  
  ❌ `df[df["ventas"]>1000]["segmento"] = "alto"`  
  ✅ `df.loc[df["ventas"]>1000, "segmento"] = "alto"`

- **Confundir inclusividad de slices**:  
  - `df.loc["a":"c"]` incluye **"c"**  
  - `df.iloc[0:3]` excluye el **3**

- **Índices no únicos**:  
  Con `.loc` por etiqueta, múltiples filas pueden coincidir. Verificá `df.index.is_unique` o reseteá índice: `df.reset_index(drop=True)`.

- **Mezclar posiciones con etiquetas**:  
  `.loc` no acepta posiciones puras (salvo que tu índice *se llame* 0..n-1). Para posiciones → `.iloc`.

---

## 18) Mini-cheatsheet `.loc` / `.iloc`

```python
# loc: por etiqueta
df.loc[mask, ["c1","c2"]]                  # filtra filas por máscara y selecciona columnas
df.loc["2025-01-01":"2025-01-31", :]       # rango por etiqueta (incluye el final)
df.loc[:, "ventas"]                        # columna por etiqueta
df.loc[("retail","A"), "ventas"]           # MultiIndex por tupla

# iloc: por posición
df.iloc[0:5, [0,2]]                        # primeras 5 filas, columnas 0 y 2
df.iloc[-3:, -2:]                          # últimas 3 filas, últimas 2 columnas
df.iloc[::2, :]                            # filas con paso 2
```
