def calc_rectangle_area(w, h):
    return w * h


def show_rectangle_area(area):
    """Shows figure area

    :param area:
    :return:
    """
    print('площадь прямоугольника', area)


area_1 = calc_rectangle_area(15, 20)
show_rectangle_area(area_1)

show_rectangle_area(calc_rectangle_area(10, 30))

show_rectangle_area(calc_rectangle_area(5, 25))
