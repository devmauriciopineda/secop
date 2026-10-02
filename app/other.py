from sodapy import Socrata
import pandas as pd
from core.config import settings

# client = Socrata("www.datos.gov.co", settings.app_token)
client = Socrata("www.datos.gov.co", None)

# Consulta: Contratos de una entidad específica firmados en 2024 con valor mayor a 500 millones
query = """
    SELECT 
        nombre_entidad, 
        proveedor_adjudicado, 
        descripcion_del_proceso, 
        valor_del_contrato, 
        fecha_de_firma 
    WHERE 
        fecha_de_firma > '2024-01-01' 
        AND valor_del_contrato > 500000000
    LIMIT 500
"""

# Nota: El parámetro $query se usa para SoQL. 
# También puedes usar 'where' como parámetro directo: where="fecha_de_firma > '2024-01-01'"
results = client.get("jbjy-vk9h", query=query)

df = pd.DataFrame.from_records(results)
print(f"Se encontraron {len(df)} contratos.")
print(df)