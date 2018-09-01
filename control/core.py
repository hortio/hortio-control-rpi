#!/usr/bin/python

from Adafruit_MCP230XX import Adafruit_MCP230XX
import time

if __name__ == '__main__':
  # ***************************************************
  # Set num_gpios to 8 for MCP23008 or 16 for MCP23017!
  # ***************************************************
  mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 8) # MCP23008
  # mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16) # MCP23017

  # Set pins 0, 1 and 2 to output (you can set pins 0..15 this way)
  mcp.config(0, mcp.OUTPUT)
  mcp.config(1, mcp.OUTPUT)
  mcp.config(2, mcp.OUTPUT)

  # Python speed test on output 0 toggling at max speed
  while (True):
    mcp.output(0, 2)  # Pin 0 High
    time.sleep(1);
    mcp.output(0, 2)  # Pin 0 Low
    time.sleep(1);