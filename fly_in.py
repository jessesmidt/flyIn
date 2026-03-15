import sys
from src.parsing import Parser

def main() -> None:
	if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    try:
        config = parse_config(sys.argv[1])
    except ValueError as e:
        print(f"Error: {e}")
        return
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return




if __name__ == "__main__":
	main()
