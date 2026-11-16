from django.test import TestCase

class TareaTest(TestCase):
    pass

    def test_suma(self):
        resultado = 4 + 4
        self.assertEqual(resultado, 8)

    def test_resta(self):
        resultado = 10 - 3
        self.assertEqual(resultado, 7)

    def comparacion(self):
        comprobacion = True
        nombre = "Francisco"
        nombre2 = "francisco"
        if nombre != nombre2:
            comprobacion = False
        self.assertTrue(comprobacion)

    def setUp(self):
        # Configuración inicial para las pruebas
        self.valor_inicial = 10
        self.valor_final = 20

    def tesT_num_sprints(self):
        sprint = Sprint.objects.all()
        self.assertEqual(numero_sprints, 5)