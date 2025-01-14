# Hanoi Towers
def hanoi_towers(n, source, target, auxiliary):
    if n > 0:
        hanoi_towers(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi_towers(n-1, auxiliary, target, source)
