# My Flask API

Este es un proyecto inicial para aprender a desarrollar APIs usando Flask en Python.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/my_flask_api.git
    cd my_flask_api
    ```

2. Crea un entorno virtual y activa el entorno:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar la aplicación, usa:
```bash
python app.py
```

La API estará disponible en `http://127.0.0.1:5000/`.

## Endpoints

- `GET /` - Muestra un mensaje de bienvenida.
- `GET /api/v1/resources/books` - Devuelve una lista de libros.
- `GET /api/v1/resources/books/<id>` - Devuelve un libro específico por ID.
