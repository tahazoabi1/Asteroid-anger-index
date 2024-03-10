def calculate_danger(asteroid, A=1, B=1, C=1):
    avg_diameter = (asteroid['est_diameter_min'] + asteroid['est_diameter_max']) / 2
    relative_speed = asteroid['relative_velocity_kph']
    miss_distance = asteroid['miss_distance_km']

    danger_index = A * avg_diameter + B * relative_speed * 1 / C * miss_distance
    return danger_index

def user_input():
    manually = input("Do you want to set A, B, C Manually? y / n : ")
    if manually:
        A = int(input("Choose A : "))
        B = int(input("Choose B : "))
        C = int(input("Choose C : "))
    else:
        A = 1
        B = 1
        C = 1
    return A, B, C
