import os
import json

def validate_avro_schema(schema):
    """
    Valida que el esquema cumpla con la especificación Avro 1.11.1.
    
    Requisitos mínimos:
      - El esquema debe ser un objeto JSON (dict).
      - Debe tener la propiedad "type" con valor "record".
      - Debe tener la propiedad "name" (string).
      - Debe tener la propiedad "fields", que es una lista.
    
    Cada elemento en "fields" debe ser un objeto que contenga:
      - "name": nombre del campo.
      - "type": tipo de dato del campo (puede ser un string, un objeto o una unión).
      
    Si el esquema no es válido, se lanza una excepción.
    """
    if not isinstance(schema, dict):
        raise ValueError("El esquema debe ser un objeto JSON (dict).")
    if schema.get("type") != "record":
        raise ValueError("El esquema Avro debe tener 'type': 'record'.")
    if "name" not in schema:
        raise ValueError("El esquema Avro debe tener la propiedad 'name'.")
    if "fields" not in schema or not isinstance(schema["fields"], list):
        raise ValueError("El esquema Avro debe tener una propiedad 'fields' de tipo lista.")
    
    for field in schema["fields"]:
        if not isinstance(field, dict):
            raise ValueError("Cada campo en 'fields' debe ser un objeto (dict).")
        if "name" not in field:
            raise ValueError("Cada campo en 'fields' debe tener la propiedad 'name'.")
        if "type" not in field:
            raise ValueError("Cada campo en 'fields' debe tener la propiedad 'type'.")

def map_api_field_type(avro_type):
    """
    Mapea el tipo definido en el esquema Avro a un tipo JSON simplificado,
    siguiendo algunas reglas básicas de la especificación Avro 1.11.1.
    
    - Si el tipo es un objeto (dict), se revisa si tiene un "logicalType"
      (por ejemplo, "decimal" o "timestamp-millis") para mapearlo a un tipo
      simplificado ("numeric", "datetime", etc.).
    - Si el tipo es un string, se realiza una conversión simple:
         "int" o "long"   -> "int"
         "float" o "double" -> "numeric"
         "boolean"         -> "boolean"
         Otros             -> "string"
    """
    if isinstance(avro_type, dict):
        base_type = avro_type.get("type")
        logical = avro_type.get("logicalType")
        if logical == "decimal":
            return "numeric"
        elif logical in ["timestamp-millis", "timestamp-micros", "datetime"]:
            return "datetime"
        elif isinstance(base_type, str):
            if base_type.lower() in ["int", "long"]:
                return "int"
            elif base_type.lower() in ["float", "double"]:
                return "numeric"
            elif base_type.lower() == "boolean":
                return "boolean"
            else:
                return "string"
        else:
            return "string"
    elif isinstance(avro_type, str):
        if avro_type.lower() in ["int", "long"]:
            return "int"
        elif avro_type.lower() in ["float", "double"]:
            return "numeric"
        elif avro_type.lower() == "boolean":
            return "boolean"
        else:
            return "string"
    else:
        return "string"

def process_api_schema_file(json_file_path, avro_output_folder, json_output_folder):
    """
    Procesa un archivo JSON de API:
      1. Lee y valida el esquema Avro según la especificación.
      2. Guarda el esquema tal cual en un archivo con extensión .avsc.
      3. Genera un archivo de mapeo JSON en el que cada campo se asocia a un tipo simplificado.
    
    Se espera que el esquema de entrada siga la estructura:
      {
        "type": "record",
        "name": "NombreRegistro",
        "fields": [
           { "name": "campo1", "type": "string", ... },
           { "name": "campo2", "type": ["null", "int"], ... },
           ...
        ]
      }
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    # Validar el esquema según la especificación Avro
    try:
        validate_avro_schema(schema)
    except ValueError as e:
        print(f"Esquema inválido en {json_file_path}: {e}")
        return
    
    # Utilizar la propiedad "name" (convertida a minúsculas) para nombrar los archivos
    schema_name = schema.get("name", "unknown").lower()
    
    # Guardar el esquema Avro en un archivo .avsc (manteniendo la estructura original)
    if not os.path.isdir(avro_output_folder):
        os.makedirs(avro_output_folder)
    avro_file_path = os.path.join(avro_output_folder, f"{schema_name}.avsc")
    with open(avro_file_path, 'w', encoding='utf-8') as avro_file:
        json.dump(schema, avro_file, indent=4)
    
    # Generar el mapeo JSON: se recorre la lista de campos y se asigna un tipo simplificado.
    field_mappings = {}
    for field in schema.get("fields", []):
        field_name = field.get("name")
        field_type = field.get("type")
        # Si el tipo es una unión (lista) que incluye "null", se descarta "null"
        if isinstance(field_type, list):
            non_null_types = [t for t in field_type if t != "null"]
            field_type = non_null_types[0] if non_null_types else "string"
        json_type = map_api_field_type(field_type)
        field_mappings[field_name.upper()] = json_type
    
    if not os.path.isdir(json_output_folder):
        os.makedirs(json_output_folder)
    mapping_file_path = os.path.join(json_output_folder, f"{schema_name}.json")
    with open(mapping_file_path, 'w', encoding='utf-8') as mapping_file:
        json.dump(field_mappings, mapping_file, indent=4)
    
    print(f"Generado Avro: {avro_file_path}")
    print(f"Generado JSON: {mapping_file_path}")

def process_api_schemas(api_folder, avro_output_folder, json_output_folder):
    """
    Procesa todos los archivos JSON en la carpeta de API y genera
    los archivos Avro (.avsc) y de mapeo JSON correspondientes.
    """
    if not os.path.isdir(api_folder):
        raise ValueError(f"La carpeta de API no existe: {api_folder}")
    
    json_files = [f for f in os.listdir(api_folder) if f.lower().endswith('.json')]
    if not json_files:
        raise ValueError("No se encontraron archivos JSON en la carpeta de API.")
    
    for json_file in json_files:
        json_file_path = os.path.join(api_folder, json_file)
        process_api_schema_file(json_file_path, avro_output_folder, json_output_folder)
    
    print("Proceso API finalizado. Todos los archivos generados correctamente.")
