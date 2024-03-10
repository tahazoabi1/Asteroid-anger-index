import matplotlib.pyplot as plt

def showing_graph(asteroid):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(asteroid['est_diameter_min'], asteroid['relative_velocity_kph'], 'o')
    plt.xlabel('Min diameter')
    plt.ylabel('Velocity')
    plt.title('min diameter - velocity graph')

    plt.subplot(1, 2, 2)
    plt.plot(asteroid['miss_distance_km'], asteroid['miss_distance_km'], 'o')
    plt.xlabel('Miss distance')
    plt.ylabel('Max diameter')
    plt.title('miss distance - max diameter graph')
    plt.tight_layout()
    plt.show()
