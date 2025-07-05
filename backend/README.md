# ContextCraft Backend

Backend API para la plataforma ContextCraft construido con FastAPI.

## Configuración Inicial

1. **Iniciar PostgreSQL con Docker:**
```bash
cd ..
docker-compose up -d
```

2. **Configurar entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus valores
```

4. **Inicializar la base de datos:**
```bash
python -m app.db.init_db
```

5. **Ejecutar el servidor:**
```bash
uvicorn app.main:app --reload --port 8000
```

## Endpoints Principales

### Usuarios
- `POST /api/v1/users/` - Crear usuario
- `GET /api/v1/users/{user_id}` - Obtener usuario
- `GET /api/v1/users/` - Listar usuarios
- `PUT /api/v1/users/{user_id}` - Actualizar usuario

### Proyectos
- `POST /api/v1/projects/` - Crear proyecto
- `GET /api/v1/projects/{project_id}` - Obtener proyecto
- `GET /api/v1/projects/` - Listar proyectos del usuario
- `PUT /api/v1/projects/{project_id}` - Actualizar proyecto
- `DELETE /api/v1/projects/{project_id}` - Eliminar proyecto

### Documentos
- `POST /api/v1/documents/claude/{project_id}` - Crear CLAUDE.md
- `POST /api/v1/documents/initial/{project_id}` - Crear INITIAL.md
- `POST /api/v1/documents/prp/{project_id}` - Crear PRP
- `GET /api/v1/documents/{doc_type}/{project_id}/latest` - Obtener última versión
- `PUT /api/v1/documents/{doc_type}/{doc_id}` - Actualizar documento (crea nueva versión)

## Documentación API

La documentación interactiva está disponible en:
- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## Testing

```bash
pytest
```

## Estructura del Proyecto

```
backend/
├── app/
│   ├── api/
│   │   └── api_v1/
│   │       ├── endpoints/
│   │       └── api.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   ├── models/
│   ├── schemas/
│   └── main.py
├── tests/
├── alembic/
├── requirements.txt
└── README.md
```