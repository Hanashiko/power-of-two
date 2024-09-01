def isPowerOfTwo(n: int) -> bool:
    for i in range(32):
        if 2**i == n:
            return True
    return False

def main() -> None:
    print(isPowerOfTwo(1))
    print(isPowerOfTwo(16))
    print(isPowerOfTwo(3))
    
if __name__ == "__main__":
    main()