import math
import threading
import time
import sys
import os
os.environ["KCFG_KIVY_LOG_LEVEL"] = "error"
import logging
from kivy.logger import Logger
Logger.setLevel(logging.ERROR)


from kivy.app import App
from kivy.core.window import Window
from kivy.clock import mainthread
from kivy.config import Config
from kivy.graphics import *
from kivy.uix.screenmanager import Screen


def start_window(main_function):
    main_app = MainApp(main_function)
    main_app.run()

class MainApp(App):
    main_function = None
    screen = None

    def __init__(self, main_function):
        self.main_function = main_function
        super(MainApp, self).__init__()

    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        self.screen = MainScreen(self.main_function)
        return self.screen

    def on_start(self):
        self.screen.start_second_thread()

    def stop(self, *largs):
        self.screen.terminate_program_flag = True
        super(MainApp, self).stop(largs)


class MainScreen(Screen):
    keyboard = None
    mouse = (0, 0)
    main_function = None

    terminate_program_flag = False
    scan_flag = False
    input_position = (0, 0)

    def set_main_function(self, main_function):
        self.main_function = main_function

    def __init__(self, main_function, **kwargs):
        super(Screen, self).__init__(**kwargs)
        # Binding
        self.keyboard = Window.request_keyboard(self.evt_unbind_keyboard, self)
        self.keyboard.bind(on_key_down=self.evt_keydown)
        Window.bind(mouse_pos=self.evt_mouse_move)
        Window.bind(on_motion=self.on_motion)

        # Create timers
        # Clock.schedule_interval(self.ioLoop, .1)
        self.main_function = main_function

        render_world(self.canvas, [[0] * 7] * 7)

    def start_second_thread(self):
        sys.stdout.flush()
        threading.Thread(target=self.second_thread).start()

    def second_thread(self):
        try:
            sys.stdout.flush()
            self.main_function(self)
        except Exception as e:
            self.terminate_program_flag = True
            Logger.exception(e)
            raise e
        finally:
            sys.stdout.flush()
            if self.terminate_program_flag:
                try:
                    App.get_running_app().stop()
                except:
                    exit()

    def print_board(self, board):
        is_valid_size = True
        if len(board) != 7:
            is_valid_size = False
        else:
            for i in range(7):
                if len(board[i]) != 7:
                    is_valid_size = False

        if is_valid_size:
            render_world(self.canvas, board)
        else:
            raise IndexError('board matrix size is not 7x7')

    def scan_position(self):
        self.scan_flag = True
        while self.scan_flag:
            if self.terminate_program_flag:
                raise SystemError('application terminated by user signal')
            time.sleep(.1)
        return self.input_position

    def close(self):
        self.terminate_program_flag = True
        App.get_running_app().stop()

    def evt_unbind_keyboard(self):
        self.keyboard.unbind(on_key_down=self.evt_keydown)
        self.keyboard = None

    def evt_keydown(self, keyboard, keycode, text, modifiers):
        # print(keycode[1])
        if keycode[1] == 'escape':
            self.terminate_program_flag = True
            App.get_running_app().stop()
        return True

    def evt_mouse_move(self, etype, motionevent):
        self.mouse = motionevent

    def on_motion(self, device, id, args):
        if id == 'begin':
            if args.button == 'left' or args.button == 'right':
                # mouse left button is pressed
                # print((self.mouse[0], self.mouse[1]))
                x0 = self.mouse[0]
                y0 = self.mouse[1]
                ni = 0
                nj = 0
                nd = 100000 * 100000
                for i in range(-1, 8):
                    for j in range(-1, 8):
                        x = camera_position_x + coordBoardScreenOffX + i * 2 * sizeBoardCell * sqr3_2 + j * sizeBoardCell * sqr3_2
                        y = camera_position_y - (coordBoardScreenOffY + j * 3 / 2 * sizeBoardCell)
                        d = (x - x0) * (x - x0) + (y - y0) * (y - y0)
                        if d < nd:
                            nd = d
                            ni = i
                            nj = j
                if 0 <= ni <= 6 and 0 <= nj <= 6 and self.scan_flag:
                    self.input_position = (ni, nj)
                    self.scan_flag = False


camera_position_x = 0
camera_position_y = 600

sizeBoardCell = 40
coordBoardScreenOffX = 90
coordBoardScreenOffY = 120
sqr3_2 = math.sqrt(3) / 2


@mainthread
def render_world(canvas, board):
    canvas.clear()
    with canvas:
        Color(1., 1., 1.)
        Rectangle(pos=(0, 0), size=(800, 600))

        draw_board()

        Color(0, 1., 0)
        for i in range(0, 7):
            for j in range(0, 7):
                draw_cell_hexagon(i, j)
        for i in range(0, 7):
            for j in range(0, 7):
                if board[i][j] == 1:
                    draw_white_disk(i, j)
                elif board[i][j] == 2:
                    draw_black_disk(i, j)


