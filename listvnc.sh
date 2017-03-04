#!/bin/bash

ps aux | grep Xvnc | grep -v grep | awk '{print $12,$1}' | sed 's/://' | sort
