from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import gridfs
import io
import os

app = Flask(__name__)
app.secret_key = "supersecretkey1234567890abcdef"
bcrypt = Bcrypt(app)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["job_portal_db"]
fs = gridfs.GridFS(db)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Initialize Database with Sample Data
def initialize_database():
    if "companies" not in db.list_collection_names():
        print("🔥 Creating database with sample data...")

        # Admin Account
        db.admin.insert_one({
            "email": "admin@gmail.com",
            "password": bcrypt.generate_password_hash("admin123").decode("utf-8")
        })

        # Sample Company
        db.companies.insert_one({
            "company_name": "Zoho Corporation",
            "email": "hr@zoho.com",
            "password": bcrypt.generate_password_hash("zoho123").decode("utf-8"),
            "address": "Chennai, Tamil Nadu",
            "created_at": datetime.now()
        })

        # Sample Candidate
        db.candidates.insert_one({
            "first_name": "Aman", "last_name": "Verma", "email": "aman@example.com",
            "password": bcrypt.generate_password_hash("aman123").decode("utf-8"),
            "gender": "Male", "location": "Bangalore, India",
            "skills": "Python, Flask, MongoDB, HTML, CSS, JavaScript",
            "education": {"xth": "85%", "xiith": "82%", "ug": "80%", "pg": "N/A"},
            "experience": "Fresher", "projects": "Job Portal, Billing System",
            "resume_file_id": None, "created_at": datetime.now()
        })

        # Sample Jobs
        sample_jobs = [
            {
                "title": "Python Developer Intern", "location": "Bangalore, Karnataka",
                "job_type": "Internship", "vacancy": 3, "salary": "₹18,000/month",
                "description": "Build REST APIs using Flask & MongoDB. Work on real projects.",
                "experience": "0-1 Years", "tags": "Python, Flask, MongoDB, Backend",
                "gender": "Any", "deadline": "2026-03-15", "company_email": "hr@zoho.com",
                "posted_date": datetime.now()
            },
            {
                "title": "Full Stack Developer", "location": "Pune, Maharashtra",
                "job_type": "Full Time", "vacancy": 5, "salary": "₹6-10 LPA",
                "description": "Complete web app development with modern stack.",
                "experience": "1-3 Years", "tags": "Python, React, Node.js, MongoDB",
                "gender": "Any", "deadline": "2026-02-28", "company_email": "hr@zoho.com",
                "posted_date": datetime.now()
            }
        ]
        db.jobs.insert_many(sample_jobs)

        # Create Indexes
        db.jobs.create_index([("title", "text"), ("tags", "text"), ("location", "text")])
        db.companies.create_index("email", unique=True)
        db.candidates.create_index("email", unique=True)

        print("✅ Database initialized with sample data!")


initialize_database()


# ================= AUTHENTICATION ROUTES =================
@app.route("/candidate_signup", methods=["GET", "POST"])
def candidate_signup():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        resume_id = None

        if resume_file and allowed_file(resume_file.filename):
            resume_id = fs.put(resume_file.read(), filename=resume_file.filename)

        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"]).decode("utf-8"),
            "gender": request.form["gender"],
            "location": request.form["location"],
            "skills": request.form["skills"],
            "education": {
                "xth": request.form["xth"], "xiith": request.form["xiith"],
                "ug": request.form["ug"], "pg": request.form["pg"]
            },
            "experience": request.form["experience"],
            "projects": request.form["projects"],
            "resume_file_id": resume_id,
            "created_at": datetime.now()
        }

        try:
            db.candidates.insert_one(data)
            flash("🎉 Account created successfully! Please login.")
            return redirect(url_for("login"))
        except Exception as e:
            flash("❌ Email already exists! Please use different email.")

    return render_template("candidate_signup.html")


@app.route("/company_signup", methods=["GET", "POST"])
def company_signup():
    if request.method == "POST":
        data = {
            "company_name": request.form["company_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"]).decode("utf-8"),
            "address": request.form["address"],
            "created_at": datetime.now()
        }

        try:
            db.companies.insert_one(data)
            flash("🎉 Company registered successfully! Please login.")
            return redirect(url_for("login"))
        except Exception:
            flash("❌ Email already exists!")

    return render_template("company_signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = (db.admin.find_one({"email": email}) or
                db.candidates.find_one({"email": email}) or
                db.companies.find_one({"email": email}))

        if user and bcrypt.check_password_hash(user["password"], password):
            session["user"] = email
            if "company_name" in user:
                session["role"] = "company"
                session["name"] = user["company_name"]
            elif "first_name" in user:
                session["role"] = "candidate"
                session["name"] = f"{user['first_name']} {user['last_name']}"
            else:
                session["role"] = "admin"
                session["name"] = "Administrator"

            flash(f"👋 Welcome back, {session['name'][:20]}!")

            next_url = session.pop("next_url", None)
            return redirect(next_url or url_for("dashboard"))

        flash("❌ Invalid email or password!")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("👋 Logged out successfully!")
    return redirect(url_for("home"))


