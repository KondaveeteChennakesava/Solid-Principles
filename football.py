from calculator import Calculator

GOALS_FOR = 'F'
GOALS_AGAINST = 'A'
TEAM = "Team"

SOCCER_FILE_PATH = "data_set/football.csv"

if __name__ == "__main__":
    calc = Calculator(SOCCER_FILE_PATH, GOALS_FOR,
                      GOALS_AGAINST, TEAM)
    print("Team with minimum goal difference:", calc.execute())
