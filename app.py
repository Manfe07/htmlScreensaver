from flask import Flask, render_template, redirect
import yaml

import hass
import background

app = Flask(__name__)

conf = yaml.safe_load(open("config.yml"))
print(conf)
hass.hassioHost = conf['hass-io']['host']
hass.token = conf['hass-io']['token']


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/api/getTemperatur")
def api_temperatur():
    return hass.getTemperatur()


@app.route("/api/getImage")
def api_image():
    img = background.getImage()
    return redirect("/static/backgrounds/" + img)


@app.route("/api/getImageList")
def api_imageList():
    return background.getImageList()



# main driver function
if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=conf['flask']['port'],
        debug=True)
