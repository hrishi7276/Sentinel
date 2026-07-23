# Changelog

All notable changes to this project will be documented in this file.

This project follows **Semantic Versioning (SemVer)**.

---

## [0.4.0] - 2026-07-24

### Added

- SQLAlchemy ORM integration
- PostgreSQL database connectivity
- Database session management
- Declarative Base architecture
- Database package organization
- Database health check integration
- Alembic migration framework initialized
- Initial migration configuration
- Version updated in Health API to `v0.4.0`

### Improved

- Project architecture refined for future scalability
- Backend foundation prepared for managed database migrations
- Health endpoint now validates database connectivity

### Notes

This release establishes Sentinel's database infrastructure and migration workflow, providing a solid foundation for future domain models and persistent storage.

---

## [0.3.0] - 2026-07-23

### Added

- FastAPI application bootstrap
- Health endpoint (`/health`)
- Configuration management using environment variables
- Centralized application settings
- PostgreSQL configuration
- Pydantic-based configuration management
- OpenAPI (Swagger) documentation

### Improved

- Application startup structure
- Environment configuration organization

### Notes

Sentinel transitioned from a project skeleton to a functional backend service capable of exposing APIs and validating application health.

---

## [0.2.0] - 2026-07-22

### Added

- Backend project organization
- Configuration directory
- Environment (`.env`) support
- Initial dependency management
- Core application modules

### Improved

- Project folder structure
- Backend modularization

### Notes

Focused on preparing the backend architecture before implementing API functionality.

---

## [0.1.0] - 2026-07-22

### Added

- Repository initialized
- ASP.NET Core MVC project created
- Python FastAPI engine initialized
- Python virtual environment configured
- Initial project architecture established
- Root `.gitignore` added
- Project documentation started

### Notes

Initial project setup. Established the foundation for the Sentinel platform.

---

## Version History

| Version | Date | Summary |
|---------|------------|--------------------------------------------|
| 0.4.0 | 2026-07-24 | Database layer, SQLAlchemy, PostgreSQL, Alembic |
| 0.3.0 | 2026-07-23 | FastAPI foundation, configuration, health API |
| 0.2.0 | 2026-07-22 | Backend architecture and configuration |
| 0.1.0 | 2026-07-22 | Initial repository and project setup |