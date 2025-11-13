from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding...")

            seed_users = [
                User(
                    FirstName="Julian Eric",
                    LastName="Parco",
                    Username="Admin",
                    email="juricparcome@gmail.com",
                    password=generate_password_hash("admin123"),
                    Birthdate="2004-12-19",
                    Gender="Male",
                    Phone="09363209985",
                    Address="Cubao, Quezon City, Metropolitan Manila",
                    StudentID="2023-11762-MN-0"
                ),
                User(
                    FirstName="Robert",
                    LastName="Robertson",
                    Username="Admin2",
                    email="example@gmail.com",
                    password=generate_password_hash("admin123"),
                    Birthdate="2000-01-01",
                    Gender="Male",
                    Phone="09171234567",
                    Address="Makati City, Metropolitan Manila",
                    StudentID="2023-11763-MN-0"     
                ),
                User(
                    FirstName="Jaecy",
                    LastName="De Vera",
                    Username="Admin3",
                    email="jaecydevera36@gmail.com",
                    password=generate_password_hash("MasterPogi"),
                    Birthdate="2000-10-20",
                    Gender="Male",
                    Phone="09171234567",
                    Address="Antipolo City, Rizal",
                    StudentID="2023-10608-MN-0"
                )
            ]
            
            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)

            db.session.commit()
            print("Database seeding completed successfully.")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error during seeding: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Database error during seeding: {e}")

        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()