from flask import Flask, request
from flask import render_template
from flask_nav import Nav
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_nav.elements import Navbar, View

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

db.create_all()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Text)

    def __init__(self, item):
        self.item = item
        self.done = False

    def __repr__(self):
        return '<Item %s>' % self.item


db.create_all()


@app.route('/items')
def datas_list():
    datas = Item.query.all()
    return render_template('shoppingList.html', datas=datas)


@app.route('/data', methods=['POST'])
def additem():
    item = request.form['item']
    if item:
        data = Item(item)
        db.session.add(data)
        db.session.commit()
        return redirect('/items')
    return 'Item not aadded'
    


@app.route('/delete/<id>')
def deleteitem(id):
    data = Item.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/items')

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myRecipes')
def recipes():
    return render_template('mR.html')

@app.route('/mylist')
def list():
    return render_template('shoppingList.html')

@app.route('/about')
def displayAbout():
    return render_template('about.html')

@app.route('/login')
def logIn():
    return render_template('login.html')

@app.route('/signup')
def signUp():
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

    