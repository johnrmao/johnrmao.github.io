from numpy import random
from scipy.stats import truncnorm
import matplotlib.pyplot as plt


class player:
	def __init__(self, skill, ready):
		self.skill = skill
		self.ready = ready
	def __repr__(self):
		return str(self.skill) + " " + str(self.ready)

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def createplayerpool(num_player):
	players = []
	skillgen = get_truncated_normal(50, 25, 0, 100)
	for n in range(num_player):
		skill_level = skillgen.rvs()
		ready = random.randint(0, 2) == 1
		players.append(player(skill_level, ready))
	return players


def graphplayers(players):
	skill_levels = list(map(lambda player: player.skill, players))
	plt.hist(skill_levels, 50)
	plt.show()
	print(skill_levels)

graphplayers(createplayerpool(100000))
