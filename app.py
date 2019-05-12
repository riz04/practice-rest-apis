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

    if op == "add":
        result = first_num + second_num
        res_op = "addition"
    elif op == "sub":
        result = first_num - second_num
        res_op = "subtraction"
    elif op == "div":
        result = first_num / second_num
        res_op = "division"
    elif op == "mul":
        result = first_num * second_num
        res_op = "multiplication"
    else:
        result = 0
        res_op = "invalid"

    return jsonify({
        "message" : "success",
        "firstNumber" : first_num,
        "secondNumber" : second_num,
        "operationPerformed" : res_op,
        "result" : result
        })


app.run(port = 5000, debug = True)