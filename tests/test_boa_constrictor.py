# 3rd Party Library
import unittest

# 1st Party Library
from models.boa_constrictor import Boa_Constrictor

class test_boa_constrictor(unittest.TestCase):
    """
    Used to tests methods from the class Boa Constrictor, with predefined values in each of its unittests.
    """
    
    def test_sonido_animal(self): # Unittest #1
        """
        Test to compare if the sound from the Boa_Constrictor method sonido_animal is equivalent to the defined within the test.
        """

        # Setting characteristics to define a Sabogae
        sabogae = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)
        
        # Comparing the sound obtained from the sonido_animal() method and unittest value defined
        self.assertEqual(sabogae.sonido_animal(), "¡Tsss!")

    def test_comer(self): # Unittest #2
        """
        Test to confirm number of rats eaten, defined in the attributes of the parameters of the comer method, as well as to confirm if the ValueError is raised when the Boas have eaten more than 10 rats, are equivalent to the unittest values defined.
        """
        
        # Setting characteristics to define a Sabogae
        sabogae = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)
        
        # Placing number of rats
        sabogae.comer(raton_comido = 4)
        
        # Confirming that the number of rats eaten from the raton_comido method is equivalent to the unittest value defined
        self.assertEqual(sabogae.get_ratones_comidos(), 4)
        
        # Increasing the number of eaten rats to reach to ten
        sabogae.comer(raton_comido = 6)
        
        # Unittest to confirm if error is raised when the number of rats surpasses 10
        with self.assertRaises(ValueError):
            sabogae.comer(raton_comido = 1)

    def test_calcular_flete(self): # Unittest #3
        """
        Test to compare the fleet calculation of a Boa, based on the attributes defined in the parameters is equivalent to the value set within the unittest.
        """
        
        # Setting characteristics to define a Sabogae
        sabogae = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)

        # Comparing fleet charge is equivalent to the value defined within unittest
        self.assertEqual(sabogae.calcular_flete(), 24.00)
    
    def test_get_pais(self): # Unittest #4
        """
        Test to compare if the country obtained from the Boa_Constrictor get_pais method, is the same as the defined one within the unittest.
        """

        # Setting characteristics to define a Sabogae
        sabogae = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)

        # Comparing country name obtained from the get_pais method is equivalent to the value defined within unittest
        self.assertEqual(sabogae.get_pais(), 'Brasil')
    
    def test_get_edad(self): # Unittest #5
        """
        Test to compare the age obtained from the Boa_Constrictor get_edad method, is the same as the defined one within the unittest.
        """
        
        # Setting characteristics to define a Sabogae
        sabogae = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)

        # Comparing age obtained from the get_edad method is equivalent to the value defined within unittest
        self.assertEqual(sabogae.get_edad(), 7)

    def test_get_nombre(self): # Unittest #6
        """Test to compare the name obatined from the get_nombre method, is the same as the defined one within the unittest."""

        # Setting characteristics to define a Sabogae
        sabogae = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)

        # Comparing name obtained from the get_nombre method is equivalent to the value defined within unittest
        self.assertEqual(sabogae.get_nombre(), 'Sabogae')
    
    