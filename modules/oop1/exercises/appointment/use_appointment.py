from appointment import Appointment


def main():
    """ Demonstrate use of the Appointment class. """
    appt1 = Appointment("Physics meeting", (9, 30), (10, 45))
    appt2 = Appointment("Brunch", (10, 30), (11, 00))
    appt3 = Appointment("English study session", (13, 00), (14, 00))
    if appt1.overlaps(appt2):
        print(f"{appt1.name} overlaps with {appt2.name}")
    else:
        print(f"{appt1.name} does not overlap with {appt2.name}")
    if appt1.overlaps(appt3):
        print(f"{appt1.name} overlaps with {appt3.name}")
    else:
        print(f"{appt1.name} does not overlap with {appt3.name}")
    assert appt1.overlaps(appt2)
    assert appt2.overlaps(appt1)
    assert not appt1.overlaps(appt3)
    assert not appt3.overlaps(appt1)
    assert not appt2.overlaps(appt3)
    assert not appt3.overlaps(appt2)


if __name__ == "__main__":
    main()