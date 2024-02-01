import pygame, requests, sys, os


class MapParams(object):
    def __init__(self, coords):
        self.lat = coords[0]
        self.lon = coords[1]
        self.zoom = 16  
        self.type = "map" 

    def ll(self):
        return str(self.lon) + "," + str(self.lat)

    def get_coords(self):
        lat = float(input("Введите широту (широта): "))
        lon = float(input("Введите долготу (долгота): "))
        self.lat = lat
        self.lon = lon


def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapParams()
    mp.get_coords()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  
            break
        map_file = load_map(mp)
        if map_file:
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    main()