# Consultas de SECOP II

Scripts sencillos para consultar contratos del conjunto de datos de [SECOP II](https://www.datos.gov.co/), disponible en la plataforma de datos abiertos de Colombia.

## Scripts

- `app/main.py`: consulta el endpoint HTTP de Socrata mediante `requests`. Filtra contratos del Valle del Cauca, con valor superior a 50 millones y estado **En ejecución**; muestra una tabla resumida de los resultados.
- `app/other.py`: usa la biblioteca `sodapy` para consultar contratos firmados después del 1 de enero de 2024 y con valor superior a 500 millones; muestra todos los resultados, hasta 500 registros.

Ambos scripts convierten la respuesta en un `DataFrame` de Pandas. El conjunto consultado es `jbjy-vk9h`.

## Instalación

Clona el repositorio y entra en su directorio:

```bash
git clone https://github.com/devmauriciopineda/secop.git
cd secop
```

Crea un entorno virtual, actívalo e instala las dependencias:

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows PowerShell
pip install -r requirements.txt
```

## Configuración

La configuración se carga desde `.env` mediante `app/core/config.py`. Crea este archivo en la raíz del proyecto:

```dotenv
app_token=TU_TOKEN_DE_DATOS_GOV_CO
```

El token se valida al iniciar los scripts. Actualmente las consultas se ejecutan sin enviarlo a la API; aun así, la variable es obligatoria para cargar la configuración.

## Ejecución

Como los scripts importan `core.config`, ejecútalos desde el directorio `app`:

```bash
cd app
python main.py
```

Para ejecutar la consulta alternativa:

```bash
python other.py
```

Se necesita conexión a Internet. `main.py` informa los contratos encontrados y muestra hasta diez en consola; `other.py` imprime el conjunto completo recibido. Los resultados no se guardan automáticamente en archivos.
