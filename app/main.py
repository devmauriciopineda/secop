import pandas as pd
import requests
from core.config import settings

# 1. Configuración del Endpoint de SECOP II - Contratos Electrónicos
DATASET_ID = "jbjy-vk9h"
ENDPOINT_URL = (
    f"https://www.datos.gov.co/api/v3/views/{DATASET_ID}/query.json"
)

# 2. Definición de Filtros Avanzados (SoQL)
# Nota: Los nombres de las columnas deben ir en minúsculas y sin acentos
consulta = {
    "query": (
        "SELECT nombre_entidad, nit_entidad, departamento, ciudad, "
        "estado_contrato, valor_del_contrato, objeto_del_contrato "
        "WHERE departamento = 'Valle del Cauca' "
        "AND valor_del_contrato > 50000000 "
        "AND estado_contrato = 'En ejecución' "
        "ORDER BY valor_del_contrato DESC"
    ),
    "page": {
        "pageNumber": 1,
        "pageSize": 100,
    },
    "includeSynthetic": False,
}

# consulta = {
#     "query": "SELECT *",
#     "page": {
#         "pageNumber": 1,
#         "pageSize": 10,
#     },
#     "includeSynthetic": False,
# }

# 3. Encabezados de la petición
headers = {
    "Content-Type": "application/json",
    # "X-App-Token": settings.app_token,
}

try:
    print("Consultando base de datos de SECOP II...")
    respuesta = requests.post(
        ENDPOINT_URL,
        # params={"app_token": settings.app_token},
        json=consulta,
        headers=headers,
    )
    respuesta.raise_for_status()

    datos = respuesta.json()

    if datos:
        # Cargar a DataFrame de Pandas
        df = pd.DataFrame(datos)

        # Formatear el valor monetario para leerlo mejor en consola
        df["valor_del_contrato"] = pd.to_numeric(
            df["valor_del_contrato"]
        ).map("${:,.2f}".format)

        print(f"\n¡Éxito! Se encontraron {len(df)} contratos con los filtros aplicados.")
        print("\nMuestra de los resultados:")
        print(
            df[
                [
                    "nombre_entidad",
                    "estado_contrato",
                    "valor_del_contrato",
                    "ciudad",
                ]
            ].head(10)
        )

        # Guardar resultados en un archivo CSV local
        # df.to_csv("contratos_secop_filtrados.csv", index=False)
    else:
        print("No se encontraron contratos que coincidan con los criterios establecidos.")

except requests.exceptions.HTTPError as err:
    print(f"Error en la petición: {err}")
