from os import mkdir
import os

app = str(input("escribe el path aqui"))

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