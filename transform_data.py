import json
import pandas as pd
import os
dir_name = "data"
df = pd.DataFrame(columns=['trip_id','vehicle_id','instant','longitude','latitude','startdate','starttime','directionId'])
print("Initiating...")
for filename in os.listdir("data"):
    with open(os.path.join("data", filename), 'r') as f:
        print("Loading "+ f.name + " ...")
        data = json.load(f)
        print("Entering data to dataframe .....")
        for pos in data["entity"]:
            tripId = pos["vehicle"]["trip"]["tripId"]
            vehicleId = pos["vehicle"]["vehicle"]["id"]
            if("startTime" in pos["vehicle"]["trip"].keys()):
                startTime = pos["vehicle"]["trip"]["startTime"]
            if("startDate" in pos["vehicle"]["trip"].keys()):
                startDate = pos["vehicle"]["trip"]["startDate"]
            if("directionId" in pos["vehicle"]["trip"].keys()):
                directionId = pos["vehicle"]["trip"]["directionId"]
            instant = pos["vehicle"]["timestamp"]
            longitude = pos["vehicle"]["position"]["longitude"]
            latitude = pos["vehicle"]["position"]["latitude"]
            row = {"trip_id": tripId,
                "vehicle_id":vehicleId,
                "starttime":startTime,
                "startdate":startDate,
                "directionId":directionId,
                "instant":int(instant),
                "longitude":float(longitude),
                "latitude":float(latitude)}
            df = df.append(row,ignore_index=True)
print("Saving to csv File")
df.to_csv("./csv/gtfs_realtime.csv",index=False)
print("========End==========")
