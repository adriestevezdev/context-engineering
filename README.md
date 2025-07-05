# ContextCraft 🚀

Plataforma SaaS que democratiza el Context Engineering para crear documentación estructurada y contextos completos para ideas y proyectos.

## 🛠️ Stack Tecnológico

- **Frontend**: Next.js 15 + TypeScript + Tailwind CSS
- **Backend**: FastAPI + PostgreSQL + SQLAlchemy
- **IA**: OpenAI GPT-4 + Langchain
- **Auth**: Clerk
- **DB Admin**: Adminer

## 🚀 Inicio Rápido con Docker

### 1. Clonar el repositorio
```bash
git clone <repository-url>
cd context-engineering
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus claves de API
```

### 3. Iniciar todos los servicios
```bash
docker-compose up -d
```

Esto levantará:
- **PostgreSQL**: Base de datos en `localhost:5432`
- **Adminer**: Administrador de BD en `http://localhost:8080`
- **Backend API**: FastAPI en `http://localhost:8000`
- **Frontend**: Next.js en `http://localhost:3000`

### 4. Inicializar la base de datos
```bash
docker-compose exec backend python -m app.db.init_db
```

## 📍 URLs de Acceso

- **Aplicación**: http://localhost:3000
- **API Docs**: http://localhost:8000/api/v1/docs
- **Adminer**: http://localhost:8080
  - Server: `postgres`
  - Username: `contextcraft`
  - Password: `password`
  - Database: `contextcraft`

## 🔧 Desarrollo Local (sin Docker)

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Base de datos
```bash
# Iniciar solo PostgreSQL
docker-compose up -d postgres adminer
```

## 📝 Comandos Útiles

```bash
# Ver logs de todos los servicios
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend

# Reiniciar un servicio
docker-compose restart backend

# Detener todos los servicios
docker-compose down

# Detener y eliminar volúmenes (⚠️ borra la BD)
docker-compose down -v

# Ejecutar comandos en contenedores
docker-compose exec backend python -m pytest
docker-compose exec frontend npm run lint
```

## 🧪 Testing

### Backend
```bash
docker-compose exec backend python -m pytest
```

### Frontend
```bash
docker-compose exec frontend npm run test
```

## 📚 Documentación

- [Documentación de la Plataforma](PLATFORM_DOCS.md)
- [Lista de Tareas](tasklist.md)
- [API Docs](http://localhost:8000/api/v1/docs)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT.