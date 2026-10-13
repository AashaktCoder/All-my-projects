import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube Simulation")

clock = pygame.time.Clock()

# --------------------------------------------------
# 3D POINTS
# --------------------------------------------------

vertices = [
    (-1, -1, -1),
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),

    (-1, -1,  1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1,  1,  1)
]

# Connections between vertices
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# --------------------------------------------------
# ROTATION
# --------------------------------------------------

def rotate_x(point, angle):
    x, y, z = point

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    y_new = y * cos_a - z * sin_a
    z_new = y * sin_a + z * cos_a

    return x, y_new, z_new


def rotate_y(point, angle):
    x, y, z = point

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    x_new = x * cos_a + z * sin_a
    z_new = -x * sin_a + z * cos_a

    return x_new, y, z_new


def rotate_z(point, angle):
    x, y, z = point

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a

    return x_new, y_new, z


# --------------------------------------------------
# 3D -> 2D PROJECTION
# --------------------------------------------------

def project(point):
    x, y, z = point

    camera_distance = 5
    scale = 300

    # Perspective projection
    factor = scale / (z + camera_distance)

    screen_x = x * factor + WIDTH / 2
    screen_y = y * factor + HEIGHT / 2

    return int(screen_x), int(screen_y)


# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------

angle_x = 0
angle_y = 0
angle_z = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 20))

    # Rotate and project every vertex
    projected_points = []

    for vertex in vertices:

        point = rotate_x(vertex, angle_x)
        point = rotate_y(point, angle_y)
        point = rotate_z(point, angle_z)

        # Move cube away from camera
        x, y, z = point
        point = (x, y, z + 5)

        projected_points.append(project(point))

    # Draw edges
    for edge in edges:

        start = projected_points[edge[0]]
        end = projected_points[edge[1]]

        pygame.draw.line(
            screen,
            (255, 255, 255),
            start,
            end,
            3
        )

    # Draw vertices
    for point in projected_points:
        pygame.draw.circle(
            screen,
            (255, 100, 100),
            point,
            6
        )

    # Rotate cube
    angle_x += 0.01
    angle_y += 0.015
    angle_z += 0.005

    pygame.display.flip()

    clock.tick(60)

pygame.quit()