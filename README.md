# Kata: number to french converter
## Design Patterns and Architecture

- Class-based approach: The solution uses a FrenchNumberConverter class that encapsulates all conversion logic.
- Strategy Pattern: The implementation allows for selecting between standard French (France) and Belgium French variants through the use_belgium_french parameter.
- Recursive approach: The number_to_french method uses recursion to handle larger numbers by breaking them down into smaller components.

## Features

Handles all special cases mentioned in the kata:

- Special names for numbers 0-16
- Different patterns for numbers ending with 1 (using "-et-")
- Special handling for French numbers 70-99
- Proper pluralization of "cent" and handling of "mille"
- Proper handling of dashes according to the 1990 orthographic reform


Supports both standard French (France) and Belgium French variants

## How to run the code

- Save the code to a file named french_number_converter.py
- Run the script with Python 3:
```
python french_number_converter.py
```

The program will process the provided dataset and output the French representation of each number in both standard French and Belgium French variants.

## How to Run the Tests

- Save the original converter code to french_number_converter.py
- Save these tests to a file named test_french_number_converter.py
- Run the tests with:
```
python -m unittest test_french_number_converter.py
```

## Tools Used
1. During the development of this French Number Converter, I utilized the following tools:

2. Claude (Anthropic) - Used as an AI assistant to help generate the initial code solution based on the kata requirements and to create comprehensive unit tests.

3. Visual Studio Code - Used as the primary development environment for editing and running the code.
4. Manual Debugging - After running the unit tests, I discovered and fixed issues with the implementation, particularly in handling the 70-79 number range.

### LLM Prompts

Initial request to write Python code to solve the kata
```
I need to write a Python solution for converting numbers to their French word representations based on the following rules:

1. Basic units (0-16): Numbers less than 16 have unique names like "zéro", "un", "deux"... through "seize"
2. Tens (20-60): Standard pattern with "vingt", "trente", "quarante", "cinquante", "soixante"
3. Numbers ending with 1: Use "-et-" connector (e.g., "vingt-et-un" for 21)
4. French 70-79 range: Uses "soixante-dix" pattern (e.g., "soixante-et-onze" for 71)
5. French 80-89 range: Uses "quatre-vingts" pattern with pluralization
6. French 90-99 range: Uses "quatre-vingt-dix" pattern
7. Hundreds: "cent" becomes plural ("cents") only at the end of a number
8. Thousands: "mille" never becomes plural
```

Request to create unit tests to cover all cases
```
Now that I have the initial implementation, please write comprehensive unit tests that specifically cover:

1. Basic numbers (0-16) and negative numbers
2. Numbers ending with 1 using "-et-" (21, 31, etc.) except 11, 81, and 91
3. Special handling for 70-79 ("soixante-dix", "soixante-et-onze", "soixante-douze", etc.)
4. Special handling for 80-89 ("quatre-vingts", "quatre-vingt-un", etc.)
5. Special handling for 90-99 ("quatre-vingt-dix", "quatre-vingt-onze", etc.)
6. Correct pluralization of "cent" (only plural at the end of a number)
7. Proper handling of "mille" (never plural)
8. Support for Belgium French variants ("septante", "huitante", "nonante")
9. Large numbers up to 999,999

Use the unittest framework and ensure each rule is thoroughly tested.
```

## Output Example

```
Standard French (France):
0: zéro
1: un
5: cinq
10: dix
11: onze
15: quinze
20: vingt
21: vingt-et-un
30: trente
35: trente-cinq
50: cinquante
51: cinquante-et-un
68: soixante-huit
70: soixante-dix
75: soixante-quinze
99: quatre-vingt-dix-neuf
100: cent
101: cent-un
105: cent-cinq
111: cent-onze
123: cent-vingt-trois
168: cent-soixante-huit
171: cent-soixante-et-onze
175: cent-soixante-quinze
199: cent-quatre-vingt-dix-neuf
200: deux-cents
201: deux-cent-un
555: cinq-cent-cinquante-cinq
999: neuf-cent-quatre-vingt-dix-neuf
1000: mille
1001: mille-un
1111: mille-cent-onze
1199: mille-cent-quatre-vingt-dix-neuf
1234: mille-deux-cent-trente-quatre
1999: mille-neuf-cent-quatre-vingt-dix-neuf
2000: deux-mille
2001: deux-mille-un
2020: deux-mille-vingt
2021: deux-mille-vingt-et-un
2345: deux-mille-trois-cent-quarante-cinq
9999: neuf-mille-neuf-cent-quatre-vingt-dix-neuf
10000: dix-mille
11111: onze-mille-cent-onze
12345: douze-mille-trois-cent-quarante-cinq
123456: cent-vingt-trois-mille-quatre-cent-cinquante-six
654321: six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un
999999: neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf

Belgium French:
0: zéro
1: un
5: cinq
10: dix
11: onze
15: quinze
20: vingt
21: vingt-et-un
30: trente
35: trente-cinq
50: cinquante
51: cinquante-et-un
68: soixante-huit
70: septante
75: septante-cinq
99: nonante-neuf
100: cent
101: cent-un
105: cent-cinq
111: cent-onze
123: cent-vingt-trois
168: cent-soixante-huit
171: cent-septante-et-un
175: cent-septante-cinq
199: cent-nonante-neuf
200: deux-cents
201: deux-cent-un
555: cinq-cent-cinquante-cinq
999: neuf-cent-nonante-neuf
1000: mille
1001: mille-un
1111: mille-cent-onze
1199: mille-cent-nonante-neuf
1234: mille-deux-cent-trente-quatre
1999: mille-neuf-cent-nonante-neuf
2000: deux-mille
2001: deux-mille-un
2020: deux-mille-vingt
2021: deux-mille-vingt-et-un
2345: deux-mille-trois-cent-quarante-cinq
9999: neuf-mille-neuf-cent-nonante-neuf
10000: dix-mille
11111: onze-mille-cent-onze
12345: douze-mille-trois-cent-quarante-cinq
123456: cent-vingt-trois-mille-quatre-cent-cinquante-six
654321: six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un
999999: neuf-cent-nonante-neuf-mille-neuf-cent-nonante-neuf
```