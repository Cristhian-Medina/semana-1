import os
from dotenv import load_dotenv
from google.genai import Client, types

load_dotenv()

client = Client(api_key=os.getenv('GEMINI_API_KEY'))

def create_simple_tasks(task):
    if not client:
        return ["Error con la api key"]
    
    prompt = """TAREA A DESCOMPONER: {task}

    CRITERIOS PARA LAS SUBTAREAS:
    - Generar entre 3 y 5 subtareas
    - Cada subtarea debe ser independiente y ejecutable
    - Usar verbos de acción claros (crear, revisar, implementar, etc.)
    - Ordenar por secuencia lógica de ejecución
    - Cada subtarea debe poder completarse en una sesión de trabajo

    FORMATO DE RESPUESTA REQUERIDO:
    Responde ÚNICAMENTE con la lista de subtareas, sin introducción ni conclusión.
    Cada subtarea en una línea nueva, iniciando con un guión y un espacio (- ).

    EJEMPLO:
    - Investigar requisitos técnicos del proyecto
    - Diseñar arquitectura básica del sistema
    - Implementar módulo de autenticación
    - Realizar pruebas unitarias
    - Documentar código y API""".format(task=task)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="""Eres un asistente especializado en descomposición de tareas.
                Tu objetivo: Dividir la tarea proporcionada en subtareas simples, específicas y accionables.""",
                temperature=0.7,
            ),
        )

        # ## Extraer subtareas de la respuesta
        # subtasks = []
        # for linea in response.text.split('\n'):
        #     if linea.strip().startswith('-'):
        #         subtasks.append(linea.strip()[1:].strip())
        # ## list comprehension: version más compacta del loop anterior
        subtasks = [
            linea.strip()[1:].strip()
            for linea in response.text.split('\n')
            if linea.strip().startswith('-')
        ]

        return subtasks
    
    except Exception as e:
        return [f"Error al generar las subtareas: {e}"]