# ================= BASIC PAGES =================
@app.route("/")
def home():
    jobs = list(db.jobs.find().sort("posted_date", -1).limit(12))
    for job in jobs:
        job["_id"] = str(job["_id"])
    return render_template("home.html", jobs=jobs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        db.contacts.insert_one({
            "name": request.form["name"],
            "email": request.form["email"],
            "message": request.form["message"],
            "date": datetime.now()
        })
        flash("📧 Message sent successfully! We'll get back to you soon.")
    return render_template("contact.html")


# ================= JOB ROUTES =================
@app.route("/job/<job_id>")
def job_detail(job_id):
    try:
        job = db.jobs.find_one({"_id": ObjectId(job_id)})
        if not job:
            flash("❌ Job not found!")
            return redirect(url_for("home"))
        job["_id"] = str(job["_id"])
        applicant_count = db.applications.count_documents({"job_id": job_id})
        return render_template("job_detail.html", job=job, applicant_count=applicant_count)
    except:
        flash("❌ Invalid job!")
        return redirect(url_for("home"))


@app.route("/apply/<job_id>", methods=["GET", "POST"])
def apply(job_id):
    if "user" not in session or session.get("role") != "candidate":
        session["next_url"] = url_for("apply", job_id=job_id)
        flash("🔐 Please login as candidate to apply")
        return redirect(url_for("login"))

    if request.method == "POST":
        candidate = db.candidates.find_one({"email": session["user"]})
        db.applications.insert_one({
            "candidate_email": session["user"],
            "candidate_name": f"{candidate['first_name']} {candidate['last_name']}",
            "job_id": job_id,
            "resume_id": candidate.get("resume_file_id"),
            "cover_letter": request.form.get("cover_letter", ""),
            "status": "pending",
            "date_applied": datetime.now()
        })
        return render_template("apply_success.html", job_id=job_id)

    try:
        job = db.jobs.find_one({"_id": ObjectId(job_id)})
        if not job:
            flash("❌ Job not found!")
            return redirect(url_for("home"))
        job["_id"] = str(job["_id"])
        return render_template("apply_step1.html", job=job, job_id=job_id)
    except:
        flash("❌ Invalid job!")
        return redirect(url_for("home"))


# ================= COMPANY ROUTES =================
@app.route("/post_job", methods=["GET", "POST"])
def post_job():
    if session.get("role") != "company":
        flash("🔐 Only companies can post jobs")
        return redirect(url_for("login"))

    if request.method == "POST":
        job_data = {
            "title": request.form["title"],
            "location": request.form["location"],
            "job_type": request.form["job_type"],
            "vacancy": int(request.form["vacancy"]),
            "salary": request.form["salary"],
            "description": request.form["description"],
            "experience": request.form["experience"],
            "tags": request.form["tags"],
            "gender": request.form["gender"],
            "deadline": request.form["deadline"],
            "company_email": session["user"],
            "posted_date": datetime.now()
        }
        db.jobs.insert_one(job_data)
        flash("✅ Job posted successfully!")
        return redirect(url_for("dashboard"))

    return render_template("post_job.html")


# ================= RESUME DOWNLOAD =================
@app.route("/resume/<resume_id>")
def download_resume(resume_id):
    try:
        file_doc = fs.get(ObjectId(resume_id))
        return send_file(io.BytesIO(file_doc.read()),
                         download_name=file_doc.filename,
                         as_attachment=True)
    except:
        flash("❌ Resume not found!")
        return redirect(url_for("dashboard"))


# ================= DASHBOARDS =================
@app.route("/dashboard")
def dashboard():
    if "role" not in session:
        return redirect(url_for("login"))

    role = session["role"]

    if role == "candidate":
        applied_jobs = []
        for app in db.applications.find({"candidate_email": session["user"]}).sort("date_applied", -1):
            job = db.jobs.find_one({"_id": ObjectId(app["job_id"])})
            applied_jobs.append({
                "job_title": job["title"] if job else "Job Removed",
                "company": job["company_email"] if job else "N/A",
                "job_id": app["job_id"],
                "date_applied": app["date_applied"],
                "status": app.get("status", "pending")
            })
        return render_template("dashboard_candidate.html", applied=applied_jobs)

    elif role == "company":
        company_jobs = []
        total_applicants = 0

        for job in db.jobs.find({"company_email": session["user"]}).sort("posted_date", -1):
            applicants = db.applications.count_documents({"job_id": str(job["_id"])})
            total_applicants += applicants
            company_jobs.append({
                "title": job["title"],
                "deadline": job["deadline"],
                "posted_date": job["posted_date"],
                "applicants": applicants,
                "job_id": str(job["_id"])
            })

        return render_template("dashboard_company.html", jobs=company_jobs, total_applicants=total_applicants)

    elif role == "admin":
        # 🔥 ADMIN DASHBOARD
        total_jobs = db.jobs.count_documents({})
        total_candidates = db.candidates.count_documents({})
        total_companies = db.companies.count_documents({})
        total_applications = db.applications.count_documents({})

        recent_jobs = list(db.jobs.find().sort("posted_date", -1).limit(5))
        recent_applications = list(db.applications.find().sort("date_applied", -1).limit(5))

        for job in recent_jobs:
            job["_id"] = str(job["_id"])
        for app in recent_applications:
            app["job_id"] = str(app["job_id"])

        return render_template("dashboard_admin.html",
                               total_jobs=total_jobs,
                               total_candidates=total_candidates,
                               total_companies=total_companies,
                               total_applications=total_applications,
                               recent_jobs=recent_jobs,
                               recent_applications=recent_applications)

    return redirect(url_for("home"))


@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login"))

    role = session["role"]
    if role == "candidate":
        user = db.candidates.find_one({"email": session["user"]})
    elif role == "company":
        user = db.companies.find_one({"email": session["user"]})
    else:
        user = {"email": session["user"], "role": "Administrator"}

    return render_template("profile.html", user=user)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
