"""
Для решения этой задачи мы можем использовать структуру данных "куча" (heap). 
В каждый момент времени у нас есть несколько прямоугольников, которые покрывают все отмеченные, 
но не окрашенные клетки. Нам нужно выбрать прямоугольник минимальной площади и обновить статус окрашенных клеток. 
После этого, повторяем эту операцию до тех пор, пока есть неокрашенные клетки.

Алгоритм решения:

Создадим структуру данных для хранения прямоугольников и их площадей. 
В качестве "кучи" будем использовать минимизирующую кучу (min heap).
Добавим все отмеченные клетки в эту "кучу" в виде прямоугольников с площадью 1.
Итеративно будем выполнять следующее:
a. Выберем прямоугольник с минимальной площадью из "кучи".
b. Проверим, есть ли в этом прямоугольнике неокрашенные клетки. Если нет, вернем количество шагов.
c. Обновим статус окрашенных клеток и пересчитаем площадь прямоугольников на границе измененной области.
d. Добавим обновленные прямоугольники обратно в "кучу".
e. Увеличим количество шагов на 1.

Каждая операция обновления статуса клеток и пересчета площади прямоугольников занимает линейное время 
от количества измененных клеток, и мы делаем не более n шагов, поэтому 
общая сложность алгоритма будет O(n log n).
"""
import heapq

def update_rectangles(rectangles, x, y):
    intersected_rectangles = [rect for rect in rectangles if rect[0][0] <= x <= rect[1][0] and rect[0][1] <= y <= rect[1][1]]
    
    for rect in intersected_rectangles:
        for i in range(rect[0][0], rect[1][0] + 1):
            for j in range(rect[0][1], rect[1][1] + 1):
                if (i, j) not in colored_cells:
                    colored_cells.add((i, j))
                    update_boundary_rectangles(rectangles, i, j)

def update_boundary_rectangles(rectangles, x, y):
    boundary_rectangles = [rect for rect in rectangles if (rect[0][0] == x or rect[1][0] == x or rect[0][1] == y or rect[1][1] == y)]
    
    for rect in boundary_rectangles:
        rect[2] = (rect[1][0] - rect[0][0] + 1) * (rect[1][1] - rect[0][1] + 1)

def count_steps(rectangles):
    min_heap = [(area, i) for i, (_, _, area) in enumerate(rectangles)]
    heapq.heapify(min_heap)

    steps = 0
    while min_heap:
        area, idx = heapq.heappop(min_heap)
        x1, y1, x2, y2 = rectangles[idx][0][0], rectangles[idx][0][1], rectangles[idx][1][0], rectangles[idx][1][1]

        if any((x1 <= x <= x2 and y1 <= y <= y2) and (x, y) not in colored_cells for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)):
            update_rectangles(rectangles, x1, y1)
            for i, (_, _, area) in enumerate(rectangles):
                heapq.heappush(min_heap, (area, i))
            steps += 1

    return steps

if __name__ == "__main__":
    n = int(input())
    rectangles = [([int(x), int(y)], [int(x), int(y)], 1) for x, y in (input().split() for _ in range(n))]
    colored_cells = set()

    result = count_steps(rectangles)
    print(result)

"""
В этом коде используется структура "куча" (heap) из модуля heapq, которая позволяет выбирать прямоугольник 
с минимальной площадью за O(log n) и добавлять/удалять элементы за O(log n). 
Функция update_rectangles обновляет статус клеток и пересчитывает площадь прямоугольников на границе 
измененной области. Функция min_area выполняет итерации и выбирает прямоугольники с минимальной площадью 
до тех пор, пока неокрашенных клеток не останется.

"""