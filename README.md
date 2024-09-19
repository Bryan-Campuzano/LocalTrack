# Proyecto LocalTrack



**LocalTrack** es una plataforma CRM modular diseñada para la gestión de inventarios, ventas, usuarios, recursos humanos y análisis de datos en pequeñas y medianas empresas. El proyecto ofrece una solución centralizada y fácil de usar para mejorar la eficiencia de las operaciones diarias.

## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Mira **Despliegue** para conocer cómo desplegar el proyecto de manera gratuita.

### Pre-requisitos 📋

Para instalar y ejecutar LocalTrack, necesitarás tener instalado lo siguiente:

- **Python 3.8 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **MySQL**: [Descargar MySQL](https://dev.mysql.com/downloads/)
- **Git**: [Instalar Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- **Pipenv** o entornos virtuales de Python: 
  ```bash
  pip install pipenv
  ```

### Instalación 🔧

Sigue estos pasos para configurar el entorno de desarrollo y ejecutar LocalTrack localmente.

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/localtrack.git
   cd localtrack
   ```

2. **Configura un entorno virtual**:
   ```bash
   python -m venv localtrackenv
   source localtrackenv/bin/activate  # En Linux/Mac
   localtrackenv\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias del proyecto**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos MySQL**:
   - Crea una base de datos en MySQL para el proyecto:
     ```sql
     CREATE DATABASE localtrack;
     ```
   - Edita el archivo `localtrack/settings.py` para configurar la base de datos:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'localtrack',
             'USER': 'tu_usuario_mysql',
             'PASSWORD': 'tu_contraseña_mysql',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Ejecuta las migraciones** para crear las tablas en la base de datos:
   ```bash
   python manage.py migrate
   ```

6. **Crea un superusuario** para acceder al panel de administración:
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicia el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

   Ahora puedes acceder a la aplicación en `http://127.0.0.1:8000/`.

### Despliegue gratuito 📦

Para desplegar **LocalTrack** de manera gratuita en servicios como **Heroku**, sigue estos pasos:

1. **Configura tu repositorio remoto en Heroku**:
   ```bash
   heroku login
   heroku create localtrack-app
   ```

2. **Configura variables de entorno para la base de datos**:
   ```bash
   heroku config:set DJANGO_SECRET_KEY='your-secret-key'
   heroku config:set DJANGO_ALLOWED_HOSTS='localtrack-app.herokuapp.com'
   heroku config:set DATABASE_URL='mysql://usuario:contraseña@host/db_name'
   ```

3. **Despliega el proyecto en Heroku**:
   ```bash
   git push heroku main
   ```

4. **Ejecuta las migraciones en Heroku**:
   ```bash
   heroku run python manage.py migrate
   ```

5. **Crea un superusuario en el entorno de producción**:
   ```bash
   heroku run python manage.py createsuperuser
   ```

   ¡El proyecto estará disponible en `https://localtrack-app.herokuapp.com/`!

## Ejecutando las pruebas ⚙️

Para ejecutar las pruebas automatizadas del sistema:

1. Asegúrate de tener configurado el entorno de pruebas.
2. Ejecuta el siguiente comando para correr los tests:
   ```bash
   python manage.py test
   ```

### Pruebas end-to-end 🔩

Estas pruebas verifican el correcto funcionamiento del sistema desde la perspectiva del usuario, incluyendo la interacción con el frontend y backend.

```
python manage.py test tests/end_to_end/
```

### Pruebas de estilo de codificación ⌨️

Para verificar el estilo de codificación según PEP8 y otras convenciones:

```
flake8 .
```

## Despliegue 📦

Sigue las instrucciones de la sección [Despliegue gratuito](#despliegue-gratuito) para desplegar el proyecto en Heroku.

Para servidores dedicados, puedes configurar el despliegue usando **Docker**, **Nginx** y **Gunicorn** para mejorar la escalabilidad.

## Construido con 🛠️

Herramientas y frameworks utilizados en el proyecto:

* [Django](https://www.djangoproject.com/) - El framework web usado
* [MySQL](https://www.mysql.com/) - Sistema de base de datos
* [Heroku](https://www.heroku.com/) - Plataforma de despliegue
* [Bootstrap](https://getbootstrap.com/) - Framework CSS para el frontend

## Contribuyendo 🖇️

Por favor, lee el [CONTRIBUTING.md](CONTRIBUTING.md) para obtener detalles sobre el código de conducta y el proceso para enviarnos pull requests.

## Autores ✒️

* **Bryan Campuzano** - *Gestor de Proyecto y desarrollo* - [github](https://github.com/Bryan-Campuzano)
* **Camilo Baquero** - *Documentación y desarrollo* 
* **Julio Montaña** - *Documentacion y desarrollo* 


También puedes ver la lista de todos los [contribuyentes](https://github.com/your/project/contributors) que han participado en este proyecto.

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para detalles.

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* Da las gracias públicamente 🤓.

---

⌨️ con ❤️ por [Bryan Campuzano](https://github.com/Bryan-Campuzano) *Equipo de LocalTrack* 😊

---
