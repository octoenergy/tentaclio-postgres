
# tentaclio-postgres

A package containing all the dependencies for the postgresql tentaclio schema .

## Quick Start

This project comes with a `Makefile` which is ready to do basic common tasks

```
$ make help
install                       Initalise the virtual env installing deps
clean                         Remove all the unwanted clutter
lock                          Lock dependencies
update                        Update dependencies (whole tree)
sync                          Install dependencies as per the lock file
lint                          Lint files with flake and mypy
format                        Run black and isort
test                          Run unit tests
circleci                      Validate circleci configuration (needs circleci cli)
```

## Development

### Setting up your environment

1. Install dependencies:
```bash
make install
```

2. (Optional) Start PostgreSQL for functional tests:
```bash
docker-compose up -d
```

### Running Tests

#### Option 1: Using Docker (Recommended)

This repository includes a Docker Compose configuration that makes it easy to run tests locally without needing to install and configure PostgreSQL manually.

**Start PostgreSQL:**
```bash
docker-compose up -d
```

This starts a PostgreSQL 15 container with:
- User: `tentaclio`
- Database: `tentaclio-db`
- Password: `testpassword`
- Port: `5432`

**Run the test suites:**
```bash
# Linting
make lint

# Unit tests (don't require database)
make unit

# Functional tests (require PostgreSQL)
TENTACLIO__CONN__POSTGRES_TEST=postgresql://tentaclio:testpassword@localhost:5432/tentaclio-db make functional
```

**Stop PostgreSQL:**
```bash
docker-compose down
```

#### Option 2: Using your own PostgreSQL installation

If you prefer to use your own PostgreSQL instance:

1. Ensure PostgreSQL is running and accessible
2. Create a database and user for testing
3. Set the connection string environment variable:
```bash
export TENTACLIO__CONN__POSTGRES_TEST=postgresql://user:password@localhost:5432/dbname
```

4. Run the tests:
```bash
make lint
make unit
make functional
```

### Test Types

- **`make lint`** - Runs flake8 and mypy checks (no database required)
- **`make unit`** - Runs unit tests with mocked dependencies (no database required)
- **`make functional`** - Runs functional tests against a real PostgreSQL database (requires `TENTACLIO__CONN__POSTGRES_TEST` environment variable)
