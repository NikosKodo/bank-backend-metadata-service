## bank-backend-metadata-service

A small REST API for managing datasets and data elements metadata. Built with Django REST Framework.

## Bank Metadata Service with Django

It allows clients to define:
- **Datasets**: business entities such as Customer, Account, Transaction
- **Data Elements**: fields belonging to a dataset such as email, date_of_birth

The service supports CRUD operations, nested element management, basic search, and OpenAPI/Swagger documentation.

---

## Data model & key design decisions

### Models

**Dataset**
- `name` (unique)
- `description`
- `created_at`, `updated_at`

**DataElement**
- belongs to a `Dataset` (ForeignKey)
- `name`
- `description`
- `data_type`
- `is_required`: whether the field is required in the dataset
- `is_pii`: the element contains personal data
- `created_at`, `updated_at`

---

## Search
- `GET /api/elements/?search=<term>`
Searches across: `name`, `description`, `data_type`, `dataset__name`

---

## API documentation (Swagger/OpenAPI)
- Swagger UI: `GET /api/docs/`
- OpenAPI schema: `GET /api/schema/`

---

## Assumptions / trade-offs
- **SQLite** is used for simplicity and local development.

---

## Run locally

### 1) Setup virtual environment
python -m venv .VirtualEnvironment
### Windows PowerShell:
.VirtualEnvironment\Scripts\Activate.ps1
### macOS/Linux:
source .VirtualEnvironment/bin/activate

### Install dependencies
pip install -r requirements.txt

### Apply migrations
python manage.py migrate

### Run the server
python manage.py runserver

### API will be available at:
http://127.0.0.1:8000/

### Swagger UI: 
http://127.0.0.1:8000/api/docs/

### Run tests
python manage.py test

## Assessment notes

  - Retention / lifecycle metadata was not implemented.
  - An explicit “business rule enforcement” test were not included (the uniqueness constraint exists at the database level).
  - Has not been deployed on Docker Setup

