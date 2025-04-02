from gamenacki.lostcitinacki.engine import LostCities
from gamenacki.lostcitinacki.players import RandomBot, ConsolePlayer
from gamenacki.lostcitinacki.renderers import ConsoleRenderer

LostCities([ConsolePlayer(0, 'Nacki', False), RandomBot(1, 'BullBot', True)], ConsoleRenderer()).play()
