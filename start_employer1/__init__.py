from otree.api import *

# test

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'start_employer1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()
    prolificid = models.CharField(initial=None,
                                  verbose_name="Before we start, please provide your Prolific ID.")


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']


class Instructions(Page):
    form_model = 'player'
    form_fields = ['prolificid']


page_sequence = [Consent, Instructions]
