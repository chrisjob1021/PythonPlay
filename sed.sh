#!/bin/bash

sed '/#/ { 
r count_bits.py
d
}' README.md
