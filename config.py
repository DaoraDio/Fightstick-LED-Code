if __name__ == '__main__':
    import init
    with open('main.py', 'r') as f:
        init.code = f.read()
    exec(init.code)

print("\033[32mconfig\033[0m")
#Fight Lights Pico V2.6.0

from machine import Pin
from init import random, rainbow, smooth, notSet
import button
import functions
import init

blank = (0,0,0)
RED = (255,0,0)
ORANGE = (255,127,0)
LIGHT_ORANGE = (255,200,0)
YELLOW = (255,255,0)
LIME = (160,255,0)
GREEN = (0,255,0)
TURQOISE = (64,224,208)
BLUE = (0,0,255)
LIGHT_BLUE = (0,193,255)
VIOLET = (170,0,255)
PINK = (255,0,170)
CYAN = (0,255,255)
WHITE = (255,255,255)

colors = [RED,ORANGE,LIGHT_ORANGE,YELLOW,LIME,GREEN,TURQOISE,BLUE,LIGHT_BLUE,VIOLET,PINK,CYAN,WHITE]

idle_mode1_colors = colors
idle_mode1_speed = 0.05
profile_name = "Profile 1"
led_count = 18
PIN_NUM = 0
leniency = 1
brightness_mod = 1
brightness_steps = smooth
idle_mode = 2
idle_after = 10
save_stats = False
input_reset_time = 50
profile_color = (0,0,255)
clear_background_on_press = False
background = ((0.05,BLUE,1),(0.05,BLUE,2),(0.05,BLUE,3),(0.05,BLUE,4),(0.05,BLUE,5),(0.05,BLUE,6),(0.05,BLUE,7),(0.05,BLUE,8),(0.05,BLUE,9),(0.05,BLUE,10),(0.05,BLUE,11),(0.05,BLUE,12),(0.05,BLUE,13),(0.05,BLUE,14),(0.05,BLUE,15),(0.05,BLUE,16),(0.05,BLUE,17),(0.05,BLUE,18))
UP_MyButton = button.MyButton(1, 'UP', functions.clear_led)
DOWN_MyButton = button.MyButton(2, 'DOWN', functions.clear_led)
RIGHT_MyButton = button.MyButton(3, 'RIGHT', functions.clear_led)
LEFT_MyButton = button.MyButton(4, 'LEFT', functions.clear_led)
SELECT_MyButton = button.MyButton(5, 'SELECT', functions.clear_led)
PS_MyButton = button.MyButton(6, 'PS', functions.clear_led)
START_MyButton = button.MyButton(7, 'START', functions.clear_led)
SQUARE_1P_MyButton = button.MyButton(8, 'SQUARE_1P', functions.clear_led)
TRIANGLE_2P_MyButton = button.MyButton(9, 'TRIANGLE_2P', functions.clear_led)
R1_3P_MyButton = button.MyButton(10, 'R1_3P', functions.clear_led)
L1_4P_MyButton = button.MyButton(11, 'L1_4P', functions.clear_led)
CIRCLE_2K_MyButton = button.MyButton(12, 'CIRCLE_2K', functions.clear_led)
X_1K_MyButton = button.MyButton(13, 'X_1K', functions.clear_led)
L2_4K_MyButton = button.MyButton(14, 'L2_4K', functions.clear_led)
R2_3K_MyButton = button.MyButton(15, 'R2_3K', functions.clear_led)

button_list = [UP_MyButton,DOWN_MyButton,RIGHT_MyButton,LEFT_MyButton,SELECT_MyButton,PS_MyButton,START_MyButton,SQUARE_1P_MyButton,TRIANGLE_2P_MyButton,R1_3P_MyButton,L1_4P_MyButton,CIRCLE_2K_MyButton,X_1K_MyButton,L2_4K_MyButton,R2_3K_MyButton]
init.button_list_length = len(button_list)


