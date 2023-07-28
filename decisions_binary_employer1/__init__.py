from otree.api import *


doc = """
Your app description
"""

import pandas as pd
import random
import numpy as np


df1 = pd.read_excel('_static/global/employer_pairs.xlsx', keep_default_na = False, engine = 'openpyxl')


class C(BaseConstants):
    NAME_IN_URL = 'decisions_binary_employer1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 16
    number_of_workers = 32
    number_of_pairs = 16
    profiles_worker = [{'id_pair': df1['IDPair'][i],
                        'worker1_general_id': df1['IDWorker'][i],
                        'worker1_id': df1['UniqueID'][i],
                        'gender_worker1': df1['gender'][i],
                        'race_worker1': df1["race"][i],
                        'agegroup_worker1': df1["agegroup"][i],
                        'worker2_id': df1['IDOpponent'][i],
                        'gender_worker2': df1['genderOpp'][i],
                        'race_worker2': df1["raceOpp"][i],
                        'agegroup_worker2': df1["agegroupOpp"][i],
                     }
                    for i in range(len(df1))]
    # print ("PROFILES WORKER", profiles_worker)
    bonushiring = cu(1)
    #examplescore = 9
    #examplebonus = examplescore * bonushiring
    num_sequences_worker = 50
    time_limit_sequences = 5


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        participant = player.participant
        all_pairs = C.profiles_worker.copy()
        all_pairs.extend(all_pairs)
        participant.pairs = all_pairs
        random.shuffle(participant.pairs)
        print ("PAIRS", participant.pairs[0])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(blank=True)
    gender1 = models.StringField(verbose_name='')
    gender2 = models.StringField(verbose_name='')
    race1 = models.StringField(verbose_name='')
    race2 = models.StringField(verbose_name='')
    offer1 = models.StringField(verbose_name='')
    offer2 = models.StringField(verbose_name='')
    age1 = models.StringField(verbose_name='')
    age2 = models.StringField(verbose_name='')
    usedprofiles = models.StringField()


# PAGES
class InstructionsHiring(Page):
    def is_displayed(player: Player):
        return player.round_number == 1


class Decisions(Page):
    form_model = 'player'
    form_fields = ['decision', 'offer1', 'offer2', 'age1', 'age2', 'race1',
                   'race2', 'gender1', 'gender2']

    def vars_for_template(player: Player):
        participant = player.participant
        profile_side = ['left', 'right']
        profile_side_decision = random.choice(profile_side)
        # print("PROFILE SIDE", profile_side_decision)
        if player.round_number == 1:
            # profiles1 = player.participant.pairs[player.round_number - 1][0]
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 2:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 3:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 4:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 5:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 6:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 7:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 8:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 9:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 10:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 11:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 12:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 13:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 14:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 15:
            profiles = participant.pairs[player.round_number - 1]
        if player.round_number == 16:
            profiles = participant.pairs[player.round_number - 1]
        # print ("PROFILES", profiles)
        worker1_id = profiles["worker1_id"]
        worker2_id = profiles["worker2_id"]
        worker1_gender = profiles["gender_worker1"]
        worker2_gender = profiles["gender_worker2"]
        worker1_race = profiles["race_worker1"]
        worker2_race = profiles["race_worker2"]
        worker1_age = profiles["agegroup_worker1"]
        worker2_age = profiles["agegroup_worker2"]
        return {
            'worker1_id': worker1_id,
            'worker2_id': worker2_id,
            'worker1_gender': worker1_gender,
            'worker2_gender': worker2_gender,
            'worker1_race': worker1_race,
            'worker2_race': worker2_race,
            'worker1_age': worker1_age,
            'worker2_age': worker2_age,
            'i1': '<input name="decision" type="radio" id="w1" value="' + worker1_id + '"' + '/>',
            'i2': '<input name="decision" type="radio" id="w2" value="' + worker2_id + '"' + '/>',
            'profile_side_decision': profile_side_decision,
        }
    # write decision into Excel file?

    def error_message(player, values):
        if values['decision'] == "":
            return 'You forgot to hire a worker. Please click on the worker who you want to hire.'


page_sequence = [InstructionsHiring, Decisions]
