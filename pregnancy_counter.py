from datetime import *
import config

class PregnancyCounter:
    shortCycleLength: int = 21
    longCycleLength: int = 35
    pregnancyLength: int = 280
    pregnancyLengthAfterOvulation: int = 266
    pregnancyOffset: int = 7


    def __init__(self, username: str):
        self.firstDayLastMenstruation=None
        self.pregnancyDuration=None
        self.birthDate=None
        self.ovulationDate=None
        self.cycleLength=None

        self.dateOfWC = None
        self.durationAtWC = None
        self.dateOfUltrasound = None
        self.durationAtUltrasound = None

        self.username = username
        self.wayOfCounting = None
        self.action = None
        self.waitForInput = None

    def get_pregnancy_length(self) -> int:
        if self.cycleLength.days is None:
            return self.pregnancyLength
        if self.cycleLength.days > self.longCycleLength:
            return self.pregnancyLength - self.pregnancyOffset
        if self.cycleLength.days < self.shortCycleLength:
            return self.pregnancyLength - self.pregnancyOffset
        return self.pregnancyLength

    def count_birth_date_by_menstruation(self):
        self.birthDate = self.firstDayLastMenstruation + timedelta(days=self.get_pregnancy_length())
        return self.birthDate

    def count_birth_date_by_ovulation_date(self):
        self.birthDate = self.ovulationDate + timedelta(days=self.pregnancyLengthAfterOvulation)
        return self.birthDate

    def count_birth_date_by_ultrasound(self):
        self.birthDate = self.dateOfUltrasound - self.durationAtUltrasound + timedelta(days=self.pregnancyLengthAfterOvulation)
        return self.birthDate

    def count_birth_date_by_wc(self):
        self.birthDate = self.dateOfWC - self.durationAtWC + timedelta(days=self.pregnancyLengthAfterOvulation)
        return self.birthDate

    def count_pregnancy_duration(self) -> timedelta:
        self.pregnancyDuration = timedelta(days=self.pregnancyLengthAfterOvulation) - (self.birthDate - datetime.now())
        return self.pregnancyDuration
