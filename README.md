
## Installation

### Prerequisites

- Python 3.12 or newer
- Git
- pip

### Setup

Clone the repository:

```powershell
git clone https://github.com/mrcqll/encryptfs.git
cd encryptfs
```

Create and activate a Python virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Initialize the database:

```powershell
python manage.py migrate
```

## Getting Started

Start the Django development server:

```powershell
python manage.py runserver 9000
```

Open http://127.0.0.1:9000/register/ to create
an account.

After registering, users can:

- Log in and log out
- Access their personal dashboard
- Upload files up to 10 MB
- View uploaded files
- Download files belonging to their account

This is an initial development prototype. File
encryption, secure sharing links, and activity
monitoring are planned for future milestones.

## Project Documentation

See [Project Documentation](docs/README.md)
for user stories, misuser stories, interface
mockups, and C4 architecture diagrams.

## License

This project is currently not licensed for
redistribution or reuse.
