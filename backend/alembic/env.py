from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.database import Base  # Import your Base
from app.models import *  # Import all your models

# This is the Alembic Config object, which provides access to the values
# within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your model's MetaData object here for 'autogenerate' support
# target_metadata is set to Base.metadata to include all models in migrations.
target_metadata = Base.metadata

# Other settings are already in place.
def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,  # Use this if you're using SQLite for migration purposes.
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
