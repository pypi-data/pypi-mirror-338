# cmtqoutilities

[![PyPI](https://img.shields.io/pypi/v/cmtqoutilities.svg)](https://pypi.org/project/cmtqoutilities/)

**cmtqoutilities** is a Python toolkit that provides high-level APIs to control and automate a diverse range of laboratory hardware devices used in quantum optics and condensed matter experiments. The package offers abstraction layers for devices such as pressure controllers, serial interfaces, positioning stages, databases, and data acquisition tools.

---

## 🚀 Key Features

- 🧪 **Experiment automation** through a unified `Operator` class
- 📡 **Instrument control** for Zaber actuators, Numato relays, Picoscope oscilloscopes, Atto IDS3010 sensors, and more
- 🧾 **Database integration** for logging and tracking experimental metadata
- 🗃️ **Filesystem and code snapshot utilities** for reproducible research
- ⚙️ **Cross-platform support** for Windows and Unix-like systems

---

## 🧱 Module Overview

### `modOp.py`
Defines the `Operator` class — a central controller for experiments, handling setup configuration, data and code paths, database connections, and version management.

### `database.py`
Handles experimental metadata logging, MySQL interactions, and retrieval of recent or historical experiment data.

### `pressureControl.py`
Provides an interface to communicate with pressure controllers over serial, supporting pressure reading and basic control commands.

### `zaber*.py`
Multiple modules to control Zaber linear actuators (LRQ600, LSQ150, etc.), supporting movement, homing, and axis configuration.

### `numatoLabRL002.py`
Enables control of Numato Lab USB relay modules for hardware switching tasks.

### `picoscope.py`, `ps4000a.py`
Modules for acquiring data from PicoTech oscilloscopes (e.g. PS4000 series), integrating with the experiment automation flow.

### `attoIDS3010.py`
Interface to Atto IDS3010 displacement sensors, providing sub-nanometer position measurement capabilities.

### `operatorManualSetup.py`
Support functions for setting up manual experimental configurations, such as pre-alignment or testing.

---

## 📦 Installation

```bash
pip install cmtqoutilities
```

Requires Python 3.8 or higher. Dependencies include `numpy`, `scipy`, `requests`, `pyserial`, `pymysql`, `nbconvert`, `jupyter`, and hardware-specific libraries.

