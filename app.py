from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'


@app.route('/post', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = {'message': f'Hello {input_json["name"]}'}
    return jsonify(dictToReturn)


@app.route('/get', methods=["GET"])
def testget():
    response = { }
    response["message"] = "Hello World"
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







# @app.route('/getWithQueryParams', methods=["GET"])
# def testGetWithQueryParams():
#     args = request.args
#     firstname = args.get("firstname")
#     lastname = args.get("lastname")
#     fullname = firstname+" "+lastname
#     dictToReturn = {'Fullname' : fullname}
#     return jsonify(dictToReturn)


# @app.route('/getWithPathParams/<fname>/<lname>', methods = ["GET"])
# def testGetWithPathParams(fname,lname):
#         #name = request.view_args['name']
#         dictToReturn = {'first_name' : fname, 'lastname': lname}
#         return jsonify(dictToReturn)

