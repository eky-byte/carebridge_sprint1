from extensions import db

# lookup table: each medication schedule (one row per schedule)
class Schedule(db.Model):
    __tablename__ = "schedule"
    id = db.Column(db.Integer, primary_key=True)
    med_name = db.Column(db.String(80), nullable=False)
    dosage = db.Column(db.String(80), nullable=False)
    time_of_day = db.Column(db.String(40), nullable=False)


# many dose logs can point to one schedule (many-to-one)
class DoseLog(db.Model):
    __tablename__ = "dose_log"
    id = db.Column(db.Integer, primary_key=True)
    when = db.Column(db.DateTime, nullable=False)
    day = db.Column(db.String(10), nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey("schedule.id"), nullable=False, index=True)
    username = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    schedule = db.relationship("Schedule", backref="dose_logs")


DEFAULT_SCHEDULES = [
    {"med_name": "Aspirin", "dosage": "1 tablet", "time_of_day": "morning"},
    {"med_name": "Vitamin D", "dosage": "1 capsule", "time_of_day": "evening"},
]


def seed_schedules():
    # insert default rows; call inside app context after create_all
    for row in DEFAULT_SCHEDULES:
        db.session.add(Schedule(**row))
