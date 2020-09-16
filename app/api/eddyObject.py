import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class EddyObject(object):
    def __init__(self,centerlon,centerlat,shapelon,shapelat,radius_s):
        # 涡旋中心点经度
        self.centerlon = centerlon
        # 涡旋中心点纬度
        self.centerlat = centerlat
        # 涡旋边界
        self.shapelon =shapelon
        # 涡旋边界
        self.shapelat = shapelat
        # 涡旋强度
        self.radius_s = radius_s

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

