from datetime import datetime
from flask import jsonify,json
from py_eddy_tracker.dataset.grid import RegularGridDataset
from app.api.eddyObject import NumpyEncoder, EddyObject


def trackeddy(filepath):
    g = RegularGridDataset(
        filepath, "longitude", "latitude"
    )
    g.add_uv("adt")
    g.bessel_high_filter("adt", 500)
    date = datetime(2020, 8, 16)
    a, c = g.eddy_identification("adt", "u", "v", date, 0.002)

    eddies = list()

    a_eddies = list()
    for obs in a.obs:
        lon = obs["lon"]
        lat = obs["lat"]
        radius_s = str(obs["radius_s"])
        shapelon = json.dumps(obs["contour_lon_s"], cls=NumpyEncoder)
        shapelat = json.dumps(obs["contour_lat_s"], cls=NumpyEncoder)
        eddyobject = EddyObject(lon, lat, shapelon, shapelat,radius_s).toJSON()
        a_eddies.append(eddyobject)
    eddies.append(a_eddies)

    c_eddies = list()
    for obs in c.obs:
        lon = obs["lon"]
        lat = obs["lat"]
        radius_s = str(obs["radius_s"])
        shapelon = json.dumps(obs["contour_lon_s"], cls=NumpyEncoder)
        shapelat = json.dumps(obs["contour_lat_s"], cls=NumpyEncoder)
        eddyobject = EddyObject(lon, lat, shapelon, shapelat,radius_s).toJSON()
        c_eddies.append(eddyobject)
    eddies.append(c_eddies)
    return eddies