def draw_board():
    deltaX = 2 * sizeBoardCell * sqr3_2
    deltaY = 3 / 2 * sizeBoardCell
    border1DeltaX = math.sqrt(3) * (sizeBoardCell) * 1
    border1DeltaY = sizeBoardCell * 1
    border2DeltaX = math.sqrt(3) / 3 * (sizeBoardCell)
    border2DeltaY = sizeBoardCell
    coordBoardPolygonX = [
        coordBoardScreenOffX - border1DeltaX,
        coordBoardScreenOffX + (7 - 1) * sizeBoardCell * sqr3_2 - border2DeltaX,
        coordBoardScreenOffX + (7 - 1) * deltaX + (7 - 1) * sizeBoardCell * sqr3_2 + border1DeltaX,
        coordBoardScreenOffX + (7 - 1) * deltaX + border2DeltaX
    ]
    coordBoardPolygonY = [
        coordBoardScreenOffY - border1DeltaY,
        coordBoardScreenOffY + (7 - 1) * deltaY + border2DeltaY,
        coordBoardScreenOffY + (7 - 1) * deltaY + border1DeltaY,
        coordBoardScreenOffY - border2DeltaY
    ]

    grayEdgeOrder = [0, 1, 2, 3, 0]
    blackEdgeOrder = [0, 3, 1, 2, 0]
    whiteEdgeOrder = [0, 1, 3, 2, 0]

    Color(.7, .7, .7)
    for i in range(1, 5):
        p1 = (camera_position_x + coordBoardPolygonX[grayEdgeOrder[i - 1]],
              camera_position_y - coordBoardPolygonY[grayEdgeOrder[i - 1]])
        p2 = (camera_position_x + coordBoardPolygonX[grayEdgeOrder[i]],
              camera_position_y - coordBoardPolygonY[grayEdgeOrder[i]])
        draw_line(p1, p2, 30)

    Color(0, 0, 0)
    for i in range(1, 5):
        p1 = (camera_position_x + coordBoardPolygonX[blackEdgeOrder[i - 1]],
              camera_position_y - coordBoardPolygonY[blackEdgeOrder[i - 1]])
        p2 = (camera_position_x + coordBoardPolygonX[blackEdgeOrder[i]],
              camera_position_y - coordBoardPolygonY[blackEdgeOrder[i]])
        draw_line(p1, p2, 20)

    Color(1., 1., 1.)
    for i in range(1, 5):
        p1 = (camera_position_x + coordBoardPolygonX[whiteEdgeOrder[i - 1]],
              camera_position_y - coordBoardPolygonY[whiteEdgeOrder[i - 1]])
        p2 = (camera_position_x + coordBoardPolygonX[whiteEdgeOrder[i]],
              camera_position_y - coordBoardPolygonY[whiteEdgeOrder[i]])
        draw_line(p1, p2, 20)


def draw_white_disk(i, j):
    Color(1., 1., 1.)
    draw_disk(i, j)


def draw_black_disk(i, j):
    Color(0, 0, 0)
    draw_disk(i, j)


def draw_disk(i, j):
    x = coordBoardScreenOffX + i * 2 * sizeBoardCell * sqr3_2 + j * sizeBoardCell * sqr3_2
    y = coordBoardScreenOffY + j * 3 / 2 * sizeBoardCell
    Ellipse(pos=(camera_position_x + (x - sizeBoardCell * .6), camera_position_y - (y + sizeBoardCell * .6)),
            size=(sizeBoardCell * 1.2, sizeBoardCell * 1.2))


def draw_cell_hexagon(i, j):
    x = coordBoardScreenOffX + i * 2 * sizeBoardCell * sqr3_2 + j * sizeBoardCell * sqr3_2
    y = coordBoardScreenOffY + j * 3 / 2 * sizeBoardCell
    coord_hexagon_x = [0, math.sqrt(3) / 2, math.sqrt(3) / 2, 0, -math.sqrt(3) / 2, -math.sqrt(3) / 2]
    coord_hexagon_y = [1, 0.5, -0.5, -1, -0.5, 0.5]
    v = []
    for i in range(0, len(coord_hexagon_x)):
        v.append(camera_position_x + x + sizeBoardCell * coord_hexagon_x[i - 1])
        v.append(camera_position_y - (y + sizeBoardCell * coord_hexagon_y[i - 1]))
        v.append(camera_position_x + x + sizeBoardCell * coord_hexagon_x[i])
        v.append(camera_position_y - (y + sizeBoardCell * coord_hexagon_y[i]))
    Color(.88, 0, 0)
    Mesh(vertices=v, indices=range(0, len(coord_hexagon_x)), mode='triangle_fan')
    Color(1., 1., 1.)
    Line(points=v, width=1.1, cap='round', joint='round')


def draw_line(point1, point2, width):
    Line(points=[point1[0], point1[1], point2[0], point2[1]], width=width, cap='round')
