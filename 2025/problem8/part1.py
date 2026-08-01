from utils import FileIO as iO


def main():
    lines = iO.parse('input1.txt', {'separator': '\n'})
    items = [list(map(int, line.split(','))) for line in lines]
    
    


if __name__ == '__main__':
    main()