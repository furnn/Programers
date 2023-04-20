from flask import Flask, request, jsonify

app=Flask(__name__)

weapon = {}

@app.route('/whoami', methods=['GET'])
def githubid():
    name={
        "name" : "furnn"
    }
    return jsonify((name))
    
@app.route('/echo', methods=['GET'])
def echo():
    n=request.args.get("string")
    print(n, type(n))
    return n


@app.route('/Create', methods=['GET'])
def create():
    name=request.args.get("name")
    stock=request.args.get("stock")
    if name in weapon.keys():
        return "Already exists"
    weapon[name]=int(stock)
    return jsonify(weapon)


@app.route('/Read', methods=['GET'])
def read():
    return jsonify(weapon)

@app.route('/Update', methods=['GET'])
def update():
    name=request.args.get("name")
    newname=request.args.get("newname")
    stock=request.args.get("stock")

    if name not in weapon.keys():
        return "No such weapon"

    if newname:
        if stock:
            weapon[newname]=int(stock)
        else:
            weapon[newname]=weapon.pop(name)
    
    else:
        weapon[name]=int(stock)

    return jsonify(weapon)

@app.route('/Delete', methods=['GET'])
def delete():
    name=request.args.get("name")
    weapon.pop(name)
    return jsonify(weapon)