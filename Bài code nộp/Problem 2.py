def convert_to_alphabetic(grade):
    if grade >= 9:
        return 'A'
    elif 8 <= grade < 9:
        return 'B'
    elif 7 <= grade < 8:
        return 'C'
    elif 6 <= grade < 7:
        return 'D'
    else:
        return 'F'

def convert_to_four_system(grade):
    if grade >= 9:
        return 4.0
    elif 8 <= grade < 9:
        return 3.5
    elif 7 <= grade < 8:
        return 3.0
    elif 6 <= grade < 7:
        return 2.0
    else:
        return 0.0

try:
    n = float(input("Enter the grade in decimal system: "))
    if n >= 0 and n <= 10:
        alphabetic = convert_to_alphabetic(n)
        four_system = convert_to_four_system(n)
        print(f"the corresponding grade in alphabetic: {alphabetic}")
        print(f"the corresponding grade in four system: {four_system}")
    else:
        print("Grade must be from 0 to 10 !")
except ValueError:
    print("Please enter a valid grade !")