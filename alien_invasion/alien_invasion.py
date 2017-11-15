import pygame

from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
	# 初始pygame、设置、和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一艘飞船
	ship = Ship(screen)

	# 开始游戏主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)


run_game()
