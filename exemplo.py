from manim import *
import numpy as np
import math

class AlinhaTriangulos(MovingCameraScene):
    def construct(self):

        # malha = NumberPlane()
        # self.play(FadeIn(malha))

        A = np.array([0., 3])
        B = np.array([-2., 0])
        C = np.array([4.5, 0])

        # calcula H (pé da altura)
        # BC_vec = C - B
        # t = np.dot(A - B, BC_vec) / np.dot(BC_vec, BC_vec)
        # H = B + t * BC_vec  # aqui H = (0,0,0)*

        AB = Line(A, B)
        self.play(FadeIn(AB))
        self.wait(4)
        # AC = Line(A, C)
        # BC = Line(B, C)
        # BA = Line(B, A)
        # CA = Line(C, A)
        # CB = Line(C, B)
        # AH = Line(A, H)

        # linha_altura = Line(H, A, color=PINK)

        # ponto_A = Dot(point=A, color=RED)
        # ponto_A2 = Dot(point=A, color=RED)
        # ponto_A3 = Dot(point=A, color=RED)
        # ponto_B = Dot(point=B, color=RED)
        # ponto_B2 = Dot(point=B, color=RED)
        # ponto_C = Dot(point=C, color=RED)
        # ponto_C2 = Dot(point=C, color=RED)
        # pontoH = Dot(point=H, color=RED)
        # pontoH2 = Dot(point=H, color=RED)
        # pontoH3 = Dot(point=H, color=RED)

        # ponto_A2_certo = Dot(point=A, color=RED)
        # ponto_B2_certo = Dot(point=B, color=RED)
        # ponto_C2_certo = Dot(point=C, color=RED)
        # ponto_A3_certo = Dot(point=A, color=RED)
        # pontoH2_certo = Dot(point=H, color=RED)
        # pontoH3_certo = Dot(point=H, color=RED)
        # label_A2_certo = MathTex("A").shift(4.5*LEFT + 3*DOWN).scale(0.6)
        # label_B2_certo = MathTex("B").shift(8.8*LEFT + 3*DOWN).scale(0.6)
        # label_C2_certo = MathTex("C").shift(2.0*RIGHT + 3*DOWN).scale(0.6)
        # label_A3_certo = MathTex("A").shift(4.05*LEFT + 3*DOWN).scale(0.6)
        # label_H2_certo = MathTex("H").shift(7.2*LEFT + 1*DOWN).scale(0.6)
        # label_H3_certo = MathTex("H").shift(2.1*LEFT + 0.2*DOWN).scale(0.6)
        # label_m2_certo = MathTex("m").shift(8.3*LEFT+1.8*DOWN)
        # label_m2_copia = label_m2_certo.copy()
        # label_n2_certo = MathTex("n").shift(0.0*RIGHT+1.3*DOWN)
        # label_n2_copia = label_n2_certo.copy()
        # label_c2_certo = MathTex("c").shift(7*LEFT+3.3*DOWN)
        # label_c2_copia = label_c2_certo.copy()
        # label_b2_certo = MathTex("b").shift(1.5*LEFT+3.3*DOWN)
        # label_b2_copia = label_b2_certo.copy()

        # label_A = MathTex("A").next_to(A, UP, buff=0.1).scale(0.6)
        # label_A2 = MathTex("A").next_to(A, UP, buff=0.1).scale(0.6)
        # label_A3 = MathTex("A").next_to(A, UP, buff=0.1).scale(0.6)
        # label_B = MathTex("B").next_to(B, DOWN+LEFT, buff=0.1).scale(0.6)
        # label_B2 = MathTex("B").next_to(B, DOWN+LEFT, buff=0.1).scale(0.6)
        # label_C = MathTex("C").next_to(C, DOWN+RIGHT, buff=0.1).scale(0.6)
        # label_C2 = MathTex("C").next_to(C, DOWN+RIGHT, buff=0.1).scale(0.6)
        # label_H = MathTex("H").next_to(H, DOWN, buff=0.1).scale(0.6)
        # label_H2 = MathTex("H").next_to(H, DOWN, buff=0.1).scale(0.6)
        # label_H3 = MathTex("H").next_to(H, DOWN, buff=0.1).scale(0.6)

        # # a → oposto de A (entre B e C)
        # label_a = MathTex("a").move_to((B + C) / 2 + 0.5*DOWN + 0.5 * LEFT)
        # label_a2 = MathTex("a").move_to((B + C) / 2 + 0.5*DOWN + 0.5 * LEFT)
        # label_a_copia = label_a.copy()
        # label_a_copia2 = label_a.copy()

        # # b → oposto de B (entre A e C)
        # label_b = MathTex("b").move_to((A + C) / 2 + 0.5*UP)
        # label_b2 = MathTex("b").move_to((A + C) / 2 + 0.5*UP)
        # label_b_copia = label_b.copy()
        # # c → oposto de C (entre A e B)
        # label_c = MathTex("c").move_to((A + B) / 2 + 0.5*LEFT)
        # label_c2 = MathTex("c").move_to((A + B) / 2 + 0.5*LEFT)
        # label_c_copia = label_c.copy()

        # label_m = MathTex("m").move_to((B + C)/2 + 0.2 * UP + 2*LEFT).scale(0.6)
        # copia_m = label_m.copy().scale(1.3)
        # label_m2 = MathTex("m").move_to((B + C)/2 + 0.2 * DOWN + 2*LEFT).scale(0.6)

        # label_n = MathTex("n").move_to((B + C)/2 + 0.2 * UP + RIGHT).scale(0.6)
        # copia_n = label_n.copy().scale(1.3)
        # label_n2 = MathTex("n").move_to((B + C)/2 + 0.2 * DOWN + RIGHT).scale(0.6)


        # linha_BC = Line(H, B)
        # linha_BC_direita = Line(H, C)

        # ang_reto2 = RightAngle(linha_altura, linha_BC, length=0.4, quadrant=(1, 1), color=YELLOW)

        # ang_reto3 = RightAngle(linha_altura, linha_BC_direita, length=0.4, quadrant=(1, 1), color=YELLOW)

        # # triângulo maior BAC
        # tri_BAC = Polygon(B, A, C, color=BLUE)
        # guardar_tri_BAC = VGroup()
        # guardar_tri_BAC.add(tri_BAC, ponto_A, ponto_B, ponto_C, label_A, label_B, label_C, label_a, label_b, label_c, linha_altura, label_m, label_n, label_H, pontoH, label_a2, label_a_copia, label_b_copia, label_c_copia)

        # maiss = MathTex("+").shift(1.8*DOWN)
        # igual = MathTex("=").shift(1.8*DOWN + 1.2*RIGHT)


        # self.play(Create(guardar_tri_BAC), run_time=8)
        # self.play(copia_m.animate.shift(2*DOWN + 0.15 * RIGHT), copia_n.animate.shift(2*DOWN+1.6*LEFT), FadeIn(maiss), label_a_copia2.animate.shift(1.3*DOWN + 1*RIGHT), FadeIn(igual))

        # self.wait()

        # grupo_obs = VGroup()
        # grupo_obs.add(copia_m, copia_n, maiss, igual, label_a_copia2)

        # self.play(grupo_obs.animate.shift(5*UP + 5*LEFT))

        # ang_reto = RightAngle(AB, AC, length=0.4, quadrant=(1, 1), color=YELLOW)

        # ang_beta = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        # ang_alfa = Angle(CA, CB, radius=0.6, other_angle=False, color=PURPLE)

        # ang_alfa_BAH = Angle(AB, AH, radius=0.6, other_angle=False, color=PURPLE)

        # ang_beta_BAH = Angle(BC, BA, radius=0.6, other_angle=False, color=ORANGE)

        # ang_beta_CAH = Angle(AH, AC, radius=0.6, other_angle=False, color=ORANGE)

        # ang_alfa_CAH = Angle(CA, CB, radius=0.6, other_angle=False, color=PURPLE)

        # beta_label = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.3*RIGHT)

        # beta_labelBAH = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.3*RIGHT)

        # beta_labelCAH = MathTex(r"\beta").move_to(ang_beta.point_from_proportion(0.5) + 0.3*UP + 0.3*RIGHT)

        # alfa_label = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.2*UP + 0.5*LEFT)

        # alfa_labelBAH = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.2*UP + 0.5*LEFT)

        # alfa_labelCAH = MathTex(r"\alpha").move_to(ang_alfa.point_from_proportion(0.5) + 0.2*UP + 0.5*LEFT)

        # guardar_angulos_lados = VGroup()
        # guardar_angulos_lados.add(ang_reto, ang_beta, ang_alfa, beta_label, alfa_label)

        # self.play(Write(guardar_angulos_lados), run_time=2)
        
        # # triângulo menor BAH (que quero transformar)
        # tri_BAH = Polygon(B, A, H, color=GREEN)
        # guardar_tri_BAH = VGroup()
        # guardar_tri_BAH.add(ang_alfa_BAH, ang_beta_BAH, tri_BAH, ang_reto2, label_H2, pontoH2, label_m2, label_A2, ponto_A2, label_B2, ponto_B2, label_c2)

        # tri_CAH = Polygon(C, A, H, color=RED)
        # guardar_tri_CAH = VGroup()
        # guardar_tri_CAH.add(tri_CAH, ang_alfa_CAH, ang_beta_CAH, ang_reto3, label_H3, pontoH3, label_n2, label_A3, ponto_A3, label_C2, ponto_C2, label_b2)

        # self.play(Create(guardar_tri_CAH), Create(guardar_tri_BAH))

        # # parâmetros numéricos (2D)
        # BA = (A - B)[:2]
        # BH = (H - B)[:2]
        # AC = (C - A)[:2]
        # theta = -math.atan2(BA[1], BA[0])         # cerca de -0.98279 rad (-56.3099°)
        # theta2 = -math.atan2(AC[1], AC[0])

        # # 1) rotaciona em torno de B
        # self.play(guardar_tri_BAH.animate.rotate(theta, about_point=B), guardar_tri_CAH.animate.rotate(theta2, about_point=C), run_time=2)

        # # # 2) aplicar reflexão no eixo x (matriz 3x3 para Manim)
        # # S = np.array([[1., 0., 0.],
        # #               [0., -1., 0.],
        # #               [0., 0., 1.]])
        # # # apply_matrix aplica a transformação diretamente às coordenadas
        # # self.play(guardar_tri_BAH.animate.apply_matrix(S, about_point=B), guardar_tri_CAH.animate.apply_matrix(S, about_point=C), run_time=2)
        # # self.play(guardar_tri_CAH.animate.move_to(2*DOWN+2*RIGHT))