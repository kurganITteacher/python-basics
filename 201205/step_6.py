def calc_rectangle_area(w, h):
    return w * h


def show_rectangle_area(area):
    print('площадь прямоугольника', area)


area = calc_rectangle_area(15, 20)
show_rectangle_area(area)

show_rectangle_area(calc_rectangle_area(10, 30))

show_rectangle_area(calc_rectangle_area(5, 25))
