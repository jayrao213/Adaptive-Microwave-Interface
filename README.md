# Adaptive Microwave Interface

## Final Report - https://drive.google.com/file/d/19xjZsuxedEbXjVZOuuivuz804D-Xpu1S

### Making microwave use safe, accessible, and intuitive for individuals with special needs.

---

## Project Overview

This project was developed as part of a client-centered design initiative in collaboration with **North Center Community Day Service** in Chicago, IL. Clients at North Center, many of whom have developmental disabilities such as autism or Down syndrome, often struggle with the complex interface of modern microwaves. 

Our team designed a **tactile, audio-enabled microwave interface** to allow clients to independently and safely prepare food using simple visual, auditory, and physical cues.

---

## Team & Roles

- **Jaden Dsouza - User Experience Lead**
- **Cade Duncan - Administrative Officer**
- **Jay Rao - Project Manager**
- **Alex Riemman - Mechanical Design Lead**

Developed for the **Design Thinking and Communication Program** at **Northwestern University**, under the mentorship of Professors Egel and Peshkin.

---

## Hardware Features

- **3D Printed Dial:** A large, tactile dial turns a rotary switch with six detents, each corresponding to a different food option.
- **Food Icons:** Colored, 3D-printed icons surround the dial (Pizza, Sandwich, Pasta, Soup, Meat, TV Dinner).
- **Speaker System:** Announces the currently selected food item aloud as the dial turns.
- **LED Strip Indicator:** Lights up bright red when the microwave is running.
- **Start & +10s Buttons:** One-button microwave start for clients; a discrete +30s button for staff (DSP) to extend time.

---

## Key Design Principles

- **Accessibility:** Interfaces designed to be intuitive for individuals with cognitive and motor impairments.
- **User Feedback:** Multi-sensory feedback through visuals, audio, and light.
- **Simplicity:** Only two visible buttons for users — Start and Open.
- **Safety:** Staff-exclusive time extension to avoid misuse or overheating.

---

## Code Summary (MicroPython)

The Raspberry Pi Pico serves as the brains of the interface. Here's how the code works:

### Inputs:
- **GPIO 0–5**: Six-position rotary switch (one pin goes LOW depending on selection)
- **GPIO 14**: Start button
- **GPIO 15**: Add Time (+30s) button
- **GPIO 10**: Microwave status pin (detects external stop)

### Outputs:
- **GPIO 7**: Speaker trigger
- **GPIO 9**: LED indicator
- **GPIO 12**: +30 second pulse output (simulates button press)

### Main Logic:
- The rotary switch selects a food item, and the speaker syncs to announce the name.
- Pressing the Start button initiates cooking by pulsing the microwave’s +30s button as many times as needed.
- An LED lights up while cooking.
- The system counts down every second.
- Staff can press the +30s button to extend cooking time mid-cycle.
- If the microwave is opened manually, the system detects it and stops the process.

### Food Timer Mapping:
| Food         | Time (sec) |
|--------------|------------|
| Pizza        | 60         |
| Sandwich     | 90         |
| Pasta        | 120        |
| Soup         | 150        |
| Meat         | 180        |
| TV Dinner    | 420        |

---

## Technologies Used
- **MicroPython**
- **Raspberry Pi Pico**
- **3D Printing (Onshape)**
- **Speaker, LED strip, rotary switch, tactile buttons**

---

## Files
- `ami.py` – Main MicroPython script for interfacing with hardware
- `README.md` – You're here!
- `Poster.pdf` - Visual poster of the project 

---

## Project Outcomes

- Provided clients with a **safe and confidence-building way to heat their own food**.
- DSP staff at North Center reported the solution was **clear, controllable, and easy to monitor**.
- The design remains open for future improvements including:
  - Cooking progress visualization
  - Portion-sensitive timing (e.g. temperature-based cutoff)
