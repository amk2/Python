from flask import Flask, request, render_template

app = Flask("wtf")

@app.route("/hello/")
def hello():
      return "hello"
#     return render_template("lista_de_noticias.html", noticias=noticias)


app.run(debug=True, port=8080, threaded=True)