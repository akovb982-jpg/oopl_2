import turtle, random, math, colorsys

class Petal:
    def __init__(self, t, color, size=140):
        self.t, self.color, self.size = t, color, size
    def draw(self):
        self.t.color(self.color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.circle(self.size, 60)
            self.t.left(120)
        self.t.end_fill()
class Leaf:
    def __init__(self, t):
        self.t = t
    def draw(self, x, y, angle, size=30):
        self.t.penup(); self.t.goto(x, y); self.t.setheading(angle); self.t.pendown()
        self.t.color("dark green")
        self.t.begin_fill()
        self.t.circle(size, 90); self.t.left(90); self.t.circle(size, 90)
        self.t.end_fill()
class Stem:
    def __init__(self, t, length=200):
        self.t, self.length = t, length
    def draw(self, x, y, angle=-90):
        self.t.penup(); self.t.goto(x, y); self.t.setheading(angle); self.t.pendown()
        self.t.color("#3a9c3a"); self.t.pensize(4)
        self.t.forward(self.length); self.t.pensize(1)
class Flower:
    @staticmethod
    def random_color():
        r, g, b = colorsys.hsv_to_rgb(random.random(), 0.85, 0.95)
        return "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))
    def __init__(self, t, x, y, stem_angle=-90, stem_length=300,
                 num_petals=6, petal_size=130):
        self.t, self.x, self.y = t, x, y
        self.stem_angle, self.num_petals, self.petal_size = stem_angle, num_petals, petal_size
        self.color = Flower.random_color()
        self.stem, self.leaf = Stem(t, stem_length), Leaf(t)
        self.petals = [Petal(t, self.color, petal_size) for _ in range(num_petals)]
    def draw(self):
        self.stem.draw(self.x, self.y, self.stem_angle)
        rad = math.radians(self.stem_angle)
        lx = self.x + 0.5 * self.stem.length * math.cos(rad)
        ly = self.y + 0.5 * self.stem.length * math.sin(rad)
        self.leaf.draw(lx, ly, self.stem_angle + 70)
        self.leaf.draw(lx, ly, self.stem_angle - 70)
        self.t.penup(); self.t.goto(self.x, self.y); self.t.setheading(0); self.t.pendown()
        for p in self.petals:
            p.draw(); self.t.left(360 / self.num_petals)
        r = max(14, self.petal_size // 7)
        self.t.penup(); self.t.goto(self.x, self.y - r); self.t.pendown()
        self.t.color("#FFD700"); self.t.begin_fill(); self.t.circle(r); self.t.end_fill()
n = int(input("Скільки квіток? (1-9): "))
screen = turtle.Screen()
screen.bgcolor("white"); screen.title("Букет квіток"); screen.setup(900, 700)
t = turtle.Turtle(); t.speed(0); t.hideturtle()
base_x, base_y = 0, -320
spread = min(40, 10 * n)
angles = [spread * (i / (n - 1) - 0.5) for i in range(n)] if n > 1 else [0]
for i in sorted(range(n), key=lambda i: abs(angles[i]), reverse=True):
    stem_len = 320 + random.randint(-20, 20)
    rad = math.radians(90 + angles[i])
    fx = base_x + stem_len * math.cos(rad)
    fy = base_y + stem_len * math.sin(rad)
    Flower(t, fx, fy,
           stem_angle=90 + angles[i] - 180,
           stem_length=stem_len,
           num_petals=random.randint(5, 8),
           petal_size=random.randint(120, 145)).draw()
screen.mainloop()