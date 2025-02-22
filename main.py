from recursive_hanoi import hanoi_recursive
from iterative_hanoi import hanoi_iterative

def main():
    while True:
        try:
            n = int(input("Enter the number of disks: "))
            if n <= 0:
                raise ValueError("Number of disks must be bigger than 0.")
            break
        except ValueError as e:
            print(e)

    print("\nRecursive Solution:")
    
    move_counter = [0] 
    hanoi_recursive(n, 'A', 'C', 'B', move_counter)

    print("\nIterative Solution:")
    hanoi_iterative(n)

if __name__ == "__main__":
    main()