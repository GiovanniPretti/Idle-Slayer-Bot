from threads.img import ImgSearch
from threads.attack import Attack
from threads.dash import Dash
from threads.autoclick import AutoClick
import models.ascending_heights as ascending_heights
import models.bonus_stage as bonus_stage
import models.chest_hunt as chest_hunt
import threads.keylistener as keylistener
import gui.main_window as main_window


app = None

# Instancia os objetos Threads
img_search_thread = ImgSearch()
attack_thread = Attack()
dash_thread = Dash()
auto_click_thread = AutoClick()

# Atribui as threads para os outros módulos manipularem
ascending_heights.img_search_thread = img_search_thread
ascending_heights.attack_thread = attack_thread
ascending_heights.dash_thread = dash_thread

bonus_stage.attack_thread = attack_thread
bonus_stage.dash_thread = dash_thread

chest_hunt.attack_thread = attack_thread
chest_hunt.dash_thread = dash_thread

keylistener.img_search_thread = img_search_thread
keylistener.attack_thread = attack_thread
keylistener.dash_thread = dash_thread
keylistener.auto_click_thread = auto_click_thread

main_window.img_search_thread = img_search_thread
main_window.attack_thread = attack_thread
main_window.dash_thread = dash_thread
main_window.auto_click_thread = auto_click_thread