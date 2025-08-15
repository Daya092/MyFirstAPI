from flask import Flask

app = Flask (__name__)


@app.route("/espanol/")
@app.route("/")
def saludo_en(nombre="daya"):
    return f"Hello world! {nombre}"

@app.route("/espanol/<nombre>")
def saludo_es(nombre="daya"):
    return f"¡Hola mundo! {nombre}"



@app.route("/frances/<nombre>")
def saludo_fr(nombre="daya"):
    return f"Bonjour le monde! {nombre}"

@app.route("/aleman/<nombre>")
def saludo_de(nombre="daya"):
    return f"Hallo Welt! {nombre}"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=53)