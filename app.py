from flask import Flask
from database import db
from models import ImageMetadata

app = Flask(__name__)

# Add config for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realreview.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# Create tables directly (instead of using @app.before_first_request)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Hello from RealReview!"

# Create tables before first request
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

