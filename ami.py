from machine import Pin, Timer, ADC
import time

# Setup 
rotary_inputs = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range(6)]
speaker_trigger = Pin(7, Pin.OUT)
led = Pin(9, Pin.OUT)
microwave_status = ADC(Pin(10))
microwave_plus30 = Pin(12, Pin.OUT)
start_button = Pin(14, Pin.IN, Pin.PULL_UP)
add_time_button = Pin(15, Pin.IN, Pin.PULL_UP)

food_options = ["Pizza", "Sandwich", "Pasta", "Soup", "Meat", "TV Dinner"]
cook_times = [60, 90, 120, 150, 180, 420]

current_selection = -1
microwave_running = False
remaining_time = 0
current_speaker_index = 0
add_time_pressed = False

# Functions
def read_rotary_position():
    for i, pin in enumerate(rotary_inputs):
        if pin.value() == 0:
            return i
    return -1

def pulse_speaker():
    speaker_trigger.high()
    time.sleep(0.1)
    speaker_trigger.low()
    time.sleep(0.1)

def sync_speaker_to(index):
    global current_speaker_index
    while current_speaker_index != index:
        pulse_speaker()
        current_speaker_index = (current_speaker_index + 1) % 6

def press_plus30():
    microwave_plus30.high()
    time.sleep(0.1)
    microwave_plus30.low()

def start_microwave(seconds):
    global microwave_running, remaining_time
    for _ in range(seconds // 30):
        press_plus30()
        time.sleep(0.1)
    led.high()
    microwave_running = True
    remaining_time = seconds

def stop_microwave():
    global microwave_running, remaining_time
    led.low()
    microwave_running = False
    remaining_time = 0
    print("Microwave finished!")

def is_microwave_running():
    return microwave_status.read_u16() > 30000

def add_time_handler(pin):
    global add_time_pressed
    add_time_pressed = True

add_time_button.irq(trigger=Pin.IRQ_FALLING, handler=add_time_handler)

# Countdown Timer 
def countdown(timer):
    global remaining_time
    if microwave_running:
        if remaining_time > 0:
            remaining_time -= 1
            print("Time left:", remaining_time)
        else:
            stop_microwave()

timer = Timer()
timer.init(freq=1, mode=Timer.PERIODIC, callback=countdown)

# Startup Speaker Reset
for _ in range(6):
    pulse_speaker()
current_speaker_index = 0

# Main Loop 
print("Microwave controller running...")

while True:
    new_selection = read_rotary_position()
    if new_selection != current_selection:
        current_selection = new_selection
        if current_selection != -1:
            print("Selected:", food_options[current_selection])
            sync_speaker_to(current_selection)

    if start_button.value() == 0 and not microwave_running and current_selection != -1:
        print("Starting microwave for:", food_options[current_selection])
        start_microwave(cook_times[current_selection])

    if add_time_pressed and microwave_running:
        remaining_time += 30
        press_plus30()
        print("Added 30s. Time left:", remaining_time)
        add_time_pressed = False

    if microwave_running and not is_microwave_running():
        print("Microwave stopped externally!")
        stop_microwave()

    time.sleep(0.1)
