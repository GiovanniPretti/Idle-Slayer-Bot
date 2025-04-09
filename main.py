import pyautogui
from gui.main_window import MainWindow
from threads.keylistener import KeyListener
import threads.manager as manager
import threads.img as img
import threads.attack as attack
import threads.dash as dash
import threads.autoclick as autoclick
import threads.keylistener as keylistener
import models.ascending_heights as ascending_heights
import models.bonus_stage as bonus_stage
import models.chest_hunt as chest_hunt
import models.buttons as buttons
import models.minions as minions
import models.statistics as statistics


def main():
	pyautogui.PAUSE = 0
	pyautogui.FAILSAFE = False

	# Instancia o objeto da GUI e KeyListener
	app = MainWindow()
	key_listener_thread = KeyListener()

	# Associa o objeto "app" nos modulos
	modules = [manager, img, attack, dash, autoclick,  keylistener, ascending_heights, 
			bonus_stage, chest_hunt, buttons, minions, statistics]
	for module in modules:
		module.app = app

	# Inicialização da GUI e KeyListener
	key_listener_thread.start_thread()
	app.help()
	app.window.mainloop()


if __name__ == "__main__":
	main()