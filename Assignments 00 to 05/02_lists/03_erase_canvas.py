import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20


def erase_objects(canvas, eraser):
    x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    y = canvas.winfo_pointery() - canvas.winfo_rooty()

    items = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    for item in items:
        if item != eraser:
            canvas.itemconfig(item, fill="white")


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    def on_click(event):
        nonlocal eraser
        eraser = canvas.create_rectangle(
            event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink"
        )
        canvas.unbind("<Button-1>")
        root.after(10, move_eraser)

    eraser = None
    canvas.bind("<Button-1>", on_click)

    def move_eraser():
        x = canvas.winfo_pointerx() - canvas.winfo_rootx()
        y = canvas.winfo_pointery() - canvas.winfo_rooty()
        canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        erase_objects(canvas, eraser)
        root.after(50, move_eraser)

    root.mainloop()


if __name__ == "__main__":
    main()
