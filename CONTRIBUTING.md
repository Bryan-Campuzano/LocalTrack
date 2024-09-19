# Guía para contribuir a LocalTrack

¡Gracias por considerar contribuir a LocalTrack! Contribuir ayuda a mejorar este proyecto y a hacerlo más útil para todos. Aquí te damos una guía rápida para contribuir de manera efectiva.

## Cómo contribuir

1. **Fork del repositorio**: Haz un fork del proyecto y clónalo a tu máquina local.
   
   ```bash
   git clone https://github.com/tu-usuario/localtrack.git

2. **Crea una rama de trabajo**: Crea una nueva rama para trabajar en tu contribución.

    ```bash
        git checkout -b mi-nueva-funcionalidad
    ```


3. **Realiza tus cambios**: Realiza los cambios que quieres proponer y asegúrate de que el código sea limpio y siga las convenciones de estilo.

4. **Ejecuta las pruebas**: Asegúrate de que todas las pruebas pasen antes de enviar tu contribución.

    ```bash
        python manage.py test
    ```


5. **Haz un commit**: Haz commit de tus cambios de manera descriptiva.

    ```bash
        git commit -m "Añade nueva funcionalidad X"
    ```


6. **Haz un push a tu repositorio**:

    ```bash
        git push origin mi-nueva-funcionalidad
    ```


7. **Crea un Pull Request**: Ve al repositorio original y crea un Pull Request describiendo tus cambios.

Normas de estilo de código

-    Sigue las convenciones de PEP8 para Python.
    Asegúrate de que el código sea claro y esté bien documentado.

-    Reportar errores (issues)

-    Si encuentras un error en LocalTrack, por favor crea un issue en el repositorio. Asegúrate de incluir información detallada para ayudar a reproducir el error.

-    Título: Describe el error brevemente.
    Descripción: Incluye los pasos para reproducir el error, la versión de Django/MySQL que estás usando y cualquier mensaje de error relevante.

¡Gracias por tu colaboración!