UP_MyButton.set_config((7,), random, False, 1, 30, 9)
DOWN_MyButton.set_config((5,), random, False, 1, 30, 9)
RIGHT_MyButton.set_config((8,), random, False, 1, 30, 9)
LEFT_MyButton.set_config((6,), random, False, 1, 30, 9)
SELECT_MyButton.set_config((14,), RED, False, 1, 30, 9)
PS_MyButton.set_config((15,), LIGHT_BLUE, False, 1, 30, 9)
START_MyButton.set_config((13,), BLUE, False, 1, 30, 9)
SQUARE_1P_MyButton.set_config((9,), random, True, 1, 30, 9)
TRIANGLE_2P_MyButton.set_config((10,), random, True, 1, 30, 9)
R1_3P_MyButton.set_config((11,), random, True, 1, 30, 9)
L1_4P_MyButton.set_config((12,), random, True, 1, 30, 9)
CIRCLE_2K_MyButton.set_config((3,), random, True, 1, 30, 9)
X_1K_MyButton.set_config((4,), random, True, 1, 30, 9)
L2_4K_MyButton.set_config((1,), random, True, 1, 30, 9)
R2_3K_MyButton.set_config((2,), random, True, 1, 30, 9)

ledOptions_color = (255,0,0)
ledOptions_profile_color_use_all_LEDs = True
ledOptions_led_buttons = [START_MyButton,SELECT_MyButton]
ledOptions_start_time = 1
ledOptions_increase_brightness = [UP_MyButton]
ledOptions_decrease_brightness = [DOWN_MyButton]
ledOptions_left_button = [LEFT_MyButton]
ledOptions_right_button = [RIGHT_MyButton]
ledOptions_confirm = [X_1K_MyButton]
OnOff_button = []
rainbow_speed = 100
activate_player_led = False
playerLED_brightness = 1
playerLED_PIN_NUM = 16
P1_color = YELLOW
P2_color = YELLOW
P3_color = YELLOW
P4_color = YELLOW
next_config = []
prev_config = []
onboard_led_on = True
smooth_brightness_speed = 0.03
eight_way_up = [(-1,),blank,UP_MyButton]
eight_way_down = [(-1,),blank,DOWN_MyButton]
eight_way_left = [(-1,),blank,LEFT_MyButton]
eight_way_right = [(-1,),blank,RIGHT_MyButton]
eight_way_upleft = [(-1,),blank]
eight_way_upright = [(-1,),blank]
eight_way_leftdown = [(-1,),blank]
eight_way_rightdown = [(-1,),blank]
skip_leds_in_idle = []
idlemode_leds = functions.remove_idle_skips()
oled_button0 = (14,35,'is_key',LEFT_MyButton,10,1)
oled_button1 = (26,47,'is_key',DOWN_MyButton,10,1)
oled_button2 = (38,35,'is_key',RIGHT_MyButton,10,1)
oled_button3 = (26,23,'is_key',UP_MyButton,10,1)
oled_button4 = (11,7,'is_key',START_MyButton,7,0)
oled_button5 = (21,7,'is_key',SELECT_MyButton,7,0)
oled_button6 = (72,7,'is_key',PS_MyButton,7,0)
oled_button7 = (82,7,'is_key',None,7,0)
oled_button8 = (92,7,'is_key',None,7,0)
oled_button9 = (102,7,'is_key',None,7,0)
oled_button10 = (67,28,'is_button',SQUARE_1P_MyButton,6,None)
oled_button11 = (82,23,'is_button',TRIANGLE_2P_MyButton,6,None)
oled_button12 = (97,24,'is_button',R1_3P_MyButton,6,None)
oled_button13 = (111,28,'is_button',L1_4P_MyButton,6,None)
oled_button14 = (68,43,'is_button',X_1K_MyButton,6,None)
oled_button15 = (82,39,'is_button',CIRCLE_2K_MyButton,6,None)
oled_button16 = (96,39,'is_button',R2_3K_MyButton,6,None)
oled_button17 = (112,44,'is_button',L2_4K_MyButton,6,None)
oled_buttons = [oled_button0,oled_button1,oled_button2,oled_button3,oled_button4,oled_button5,oled_button6,oled_button7,oled_button8,oled_button9,oled_button10,oled_button11,oled_button12,oled_button13,oled_button14,oled_button15,oled_button16,oled_button17,]
oled_idle = 0
oled_layout = 0
oled_type = 0
invert_oled = False
rotate_oled = False
i2c_interface = 1
oled_sda = 26
oled_scl = 27
oled_animation_delay = 0
splash = bytearray([
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x01,  0xF8,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x0F,  0xF1,  0xC0,  0x07,  0xFC,  0x00,  0x00,  0x70,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x03,  0xFF,  0xF1,  0xC0,  0x1F,  0xFC,  0x0E,  0x00,  0x70,  0x00,  0xFF,  0x80,  0x00,  0x00,  0x00,  0x00, 
 0x03,  0xFF,  0xF1,  0xC0,  0x3F,  0x3C,  0x0E,  0x00,  0x77,  0xFF,  0xFF,  0x80,  0x00,  0x01,  0xFF,  0x80, 
 0x03,  0xE0,  0x01,  0xC0,  0x7C,  0x18,  0x0E,  0x00,  0x77,  0xFF,  0xFF,  0x80,  0x00,  0x03,  0xFF,  0xE0, 
 0x03,  0x80,  0x03,  0xC0,  0xF8,  0x00,  0x0E,  0x00,  0x77,  0xFF,  0x00,  0x00,  0x00,  0x07,  0xFF,  0xF0, 
 0x03,  0x80,  0x03,  0x80,  0xF0,  0x00,  0x0E,  0x00,  0x70,  0x07,  0x00,  0x00,  0x00,  0x07,  0xC1,  0xF0, 
 0x03,  0x80,  0x03,  0x81,  0xE0,  0x00,  0x0E,  0x00,  0x70,  0x07,  0x00,  0x00,  0x00,  0x07,  0x80,  0xF8, 
 0x03,  0x00,  0x03,  0x83,  0xC0,  0x00,  0x1E,  0x00,  0xF0,  0x07,  0x00,  0x00,  0x00,  0x07,  0x80,  0x78, 
 0x03,  0x07,  0xC3,  0x83,  0xC0,  0x1C,  0x1E,  0x03,  0xE0,  0x0F,  0x00,  0x00,  0x00,  0x07,  0xFC,  0x38, 
 0x07,  0xFF,  0xC3,  0x83,  0x80,  0x3C,  0x1F,  0xFF,  0xE0,  0x0E,  0x00,  0x00,  0x00,  0x07,  0xFC,  0x38, 
 0x07,  0xFF,  0xC3,  0x07,  0x80,  0x3C,  0x1F,  0xFF,  0xE0,  0x0E,  0x00,  0x00,  0x00,  0x03,  0xFC,  0x38, 
 0x07,  0xFE,  0x07,  0x07,  0x00,  0x38,  0x1F,  0xFF,  0xE0,  0x0E,  0x00,  0x00,  0x00,  0x00,  0x00,  0x38, 
 0x07,  0x00,  0x07,  0x07,  0x00,  0x78,  0x1C,  0x01,  0xE0,  0x0E,  0x00,  0x00,  0x00,  0x00,  0x00,  0x38, 
 0x07,  0x00,  0x07,  0x07,  0x00,  0xF8,  0x18,  0x01,  0xE0,  0x0E,  0x00,  0x00,  0x00,  0x00,  0x00,  0x38, 
 0x07,  0x00,  0x07,  0x07,  0x03,  0xF8,  0x18,  0x01,  0xE0,  0x0E,  0x00,  0x3F,  0xF0,  0x00,  0x00,  0xF8, 
 0x07,  0x00,  0x07,  0x07,  0x8F,  0xF0,  0x38,  0x01,  0xE0,  0x0E,  0x0F,  0xFF,  0xFE,  0x00,  0x03,  0xF8, 
 0x07,  0x00,  0x07,  0x07,  0xFF,  0xF0,  0x38,  0x01,  0xE0,  0x0E,  0x0F,  0xFF,  0xFF,  0xF0,  0x1F,  0xF0, 
 0x07,  0x00,  0x07,  0x03,  0xFE,  0x70,  0x38,  0x01,  0xE0,  0x0E,  0x0F,  0xF0,  0x3F,  0xFF,  0xFF,  0xE0, 
 0x07,  0x00,  0x07,  0x01,  0xF8,  0x70,  0x38,  0x01,  0xE0,  0x0E,  0x00,  0x00,  0x07,  0xFF,  0xFF,  0x80, 
 0x07,  0x00,  0x00,  0x00,  0x00,  0x70,  0x38,  0x01,  0xC0,  0x00,  0x00,  0x00,  0x00,  0x3F,  0xF8,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x70,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x70,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x07,  0xE0,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x0E,  0x00,  0x07,  0x00,  0x1F,  0xF0,  0x00,  0x01,  0xC0,  0x00,  0x00,  0x07,  0xF0, 
 0x00,  0x00,  0x00,  0x1E,  0x00,  0x07,  0x00,  0x7F,  0xF0,  0x38,  0x01,  0xC0,  0x03,  0xFE,  0x3F,  0xFC, 
 0x00,  0x00,  0x00,  0x1E,  0x00,  0x07,  0x00,  0xFC,  0xF0,  0x38,  0x01,  0xDF,  0xFF,  0xFE,  0x7F,  0xFC, 
 0x00,  0x00,  0x00,  0x1E,  0x00,  0x07,  0x01,  0xF0,  0x60,  0x38,  0x01,  0xDF,  0xFF,  0xFE,  0xFC,  0x3C, 
 0x00,  0x00,  0x00,  0x1E,  0x00,  0x0F,  0x03,  0xE0,  0x00,  0x38,  0x01,  0xDF,  0xFC,  0x01,  0xE0,  0x1C, 
 0x00,  0x00,  0x00,  0x1C,  0x00,  0x0E,  0x03,  0xC0,  0x00,  0x38,  0x01,  0xC0,  0x1C,  0x01,  0xC0,  0x00, 
 0x00,  0x00,  0x00,  0x1C,  0x00,  0x0E,  0x07,  0x80,  0x00,  0x38,  0x01,  0xC0,  0x1C,  0x01,  0xC0,  0x00, 
 0x00,  0x00,  0x00,  0x1C,  0x00,  0x0E,  0x0F,  0x00,  0x00,  0x78,  0x03,  0xC0,  0x1C,  0x01,  0xE0,  0x00, 
 0x00,  0x00,  0x00,  0x1C,  0x00,  0x0E,  0x0F,  0x00,  0x70,  0x78,  0x0F,  0x80,  0x3C,  0x01,  0xFC,  0x00, 
 0x00,  0x00,  0x00,  0x1C,  0x00,  0x0E,  0x0E,  0x00,  0xF0,  0x7F,  0xFF,  0x80,  0x38,  0x00,  0xFF,  0x80, 
 0x00,  0x00,  0x00,  0x1C,  0x00,  0x0C,  0x1E,  0x00,  0xF0,  0x7F,  0xFF,  0x80,  0x38,  0x00,  0x3F,  0xE0, 
 0x03,  0xFF,  0x00,  0x3C,  0x00,  0x1C,  0x1C,  0x00,  0xE0,  0x7F,  0xFF,  0x80,  0x38,  0x00,  0x0F,  0xF0, 
 0x03,  0xFF,  0x80,  0x38,  0x00,  0x1C,  0x1C,  0x01,  0xE0,  0x70,  0x07,  0x80,  0x38,  0x00,  0x00,  0xF8, 
 0x07,  0xFF,  0xC0,  0x38,  0x00,  0x1C,  0x1C,  0x03,  0xE0,  0x60,  0x07,  0x80,  0x38,  0x00,  0x00,  0x38, 
 0x07,  0x87,  0xC0,  0x38,  0x00,  0x1C,  0x1C,  0x0F,  0xE0,  0x60,  0x07,  0x80,  0x38,  0x00,  0x00,  0x78, 
 0x0F,  0x03,  0xC0,  0x38,  0xFF,  0x9C,  0x1E,  0x3F,  0xC0,  0xE0,  0x07,  0x80,  0x38,  0x00,  0x00,  0xF0, 
 0x0F,  0x07,  0xC0,  0x3F,  0xFF,  0x9C,  0x1F,  0xFF,  0xC0,  0xE0,  0x07,  0x80,  0x38,  0x03,  0x87,  0xF0, 
 0x1E,  0x3F,  0xC0,  0x3F,  0xFF,  0x9C,  0x0F,  0xF9,  0xC0,  0xE0,  0x07,  0x80,  0x38,  0x03,  0xFF,  0xC0, 
 0x1E,  0x3F,  0x80,  0x3F,  0x80,  0x1C,  0x07,  0xE1,  0xC0,  0xE0,  0x07,  0x80,  0x38,  0x03,  0xFF,  0x00, 
 0x1E,  0x3F,  0x00,  0x3C,  0x00,  0x00,  0x00,  0x01,  0xC0,  0xE0,  0x07,  0x00,  0x00,  0x01,  0xFC,  0x00, 
 0x1C,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x01,  0xC0,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x1E,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x01,  0xC0,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x1E,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x1F,  0x80,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x0F,  0xF0,  0x00,  0x7F,  0xFF,  0xFF,  0x80,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x07, 
 0x0F,  0xFF,  0xE3,  0xFF,  0xFF,  0xFF,  0xF0,  0x00,  0x00,  0x00,  0x00,  0x00,  0x7E,  0x00,  0x00,  0x3F, 
 0x03,  0xFF,  0xFF,  0xFF,  0xFF,  0xFF,  0xFC,  0x00,  0x00,  0x00,  0x01,  0xFF,  0xFF,  0xF0,  0x00,  0xFF, 
 0x00,  0x3F,  0xFF,  0xE0,  0x00,  0x01,  0xFF,  0x00,  0x00,  0x00,  0x3F,  0xFF,  0xFF,  0xFF,  0xC3,  0xFE, 
 0x00,  0x00,  0x7F,  0x00,  0x00,  0x00,  0x7F,  0xE0,  0x00,  0x01,  0xFF,  0xFF,  0xE7,  0xFF,  0xFF,  0xF0, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x1F,  0xFC,  0x00,  0x0F,  0xFF,  0x80,  0x00,  0x3F,  0xFF,  0xE0, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x07,  0xFF,  0xFF,  0xFF,  0xF8,  0x00,  0x00,  0x01,  0xFF,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x7F,  0xFF,  0xFF,  0xC0,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x0F,  0xFF,  0xFC,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,
])
overlay = bytearray([
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x07,  0x70,  0x00,  0x74,  0x93,  0x60,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x05,  0x40,  0x00,  0x46,  0x92,  0x50,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x07,  0x70,  0x00,  0x75,  0x93,  0x50,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x04,  0x10,  0x00,  0x44,  0x9A,  0x50,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x04,  0x70,  0x00,  0x40,  0x03,  0x60,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x70,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x50,  0x02,  0x30,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0xA8,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x88,  0x02,  0x10,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x00,  0x01,  0x04,  0x02,  0x10,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x00,  0x02,  0x02,  0x02,  0x10,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0xFE,  0x03,  0xFE,  0x02,  0x10,  0x0E,  0x60,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x82,  0x00,  0x00,  0x03,  0xB8,  0x0A,  0x20,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x82,  0x00,  0x00,  0x00,  0x00,  0x0A,  0x20,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x82,  0x00,  0x00,  0x00,  0x00,  0x0C,  0x20,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x82,  0x00,  0x00,  0x00,  0x00,  0x0A,  0x20,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x82,  0x00,  0x00,  0x00,  0x00,  0x0A,  0x70,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0xFE,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x04,  0x00,  0x00,  0x01,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x08,  0x00,  0x00,  0x00,  0x80,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x1F,  0xC0,  0x00,  0x1F,  0xC0,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x08,  0x00,  0x00,  0x00,  0x80,  0x00,  0x00,  0x00,  0x00,  0xF8,  0x04,  0x70,  0x00,  0x00,  0x00, 
 0x00,  0x04,  0x00,  0x00,  0x01,  0x00,  0x00,  0x00,  0x00,  0x01,  0x8C,  0x04,  0x50,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x01,  0x04,  0x04,  0x10,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x01,  0x04,  0x04,  0x70,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x41,  0x01,  0x04,  0x04,  0x40,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x22,  0x01,  0x8C,  0x07,  0x70,  0x07,  0x70,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x14,  0x00,  0xF8,  0x00,  0x00,  0x05,  0x50,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x08,  0x00,  0x00,  0x00,  0x00,  0x05,  0x10,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x14,  0x00,  0x00,  0x00,  0x00,  0x06,  0x70,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x22,  0x00,  0x00,  0x00,  0x00,  0x05,  0x40,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x41,  0x00,  0x00,  0x00,  0x00,  0x05,  0x70,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0xA8,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x70,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x20,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00, 
 0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,  0x00,
])
############do not delete this line#######################