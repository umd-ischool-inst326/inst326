import csv


class Vaccinations:

    def __init__(self):
        self.records = []

    def read_csv(self, csv_file):
        fh = open(csv_file, 'r', encoding='utf8')
        for row in csv.DictReader(fh):
            date = row['VACCINATION_DATE']
            race = row['RACE_CODE'] 
            first_dose = row['FirstDoseDaily']
            second_dose = row['SecondDoseDaily']
            record = VaccinationRecord(date, race, first_dose, second_dose)
            self.records.append(record)

    def total_records(self):
        return len(self.records)


class VaccinationRecord:

    def __init__(self, date, race, first_dose, second_dose):
        self.date = date
        self.race = race
        self.first_dose = first_dose
        self.second_dose = second_dose

    def is_anomalous(self):
        if self.date < "2020/12/11":
            return True
        else:
            return False
