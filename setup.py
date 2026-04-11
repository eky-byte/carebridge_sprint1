# run in flask shell: from setup import setup; setup()
# delete instance/carebridge.db first if you want a clean file
from extensions import db
from models import seed_schedules

from app import app


def setup():
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_schedules()
        db.session.commit()
