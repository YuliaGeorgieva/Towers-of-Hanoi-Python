def move_disk(disk, from_rod, to_rod, move_number):
    print(f"{move_number}. Move disk {disk} from {from_rod} -> {to_rod}")

def hanoi_iterative(n):
   
    if n < 1:
        raise ValueError("Number of disks must be bigger than 0.")

    total_moves = 2 ** n - 1 
    startRod, middleRod, endRod = 'A', 'B', 'C' 

    if n % 2 == 0:
        middleRod, endRod = endRod, middleRod

    pegs = {startRod: list(range(n, 0, -1)), middleRod: [], endRod: []}

    move_counter = 0 

    for move in range(1, total_moves + 1):

        from_rod = (move & move - 1) % 3
        to_rod = ((move | move - 1) + 1) % 3

        rods = [startRod, middleRod, endRod]  
        from_rod = rods[from_rod]
        to_rod = rods[to_rod]

        if pegs[from_rod]:

            disk = pegs[from_rod].pop() 
            pegs[to_rod].append(disk)  
            move_counter += 1
            move_disk(disk, from_rod, to_rod, move_counter)

        else:
            
            disk = pegs[to_rod].pop()  
            pegs[from_rod].append(disk) 
            move_counter += 1
            move_disk(disk, to_rod, from_rod, move_counter)
