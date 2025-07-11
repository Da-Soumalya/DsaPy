def process_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y-axis at y={y}")
        case (x, 0):
            print(f"X-axis at x={x}")
        case (x, y):
            print(f"Point at x={x}, y={y}")
        case _:
            print("Not a 2D point")

process_point((0, 0))     # Origin
process_point((5, 0))     # X-axis at x=5
process_point((3, 4))     # Point at x=3, y=4
