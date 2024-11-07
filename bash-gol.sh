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

row_count=${#board[@]}
column_count=${#board[0]}

check_neighbours () {
	local -i neighbours=0

	local row_index=$1
	local column_index=$2

	directions=(
		"-1 -1" "-1 0" "-1 1"
		"0 -1" "0 1"
		"1 -1" "1 0" "1 1"
	)

	for dir in "${directions[@]}"; do
		set -- $dir

		local direction_row=$1
		local direction_column=$2

		local neighbour_row=$((row_index + direction_row))
		local neighbour_column=$((column_index + direction_column))

		if [[ $neighbour_row -ge 0 && $neighbour_row -lt $row_count && $neighbour_column -ge 0 && $neighbour_column -lt $column_count ]]; then
			if [[ ${board[neighbour_row]:neighbour_column:1} == "X" ]]; then
				neighbours=$((neighbours + 1))
			fi
		fi
	done

	echo "$neighbours"
}

update_board () {
	local new_board=()

	for ((i=0; i<$row_count; i++)); do
		new_row=""
		for ((j=0; j<$column_count; j++)); do
			neighbour_count=$(check_neighbours $i $j)
			cell=${board[i]:j:1}

			if [[ $cell = "X" && $neighbour_count -eq 2 ]]; then
				new_row=${new_row}X
			elif [[ "$neighbour_count" -eq 3 ]]; then
				new_row=${new_row}X
			else
				new_row=${new_row}O
			fi
		done
		new_board+=($new_row)
	done

	board=(${new_board[@]})
}

write_board () {
	filename=$1
	for row in ${board[@]}; do
		echo $row >> $filename
	done
}

choice=""
while [[ -z $choice ]]; do
	print_board
	update_board
	read choice
done
#write_board output.txt