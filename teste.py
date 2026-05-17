from manim import *
import numpy as np
import math

class Teste(MovingCameraScene):
    def construct(self):

        # malha = NumberPlane()
        # self.play(FadeIn(malha))

        A = np.array([0., 3., 0.])
        B = np.array([-2., 0., 0.])
        C = np.array([4.5, 0., 0.])
        D = np.array([1, 1, 0])

        # triangulo = Polygon(A, B)
        # self.play(FadeIn(triangulo))
        BC_vec = C - B
        # self.play(BC_vec)
        # self.wait(10)
        print(BC_vec)
        BC_vec = C - B
        t = np.dot(A - B, BC_vec) / np.dot(BC_vec, BC_vec)
        H = B + t * BC_vec  # aqui H = (0,0,0)*
        print(H)