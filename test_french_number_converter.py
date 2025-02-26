import unittest
from french_number_converter import FrenchNumberConverter

class TestFrenchNumberConverter(unittest.TestCase):
    def setUp(self):
        self.converter = FrenchNumberConverter()
        self.belgium_converter = FrenchNumberConverter(use_belgium_french=True)
    
    def test_zero(self):
        self.assertEqual(self.converter.number_to_french(0), "zéro")
    
    def test_negative_numbers(self):
        self.assertEqual(self.converter.number_to_french(-1), "moins-un")
        self.assertEqual(self.converter.number_to_french(-42), "moins-quarante-deux")
    
    def test_units_1_to_16(self):
        expected = [
            "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", 
            "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"
        ]
        for i, exp in enumerate(expected, 1):
            self.assertEqual(self.converter.number_to_french(i), exp)
    
    def test_numbers_ending_with_1(self):
        # Testing numbers ending with 1 (excluding 11 which is "onze")
        self.assertEqual(self.converter.number_to_french(21), "vingt-et-un")
        self.assertEqual(self.converter.number_to_french(31), "trente-et-un")
        self.assertEqual(self.converter.number_to_french(41), "quarante-et-un")
        self.assertEqual(self.converter.number_to_french(51), "cinquante-et-un")
        self.assertEqual(self.converter.number_to_french(61), "soixante-et-un")
        self.assertEqual(self.converter.number_to_french(71), "soixante-et-onze")
        self.assertEqual(self.converter.number_to_french(81), "quatre-vingt-et-un")
        self.assertEqual(self.converter.number_to_french(91), "quatre-vingt-onze")
        self.assertEqual(self.converter.number_to_french(101), "cent-un")
    
    def test_tens_20_to_60(self):
        tens = {
            20: "vingt", 30: "trente", 40: "quarante",
            50: "cinquante", 60: "soixante"
        }
        for num, expected in tens.items():
            self.assertEqual(self.converter.number_to_french(num), expected)
    
    def test_tens_with_units(self):
        # Test some examples like 22, 35, etc.
        self.assertEqual(self.converter.number_to_french(22), "vingt-deux")
        self.assertEqual(self.converter.number_to_french(35), "trente-cinq")
        self.assertEqual(self.converter.number_to_french(48), "quarante-huit")
        self.assertEqual(self.converter.number_to_french(56), "cinquante-six")
        self.assertEqual(self.converter.number_to_french(69), "soixante-neuf")
    
    def test_french_70_79(self):
        self.assertEqual(self.converter.number_to_french(70), "soixante-dix")
        self.assertEqual(self.converter.number_to_french(71), "soixante-et-onze")
        self.assertEqual(self.converter.number_to_french(72), "soixante-douze")
        self.assertEqual(self.converter.number_to_french(73), "soixante-treize")
        self.assertEqual(self.converter.number_to_french(74), "soixante-quatorze")
        self.assertEqual(self.converter.number_to_french(75), "soixante-quinze")
        self.assertEqual(self.converter.number_to_french(76), "soixante-seize")
        self.assertEqual(self.converter.number_to_french(77), "soixante-dix-sept")
        self.assertEqual(self.converter.number_to_french(78), "soixante-dix-huit")
        self.assertEqual(self.converter.number_to_french(79), "soixante-dix-neuf")
    
    def test_french_80_89(self):
        self.assertEqual(self.converter.number_to_french(80), "quatre-vingts")
        self.assertEqual(self.converter.number_to_french(81), "quatre-vingt-un")
        self.assertEqual(self.converter.number_to_french(82), "quatre-vingt-deux")
        self.assertEqual(self.converter.number_to_french(85), "quatre-vingt-cinq")
        self.assertEqual(self.converter.number_to_french(89), "quatre-vingt-neuf")
    
    def test_french_90_99(self):
        self.assertEqual(self.converter.number_to_french(90), "quatre-vingt-dix")
        self.assertEqual(self.converter.number_to_french(91), "quatre-vingt-onze")
        self.assertEqual(self.converter.number_to_french(92), "quatre-vingt-douze")
        self.assertEqual(self.converter.number_to_french(95), "quatre-vingt-quinze")
        self.assertEqual(self.converter.number_to_french(99), "quatre-vingt-dix-neuf")
    
    def test_hundreds(self):
        self.assertEqual(self.converter.number_to_french(100), "cent")
        self.assertEqual(self.converter.number_to_french(200), "deux-cents")
        self.assertEqual(self.converter.number_to_french(300), "trois-cents")
        self.assertEqual(self.converter.number_to_french(900), "neuf-cents")
    
    def test_hundreds_with_units(self):
        self.assertEqual(self.converter.number_to_french(101), "cent-un")
        self.assertEqual(self.converter.number_to_french(110), "cent-dix")
        self.assertEqual(self.converter.number_to_french(111), "cent-onze")
        self.assertEqual(self.converter.number_to_french(121), "cent-vingt-et-un")
        self.assertEqual(self.converter.number_to_french(152), "cent-cinquante-deux")
        self.assertEqual(self.converter.number_to_french(199), "cent-quatre-vingt-dix-neuf")
        self.assertEqual(self.converter.number_to_french(201), "deux-cent-un")
        self.assertEqual(self.converter.number_to_french(252), "deux-cent-cinquante-deux")
        self.assertEqual(self.converter.number_to_french(555), "cinq-cent-cinquante-cinq")
        self.assertEqual(self.converter.number_to_french(999), "neuf-cent-quatre-vingt-dix-neuf")
    
    def test_thousands(self):
        self.assertEqual(self.converter.number_to_french(1000), "mille")
        self.assertEqual(self.converter.number_to_french(2000), "deux-mille")
        self.assertEqual(self.converter.number_to_french(5000), "cinq-mille")
    
    def test_thousands_with_units(self):
        self.assertEqual(self.converter.number_to_french(1001), "mille-un")
        self.assertEqual(self.converter.number_to_french(1010), "mille-dix")
        self.assertEqual(self.converter.number_to_french(1100), "mille-cent")
        self.assertEqual(self.converter.number_to_french(1111), "mille-cent-onze")
        self.assertEqual(self.converter.number_to_french(1234), "mille-deux-cent-trente-quatre")
        self.assertEqual(self.converter.number_to_french(2020), "deux-mille-vingt")
        self.assertEqual(self.converter.number_to_french(2021), "deux-mille-vingt-et-un")
        self.assertEqual(self.converter.number_to_french(2345), "deux-mille-trois-cent-quarante-cinq")
        self.assertEqual(self.converter.number_to_french(9999), "neuf-mille-neuf-cent-quatre-vingt-dix-neuf")
    
    def test_large_numbers(self):
        self.assertEqual(self.converter.number_to_french(10000), "dix-mille")
        self.assertEqual(self.converter.number_to_french(11111), "onze-mille-cent-onze")
        self.assertEqual(self.converter.number_to_french(12345), "douze-mille-trois-cent-quarante-cinq")
        self.assertEqual(self.converter.number_to_french(123456), "cent-vingt-trois-mille-quatre-cent-cinquante-six")
        self.assertEqual(self.converter.number_to_french(654321), "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un")
        self.assertEqual(self.converter.number_to_french(999999), "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf")
    
    def test_belgium_french_numbers(self):
        # Test specific Belgium French variants
        self.assertEqual(self.belgium_converter.number_to_french(70), "septante")
        self.assertEqual(self.belgium_converter.number_to_french(71), "septante-et-un")
        self.assertEqual(self.belgium_converter.number_to_french(75), "septante-cinq")
        self.assertEqual(self.belgium_converter.number_to_french(80), "huitante")
        self.assertEqual(self.belgium_converter.number_to_french(81), "huitante-et-un")
        self.assertEqual(self.belgium_converter.number_to_french(85), "huitante-cinq")
        self.assertEqual(self.belgium_converter.number_to_french(90), "nonante")
        self.assertEqual(self.belgium_converter.number_to_french(91), "nonante-et-un")
        self.assertEqual(self.belgium_converter.number_to_french(95), "nonante-cinq")
        self.assertEqual(self.belgium_converter.number_to_french(99), "nonante-neuf")
        self.assertEqual(self.belgium_converter.number_to_french(175), "cent-septante-cinq")
        self.assertEqual(self.belgium_converter.number_to_french(185), "cent-huitante-cinq")
        self.assertEqual(self.belgium_converter.number_to_french(195), "cent-nonante-cinq")
    
    def test_convert_list(self):
        # Test the convert method with a list of numbers
        numbers = [1, 2, 10, 21]
        expected = ["un", "deux", "dix", "vingt-et-un"]
        self.assertEqual(self.converter.convert(numbers), expected)
    
    def test_dataset_examples(self):
        # Test with some numbers from the kata's dataset
        dataset_examples = {
            0: "zéro",
            1: "un",
            5: "cinq",
            10: "dix", 
            11: "onze", 
            15: "quinze", 
            20: "vingt", 
            21: "vingt-et-un", 
            30: "trente", 
            35: "trente-cinq", 
            50: "cinquante", 
            51: "cinquante-et-un", 
            68: "soixante-huit", 
            70: "soixante-dix", 
            75: "soixante-quinze", 
            99: "quatre-vingt-dix-neuf", 
            100: "cent", 
            101: "cent-un", 
            105: "cent-cinq", 
            111: "cent-onze", 
            123: "cent-vingt-trois", 
            168: "cent-soixante-huit", 
            171: "cent-soixante-et-onze", 
            175: "cent-soixante-quinze", 
            199: "cent-quatre-vingt-dix-neuf", 
            200: "deux-cents", 
            201: "deux-cent-un", 
            555: "cinq-cent-cinquante-cinq", 
            999: "neuf-cent-quatre-vingt-dix-neuf", 
            1000: "mille", 
            1001: "mille-un",
            1111: "mille-cent-onze", 
            1234: "mille-deux-cent-trente-quatre", 
            2000: "deux-mille", 
            2021: "deux-mille-vingt-et-un"
        }
        
        for num, expected in dataset_examples.items():
            self.assertEqual(self.converter.number_to_french(num), expected)


if __name__ == "__main__":
    unittest.main()