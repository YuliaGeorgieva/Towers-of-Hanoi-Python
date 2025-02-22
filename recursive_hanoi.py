def move_disk(disk, fromRod, toRod, move_number):
    print(f"{move_number}. Move disk {disk} from {fromRod} -> {toRod}")

def hanoi_recursive(n, startRod, endRod, middleRod, move_counter):
    
    if n == 1:

        move_counter[0] += 1
        move_disk(n, startRod, endRod, move_counter[0])  

        return

    hanoi_recursive(n - 1, startRod, middleRod, endRod, move_counter)

    move_counter[0] += 1

    move_disk(n, startRod, endRod, move_counter[0])

    hanoi_recursive(n - 1, middleRod, endRod, startRod, move_counter)