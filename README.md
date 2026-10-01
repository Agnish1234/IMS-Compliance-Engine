# Production System Hub: IMS Core Engine v1.0.4

Welcome to the official system documentation hub for the **Inventory & Order Management System (IMS) Core Engine**. This enterprise application provides high-performance data persistence, transaction auditing, and responsive analytics interfaces for warehouse logistics tracking.

This documentation suite serves as the singular source of truth (SSoT) for engineering, quality assurance, and technical support divisions.

## Architectural Blueprint

The application leverages a modular, data-driven architecture optimized for local data consistency and rapid analytical reporting:
- **Presentation Layer:** Managed natively through an interactive Streamlit UI engine, enforcing decoupled, asynchronous reactive state loops.
- **Application Logic Layer:** Driven by Python 3.10 microservices handling validation rules, query optimization, and transaction logs.
- **Persistence Layer:** Embedded relational storage via SQLite, leveraging strict constraint definitions, foreign key cascades, and complex transactional triggers.

---

## Quick-Start Installation Framework

Follow these sequential steps to safely configure the execution environment on your local server.

### 1. Prerequisites Configuration
Ensure your operating system environment satisfies the baseline compiler requirements:
- **Python Version:** Python 3.10.x or higher
- **Runtime Environment:** Windows 11 Enterprise x64 / POSIX Compliance Terminal
- **IDE Context:** Visual Studio Code (VS Code) with explicit Python Linter configurations

### 2. Sandbox Setup and Virtual Initialization
Open your system shell and initialize an isolated execution space to eliminate dependency collisions:

```bash
# Clone the system repository
git clone https://github.com/Agnish1234/Web-Development.git
cd Web-Development

# Instantiate the localized virtual environment
python -m venv venv

# Activate the terminal sandbox context
# For Windows environments:
.\venv\Scripts\activate
# For Linux/macOS environments:
source venv/bin/activate
```

### 3. Dependency Injection
Execute standard library packaging to inject core functional tools into your local workspace:

```bash
# Verify baseline system installer tools are optimized
python -m pip install --upgrade pip

# Inject enterprise requirements from the build matrix
pip install streamlit pandas
```

### 4. Database Seeding & Application Launch
Instantiate database migration files and launch the presentation portal:

```bash
# Initialize data schemas and create localized SQLite files
python src/database/seed_engine.py

# Spin up the reactive frontend layer
streamlit run src/app.py
```
