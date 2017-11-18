import pygame
from pygame.sprite import Group
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

	# 创建一艘飞船、一个子弹的编组和一个外星人编组
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# 开始游戏主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
