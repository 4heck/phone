from app import app
from models import Customer
from models import Owner
from models import Deal
from models import Film
from flask import jsonify
from flask import request
from app import db
import json

#api's for customer
@app.route('/api/customer', methods=['GET'])
def api_customer_get():
    customers = Customer.query.all()
    customers_json = [{"id": customer.id, "name": customer.name}
                  for customer in customers]
    return jsonify(customers_json)

@app.route('/api/customer/<id>', methods=['GET'])
def api_customer_get_id(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/customer', methods=['POST'])
def api_customer_insert():
    new_customer = request.get_json()
    customer = Customer(id=new_customer['id'], name=new_customer['name'])
    db.session.add(customer)
    db.session.commit()
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/customer/<id>', methods=['DELETE'])
def api_customer_delete(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    db.session.delete(customer)
    db.session.commit()
    return jsonify()

@app.route('/api/customer/<id>', methods=['PUT'])
def api_customer_update(id):
    updated_customer = request.get_json()
    customers_to_update = Customer.query.filter_by(id=id)
    data = json.loads(request.get_data())
    customer_to_update = customers_to_update[0]
    customer_to_update = db.session.query(Customer).filter_by(id = id).first()
    customer_to_update.name = data['name']
    db.session.commit()
    return jsonify(customer_to_update.to_dict())

#api's for owner
@app.route('/api/owner', methods=['GET'])
def api_owner_get():
    owners = Owner.query.all()
    owners_json = [{"id": owner.id, "name": owner.name}
                  for owner in owners]
    return jsonify(owners_json)

@app.route('/api/owner/<id>', methods=['GET'])
def api_owner_get_id(id):
    owners = Owner.query.filter_by(id=id)
    if not owners:
        abort(404)
    owner = owners[0]
    owner_json = {"id": owner.id, "name": owner.name}
    return jsonify(owner_json)

@app.route('/api/owner', methods=['POST'])
def api_owner_insert():
    new_owner = request.get_json()
    owner = Owner(id=new_owner['id'], name=new_owner['name'])
    db.session.add(owner)
    db.session.commit()
    owner_json = {"id": owner.id, "name": owner.name}
    return jsonify(owner_json)

@app.route('/api/owner/<id>', methods=['DELETE'])
def api_owner_delete(id):
    owners = Owner.query.filter_by(id=id)
    if not owners:
        abort(404)
    owner = owners[0]
    db.session.delete(owner)
    db.session.commit()
    return jsonify()

@app.route('/api/owner/<id>', methods=['PUT'])
def api_owner_update(id):
    updated_owner = request.get_json()
    owners_to_update = Owner.query.filter_by(id=id)
    data = json.loads(request.get_data())
    owner_to_update = owners_to_update[0]
    owner_to_update = db.session.query(Owner).filter_by(id = id).first()
    owner_to_update.name = data['name']
    db.session.commit()
    return jsonify(owner_to_update.to_dict())

#api's for deal
@app.route('/api/deal', methods=['GET'])
def api_deal_get():
    deals = Deal.query.all()
    deals_json = [{"id": deal.id, "owner": deal.owner, "customer": deal.customer, "film": deal.film}
                  for deal in deals]
    return jsonify(deals_json)

@app.route('/api/deal/<id>', methods=['GET'])
def api_deal_get_id(id):
    deals = Deal.query.filter_by(id=id)
    if not deals:
        abort(404)
    deal = deals[0]
    deal_json = {"id": deal.id, "owner": deal.owner, "customer": deal.customer, "film": deal.film}
    return jsonify(deal_json)

@app.route('/api/deal', methods=['POST'])
def api_deal_insert():
    new_deal = request.get_json()
    deal = Deal(id=new_deal['id'], owner=new_deal['owner'], customer=new_deal['customer'], film=new_deal['film'])
    db.session.add(deal)
    db.session.commit()
    deal_json = {"id": deal.id, "owner": deal.owner, "customer": deal.customer, "film": deal.film}
    return jsonify(deal_json)

@app.route('/api/deal/<id>', methods=['DELETE'])
def api_deal_delete(id):
    deals = Deal.query.filter_by(id=id)
    if not deals:
        abort(404)
    deal = deals[0]
    db.session.delete(deal)
    db.session.commit()
    return jsonify()

@app.route('/api/deal/<id>', methods=['PUT'])
def api_deal_update(id):
    updated_deal = request.get_json()
    deals_to_update = Deal.query.filter_by(id=id)
    data = json.loads(request.get_data())
    deal_to_update = deals_to_update[0]
    deal_to_update = db.session.query(Deal).filter_by(id = id).first()
    deal_to_update.owner = data['owner']
    deal_to_update.customer = data['customer']
    deal_to_update.film = data['film']
    db.session.commit()
    return jsonify(deal_to_update.to_dict())
    
#api's for film
@app.route('/api/film', methods=['GET'])
def api_film_get():
    films = Film.query.all()
    films_json = [{"id": film.id, "name": film.name, "duration": film.duration, "year": film.year}
                  for film in films]
    return jsonify(films_json)

@app.route('/api/film/<id>', methods=['GET'])
def api_film_get_id(id):
    films = Film.query.filter_by(id=id)
    if not films:
        abort(404)
    film = films[0]
    film_json = {"id": film.id, "name": film.name, "duration": film.duration, "year": film.year}
    return jsonify(film_json)

@app.route('/api/film', methods=['POST'])
def api_film_insert():
    new_film = request.get_json()
    film = Film(id=new_film['id'], name=new_film['name'], duration=new_film['duration'], year=new_film['year'])
    db.session.add(film)
    db.session.commit()
    film_json = {"id": film.id, "name": film.name, "duration": film.duration, "year": film.year}
    return jsonify(film_json)

@app.route('/api/film/<id>', methods=['DELETE'])
def api_film_delete(id):
    films = Film.query.filter_by(id=id)
    if not films:
        abort(404)
    film = films[0]
    db.session.delete(film)
    db.session.commit()
    return jsonify()

@app.route('/api/film/<id>', methods=['PUT'])
def api_film_update(id):
    updated_film = request.get_json()
    films_to_update = Film.query.filter_by(id=id)
    data = json.loads(request.get_data())
    film_to_update = films_to_update[0]
    film_to_update = db.session.query(Film).filter_by(id = id).first()
    film_to_update.name = data['name']
    film_to_update.duration = data['duration']
    film_to_update.year = data['year']
    db.session.commit()
    return jsonify(film_to_update.to_dict())
