from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))  # Specify the correct type here

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    return jsonify({'drinks': [str(drink) for drink in drinks]})

    output=[]
    for drink in drinks:
        drink_data = {'name':drink.name, 'description': drink.description}

        output.append(drink_data)

    return{"drinks":output}


# This block is only required if you run the script directly
# instead of using the flask command
if __name__ == "__main__":
    app.run(debug=True)
