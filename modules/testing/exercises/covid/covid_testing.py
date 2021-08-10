"""
Covid testing data collection utility.
"""

def main():
    results = []

    while True:
        print()

        name = input("Name (or stop): ")
        if name == "stop":
            break

        answer = input("Test positive? [y,n]: ")
        if answer == "y":
            test_result = 1 
        elif answer == "n":
            test_result = 0
        else:
            print("Invalid input, please try again")
            continue

        q = float(input("Sample quality: "))
        t = int(input("Minutes since last calibration: "))

        if not is_valid_sample(q):
            print("Invalid sample, stopping!")
            break
        elif not is_valid_calibration(t):
            print("Invalid calibration, stopping!")
            break
        else:
            results.append([name, test_result, q, t])

    save_results(results)


def save_results(results):
    """Write existing test data.

    This function accepts a list of tests results and writes them to the 
    file covid-results.csv.
    """
    with open('covid-results.csv', 'w') as data:
        for result in results:
            data.write(','.join(map(str, result)) + "\n")

def is_valid_sample(sample_quality):
    """Test if the sample quality is acceptable.

    Returns True if the sample quality is high enough for valid test results
    and, False if it is not.
    """
    if sample_quality > .9:
        return True
    else:
        return False


def is_valid_calibration(calibration_time):
    """Test if the calibration is acceptable.

    Returns True if the calibration time is low enough for valid results, and
    False if it is not.
    """
    if calibration_time < 5:
        return True
    else:
        return False

main()
