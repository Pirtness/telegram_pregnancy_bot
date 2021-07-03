from actions import Action
from bot import bot
import resources.messages as msgs
from pregnancy_counter import PregnancyCounter
from wait_for_input import WaitForInput
from ways_of_counting import WayOfCounting


def next_step(user: PregnancyCounter):
    if user.wayOfCounting == WayOfCounting.BY_MENSTRUATION:
        next_step_menstruation(user)
    if user.wayOfCounting == WayOfCounting.BY_OVULATION:
        next_step_ovulation(user)
    if user.wayOfCounting == WayOfCounting.BY_ULTRASOUND:
        next_step_ultrasound(user)
    if user.wayOfCounting == WayOfCounting.BY_WC:
        next_step_wc(user)

def next_step_menstruation(user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        user.waitForInput = WaitForInput.TIMEDELTA
        return
    if user.waitForInput == WaitForInput.TIMEDELTA:
        user.waitForInput = WaitForInput.HAS_EVERYTHING
        return
    if user.waitForInput == WaitForInput.HAS_EVERYTHING:
        user.waitForInput = None
        return

def next_step_ovulation(user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        user.waitForInput = WaitForInput.HAS_EVERYTHING
        return
    if user.waitForInput == WaitForInput.HAS_EVERYTHING:
        user.waitForInput = None
        return

def next_step_ultrasound(user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        user.waitForInput = WaitForInput.TIMEDELTA
        return
    if user.waitForInput == WaitForInput.TIMEDELTA:
        user.waitForInput = WaitForInput.HAS_EVERYTHING
        return
    if user.waitForInput == WaitForInput.HAS_EVERYTHING:
        user.waitForInput = None
        return

def next_step_wc(user: PregnancyCounter):
    if user.waitForInput == WaitForInput.DATE:
        user.waitForInput = WaitForInput.TIMEDELTA
        return
    if user.waitForInput == WaitForInput.TIMEDELTA:
        user.waitForInput = WaitForInput.HAS_EVERYTHING
        return
    if user.waitForInput == WaitForInput.HAS_EVERYTHING:
        user.waitForInput = None
        return
