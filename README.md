Este proyecto es una app web desarrollada con Streamlit y Python para descargar videos de YouTube de manera sencilla y eficiente. 

Permite a los usuarios ingresar una URL de YouTube, seleccionar entre varias opciones de streaming (audio y video), elegir la carpeta de destino para la descarga 
y luego iniciar el proceso de descarga.

La app corre solo de manera local por lo tanto es necesario tener Python y pip instalado en el sistema. 

Una vez corroborado esto, clonar el repositorio e instalar las dependencias especificadas en requirements.txt 
(Se puede encontrar en el mismo repositorio)

Se recomienda instalar estas dependencias en un entorno virtual para que no generen conflictos con otras ya instaladas.

Una vez completado todos los pasos usar:  streamlit run "NombreDelArchivo.py"

Para iniciar el archivo con el navegador predeterminado.





Guia:
------------------------------------------------------------------------------------------------

1- Clonar el repositorio:

		git clone https://github.com/Luchossd/YT-Downloader.git

		cd YT-Downloader

------------------------------------------------------------------------------------------------

2- Configurar un entorno virtual (opcional pero recomendado):

		python -m venv venv

		source venv/bin/activate (Unix/macOS)

		venv\Scripts\activate  (Para Windows)

------------------------------------------------------------------------------------------------

3- Instalar las dependencias desde requirements.txt:

		pip install -r requirements.txt

------------------------------------------------------------------------------------------------

4- Ejecutar la aplicación con Streamlit:

		streamlit run NombreDelArchivo.py

------------------------------------------------------------------------------------------------
