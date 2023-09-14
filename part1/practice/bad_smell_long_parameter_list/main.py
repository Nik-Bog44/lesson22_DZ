# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


# class Unit:
#     def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):
#
#         if is_fly and crawl:
#             raise ValueError('Рожденный ползать летать не должен!')
#
#         if is_fly:
#             speed *= 1.2
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#         if crawl:
#             speed *= 0.5
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#
#             field.set_unit(x=new_x, y=new_y, unit=self)

class Unit:
    def __init__(self, is_fly=False, crawl=False, speed=1):
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = speed




class Unit:
    def __init__(self, is_fly=False, crawl=False, speed=1):
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = speed

    def move(self, field, x_coord, y_coord, direction):
        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if self.is_fly:
            self.speed *= 1.2
        elif self.crawl:
            self.speed *= 0.5

        dx, dy = 0, 0
        if direction == 'UP':
            dy = self.speed
        elif direction == 'DOWN':
            dy = -self.speed
        elif direction == 'LEFT':
            dx = -self.speed
        elif direction == 'RIGHT':
            dx = self.speed
        else:
            raise ValueError('Эк тебя раскорячило')

        field.set_unit(x=x_coord + dx, y=y_coord + dy, unit=self)
