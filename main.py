from machine import reset
from src.utils.microdot.microdot import Microdot, Response, send_file
from src.utils.sensors.sensors import create_distance_sensor
from src.storage_tank import StorageTank
from src.utils.math.volumes.volume import get_volume_obj

import json

with open("config.json", "r") as file:
    config = json.load(file)

config = config["tank"]
app = Microdot()

sensor = create_distance_sensor(config["sensor"])
lower_tank = get_volume_obj(config["lower_tank"])
upper_tank = get_volume_obj(config["upper_tank"])

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


def prep_html(name: str, volume: float, depth: float, percent: float):
    with open("./public/cone_index.html") as f:
        html = f.read()

    html = html.replace("TANK_NAME", name)

    if volume >= 0:
        # percent = 100 * volume / tank.max_volume

        html = html.replace("TANK_VOLUME", f"{volume:.0f}")
        html = html.replace("TANK_PERCENT", f"{percent:.0f}")
        html = html.replace("TANK_DEPTH", f"{depth:.0f}")
    else:
        html = html.replace("TANK_VOLUME", "ERROR")
        html = html.replace("TANK_PERCENT", "ERROR")
        html = html.replace("TANK_DEPTH", "ERROR")

    # print(html)
    return html


@app.route("/")
async def main(request):
    global tank
    # return send_file("index.html")
    print("\nMain page request received")

    (volume, depth, percent) = (None, None, None)

    try:
        (volume, depth, percent) = tank.read_tank()
    except Exception as e:
        print(f"Error reading volume, error was: {e}")
        (volume, depth, percent) = (-1, -1, -1)
    # volume = tank.get_volume_average(3)
    # Format the html
    html = prep_html(volume=volume, depth=depth, name=config["name"], percent=percent)
    return html


def start_server():

    print("Starting app...")
    try:
        app.run(port=80)
    except KeyboardInterrupt:
        app.shutdown()
    except Exception as e:
        print(f"An error occurred: {e}")
        app.shutdown()
        reset()


def get_volume_test():
    global tank

    (volume, depth, percent) = tank.read_tank()
    print(f"Volume: {volume}, depth: {depth}, percent: {percent}")


def repeat_distance_measurements():
    import time

    global tank

    while True:
        print(f"{sensor.read_range()} {sensor._units}\n")
        time.sleep(1)


# repeat_distance_measurements()
start_server()
