import random
import math
points = [[0, 4, 1], [4, 1, 0], [3, 2, 0], [2, 3, 2], [2, 4, 1], [2, 3, 4]]
INF = math.inf
n_cluster = 3


def calc_dist(a, b):
    xA = a[0]
    yA = a[1]
    zA = a[2]
    xB = b[0]
    yB = b[1]
    zB = b[2]
    return math.sqrt(math.pow((xA-xB), 2) + math.pow((yA-yB), 2) + math.pow((zA - zB), 2))


def kmeans_init_center(X, n_cluster):
    return random.choices(X, k=n_cluster)


def kmeans_update_centers(X, labels, n_cluster):
    centers = []
    for k in range(n_cluster):
        points = []
        for i in range(len(X)):
            if labels[i] == k:
                points.append(X[i])
        x_sum = 0
        y_sum = 0
        z_sum = 0
        for point in points:
            x_sum += point[0]
            y_sum += point[1]
            z_sum += point[2]
        x_sum /= len(points)
        y_sum /= len(points)
        z_sum /= len(points)
        centers.append([x_sum, y_sum, z_sum])
    return centers


def kmeans_has_converged(centers, new_centers):
    return (set([tuple(a) for a in centers]) == set([tuple(a) for a in new_centers]))


def kmeans_predict_labels(X, centers):
    labels = []
    for x in X:
        closest_center_id = -1
        dist = INF
        for i in range(len(centers)):
            if dist > calc_dist(x, centers[i]):
                closest_center_id = i
                dist = calc_dist(x, centers[i])
        labels.append(closest_center_id)
    return labels


def kmeans(init_centers, init_labels, X, n_cluster):
    centers = init_centers
    labels = init_labels
    while True:
        labels = kmeans_predict_labels(X, centers)
        new_centers = kmeans_update_centers(X, labels, n_cluster)
        if kmeans_has_converged(centers, new_centers):
            break
        centers = new_centers
    return (centers, labels)


init_centers = kmeans_init_center(points, n_cluster)
print("Init centers by kmeans:")
print(init_centers)
init_labels = [-1 for i in range(len(points))]
centers, labels = kmeans(init_centers, init_labels, points, n_cluster)
print("Centers: ")
print(*centers)
print("Labels:")
print(*labels)
