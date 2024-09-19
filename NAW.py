from os import mkdir

app = str(input("escribe el path aquí o el nombre del proyecto: "))
print (app)

while True:
    print("presiona 0 para una estructura de carpetas simple")
    print("presiona 1 para una estructura de carpetas modulada")
    eleccion = str(input("eleccion : "))
    if eleccion == "0":

        path_folder = (app,f"{app}/static"
                    ,f"{app}/static/js",
                    f"{app}/static/css",
                    f"{app}/static/img",
                    f"{app}/templates",
                    f"{app}/templates/layouts",
                    f"{app}/templates/auth")

        path_file = (f"{app}/app.py",f"{app}/templates/index.html")

        content = ("""from flask import Flask, render_template, request, redirect, url_for

        app = Flask(__name__,template_folder="templates",static_url_path='/static')

        @app.route("/")
        def index():
            return render_template("index.html")

        if __name__ == "__main__":
            app.run(debug=True,port=2000)"""
        ,
        """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            
        </body>
        </html>"""
        )

        def new_file(path,content):
            print(path)
            with open(path,"w") as im:
                im.write(content)

        for i in (path_folder):
            try:
                mkdir(i)
            except Exception as e:
                print(e)

        for i in range(2):
            print(i)
            try:
                new_file(path_file[i],content[i])
            except Exception as e:
                print(e)
        break

    elif eleccion == "1":
        path_folder = (app,
            f"{app}/app",
            f"{app}/app/static",
            f"{app}/app/static/js",
            f"{app}/app/static/css",
            f"{app}/app/static/img",
            f"{app}/app/templates",
            f"{app}/app/templates/layouts",
            f"{app}/app/templates/auth")

        path_file = (f"{app}/run.py",
                    f"{app}/app/__init__.py",
                    f"{app}/app/models.py",
                    f"{app}/app/routes.py",
                    f"{app}/app/templates/index.html")

        content = ("""from app import app_web

app = app_web()

if __name__ == "__main__":
    app.run(debug=True,port=2000)"""
        ,"""from flask import Flask

def app_web():

    app = Flask(__name__)
    app.config['SECRET_KEY']="clave muy secreta"

    from .routes import main
    app. register_blueprint(main)

    return app""",
        """import pymysql

def getconn():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        db="data base"
        )

class leer:
    def __init__(self,conn,comand):
        self.data=[]
        try:
            with conn.cursor() as cursor:
                cursor.execute(comand)
                self.data = cursor.fetchall()
            conn.close()
        except Exception as e:
            print(e)
            self.data = None

class commit:
    def __init__(self,conn,comand):
        self.data=[]
        try:
            with conn.cursor() as cursor:
                cursor.execute(comand)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

# tabla = leer(getconn(),"comando para executar mysql")

# print(tabla.data) # extrae la informacion de la db para su uso""",
        """from flask import Blueprint, render_template

main = Blueprint('main', __name__,template_folder="templates",static_url_path='/static')

@main.route('/')
def index():
    return render_template("index.html")""",
        """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            
        </body>
        </html>"""
        )

        def new_file(path,content):
            print(path)
            with open(path,"w") as im:
                im.write(content)

        for i in (path_folder):
            try:
                mkdir(i)
            except Exception as e:
                print(e)

        for i in range(5):
            print(i)
            try:
                new_file(path_file[i],content[i])
            except Exception as e:
                print(e)
        break