"""This package implements the tentaclio postgres client """
from tentaclio import *  # noqa

from .clients.postgres_client import ClientClassName


# Add DB registry
DB_REGISTRY.register("postgresql", ClientClassName)  # type: ignore
