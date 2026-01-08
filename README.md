# SocialCore Backend

A clean and scalable Flask backend built to handle public contact messages
submitted through a portfolio website. It exposes a RESTful API that validates
incoming requests using Marshmallow and securely stores data in a MySQL
database via SQLAlchemy. The project follows industry-standard backend
architecture and best practices.

---

<p align="center">
  <img src="https://res.cloudinary.com/darzb0s3m/image/upload/v1767882824/camap_1_fonzr8.webp" alt="Project Preview" width="700">
</p>

---

## 🎯 Purpose

This backend is designed specifically for a **portfolio website contact form**.
When a visitor submits their name, email, and message, the request is validated
and the data is securely stored in a MySQL database. These messages can later
be reviewed directly from the database or exposed through admin APIs.

---

## 📦 Packages

This project uses the following core packages:

- **Flask** – Core web framework
- **Flask-SQLAlchemy** – ORM integration with Flask
- **SQLAlchemy** – Database toolkit
- **PyMySQL** – MySQL database driver
- **Flask-Migrate** – Database migration support
- **Alembic** – Migration engine
- **Marshmallow** – Request data validation
- **python-dotenv** – Environment variable management

All dependencies and versions are defined in `requirements.txt`.

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root directory and define the following
environment variable:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/socialcore
