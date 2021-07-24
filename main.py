from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsApp(GridLayout):

    count = 0  # initialised count variable to 0
    isEnabled = BooleanProperty(False)  # toggle button state is initialised to False
    # slider_value = StringProperty("Value")  # fetches value from slider

    # my_text = StringProperty("Default Hello!")
    my_text = StringProperty("0")  # default display value of text in label
    text_input_str = StringProperty("foo")

    def on_button_click(self):
        """"
        print("Clicked!")  # displays Clicked! in Terminal when button is clicked
        self.my_text = "You Clicked!"  # when button is clicked, default value changes to that of my_text
        """
        print("Clicked!")

        # if toggle button is OFF, counter cannot be increased
        if self.isEnabled:
            self.count += 1  # Increases value by 1
            self.my_text = str(self.count)  # displays updated count variable


    def on_toggle(self, widget):

        # displays text in console when toggle button is clicked
        print("Toggled!" + widget.state)  # gets value of on_state: down or normal

        # display text of button as ON/OFF when in respective state
        if widget.state == "normal":
            widget.text = "OFF"  # toggle button is OFF
            self.isEnabled = False  # when button is OFF, count button cannot be increased by 1
        else:
            widget.text = "ON"  # toggle button is ON
            self.isEnabled = True  # when button is ON, count button can be increased by 1


    """"
    def on_slider_value(self, widget):
        print("Slider: " + str(int(widget.value)))  # float value by default; converted to int then to string
        # self.slider_value = str(int(widget.value))  # displays slider value equal to its range
    """


    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))


    def on_text_validate(self, widget):
        # self.text_input_str = widget.text
        self.text_input_str = widget.text  # updates label text after when Enter key is pressed



class StackLayoutApp(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # creating widgets using loop stacked left to right
        for i in range(0, 100):  # creates 10 buttons
            # btn = Button(text="Z", size_hint=(0.2, 0.2))  # creates a button with text: "Z"

            # create 10 buttons; each occupying 20% of total space
            # btn = Button(text=str(i+1), size_hint=(0.2, 0.2))

            # creates responsive layout with 10 buttons
            btn = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(btn)  # adds button: `btn` to MainWidget

            # create buttons of different sizes
            # size = dp(100) + i * 10
            # btn = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            # self.add_widget(btn)  # adds button: `btn` to MainWidget


# declared class and parameter in .kv file
# class GridLayoutApp(GridLayout):
#     pass


class AnchorLayoutApp(AnchorLayout):
    pass


class BoxLayoutApp(BoxLayout):
    """"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"  # changes orientation :: default: "horizontal"
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
    """


class MainWidget(Widget):
    pass


class LearnKivyApp(App):
    pass


class CanvasApp(Widget):
    pass


class CanvasApp2(Widget):
    pass


class CanvasApp3(Widget):
    pass


class CanvasApp4(Widget):  # using canvas property in python code
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # instructions here
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(500, 300, 150, 100), width=2)
            # Rectangle(pos=(600, 100), size=(150, 100))  # filled rectangle
            self.rect = Rectangle(pos=(600, 100), size=(150, 100))  # filled rectangle instantiated with variable rect

    def on_canvas_button_click(self):
        # print("Clicked!")
        # update position of rectangle with every click on button
        x, y = self.rect.pos  # get x, y from rectangle position
        w, h = self.rect.size  # get width, height of rectangle
        inc = dp(10)  # variable to increase rectangle position 10dp forward

        # when rectangle reaches end of screen, it stops stepping forward
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc  # moves rectangle forward w.r.t var inc
        # self.rect.pos = (100, 100)  # moves rectangle from initial position to (100, 100)
        self.rect.pos = (x, y)


class CanvasApp5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)  # size of ball
        self.velX = dp(3)  # velocity of ball on x axis
        self.velY = dp(4)  # velocity of ball on y axis

        with self.canvas:
            # display ellipse in center of screen
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)  # update ball in every 1/60th of second (60fps)

    def on_size(self, *args):
        print("on size: " + str(self.width) + ", " + str(self.height))  # displays size of screen (width, height)
        # self.ball.pos = self.center  # changes position of ball w.r.t screen size
        # display ball at center of screen
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        # print("Update")  # displays update at interval of 1/60th of second
        x, y = self.ball.pos  # fetch position of ball

        # x, y are lower-left part of body
        x += self.velX  # increases coordinates of ball on x axis at speed of 3dp
        y += self.velY  # increases coordinates of ball on y axis at speed of 4dp

        # check if ball is going out of window
        # top
        if y + self.ball_size > self.height:  # ball_size > height of window
            y = self.height - self.ball_size  # maximum value of y
            self.velY = -self.velY  # if ball is going out of window, its velocity is to be reversed
        # right
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.velX = -self.velX
        # bottom
        if y < 0:
            y = 0
            self.velY = -self.velY  # reverse on y axis
        if x < 0:
            x = 0
            self.velX = -self.velX  # reverse on X axis

        self.ball.pos = (x, y)  # moves ball on x-axis


class CanvasApp6(BoxLayout):
    pass




LearnKivyApp().run()


"""
Layouts:
  Box Layout
    Stacks elements vertically or horizontally
  Anchor Layout
    can put content in every corner of screen or center
  Grid Layout
    content is organised in rows and columns
  Stack Layout
  Scroll View
  Page Layout
  Float Layout
  Relative Layout
  Scatter Layout

"""