from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:2952@localhost:5432/recipe"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text(),nullable=False)
    
    
    def __repr__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        return cls.query.getall()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def save(self):
        db.session.add(self)
        db.session.commit()    


class RecipeSchema(Schema):
    id=fields.Integer()
    name= fields.String()
    description= fields.String()      



@app.route('/recipes',methods=['GET'])
def get_all_recipes():
    recipes=Recipe.get_all()
    serializer=RecipeSchema(many=True)
    data= serializer.dump(recipes)
    
    return jsonify(
        data
    )
    
    
@app.route('/recipes',methods=['POST'])
def create_a_recipes():
    pass

@app.route('/recipe/<int:id>',methods=['GET'])
def get_recipe(id):
    pass

@app.route('/recipe/<int:id>',methods=['PUT'])
def update_recipe(id):
    pass

@app.route('/recipe/<int:id>',methods=['DELETE'])
def delete_recipe(id):
    pass




if __name__ == '__main_':
    app.run(debug=True)
