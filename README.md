# LawAi - Legal AI Assistant

A Django-based web application designed for legal services with integrated AI-powered chatbot, lawyer dashboard, and user authentication.

## 📋 Project Overview

LawAi is a comprehensive legal services platform that combines:
- **Authentication System** - Secure user signup and login functionality
- **Lawyer Dashboard** - Administrative interface for lawyers to manage cases and clients
- **AI Chatbot** - Intelligent chatbot for legal inquiries and guidance
- **SQLite Database** - Lightweight data persistence

## 🏗️ Project Structure

```
LawAi/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── requirements.txt         # Python dependencies
├── apps/                    # Django applications
│   ├── signing/            # Authentication & user management
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── templates/
│   │       └── signing/
│   │           ├── login.html
│   │           └── signup.html
│   ├── dashboard/          # Lawyer dashboard
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── templates/
│   │       └── dashboard/
│   │           └── lawyer_dashboard.html
│   └── chatbot/            # AI-powered chatbot
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── admin.py
│       └── templates/
├── LawAi/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __init__.py
├── services/               # Business logic & services
├── utils/                  # Utility functions
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd LawAi
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

### Running the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 📱 Application Features

### 1. **Signing (Authentication)**
   - User registration (signup)
   - User login
   - Session management
   - User profile management

### 2. **Dashboard**
   - Lawyer dashboard interface
   - Case management
   - Client information
   - Document handling

### 3. **Chatbot**
   - AI-powered legal assistance
   - Interactive chat interface
   - Legal information retrieval
   - Query processing

## 🛠️ Available Commands

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Access Django admin panel
# Navigate to: http://localhost:8000/admin
```

## 📚 API Endpoints

Update this section with your actual routes. Common URLs include:
- `/admin/` - Django admin panel
- `/signing/login/` - User login
- `/signing/signup/` - User registration
- `/dashboard/` - Lawyer dashboard
- `/chatbot/` - AI chatbot interface

## 🗄️ Database

The project uses **SQLite** for data persistence. The database file (`db.sqlite3`) is automatically created when migrations are run.

### Key Models:
- **User** - Extended Django User model
- **Cases** - Legal cases and information
- **Clients** - Client details and information
- **Chat Messages** - Chatbot conversation history

## 🔧 Configuration

### Important Settings in `settings.py`:
- **DEBUG** - Set to `False` in production
- **ALLOWED_HOSTS** - Configure for production deployment
- **SECRET_KEY** - Change in production environment
- **DATABASE** - Configure database settings
- **INSTALLED_APPS** - Register Django apps here

## 🔐 Security Notes

⚠️ **Before deploying to production:**
1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Use environment variables for sensitive data
5. Set up proper HTTPS
6. Configure CSRF settings appropriately

## 📦 Dependencies

Common dependencies (update based on your actual requirements.txt):
- Django 6.0.3
- Python 3.8+

See `requirements.txt` for complete list.

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test apps.signing
python manage.py test apps.dashboard
python manage.py test apps.chatbot
```

## 📝 Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation when adding new features
- Use meaningful commit messages
- Create branches for new features: `feature/feature-name`

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Write/update tests
4. Commit with clear messages
5. Push to repository
6. Create a pull request

## 📞 Support & Contact

For issues or questions, please contact the development team or create an issue in the repository.

## 📄 License

[Add your license information here]

## 🔄 Version History

- **v1.0.0** - Initial release
  - User authentication system
  - Lawyer dashboard
  - AI chatbot integration

---

**Last Updated:** March 2026
