# Rubu Tech – Temas Socket API

## Overview

This Python package provides an easy-to-use API for controlling Temas hardware devices via TCP/IP socket communication. It is designed for laboratory setups, test stations, robotic platforms, or any scenario requiring accurate positioning and sensor feedback.

---

## Features

- TCP socket communication with Temas devices
- Distance and mean distance queries
- Azimuth and elevation positioning in coarse, fast, fine steps
- Device control commands like `move_home`, `shutdown`, `restart`
- System status queries: temperature, hostname, MAC address, etc.
- Simple object-oriented interface for quick integration

---

## Installation

Install via pip:

```bash
pip install rubu-tech-pypi

## Usage

## Basic Example: Query distance

```python
from rubu_tech.temas import Control

temas = Control(port=8082)
distance = temas.distance()
print(f"Measured distance: {distance}")