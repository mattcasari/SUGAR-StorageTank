from machine import reset
from src.utils.microdot import Microdot, Response, send_file
from src.utils.sensors.sensors import create_distance_sensor
from src.storage_tank import StorageTank
from src.utils.math.volumes.volume import get_volume_obj

import json

with open("config.json", "r") as file:
    config = json.load(file)

app = Microdot()

sensor = create_distance_sensor(config["sensor"])
lower_tank = get_volume_obj(config["tank"]["lower_tank"])
upper_tank = get_volume_obj(config["tank"]["upper_tank"])

tank = StorageTank(
    sensor.read_range,
    lower_tank=lower_tank,
    upper_tank=upper_tank,
    mounted_distance=config["sensor"]["mounted_distance"],
)
current_task = None
Response.default_content_type = "text/html"


@app.route("/volume")
async def get_volume(request):
    #
    print("volume request received")
    return str(tank.read_tank()[0])


@app.route("/")
async def main(request):
    global tank
    # return send_file("index.html")
    print("\nMain page request received")
    with open("index.html") as f:
        html = f.read()

    (volume, depth) = (None, None)

    try:
        (volume, depth) = tank.read_tank()
    except:
        pass
    # volume = tank.get_volume_average(3)

    if volume >= 0:
        percent = 100 * volume / tank.TOTAL_VOLUME_GALLONS

        html = html.replace("TANK_VOLUME", f"{volume:.0f}")
        html = html.replace("TANK_PERCENT", f"{percent:.0f}")
        html = html.replace("TANK_DEPTH", f"{depth:.0f}")
    else:
        html = html.replace("TANK_VOLUME", "ERROR")
        html = html.replace("TANK_PERCENT", "ERROR")
        html = html.replace("TANK_DEPTH", "ERROR")
    return html


def start_server():

    print("Starting app...")
    try:
        app.run(port=80)
    except:
        app.shutdown()
        reset()


start_server()
