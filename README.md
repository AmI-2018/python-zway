# REST operation of On/Off Devices in Python #

The modules provided in this repository show how some devices can be operated (i.e., turned on or off, and get data from them) on Z-Wave networks using REST APIs (through the [Z-Way server](https://z-wave.me/z-way/)). It supports the connection to the Z-Way API through HTTP Basic Auth.

* The `rest.py` module provides a really basic API for easily calling REST services
* The `zway.py` shows how to turn on every "switch" device (i.e., lamps) connected to a Z-Wave network. Such devices are turned on and, after 10s, they are turned off.

_Please be aware that this module only works on machines running the [Z-Way server](https://z-wave.me/z-way/)._
