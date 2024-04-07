def put_out_fire(terrain, mouse_pos, radius):
    col = mouse_pos[0] // 5
    row = mouse_pos[1] // 5

    for r in range(max(0, row - radius), min(len(terrain), row + radius + 1)):
        for c in range(max(0, col - radius), min(len(terrain[0]), col + radius + 1)):
            cell = terrain[r, c]
            distance = ((row - r) ** 2 + (col - c) ** 2) ** 0.5
            if distance <= radius and cell.state == 2:
                cell.state = 3

def remove_trees_right_click(terrain, mouse_pos, radius2):
    col = mouse_pos[0] // 5
    row = mouse_pos[1] // 5

    for r in range(max(0, row - radius2), min(len(terrain), row + radius2 + 1)):
        for c in range(max(0, col - radius2), min(len(terrain[0]), col + radius2 + 1)):
            cell = terrain[r, c]
            distance = ((row - r) ** 2 + (col - c) ** 2) ** 0.5
            if distance <= radius2 and cell.state == 1:
                cell.state = 0
