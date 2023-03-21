from slow_alg import SlowSuperstructureAlgorithm
from fast_alg import FastSuperstructureAlgorithm

def main() -> None:
    a = SlowSuperstructureAlgorithm()
    print(a.compute_superstructure(["abc", "bcdflk", "clkm"]))
    b = FastSuperstructureAlgorithm()
    print(b.compute_superstructure(["abc", "bcdflk", "clkm"]))
    return None

if __name__ == '__main__':
    main()
