# Hospital Management System

## Overview
The Hospital Management System is a comprehensive web application designed to manage various aspects of hospital operations efficiently. Developed using Django, it provides functionalities for managing patient records, appointments, doctors, and administrative tasks while ensuring data security and accessibility.

## Key Features
- **Patient Management:**
  - Add new patient records.
  - View patient details and medical history.
  - Manage patient appointments.
- **Doctor Management:**
  - Add and manage doctor profiles.
  - Assign doctors to specific departments.
- **Appointment Management:**
  - Schedule appointments for patients with doctors.
  - Notify patients and doctors about upcoming appointments.
- **Administrative Tools:**
  - Manage hospital departments and staff roles.
  - Generate reports on patient demographics, appointments, etc.
- **Security and Access Control:**
  - User authentication and authorization.
  - Role-based access control for different user types (admin, doctor, staff).

## Technologies Used
- **Backend:** Django Framework, Django ORM
- **Frontend:** HTML, CSS, Bootstrap (optional)
- **Database:** MySQL, PostgreSQL (optional)
- **Authentication:** Django's built-in authentication system

## Installation

### Prerequisites
- Python 3.x
- Django
- MySQL or PostgreSQL

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hospital-management-system.git
    cd hospital-management-system
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Configure your database settings in `settings.py`.
    - Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### User Authentication
- **Sign Up:** Register as a new user (admin, doctor, staff).
- **Login:** Use your credentials to access the system.
- **Logout:** Securely log out of the system.

### Patient Management
- **Add Patient:** Enter patient details and medical history.
- **View Patients:** Browse through patient records and details.
- **Manage Appointments:** Schedule, reschedule, or cancel patient appointments.

### Doctor Management
- **Add Doctor Profile:** Include doctor information and specialization.
- **Assign Departments:** Allocate doctors to specific hospital departments.

### Administrative Tools
- **Manage Departments:** Create, edit, or delete hospital departments.
- **Generate Reports:** Obtain reports on patient demographics, appointment statistics, etc.

## Code Overview

### Views
- `index`: Homepage displaying system overview and options.
- `patient_list`: Displays a list of all patients (login required).
- `add_patient`: Form for adding new patient records (login required).
- `edit_patient`: Allows editing patient details (login required).
- `doctor_list`: Lists all doctors registered in the system (login required).
- `add_doctor`: Form for adding new doctors (admin access required).
- `appointment_list`: Shows upcoming appointments (login required).
- `schedule_appointment`: Handles appointment scheduling (login required).
- `department_list`: Lists hospital departments (admin access required).

### Models
- `Patient`: Stores patient information and medical history.
- `Doctor`: Represents doctors with fields for specialization, contact information, etc.
- `Appointment`: Manages patient appointments with related fields for date, time, doctor, etc.
- `Department`: Represents hospital departments with details like name, description, etc.


