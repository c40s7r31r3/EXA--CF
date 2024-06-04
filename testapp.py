import unittest
from flask import Flask
from flask_testing import TestCase
from app import app
 
class TestApp(TestCase):
 
    def create_app(self):
        app.config['TESTING'] = True
        return app
 
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculadora de Salario', response.data)
 
    def test_calculate_salary(self):
        response = self.client.post('/calcular', data={
            'nombre': 'Juan',
            'edad': 30,
            'salario_base': 50000,
            'tipo_empleado': 'empleado'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'El salario de Juan es:', response.data)
 
if __name__ == '__main__':
    unittest.main()
