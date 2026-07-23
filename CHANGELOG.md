# Changelog

All notable changes to this project will be documented in this file.

This project follows Semantic Versioning (SemVer).

---

## [0.5.0] - 2026-07-24

### Added

- Repository Layer implementation
- Service Layer implementation
- Symbol Repository
- Symbol Service
- Symbol API endpoints
- CRUD operations for Symbols
- Pydantic request/response schemas
- Dependency Injection for services
- Duplicate symbol validation
- HTTP 409 Conflict handling for duplicate symbols

### Improved

- Clear separation between API, business logic, and data access layers
- Modular architecture for future domain services
- Cleaner dependency management
- Better API error handling

### Notes

Milestone 11 completed.

Sentinel now follows a production-style layered architecture using:

- Routers
- Services
- Repositories
- Models
- Schemas

This establishes the application's business layer and prepares the project for authentication, additional domain modules, and trading engine development.

---

## [0.4.0] - 2026-07-24

### Added

- SQLAlchemy ORM integration
- PostgreSQL connectivity
- Database session management
- Declarative Base
- Alembic migration framework
- Database health checks

### Improved

- Backend infrastructure
- Migration workflow
- Database architecture

---

## [0.3.0] - 2026-07-23

### Added

- FastAPI bootstrap
- Health endpoint
- Environment configuration
- Swagger/OpenAPI
- Application configuration management

---

## [0.2.0] - 2026-07-22

### Added

- Backend project organization
- Core application modules
- Environment support

---

## [0.1.0] - 2026-07-22

### Added

- Repository initialized
- ASP.NET Core MVC project
- Python FastAPI project
- Initial architecture
- Documentation
- Git configuration

---

## Version History

| Version | Milestone | Summary |
|----------|-----------|---------|
| 0.5.0 | Repository & Service Layer | Layered architecture, Symbol CRUD |
| 0.4.0 | Database Infrastructure | SQLAlchemy, PostgreSQL, Alembic |
| 0.3.0 | FastAPI Foundation | API, Health, Swagger |
| 0.2.0 | Backend Architecture | Configuration & project structure |
| 0.1.0 | Project Initialization | Repository setup |