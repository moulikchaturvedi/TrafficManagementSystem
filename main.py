import time, random

t = 2
car_threshold = 5

roads = [
    {
        'name': 'A',
        'leftlane': 10,
        'rightlane': 5,
        'green': [False, False, False],
        'incoming_vehicles': 10,
        'outgoing_vehicles': 10,
        'timer': 0,
    },
    {
        'name': 'B',
        'leftlane': 13,
        'rightlane': 2,
        'green': [False, False, False],
        'incoming_vehicles': 6,
        'outgoing_vehicles': 12,
        'timer': 0,
    },
    {
        'name': 'C',
        'leftlane': 17,
        'rightlane': 8,
        'green': [False, False, False],
        'incoming_vehicles': 12,
        'outgoing_vehicles': 17,
        'timer': 0,
    },
    {
        'name': 'D',
        'leftlane': 5,
        'rightlane': 15,
        'green': [False, False, False],
        'incoming_vehicles': 15,
        'outgoing_vehicles': 8,
        'timer': 0,
    },
]

def roads_sorting_desc():
    global roads
    roads = sorted(roads, key=lambda d: d['leftlane'])
    roads.reverse()

def traffic_light_manager():
    if (roads[0]["incoming_vehicles"] >= 0.66*roads[0]["incoming_vehicles"]):
        roads[0],roads[1] = roads[1], roads[0]
    roads[0]["green"] = [True, True, True]
    roads[1]["green"] = [True, False, False]
    roads[2]["green"] = [True, False, False]
    roads[3]["green"] = [True, False, False]

def road_state_update():
    roads[0]["leftlane"], roads[0]["timer"] = random.randint(0, 20), 0
    roads[1]["leftlane"], roads[1]["timer"] = random.randint(0, 20), roads[1]["timer"]+1
    roads[2]["leftlane"], roads[2]["timer"] = random.randint(0, 20), roads[2]["timer"]+1
    roads[3]["leftlane"], roads[3]["timer"] = random.randint(0, 20), roads[3]["timer"]+1

if __name__ == '__main__':
    c = 5
    while c!=0:
        roads_sorting_desc()
        print("\n\nIteration: \n")
        for road in roads:
            print("Name of Road: " + road["name"] + " \t\t " + "Cars on Red Light: " + str(road["leftlane"]) + " \t\t " + "Incoming Cars from previous Red Light: " + str(road["incoming_vehicles"]))
        traffic_light_manager()
        if roads[0]["leftlane"] <= car_threshold:
            print("\n Time given to " + roads[0]["name"] + " for green: " + str(t/2) + " minutes")
            time.sleep(t/2)
        else:
            print("\n\t\t\tTime given to " + roads[0]["name"] + " for green: " + str(t) + " minutes")
            time.sleep(t)
        road_state_update()
        c = c-1
        