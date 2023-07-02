from flask import Flask, jsonify, request

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
# app.config["ENV"] = "development"
# # print(app.config["ENV"])

@app.route("/", methods=["GET", "POST"])
def homepage():
  '''_summary_
  '''
  # data = request.get_json()
  # print(data)
  return jsonify( {
    "code": 0,
    "data": {
      "info": "homepage",
      "name": "pengfei1.tang",
      "email": "pengfei1.tang@momenta.ai"
    }
  })


@app.route("/lacar/history", methods=["GET", "POST"])
def get_lacar_log_history():
  '''_summary_
  '''
  # data = request.get_json()
  # print(data)
  return {
    "code": 0,
    "data": {
      "info": "history",
      "name": "pengfei1.tang",
      "email": "pengfei1.tang@momenta.ai"
    }
  }

# @app.route("/user/login", methods=["POST"])
# def user_login():
#   '''_summary_
#   '''
#   data = request.get_json()
#   user_name = data.get("user_name")
#   passwd = data.get("passwd")
#   if user_name == "admin" and passwd == "123456":
#     return jsonify({
#       "code": 0,
#       "data": {
#         "token": "666666"
#       }
#     })
#   else:
#     return jsonify({
#       "code": 1,
#       "msg": "用户名或密码错误"
#     })

# @app.route("/user/info", methods=["GET", "POST"])
# def user_info():
#   print("hello")
#   token = request.headers.get("token")
#   if token == "666666":
#     return jsonify({
#       "code": 0,
#       "data": {
#         "id": "1",
#         "user_name": "admin",
#         "real_name": "zhangsan",
#         "user_type": 1
#       }
#     })
#   return jsonify({
#     "code": 2,
#     "msg": "账户不存在或已过期"
#   })

# if __name__ == "__main__":
#   app.run(host="0.0.0.0")