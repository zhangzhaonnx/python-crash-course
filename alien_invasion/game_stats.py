import json

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏启动时处于活动状态
        self.game_active = False

        self.file_name = "files/store.json"
        self.restore()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def store(self):
        """持久化最高分"""
        with open(self.file_name, 'w') as f_obj:
            json.dump(self.high_score, f_obj)

    def restore(self):
        """从文件恢复最高分"""
        with open(self.file_name) as f_obj:
            self.high_score = json.load(f_obj)
