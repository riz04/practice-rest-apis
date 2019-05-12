from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return "Enter 2 numbers & and an operation to perform"

@app.route("/operation" , methods = ["POST"])
def operation():
    # receive the body of the request
    request_body = request.get_json()
    # extract the fields
    first_num = request_body["firstNumber"]
    second_num = request_body["secondNumber"]
    op = request_body["operation"]
    print(first_num)
    print(second_num)
    print(op)
    return jsonify({"message" : " "})


app.run(port = 5000, debug = True)