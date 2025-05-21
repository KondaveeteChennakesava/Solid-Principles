from calculator import Calculator

# Named variables for column indices
MAX_TEMP = 'MxT'
MIN_TEMP = 'MnT'
DAY = 'Dy'

WEATHER_FILE_PATH = "data_set/weather.csv"

if __name__ == "__main__":
    calc = Calculator(WEATHER_FILE_PATH, MAX_TEMP,
                      MIN_TEMP, DAY)
    print("Day with minimum temperature spread:", calc.execute())
