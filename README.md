## Boilerplate Flask web app

For practice purposes. But once finished, it can be easily copied and adapted to suit all kinds of needs. It works locally but since i'm still learning, a lot of things are not configured according to best practices.

### Tech Stack
- Web: Flask
- ORM: SQLAlchemy
- Database: PostgreSQL
- Containerization: Docker
- WSGI Server: Gunicorn
- Reverse Proxy Server: NGINX

### Todo / Roadmap
- [x] Basic Flask container
- [x] Basic dockerization
- [x] models for SQLAlchemy
- [x] Postgres container
- [x] Postgres integration into Flask
- [x] use __init__.py for Flask
- [x] Flask separate config.py
- [x] Routes via blueprints
- [ ] Frontend for doing CRUD
- [x] Nginx server container
- [x] WSGI-Gunicorn
- [ ] Reorganize Flask app folder structure
- [ ] validation through Pydantic
- [ ] User auth and respective routes
- [ ] Redis?
- [ ] Celery?
- [ ] RabbitMQ?

### Instructions
1. Rename .env_flask.sample and .env_pg.sample to .env_flask and .env_pg
2. Replace your Postgres username, password and db_name in both files.
3. smtn smtn run manage.py to create tables
4. Run 'chmod +x entrypoint.sh' (not sure if Github keeps permissions)
5. run 'docker compose up'
6. run 'docker compose build'