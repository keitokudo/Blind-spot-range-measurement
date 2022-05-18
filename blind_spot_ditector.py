import argparse
from pathlib import Path
from typing import List, Dict, Union, Optional
import tkinter as tk
import math

# Canvasの作成
root = tk.Tk()
root.geometry("1280x800")
root.update_idletasks()
width, height = root.winfo_width(), root.winfo_height()
#ratio = root.winfo_width() / root.winfo_screenwidth()
#d = math.sqrt(root.winfo_width()**2 + root.winfo_height()**2)
#pixel_per_mm = d / (13.3 * ratio * 25.4)
canvas = tk.Canvas(root, bg = "white")

def key_event(e):
    key = e.keysym
    # 単位はmm(にしたい)
    #pixel_per_mm = 5.026690556421138
    #dx, dy = pixel_per_mm * 5, pixel_per_mm * 5
    dx, dy = 1, 1
    x, y = 0, 0
    
    if key == "Up":
        y -= dy
    if key == "Down":
        y += dy
    if key == "Left":
        x -= dx
    if key == "Right":
        x += dx
    if key == "Right":
        x += dx
       
    canvas.move("circle", x, y)
   
def draw_point(e):
    x0, y0, x1, y1 = canvas.bbox("circle")
    point_center_x, point_center_y = (x0 + x1) /2, (y0 + y1) /2
    
    canvas.create_oval(
        point_center_x + 2, point_center_y + 2,
        point_center_x - 2, point_center_y - 2,
        fill="RED",
        outline=None,
    )

   
def main(args):
    # Canvasを配置
    canvas.pack(fill = tk.BOTH, expand = True)

    
    if args.mode == "horizontal":
        if args.eye == "right":
            center_x, center_y = 300, 300
            cross_radius = 10
            circle_x, circle_y = center_x + 100, center_y
            radius = cross_radius
        elif args.eye == "left":
            center_x, center_y = width - 300, 300
            cross_radius = 10
            circle_x, circle_y = center_x - 100, center_y
            radius = cross_radius
        else:
            raise NotImplementedError()
            
        
    elif args.mode == "vertical":
        if args.eye == "right":
            center_x, center_y = 640, height - 100
            cross_radius = 10    
            circle_x, circle_y = center_x, center_y - 100
            radius = cross_radius
        elif args.eye == "left":
            center_x, center_y = 640, 400
            cross_radius = 10    
            circle_x, circle_y = center_x, center_y - 100
            radius = cross_radius
        else:
            raise NotImplementedError()
        
    else:
        raise NotImplementedError()
    
    circle_id = canvas.create_oval(
        circle_x - radius, circle_y - radius,
        circle_x + radius, circle_y + radius,
        tag="circle",
        fill="BLACK",
    )

    line_width = 2
    vertical_line = canvas.create_line(
        center_x,
        center_y - cross_radius,
        center_x,
        center_y + cross_radius,
        width=line_width,
    )
    
    horizontal_line = canvas.create_line(
        center_x - cross_radius,
        center_y,
        center_x + cross_radius,
        center_y,
        width=line_width,
    )
    
    root.bind("<KeyPress>", key_event)
    root.bind('<Return>', draw_point)
    root.mainloop()
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        type=str,
        choices=["horizontal", "vertical"],
        default="horizontal",
    )

    parser.add_argument(
        "--eye",
        type=str,
        choices=["right", "left"],
        default="right",
    )
    
    args = parser.parse_args()
    main(args)

    
