def pyramid(type, height):
    for i in range(height):
        if type == 'left':
            print(f"{'*'*(i+1):>{height}}")
        elif type == 'right':
            print(f"{'*'*(i+1):<{height}}")
        elif type == 'both':
            print(f"{'**'*(i + 1):^{height*2}}")


if __name__ == '__main__':
    pyramid('both', 10)