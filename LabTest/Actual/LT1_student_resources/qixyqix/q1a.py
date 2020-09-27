def get_tank_volume(width, length, height):
    if width <=0 or length <= 0 or height <= 0:
        print("Error: width, length and height should be positive integers")
    else:
        return (width*length*height)//1000
    
