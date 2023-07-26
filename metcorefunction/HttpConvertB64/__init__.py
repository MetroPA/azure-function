import logging
import base64
import json
import azure.functions as func
from azure.storage.blob import BlobServiceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Obtener el nombre del blob de la consulta de la solicitud HTTP
    blob_name = req.params.get('blob_name')
    if not blob_name:
        return func.HttpResponse(
            "Por favor, proporciona 'blob_name' en los parámetros de la solicitud.",
            status_code=400
        )
    
    # Configurar la conexión al almacenamiento de blobs
    connection_string = "Tu cadena de conexión"
    container_name = "Nombre de tu contenedor"

    # Obtener el contenido binario del archivo de Blob
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=filesuscription;AccountKey=H8w5/iGNO7q4VE7diOqkUxc5kGdhwgWbLOi97muUd84E5jN5dP4l2JOzGrsjL2HA/E3CrjUvdLbi+AStj52ijw==;EndpointSuffix=core.windows.net")
    blob_client = blob_service_client.get_blob_client(container="suscrip", blob=blob_name)
    content = blob_client.download_blob().readall()
    
    # Convertir el contenido binario a base64
    content_base64 = base64.b64encode(content).decode('utf-8')
    # Crear un diccionario con el resultado
    result = {'base64': content_base64}
    # Convertir a JSON
    json_result = json.dumps(result)
    
    # Devolver la respuesta como JSON
    return func.HttpResponse(
        json_result, 
        mimetype="application/json",
        status_code=200
        )
    

