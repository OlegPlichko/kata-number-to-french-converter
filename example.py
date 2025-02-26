from french_number_converter import FrenchNumberConverter

converter = FrenchNumberConverter()
result = converter.convert([42, 100, 2021])
print(result)  # ['quarante-deux', 'cent', 'deux-mille-vingt-et-un']