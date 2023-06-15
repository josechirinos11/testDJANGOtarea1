
# Bike Network Information

Este proyecto es una aplicación Django que muestra información sobre redes de bicicletas. Utiliza la API de CityBik.es para obtener datos en tiempo real sobre diferentes redes de bicicletas disponibles.

## Características

- Obtiene datos de la API de CityBik.es y los almacena en una base de datos.
- Permite ver la información de las redes de bicicletas en el panel de administración de Django.
- Muestra la información de las redes de bicicletas en una página web utilizando Bootstrap para el diseño.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual e instala las dependencias del proyecto:
   ```
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
3. Ejecuta las migraciones de la base de datos:
   ```
   python manage.py migrate
   ```
4. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
5. Abre tu navegador y accede a `http://localhost:8000` para ver la aplicación.

## Uso
- Ve a `http://localhost:8000/api/obtener-datos/` para gestionar ir a la aip y guardar la informacion en postgreSQL.
- Ve a `http://localhost:8000/bike-network-info` para ver la información de las redes de bicicletas en formato de tabla.
- Accede al panel de administración de Django en `http://localhost:8000/admin` para gestionar las redes de bicicletas y sus datos.


## Contribución

Si quieres contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama con tus cambios:
   ```
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus modificaciones y realiza commits descriptivos.
4. Envía un pull request explicando tus cambios y mejoras.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

## Autor

jose chirinos - josechirinos11@gmail.com
