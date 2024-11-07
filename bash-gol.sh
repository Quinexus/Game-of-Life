#!/bin/bash

# Remaking my python Conway's game of life in bash

### Rules
# underpopulation <2 neighbours dies
# lives with 2 or 3 neighbours
# overpopulation >3 neighbours dies
# reproduction dead with =3 neighbours lives

mapfile -t board < board.txt

print_board () {
	for i in ${board[@]}; do
		echo $i
	done
}

check_neighbours (line_index, cell_index) {
	declare -i n = 0

	#top cell = line - 1
	if [$line_index != 0]
	then
		if [${board[$line_index-1][cell_index]} == 'X']
		then
			n = $((n + 1))
		fi
	fi
	



}

