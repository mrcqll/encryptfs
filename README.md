## Executive Summary

encryptfs is a secure, web-based file storage and sharing application designed to provide users with a convenient way to manage and exchange sensitive information. The application focuses on protecting file confidentiality through encryption, user authentication, and controlled access mechanisms while maintaining a straightforward and accessible user experience.

The platform will allow users to upload, store, download, and securely share files through an intuitive web interface. Planned security features include AES-256-GCM encryption, time-limited sharing links, access revocation, and file activity monitoring. These capabilities are intended to reduce the risks associated with unauthorized file access, data exposure, and insecure file distribution.

What makes encryptfs interesting is its security-first approach to a common challenge: securely sharing files without sacrificing usability. Rather than treating security as an additional feature, encryptfs incorporates confidentiality, access control, and accountability into its core application design.

The application is being developed using Python and the Django web framework, with a dark-mode interface designed for simplicity and ease of use. The initial prototype demonstrates user authentication, file uploads, downloads, and basic file management. Additional encryption and secure sharing functionality will be implemented in subsequent development milestones.

Ultimately, encryptfs aims to demonstrate how modern web application development practices and cybersecurity principles can be combined to create a practical, secure, and user-friendly file-sharing solution.

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
