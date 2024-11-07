#!/bin/bash

# Remaking my python Conway's game of life in bash

### Rules
# underpopulation <2 neighbours dies
# lives with 2 or 3 neighbours
# overpopulation >3 neighbours dies
# reproduction dead with =3 neighbours lives

mapfile -t array < board.txt