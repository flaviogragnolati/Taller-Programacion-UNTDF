# 🌱 Guía básica de Git y GitHub para estudiantes

> Esta guía explica las **operaciones esenciales de Git y GitHub**, pensada para quienes recién comienzan a programar o a trabajar en proyectos colaborativos.
> El objetivo es **usar Git como herramienta básica de organización y respaldo**, no dominarlo en profundidad.

---

## 🧩 ¿Qué es Git y qué es GitHub?

- **Git** es un sistema de control de versiones: permite guardar cambios en tu código y volver atrás si algo sale mal.
- **GitHub** es una plataforma en línea que usa Git para compartir, colaborar y almacenar proyectos.

Podés pensar en Git como el “historial de versiones” de tu proyecto, y en GitHub como la “nube” donde ese historial vive y se comparte.

---

## 🍴 1. Forkear un repositorio

**Forkear** significa hacer una copia de un repositorio (proyecto) que está en GitHub hacia tu propia cuenta.
Te permite **experimentar y trabajar libremente** sin afectar el proyecto original.

**Pasos:**
1. Entra al repositorio que querés copiar (por ejemplo, el del taller).
2. Clic en el botón **“Fork”** (arriba a la derecha).
3. Elegí tu cuenta personal.
4. GitHub creará una copia idéntica en tu perfil.

Ahora tenés tu propia versión del proyecto, donde podés hacer cambios.

---

## 💾 2. Commit

Un **commit** es como sacar una “foto” del estado actual de tu trabajo.
Cada vez que terminás algo importante (por ejemplo, arreglar un error o agregar una función), hacés un commit.

**Comandos:**
```bash
git add .
git commit -m "Descripción corta del cambio"
```

- `git add .` prepara los archivos para ser guardados.
- `git commit -m "mensaje"` guarda los cambios en tu historial local.

💡 *Tip:* el mensaje del commit debe ser breve y claro:
Ejemplo: `"Agrego función para calcular promedio"` o `"Corrijo error en carga de datos"`.

---

## 🔁 3. Pull y Push

Estos comandos sirven para **sincronizar tu trabajo** entre tu computadora (local) y GitHub (remoto):

- **Push**: sube tus commits a GitHub.
- **Pull**: descarga los cambios más recientes del repositorio remoto.

**Comandos:**
```bash
git push origin main      # sube tus cambios a GitHub
git pull origin main      # trae los cambios de GitHub a tu PC
```

💡 Siempre es buena idea hacer `git pull` antes de empezar a trabajar, para asegurarte de tener la última versión.

---

## 🔀 4. Merge y Pull Request

- Un **merge** combina cambios de una rama (branch) con otra.
- Un **pull request (PR)** es una solicitud para unir tus cambios (desde tu fork o tu branch) al proyecto principal en GitHub.

**Ejemplo típico:**
1. Hacés cambios en tu rama o fork.
2. Los subís (`git push`).
3. En GitHub, hacés clic en **“Compare & pull request”**.
4. Explicás qué hiciste y enviás la solicitud.
5. Los administradores revisan y pueden aceptar (mergear) tu PR.

---

## 🌿 5. Branches y Checkout

Las **ramas (branches)** te permiten trabajar en una parte del proyecto sin afectar el resto.
Por ejemplo, podés crear una rama para probar una nueva función o hacer un cambio experimental.

**Comandos básicos:**
```bash
git branch               # muestra las ramas existentes
git branch nueva-rama    # crea una nueva rama
git checkout nueva-rama  # cambia a esa rama
```

Cuando termines y quieras unir tus cambios:
```bash
git checkout main        # vuelve a la rama principal
git merge nueva-rama     # une los cambios
```

💡 *Tip:* usá nombres descriptivos para tus ramas, como `arreglo-login` o `nueva-funcion-calculo`.

---

## 📚 Recursos recomendados

- **Documentación oficial de Git:**
  👉 [https://git-scm.com/doc](https://git-scm.com/doc)

- **Guía oficial de GitHub para principiantes:**
  👉 [https://docs.github.com/es/get-started](https://docs.github.com/es/get-started)

- **Tutorial interactivo (en español):**
  👉 [https://learngitbranching.js.org/?locale=es_ES](https://learngitbranching.js.org/?locale=es_ES)

- **Curso corto y gratuito:**
  👉 [https://www.freecodecamp.org/news/learn-git-and-github/](https://www.freecodecamp.org/news/learn-git-and-github/)

- **Cheatsheet de comandos Git (GitHub):**
  👉 [https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---

✅ **Resumen rápido**

| Concepto | Qué hace | Comando principal |
|-----------|-----------|------------------|
| Fork | Copiar un repo a tu cuenta | GitHub (botón “Fork”) |
| Commit | Guardar un cambio | `git commit -m "mensaje"` |
| Push | Subir cambios a GitHub | `git push origin main` |
| Pull | Descargar actualizaciones | `git pull origin main` |
| Branch | Nueva línea de trabajo | `git branch nombre` |
| Checkout | Cambiar de rama | `git checkout nombre` |
| Merge / PR | Combinar cambios | `git merge` / PR en GitHub |
