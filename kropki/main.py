from dot_drawing import Rysowacz
from create_dot_test import create_test
from dot_drawing import Rysowacz
import test_data


class Dot_classifier:
    def __init__(self, area, test=[]):
        self.area = area
        self.test = test
        self.restrictions = []
        self.initializer()

    def initializer(self):
        if self.test:
            pass
        else:
            self.test = create_test(10000)
        self.run()

    def restrictions_maker(self):
        for i in range(len(self.area) - 1):
            area_rest = self.line_determinants(self.area[i], self.area[i + 1])
            self.restrictions += [area_rest]

    def line_determinants(self, point1, point2):
        xa, ya = point1
        xb, yb = point2
        if xa != xb and ya != yb:
            a = (ya - yb) / (xa - xb)
            b = ya - (ya - yb) / (xa - xb) * xa
            return (a, b, xa, xb, ya, yb)
        elif xa == xb:
            # tj x = constans
            return ('uwaga1', xa, xb, ya, yb)
        else:
            # tj y = constans
            return ('uwaga2', xa, xb, ya, yb)


    def x_value(self, a, b, y):
        x = (y - b) / a
        return x

    def classify(self, my_point):
        x, y = my_point
        #info_jesli podwojny_punkt = []
        ograniczenia_x = []
        for restriction in self.restrictions:

            if restriction[0] == 'uwaga1':
                # print('uwaga1')
                y1 = restriction[-1]
                y2 = restriction[-2]
                x1 = restriction[-3]
                # gdzy y jest pomiedzy

                if min(y1, y2) <= y <= max(y1, y2) and x1 == x:
                    # to jestem na kresce
                    # print(x1)
                    log = '(%s, %s)outside na lini x = %s' % (x, y, x1)
                    #ograniczenia_x += [x1]
                    return ['out_line', my_point, log]
                if min(y1, y2) <= y <= max(y1, y2):
                    ograniczenia_x += [x1]
                # ograniczenia_x += [x1]

            elif restriction[0] == 'uwaga2':
                y1 = restriction[-1]
                x2 = restriction[-4]
                x1 = restriction[-3]

                if min(x1, x2) <= x <= max(x1, x2) and y1 == y:
                    # to jestem na kresce
                    # print(x1)
                    log = '(%s, %s)outside na lini x = %s' % (x, y, y1)
                    print(log)
                    return ['out_line', my_point, log]

                # print('uwaga2')
                # if y == przypadek[-1]:
                # to jestem na kresce
                # print('(%s, %s) outside na kresce poziomej' % (x,y) )
                # return
            else:
                a, b, x1, x2, y1, y2 = restriction
                # to teraz wyliczam x z y

                if min(y1, y2) <= y <= max(y1, y2):
                    # obliczam wartosc y dla tych funkcji
                    ogrx = self.x_value(a, b, y)
                    ograniczenia_x += [ogrx]

        ograniczenia_x += [x]
        # ograniczenia_y += [y]
        ograniczenia_x = set(ograniczenia_x)
        dox = sorted(ograniczenia_x)
        # doy = sorted(ograniczenia_y)

        ix = dox.index(x)
        # iy = doy.index(y)
        # print('*****************')
        if len(dox) <= 1:  # or len(dox) <=1 :
            # print(my_point, 'OUTSIDE')
            return ['outside', my_point]
        if ix % 2 != 0:  # and iy %2 != 0:
            # print(dox, ix)
            # print(my_point, 'inside!')
            return ['inside', my_point]
        else:
            # print(my_point, 'outside')
            return ['outside', my_point]


    def run(self):
        self.restrictions_maker()
        self.v_inside = []
        self.v_outside = []
        self.v_out_line = []
        for my_point in self.test:
            dot_data = self.classify(my_point)
            if dot_data[0] == 'inside':
                self.v_inside += [dot_data[1]]
            if dot_data[0] == 'outside':
                self.v_outside += [dot_data[1]]
            if dot_data[0] == 'out_line':
                self.v_out_line += [dot_data[1]]

        self.enable_graph()

    def enable_graph(self):
        Rysowacz(self.area, inside=self.v_inside, out_line=self.v_out_line, outside=self.v_outside)


if __name__ == '__main__':
    Dot_classifier(test_data.area)

#popsute proste linie nie liczy ich
#problem gdy w tym samym punkcie sie stykaja proste i liczy jako 2 a nie jako 1