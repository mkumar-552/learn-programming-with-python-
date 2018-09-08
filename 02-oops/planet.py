class Planet(object):
    def rotate(self):
        print("rotate")

    def revolve(self):
        print("revolve")

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()
    def rotation(self,speed):
        return (" the rotation of the planet is very {}".format(speed))

earth = Planet()
earth.rotate_and_revolve()
print(earth.rotation('fast'))
