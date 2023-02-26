import random


team = ["Person 1", "Person 2", "Person 3"]
away = []


for i in range(len(team)):
    if len(team) <= 3:
        join_team = ", ".join(team)
        print(f"Week {i+1}: {join_team}")
        break
    elif len(team) == 0:
        break
    else:
        temp_list = []
        selection = random.choice(team)
        temp_list.append(selection)
        team.remove(selection)
        selection = random.choice(team)
        temp_list.append(selection)
        team.remove(selection)
        print(f"Week {i+1} {temp_list[0]}, {temp_list[1]}")
