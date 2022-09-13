from google.transit import gtfs_realtime_pb2
import requests
from google.protobuf.json_format import MessageToJson
import time

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get(
    'https://romamobilita.it/sites/default/files/rome_rtgtfs_vehicle_positions_feed.pb')
feed.ParseFromString(response.content)
timestr = time.strftime("%Y%m%d-%H%M%S")

with open(timestr+'.json', 'w') as f:
    f.write(MessageToJson(feed))
