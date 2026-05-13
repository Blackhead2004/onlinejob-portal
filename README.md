# 🚀 Online Job Portal

A full-stack web application that connects job seekers with employers, built with **Python Flask** and **MongoDB**. Features intelligent job matching, application tracking, and comprehensive admin dashboard for efficient recruitment management.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Latest-green?logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Database Schema](#-database-schema)
- [API Endpoints](#-api-endpoints)
- [User Roles](#-user-roles)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🔐 Authentication & Authorization
- User registration for candidates and companies
- Secure password hashing with bcrypt
- Role-based access control (Admin, Company, Candidate)
- Session management

### 💼 Job Posting & Browsing
- Companies can post jobs with detailed requirements
- Advanced search filters (location, experience, job type, salary range)
- Full-text search across job titles, tags, and locations
- Job detail pages with applicant count

### 📝 Job Applications
- Candidates can apply to multiple jobs
- Resume upload and storage (PDF, DOC, DOCX)
- Cover letter submission
- Application status tracking (Pending, Approved, Rejected)

### 👤 User Profiles
- Candidate profiles with education, skills, and projects
- Company profiles with detailed information
- Resume management and download

### 📊 Dashboards
- **Candidate Dashboard**: Track applied jobs and application status
- **Company Dashboard**: View posted jobs and applicants
- **Admin Dashboard**: System statistics and recent activity

### 📞 Contact & Support
- Contact form for inquiries
- About page with company information

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python Flask |
| **Database** | MongoDB |
| **File Storage** | GridFS (MongoDB) |
| **Authentication** | Flask-Bcrypt |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Session Management** | Flask Sessions |

---

## 📁 Project Structure

```
onlinejob-portal/
│
├── app.py                    # Main Flask application
├── config.py                 # Database and configuration
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
│
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├── home.html            # Homepage
│   ├── login.html           # Login page
│   ├── candidate_signup.html # Candidate registration
│   ├── company_signup.html  # Company registration
│   ├── job_detail.html      # Job details page
│   ├── apply_step1.html     # Application form
│   ├── apply_success.html   # Success message
│   ├── dashboard_candidate.html # Candidate dashboard
│   ├── dashboard_company.html   # Company dashboard
│   ├── dashboard_admin.html     # Admin dashboard
│   ├── post_job.html        # Job posting form
│   ├── profile.html         # User profile
│   ├── about.html           # About page
│   └── contact.html         # Contact page
│
├── static/                   # Static files
│   ├── css/                 # Stylesheets
│   └── js/                  # JavaScript files
│
├── uploads/                  # Resume uploads
│
└── README.md                # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- MongoDB (local or Atlas)
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Blackhead2004/onlinejob-portal.git
cd onlinejob-portal
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
# MongoDB Connection
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB_NAME=job_portal_db

# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### Step 5: Setup MongoDB

**Option A: Local MongoDB**
```bash
# Make sure MongoDB is running on port 27017
mongod
```

**Option B: MongoDB Atlas (Cloud)**
- Create an account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Create a cluster and get the connection string
- Replace `MONGODB_URI` in `.env` with your Atlas connection string

### Step 6: Run the Application

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

---

## ⚙️ Configuration

### Sample Data Initialization

On first run, the application automatically creates:
- **Admin Account**: `admin@gmail.com` / `admin123`
- **Sample Company**: `hr@zoho.com` / `zoho123`
- **Sample Candidate**: `aman@example.com` / `aman123`
- **Sample Jobs**: 2 internship and full-time positions

### File Upload Settings

Supported file types for resume uploads:
- `.pdf` - PDF documents
- `.doc` - Microsoft Word (.doc)
- `.docx` - Microsoft Word (.docx)

Maximum upload size: Configurable in Flask settings (default: 16MB)

---

## 💻 Usage

### For Job Seekers (Candidates)

1. **Sign Up**: Create an account with your details, education, and skills
2. **Browse Jobs**: Search for jobs using filters and keywords
3. **Apply**: Submit applications with cover letters
4. **Track Applications**: Monitor your application status in the dashboard
5. **Download Resume**: View and download your resume from profile

### For Employers (Companies)

1. **Register**: Create a company account
2. **Post Jobs**: List job openings with detailed requirements
3. **View Applications**: See all applicants for your jobs
4. **Download Resumes**: Access candidate resumes for review
5. **Track Metrics**: Monitor total applicants and job postings

### For Administrators

1. **Login**: Use admin credentials
2. **Dashboard**: View system statistics and recent activity
3. **Manage System**: Monitor total jobs, candidates, companies, and applications
4. **Review Activity**: Check recent job postings and applications

---

## 📸 Screenshots

### 🏠 Homepage - "Find Your Dream Job"
Browse available job opportunities with advanced search and filters.
![Homepage](https://imgur.com/placeholder1.png)

### 👤 Candidate Registration
Create a candidate account with education, skills, and resume upload.
![Candidate Registration](https://imgur.com/placeholder2.png)

### 🏢 Company Registration
Register your company to start posting job openings.
![Company Registration](https://imgur.com/placeholder3.png)

### 🔐 Login Page
Secure login for all user types (Candidate, Company, Admin).
![Login](https://imgur.com/placeholder4.png)

---

## 🗄️ Database Schema

### Collections

#### `candidates`
```json
{
  "_id": ObjectId,
  "first_name": "String",
  "last_name": "String",
  "email": "String (unique)",
  "password": "String (hashed)",
  "gender": "String",
  "location": "String",
  "skills": "String",
  "education": {
    "xth": "String",
    "xiith": "String",
    "ug": "String",
    "pg": "String"
  },
  "experience": "String",
  "projects": "String",
  "resume_file_id": "ObjectId (GridFS)",
  "created_at": "DateTime"
}
```

#### `companies`
```json
{
  "_id": ObjectId,
  "company_name": "String",
  "email": "String (unique)",
  "password": "String (hashed)",
  "address": "String",
  "created_at": "DateTime"
}
```

#### `jobs`
```json
{
  "_id": ObjectId,
  "title": "String",
  "location": "String",
  "job_type": "String (Full Time/Internship/Part Time)",
  "vacancy": "Integer",
  "salary": "String",
  "description": "String",
  "experience": "String",
  "tags": "String",
  "gender": "String",
  "deadline": "Date",
  "company_email": "String",
  "posted_date": "DateTime"
}
```

#### `applications`
```json
{
  "_id": ObjectId,
  "candidate_email": "String",
  "candidate_name": "String",
  "job_id": "String",
  "resume_id": "ObjectId (GridFS)",
  "cover_letter": "String",
  "status": "String (pending/approved/rejected)",
  "date_applied": "DateTime"
}
```

---

## 🔌 API Endpoints

### Authentication Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/candidate_signup` | Candidate registration |
| GET/POST | `/company_signup` | Company registration |
| GET/POST | `/login` | User login |
| GET | `/logout` | User logout |

### Job Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage with latest jobs |
| GET | `/job/<job_id>` | Job details page |
| GET/POST | `/apply/<job_id>` | Apply for a job |

### Company Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/post_job` | Post a new job |

### User Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard` | User dashboard |
| GET | `/profile` | User profile |
| GET | `/resume/<resume_id>` | Download resume |

### Static Pages

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/about` | About page |
| GET/POST | `/contact` | Contact form |

---

## 👥 User Roles

### 1. **Admin**
- System overview and statistics
- Monitor total jobs, candidates, companies
- View recent activity and applications

### 2. **Company**
- Post and manage job listings
- View applications for posted jobs
- Download candidate resumes

### 3. **Candidate**
- Browse and search jobs
- Apply for positions
- Track application status
- Upload and manage resume

---

## 🎨 Key Features in Detail

### Advanced Search
- Filter by location, job type, experience level
- Full-text search across job titles and descriptions
- Salary range filtering

### File Management
- Secure resume upload using GridFS
- Multiple file format support
- Download management

### Session Management
- Secure session handling
- Role-based redirects
- Login requirement enforcement

### Data Validation
- Email uniqueness validation
- Form input validation
- File type validation for uploads

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python
- Add comments for complex logic
- Test your changes before submitting PR
- Update README if adding new features

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Support & Contact

For support, questions, or suggestions:
- Create an issue on GitHub
- Use the Contact form in the application
- Email: [Your Email]

---

## 🎯 Future Enhancements

- [ ] Email notifications for applications
- [ ] Advanced analytics and reporting
- [ ] User reviews and ratings
- [ ] Job recommendations using ML
- [ ] Mobile app integration
- [ ] Payment gateway integration
- [ ] Two-factor authentication
- [ ] API documentation with Swagger

---

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Python Best Practices](https://www.python.org/dev/peps/pep-0008/)

---

<div align="center">

**Made with ❤️ by [Blackhead2004](https://github.com/Blackhead2004)**

⭐ If you found this helpful, please consider giving it a star!

</div>
