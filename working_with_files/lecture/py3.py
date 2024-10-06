import sys 
from py1 import main as greating
from py2 import main as exiting
def main():
    try:
        if sys.argv[1] == 'greet':
            greating()
        elif sys.argv[1] == 'goodbuy':
            exiting()
        else:
            print('Unknown argument')
        
    except IndexError:
        print(3)
    

if __name__ == "__main__":
    main()