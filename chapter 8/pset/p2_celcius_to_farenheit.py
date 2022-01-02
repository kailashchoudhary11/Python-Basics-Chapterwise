celcius = float(input("Enter the temperature in degree celcius: "))

def celciusToFarenheit(celcius):
    return (celcius * (9 / 5)) + 32

print(f"{celcius} celcius to farenheit is {celciusToFarenheit(celcius)}")