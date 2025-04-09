from . import bonus_stage # BonusStage_Success_count
from . import ascending_heights # AscendingHeights_count
from . import chest_hunt # ChestHunt_PerfectChest_count, ChestHunt_count
from . import buttons # SilverChest_count, Rage_count, BonusStage_Failed_count


app = None

def statistics():
    app.log_message('=============== Estatísticas ===============', jump_line=True, show_time=False)
    app.log_message(f'Estágio Bônus concluídos: {bonus_stage.BonusStage_Success_count}', show_time=False)
    app.log_message(f'Estágio Bônus incompletos: {buttons.BonusStage_Failed_count}', show_time=False)
    app.log_message(f'Alturas Ascendentes concluídas: {ascending_heights.AscendingHeights_count}', show_time=False)
    app.log_message(f'Caça ao Baú concluídas: {chest_hunt.ChestHunt_count}', show_time=False)
    app.log_message(f'Caça ao Baú Perfeita concluídas: {chest_hunt.ChestHunt_PerfectChest_count}', show_time=False)
    if buttons.SilverChest_count == 0:
        app.log_message(f'Baús de Prata resgatados: {buttons.SilverChest_count}', show_time=False)
    else:
        app.log_message(f'Baús de Prata resgatados: {buttons.SilverChest_count} ({buttons.SilverChest_count}*5 = {buttons.SilverChest_count * 5})', show_time=False)
    app.log_message(f'Modo Fúria utilizados: {buttons.Rage_count}\n', show_time=False)