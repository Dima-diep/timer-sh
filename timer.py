#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import time
import os

print("Write time in sec:")
a = int(input())

for i in range(0, a):
  print(i)
  time.sleep(1)
  os.system("clear")
print("END!")
