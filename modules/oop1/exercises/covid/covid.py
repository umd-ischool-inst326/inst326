class CovidTestResult:

    def __init__(self, sample_quality, last_calibration):
        self.sample_quality = sample_quality
        self.last_calibration = last_calibration

    def is_valid(self):
        if self.sample_quality >= .95 and self.last_calibration < 5:
            return True
        else:
            return False
