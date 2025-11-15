# Dual-Mode Dynamic RGB Lighting System

A smart RGB lighting setup that can operate in **two modes**;
**Static**, for manual color control, and **Dynamic**, for screen-adaptive lighting that mirrors your display in real-time.

It’s a blend of hardware engineering, circuit logic, Python automation, and a touch of design aesthetics; all powered by Arduino and 3D-printed precision.

<br>

## Overview

This system allows you to switch between **two distinct operating modes** using a **2-Pole 2-Throw (2P2T)** switch:

* **Static Mode** – Manually control the Red, Green, and Blue intensities using three potentiometers.
* **Dynamic Mode** – Automatically match the lighting to your screen colors in real-time using Python-based screen capture and serial communication.

The two modes are **mutually exclusive**; only one is powered at any given time; which ensures efficient power usage and prevents circuit conflicts.

<br>

## Demo

Watch the magic: (with audio please :)

https://github.com/user-attachments/assets/77e02d70-a3d1-4c4b-9277-59fa5aef3f31


<br>

## How It Works

### **Static Mode**

* Three potentiometers are connected as analog inputs to the **Arduino Uno**.
* Their readings are normalized to 8-bit values (0–255) corresponding to RGB intensities.
* These signals drive three **NPN transistors** that regulate a **12 V DC** supply to the RGB LED strip.
* This setup provides smooth analog control of light color and brightness.

### **Dynamic Mode**

* A Python script captures the screen at ~16 FPS using **PyAutoGUI**.
* Each frame is analyzed using **PIL** and **NumPy** to compute the dominant RGB color.
* These RGB values are sent over **Serial (COM)** to the Arduino.
* The Arduino receives the values and outputs PWM signals to the same transistors controlling the LED strip; creating real-time adaptive ambient lighting.

<br>

## Hardware Architecture

| Component                | Purpose                                                  |
| ------------------------ | -------------------------------------------------------- |
| **Arduino Uno**          | Core controller for PWM output and serial communication  |
| **NPN Transistors (x3)** | Amplify PWM signals to drive high-current RGB channels   |
| **Potentiometers (x3)**  | Manual analog input for static RGB control               |
| **12 V Adapter**         | Power source for LED strip                               |
| **RGB LED Strip**        | Lighting output device                                   |
| **2P2T Toggle Switch**   | Switches power rails between Static and Dynamic circuits |

### Circuit Design Highlights

* The **2P2T switch** isolates both modes at the power level.
* In **Static Mode**, the potentiometers and LED strip receive power directly from the adapter.
* In **Dynamic Mode**, power is rerouted to the Arduino and transistor bases.
* Only one circuit path is live at a time; making the setup power-efficient and electrically safe.

<br>

## Software Architecture

### **Python Script** (`rgb.py`)

* Captures the display using PyAutoGUI.
* Downscales and processes frames with PIL.
* Uses NumPy to compute the average or dominant RGB color.
* Sends RGB values via serial to Arduino in real-time.

### **Arduino Sketch**

* Listens to serial input (formatted RGB data).
* Parses the data and converts it into PWM output on three pins.
* Each PWM channel controls the base of a transistor connected to the respective RGB channel of the LED strip.

<br>

## 3D-Printed Control Panel

Designed and modeled in **Blender**, the control panel houses:

* 3 dials for RGB potentiometers
* A custom dynamic/static mode switch
* Rear casing to mount potentiometers and the 2P2T switch

The model was optimized for 3D printing with internal supports and ergonomic spacing for wiring.
It gives the system a polished, modern look; like a professional lighting console.

<br>

## The crux
<img width="6973" height="2216" alt="IMG_20240430_202234486 (1)" src="https://github.com/user-attachments/assets/7eef11eb-275e-4952-8352-f427d773f426" />
<br>

## Testing & Optimization

* Verified analog and serial data flow independently before full integration.
* Conducted modular testing for each circuit branch.
* Iteratively rewired for minimal voltage drop and maximum power efficiency.
* Final configuration allows seamless mode switching without rebooting or interference.

<br>


## Tech Stack

**Hardware:** Arduino Uno, NPN Transistors, RGB LED Strip, Potentiometers, 2P2T Switch
**Software:** Python (PyAutoGUI, PIL, NumPy), Arduino C++
**Design:** Blender (for enclosure modeling and 3D printing)

<br>

## Future Improvements

* Add wireless control via ESP8266 for smart integration.
* Implement color transition smoothing for cinematic effects.
* Introduce multi-zone ambient lighting across displays.

<br>

## Author

**Satwik Bhusanur**

Inventor | Developer | Designer

[GitHub](https://github.com/voidconsole) | [LinkedIn](https://linkedin.com/in/satwikbhusanur)
