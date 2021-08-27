def is_valid_sample(sample_quality):
    """Test if the sample quality is acceptable.

    Returns True if the sample quality is high enough for valid test results
    and, False if it is not.
    """
    if sample_quality >= .9:
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

def main():
    total_tests = 0
    positive_tests = 0

    while True:
        answer = input("Test positive? [y,n or stop]: ")
        if answer == "stop":
            break

        if answer == "y":
            test_result = True
        else:
            test_result = False

        q = float(input("Sample quality: "))
        t = int(input("Minutes since last calibration: "))

        total_tests += 1

        if is_valid_sample(q) or is_valid_calibration(t):
            positive_tests += 1

    print()
    print("Total tests: ", total_tests)
    print("Positive: ", positive_tests)
    print("Negative: ", total_tests - positive_tests)

main()


