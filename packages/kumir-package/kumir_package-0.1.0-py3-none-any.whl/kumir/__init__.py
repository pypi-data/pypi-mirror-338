"""
KUMIR - модуль для работы с роботом в стиле КУМИР.
"""

__version__ = "0.1.0"

# Импортируем класс Robot из модуля robot
from .robot import Robot

# Создаем экземпляр робота для удобного использования
robot = Robot()

# Экспортируем основные функции для работы с роботом
up = robot.up
down = robot.down
left = robot.left
right = robot.right
paint = robot.paint
repeat = robot.start_repeat
end_repeat = robot.end_repeat
get_result = robot.get_result

# Список всех публичных объектов, которые будут доступны при импортеs
__all__ = [
    'Robot',
    'up',
    'down',
    'left',
    'right',
    'paint',
    'start_repeat',
    'end_repeat',
    'get_result'
]
