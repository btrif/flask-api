#  Created by Bogdan Trif on 2021.08.31 , 9:36 AM ; btrif
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# the definition of our application
app = Flask(__name__)


## Make connection to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
## db Model
db = SQLAlchemy(app)




# our data model
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column( db.String(80), unique = True, nullable = False )
    description = db.Column(db.String(120) )


    def __repr__(self):
        return f'{self.name} - {self.description}'




'''
### CONSOLE OPERATIONS L
1.          from application import db
2. from application import Drink
3.        db.create_all()
4.      drink = Drink(name='Grape Soda', description='Tastes like grapes')
        Drink(name='Galbenele tea', description = 'Ceaiul de galbenele e bun pentru aparatul digestiv')
5.     # To add it to our table :
db.session.add(drink)
db.session.commit()
6. you can make queries :

'''




@app.route('/')
def index():
    return 'Hello!'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks :
        drink_data = {'name' : drink.name, 'description' : drink.description }
        output.append(drink_data)


    return {'drinks' : output  }


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({'name' :drink.name , 'description' : drink.description })        # Because a dict we don't have to use jsonify !!!!


@app.route('/drinks', methods =['POST'] )
def add_drink():
    drink = Drink(name=request.json['name'] , description=request.json['description'] )
    db.session.add(drink)
    db.session.commit()
    return { 'id' : drink.id }

@app.route('/drinks/<id>', methods=['DELETE'] )
def delete_drink( id ):
    drink = Drink.query.get(id)
    if drink is None :
        return {'error': 'not found'}
    db.session.delete(drink)
    db.session.commit()
    return {'message' : 'you deleted '+str(drink.name) }