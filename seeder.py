from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding...")
            
            seed_users = [
                User(
                    fname="Admin",
                    mname="admin",
                    lname="Admin",
                    username="User",
                    email="admin@test.com",
                    pass_word=generate_password_hash("admin123"),
                    birthday="1990-01-01",
                    gender="Male",
                    phonenumber="1234567890",
                    address="123 Admin St, City, Country",
                    student_id="A0001"         
                ),
                User(
                    fname="Julian",
                    mname="B",
                    lname="Parco",
                    username="Kusabimaru",
                    email="juricparcome@gmail.com",
                    pass_word=generate_password_hash("admin1234"),
                    birthday="2004-12-19",
                    gender="Male",
                    phonenumber="09363209985",
                    address="14 Avenue Socorro, Quezon City, Metoro Manila",
                    student_id="A0002" 
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
            print(f"Integrity Error during seeding: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLAlchemy Error during seeding: {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()
                
