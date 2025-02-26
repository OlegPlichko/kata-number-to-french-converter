class FrenchNumberConverter:
    def __init__(self, use_belgium_french=False):
        """
        Initialize the French number converter
        
        Args:
            use_belgium_french (bool): Whether to use Belgium French variants (septante, etc.)
        """
        self.use_belgium_french = use_belgium_french
        
        # Basic numbers dictionary
        self.units = {
            0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre",
            5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf",
            10: "dix", 11: "onze", 12: "douze", 13: "treize",
            14: "quatorze", 15: "quinze", 16: "seize"
        }
        
        # Tens dictionary
        self.tens = {
            1: "dix", 2: "vingt", 3: "trente", 4: "quarante",
            5: "cinquante", 6: "soixante", 7: "septante" if use_belgium_french else "soixante-dix",
            8: "huitante" if use_belgium_french else "quatre-vingts",
            9: "nonante" if use_belgium_french else "quatre-vingt-dix"
        }
        
        self.hundred = "cent"
        self.thousand = "mille"
    
    def convert(self, numbers):
        """
        Convert a list of numbers to their French word representations
        
        Args:
            numbers (list): List of integers to convert
            
        Returns:
            list: List of French word representations
        """
        return [self.number_to_french(num) for num in numbers]
    
    def number_to_french(self, number):
        """
        Convert a single number to its French word representation
        
        Args:
            number (int): Integer to convert
            
        Returns:
            str: French word representation
        """
        if number == 0:
            return self.units[0]
        
        # Handle negative numbers
        if number < 0:
            return "moins-" + self.number_to_french(abs(number))
        
        parts = []
        
        # Handle thousands
        if number >= 1000:
            thousands = number // 1000
            if thousands == 1:
                parts.append(self.thousand)
            else:
                parts.append(self.number_to_french(thousands) + "-" + self.thousand)
            number %= 1000
            
            # Add a dash if there's more to come
            if number > 0:
                parts[-1] = parts[-1] + "-"
        
        # Handle hundreds
        if number >= 100:
            hundreds = number // 100
            if hundreds == 1:
                parts.append(self.hundred)
            else:
                parts.append(self.number_to_french(hundreds) + "-" + self.hundred)
            
            number %= 100
            
            # Add plural 's' to cent if it's the end
            if number == 0 and hundreds > 1 and len(parts) == 1:
                parts[-1] = parts[-1] + "s"
            # Add a dash if there's more to come
            elif number > 0:
                parts[-1] = parts[-1] + "-"
        
        # Handle remaining number under 100
        if number > 0:
            if number <= 16:  # Direct units
                parts.append(self.units[number])
            else:
                # Extract tens and units
                ten, unit = divmod(number, 10)
                
                if self.use_belgium_french:
                    # Belgium French is more regular
                    if unit == 0:
                        parts.append(self.tens[ten])
                    elif unit == 1:
                        parts.append(self.tens[ten] + "-et-" + self.units[unit])
                    else:
                        parts.append(self.tens[ten] + "-" + self.units[unit])
                else:
                    # Handle the special French cases
                    if ten == 7:  # 70-79
                        if unit == 0:  # 70
                            parts.append("soixante-dix")
                        elif unit == 1:  # 71
                            parts.append("soixante-et-onze")
                        elif unit <= 6:  # 72-76: use soixante + units from 12-16
                            parts.append("soixante-" + self.units[unit + 10])
                        else:  # 77-79: use soixante-dix + units from 7-9
                            parts.append("soixante-dix-" + self.units[unit])
                    elif ten == 8:  # 80-89
                        if unit == 0:  # 80
                            parts.append("quatre-vingts")
                        else:  # 81-89
                            if unit == 1:
                                parts.append("quatre-vingt-un")
                            else:
                                parts.append("quatre-vingt-" + self.units[unit])
                    elif ten == 9:  # 90-99
                        if unit == 0:  # 90
                            parts.append("quatre-vingt-dix")
                        elif unit == 1:  # 91
                            parts.append("quatre-vingt-onze")
                        elif unit <= 6:  # 92-96: use quatre-vingt + units from 12-16
                            parts.append("quatre-vingt-" + self.units[unit + 10])
                        else:  # 97-99: use quatre-vingt-dix + units from 7-9
                            parts.append("quatre-vingt-dix-" + self.units[unit])
                    else:
                        # Regular cases: 20-29, 30-39, etc.
                        if unit == 0:
                            parts.append(self.tens[ten])
                        elif unit == 1:
                            parts.append(self.tens[ten] + "-et-un")
                        else:
                            parts.append(self.tens[ten] + "-" + self.units[unit])
        
        return "".join(parts)


def main():
    """Main function to run the converter on the exercise dataset"""
    input_numbers = [
        0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 
        111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 
        1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 
        654321, 999999
    ]
    
    # Using standard French (France)
    converter = FrenchNumberConverter()
    results = converter.convert(input_numbers)
    
    print("Standard French (France):")
    for num, french in zip(input_numbers, results):
        print(f"{num}: {french}")
    
    # Optional: Using Belgium French
    print("\nBelgium French:")
    belgium_converter = FrenchNumberConverter(use_belgium_french=True)
    belgium_results = belgium_converter.convert(input_numbers)
    
    for num, french in zip(input_numbers, belgium_results):
        print(f"{num}: {french}")


if __name__ == "__main__":
    main()
