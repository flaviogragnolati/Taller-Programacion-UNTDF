# 🛠️ Guía de instalación del entorno de programación (Windows, Ubuntu/WSL)  

> Objetivo: dejar todo listo para trabajar en el taller con **Python + Jupyter Notebooks**, control de versiones con **Git/GitHub**, y (opcional) **VS Code** como editor.  
> Se ofrecen dos caminos en Windows (Anaconda o binarios) y uno para Ubuntu/WSL.

---

## 0) Crear cuenta en GitHub (requisito para el taller)

1. Ir a **[github.com/signup](https://github.com/signup)** y completar el registro.  
2. Verificar el email (sin verificación algunas funciones no estarán disponibles).

---

## 1) Configurar credenciales de Git (común a todos los métodos)

> Podés autenticarte por **HTTPS** (más simple) o **SSH** (recomendado a mediano plazo).

### 1.1 HTTPS (rápido)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
git config --global credential.helper store
```

### 1.2 SSH (recomendado)
1. Generar clave:
   - **Windows (PowerShell)**:
     ```powershell
     ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"
     Start-Process "$env:USERPROFILE\.ssh"
     ```
   - **Linux/WSL**:
     ```bash
     ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"
     cat ~/.ssh/id_ed25519.pub
     ```
2. Copiar la clave pública y **agregarla en GitHub**: *Settings → SSH and GPG keys → New SSH key*.  
3. Probar conexión:
   ```bash
   ssh -T [email protected]
   ```

---

## 2) Windows — Método A: **Anaconda** (recomendado para principiantes)

### 2.1 Instalar Anaconda (incluye Jupyter Notebook)
1. Descargar **Anaconda Distribution** para Windows desde la [página oficial](https://www.anaconda.com/products/distribution).  
2. Ejecutar el instalador (dejar las opciones por defecto).  
3. Abrir **Anaconda Navigator** y lanzar **Jupyter Notebook**.

### 2.2 Instalar **Git for Windows** (incluye Git Bash)
1. Descargar e instalar desde [gitforwindows.org](https://gitforwindows.org).  
2. Abrir **Git Bash** y ejecutar la sección anterior.

### 2.3 (Opcional) Instalar **Windows Terminal**
- Descargar desde [Microsoft Store](https://aka.ms/terminal).

### 2.4 Probar el entorno
```python
import sys, numpy as np, pandas as pd
print(sys.version)
print(np.__version__, pd.__version__)
```

---

## 3) Windows — Método B: **Binarios + VS Code**

### 3.1 Instalar **Python**
- Descargar desde [python.org/downloads](https://www.python.org/downloads/).
- Tildar “**Add python.exe to PATH**”.
- Verificar:
  ```powershell
  python --version
  pip --version
  ```

### 3.2 Instalar **Windows Terminal**
- Instalar desde [Microsoft Store](https://aka.ms/terminal).

### 3.3 Instalar **Git for Windows**
- Descargar desde [gitforwindows.org](https://gitforwindows.org).

### 3.4 Instalar **Visual Studio Code**
- Descargar desde [code.visualstudio.com](https://code.visualstudio.com/).

### 3.5 Instalar extensiones
- Python (Microsoft)
- Jupyter (Microsoft)

### 3.6 Probar Jupyter
```python
import math
math.factorial(5)
```

---

## 4) Ubuntu/WSL — Instalación base

### 4.1 (Windows) Instalar WSL + Ubuntu
```powershell
wsl --install
```

### 4.2 VS Code integrado
- Instalar extensión **Remote - WSL** en VS Code.

---

## 5) Instalar **uv** y Python

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install --default
uv venv .venv
source .venv/bin/activate
python -V
```

(Alternativa con APT)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

---

## 6) Instalar **VS Code + Jupyter**

- En VS Code, instalar extensiones:
  - Python (Microsoft)
  - Jupyter (Microsoft)

---

## 7) Probar Jupyter Notebook
```bash
python -m pip install --upgrade pip
python -m pip install jupyter numpy pandas matplotlib
jupyter notebook
```

```python
import sys, numpy as np, pandas as pd, matplotlib
print(sys.version)
print(np.__version__, pd.__version__, matplotlib.__version__)
```

---

## 8) Buenas prácticas
- Commits frecuentes.
- Usar entornos virtuales.
- Extensiones necesarias únicamente.

---

## ✅ Checklist final

- [ ] `git --version`
- [ ] `python --version`
- [ ] `jupyter notebook` abre correctamente.
- [ ] Puedo clonar y hacer push a GitHub.
