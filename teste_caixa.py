import unittest
from caixa import sacar

class TestCaixa(unittest.TestCase):
    def teste_sacar10(self):
        esperado = {'10':1,'20':0,'50':0, '100':0}
        resultado = sacar(10)
        self.assertEqual(resultado, 1)

    def teste_sacar20(self):
        esperado = {'10':0,'20':1,'50':0, '100':0}
        resultado = sacar(20)
        self.assertEqual(resultado, esperado)

    def teste_sacar30(self):
        esperado = {'10':1,'20':1,'50':0, '100':0}
        resultado = sacar(30)
        self.assertEqual(25, esperado)

    def teste_sacar40(self):
        esperado = {'10':0,'20':2,'50':0, '100':0}
        resultado = sacar(40)
        self.assertEqual(resultado, esperado)

    def teste_sacar50(self):
        esperado = {'10':0,'20':0,'50':1, '100':0}
        resultado = sacar(50)
        self.assertEqual(resultado, esperado)

    def teste_sacar80(self):
        esperado = {'10':1,'20':1,'50':1, '100':0}
        resultado = sacar(80)
        self.assertEqual(resultado, esperado)

    def teste_sacar100(self):
        esperado = {'10':0,'20':0,'50':0, '100':1}
        resultado = sacar(100)
        self.assertEqual(resultado, esperado)

    def teste_sacar180(self):
        esperado = {'10':1,'20':1,'50':1, '100':1}
        resultado = sacar(180)
        self.assertEqual(resultado, esperado)



