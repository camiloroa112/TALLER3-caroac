# 3rd Party Library
import unittest

# 1st Party Library
from models.huron import Huron

class test_Huron(unittest.TestCase):
    """
    Used to tests methods from the class Boa Constrictor, with predefined values in each of its unittests.
    """

    def test_sonido_animal(self): # Unittest #1
        """
        Test to compare if the sound from the Huron method sonido_animal is equivalent to the defined within the test.
        """
        
        # Setting characteristics to define a Albino
        sabogae = Huron(nombre = 'Albino', edad = 4, peso = 10, pais_origen = 'Sudafrica', impuestos = 0.15)

        # Comparing the sound obtained from the sonido_animal() method and unittest value defined
        self.assertEqual(sabogae.sonido_animal(), "¡Eek Eek!")

    def test_calcular_flete(self): # Unittest #2
        """
        Test to compare the fleet calculation of an Huron, based on the attributes defined in the parameters is equivalent to the value set within the unittest.
        """

        # Setting characteristics to define a Albino
        sabogae = Huron(nombre = 'Albino', edad = 7, peso = 10, pais_origen = 'Sudafrica', impuestos = 0.15)

        # Comparing fleet charge is equivalent to the value defined within unittest
        self.assertEqual(sabogae.calcular_flete(), 1.50)
    
    def test_get_pais(self): # Unittest #3
        """
        Test to compare if the country obtained from the Huron get_pais method, is the same as the defined one within the unittest.
        """

        # Setting characteristics to define a Albino
        sabogae = Huron(nombre = 'Albino', edad = 7, peso = 10, pais_origen = 'Sudafrica', impuestos = 0.15)

        # Comparing country name obtained from the get_pais method is equivalent to the value defined within unittest
        self.assertEqual(sabogae.get_pais(), 'Sudafrica')
    
    def test_get_edad(self): # Unittest #4
        """
        Test to compare the age obtained from the Huron get_edad method, is the same as the defined one within the unittest.
        """

        # Setting characteristics to define a Albino
        sabogae = Huron(nombre = 'Albino', edad = 7, peso = 10, pais_origen = 'Sudafrica', impuestos = 0.15)

        # Comparing age obtained from the get_edad method is equivalent to the value defined within unittest
        self.assertEqual(sabogae.get_edad(), 7)

    def test_get_nombre(self): # Unittest #5
        
        # Setting characteristics to define a Albino
        sabogae = Huron(nombre = 'Albino', edad = 7, peso = 10, pais_origen = 'Sudafrica', impuestos = 0.15)

        # Comparing age obtained from the get_edad method is equivalent to the value defined within unittest
        self.assertEqual(sabogae.get_nombre(), 'Albino')
    
    