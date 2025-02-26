# Sistema Inteligente Anti-Robo.
<img src="https://github.com/AredAngel23/siar-web/blob/db5ef35176d5290b84cb4e53a618be885b4745ff/mysite/home/static/images/SIAR_LOGO.svg" width="150" height="150" alt="SIAR Logo">
Repositorio oficial del sitio web de SIAR, el sistema antirrobo en IoT. Aquí encontrarás el código fuente, recursos y documentación necesaria para la implementación y despliegue de la plataforma web que presenta las características, tecnología, casos de uso y opciones de contacto para obtener el sistema. Contribuciones y sugerencias son bienvenidas.

## Requisitos
- Python 3.x - pip
- Django
- Tailwind CSS
- Node.js - npm
- VS Code
- Git

## Pasos para ejecutar el proyecto en local
1. **Clonar el repositorio:**

   ```bash
   $ git clone https://github.com/AredAngel23/siar-web.git
   $ cd siar-web 

2. **Crear y activar un entorno virtual:**

   ```bash
   $ py -m venv venv
   $ source venv\Scripts\activate

3. **Instalar las dependencias del proyecto:**

   ```bash
   $ pip install -r requirements.txt

4. **Aplicar migraciones de la DB por defecto de Django: (opcional)**

   ```bash
   $ py manage.py migrate

5. **Configurar Node.js para el funcionamiento de Tailwind CSS:**

   - Agregar a las variables de entorno del sistema en el PATH, la siguiente ruta:
     ```
     C:\Program Files\nodejs\npm.cmd
     ```

   - Instalar dependencias de NodeJS.
     Ubícate en la carpeta donde se encuentre el archivo `package.json` del proyecto:
     ```bash
     cd mysite/theme/static_src
     ```
     Ejecuta:
     ```bash
     npm install
     ```

6. **Correr el proyecto:**

   - Regresa a la ruta `siar-web/mysite` para iniciar el servidor y ver la página:
     ```bash
     py manage.py runserver
     ```
   - En otra terminal, inicia Tailwind para cargar los estilos:
     ```bash
     py manage.py tailwind start
     ```