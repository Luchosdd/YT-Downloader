import pytube 
import streamlit as st
import os
from pathlib import Path

class YTDownloader:
    def __init__(self, url):
        self.url = url
        self.yt = pytube.YouTube(self.url, on_progress_callback=YTDownloader.onProgress)
        self.stream = None # Inicializar el stream como nulo al principio

    def showTitle(self):
        # Mostrar el título del video y opciones de streaming
        st.write(f"**Título:** {self.yt.title}")
        self.showStreams()

    def showStreams(self):
        # Recuperar y mostrar las opciones de stream disponibles y formatearlas para el select box
        streams = self.yt.streams
        stream_options = [
            f"Resolución: {stream.resolution or 'N/A'} / FPS: {getattr(stream, 'fps', 'N/A')} / Tipo: {stream.mime_type}"
            for stream in streams
        ]
        seleccion = st.selectbox("Selecciona una opción de stream", stream_options)
        self.stream = streams[stream_options.index(seleccion)] # Selecciona el stream que desea el usuario

    def getFileSize(self):
        # Mostrar el el tamaño del archivo a descargar en MB
        file_size = self.stream.filesize / 1000000
        return file_size

    def getDownloadFolder(self, download_folder):
        # Obtener la carpeta de descarga. Usa la carpeta por defecto si no se especifica
        if not download_folder:
            download_folder = str(Path.home() / "Downloads" or "Descargas")  # Carpeta por defecto "Downloads" o "Descargas"
        return download_folder

    def getPermissionToContinue(self, file_size, download_folder):
        # Mostrar información del video seleccionado y la carpeta de descarga. Esperar la confirmación del usuario para iniciar con la descarga
        st.write(f"*Título:* {self.yt.title}")
        st.write(f"*Autor:* {self.yt.author}")
        st.write(f"*Tamaño:* {file_size:.2f} MB")
        st.write(f"*Resolución:* {self.stream.resolution or 'N/A'}")
        st.write(f"*FPS:* {getattr(self.stream, 'fps', 'N/A')}")

        download_folder = self.getDownloadFolder(download_folder)
        st.write(f"*Descargando en:* {download_folder}")

        if st.button("Descargar"):
            self.download(download_folder)

    def download(self, download_folder):
        # Valida si la carpeta de descarga es válida
        if not os.path.isdir(download_folder):
            st.error("La carpeta de destino no es válida.")
            return

        # Intentar descargar el video en la carpeta especificada
        try:
            self.stream.download(output_path=download_folder)
            st.success("¡Descarga completada!") # Muestra mensaje de éxito si la descarga se completa sin errores
        except Exception as e:
            st.error(f"Error durante la descarga: {e}") # Muestra mensaje de error si ocurre algún problema durante la descarga

    @staticmethod
    def onProgress(stream=None, chunk=None, remaining=None):
        # Método estático para manejar la devolución de progreso durante la descarga
        file_size = stream.filesize / 1000000
        file_download = file_size - (remaining / 1000000)
        st.progress(file_download / file_size) # Mostrar el progreso de descarga como una barra de progreso

if __name__ == "__main__":
    # Interfaz de usuario básica con Streamlit
    st.title("YT Downloader")
    url = st.text_input("Ingrese la URL:")
    download_folder = st.text_input("Ingrese la ruta donde quiere guardar su video (deje en blanco para usar la carpeta por defecto):")

    if url:
        # Crea una instancia del descargador de YouTube con la URL dada
        downloader = YTDownloader(url)
        downloader.showTitle() # Muestra el título del video y las opciones de stream
        
        if downloader.stream:
            file_size = downloader.getFileSize() # Obtiene el tamaño del archivo seleccionado
            downloader.getPermissionToContinue(file_size, download_folder) # Pide la confirmación del usuario para iniciar la descarga
