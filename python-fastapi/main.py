from fastapi import FastAPI
import json
import math
import sys
import time

DATA = '[{"type":"triangle","sizeA":54,"sizeB":93,"sizeC":133},{"type":"triangle","sizeA":35,"sizeB":48,"sizeC":46},{"type":"square","size":59},{"type":"triangle","sizeA":36,"sizeB":76,"sizeC":51},{"type":"rectangle","sizeA":51,"sizeB":31},{"type":"square","size":94},{"type":"square","size":84},{"type":"circle","diameter":77},{"type":"circle","diameter":79},{"type":"square","size":45},{"type":"rectangle","sizeA":3,"sizeB":72},{"type":"circle","diameter":47},{"type":"triangle","sizeA":38,"sizeB":66,"sizeC":63},{"type":"rectangle","sizeA":83,"sizeB":71},{"type":"square","size":75},{"type":"square","size":41},{"type":"triangle","sizeA":42,"sizeB":27,"sizeC":25},{"type":"rectangle","sizeA":83,"sizeB":5},{"type":"triangle","sizeA":36,"sizeB":21,"sizeC":56},{"type":"triangle","sizeA":55,"sizeB":78,"sizeC":115},{"type":"rectangle","sizeA":87,"sizeB":42},{"type":"square","size":11},{"type":"square","size":24},{"type":"triangle","sizeA":52,"sizeB":14,"sizeC":41},{"type":"rectangle","sizeA":89,"sizeB":41},{"type":"square","size":14},{"type":"rectangle","sizeA":36,"sizeB":38},{"type":"square","size":81},{"type":"triangle","sizeA":36,"sizeB":22,"sizeC":16},{"type":"rectangle","sizeA":100,"sizeB":75},{"type":"triangle","sizeA":100,"sizeB":26,"sizeC":118},{"type":"rectangle","sizeA":65,"sizeB":68},{"type":"triangle","sizeA":70,"sizeB":22,"sizeC":91},{"type":"rectangle","sizeA":79,"sizeB":46},{"type":"triangle","sizeA":7,"sizeB":97,"sizeC":97},{"type":"square","size":80},{"type":"rectangle","sizeA":77,"sizeB":66},{"type":"square","size":44},{"type":"triangle","sizeA":51,"sizeB":55,"sizeC":59},{"type":"triangle","sizeA":32,"sizeB":30,"sizeC":59},{"type":"circle","diameter":66},{"type":"square","size":72},{"type":"circle","diameter":17},{"type":"triangle","sizeA":9,"sizeB":56,"sizeC":63},{"type":"triangle","sizeA":40,"sizeB":93,"sizeC":61},{"type":"triangle","sizeA":40,"sizeB":17,"sizeC":42},{"type":"square","size":67},{"type":"circle","diameter":54},{"type":"rectangle","sizeA":65,"sizeB":85},{"type":"rectangle","sizeA":100,"sizeB":69},{"type":"circle","diameter":49},{"type":"square","size":17},{"type":"square","size":11},{"type":"triangle","sizeA":31,"sizeB":24,"sizeC":42},{"type":"circle","diameter":29},{"type":"rectangle","sizeA":66,"sizeB":63},{"type":"rectangle","sizeA":76,"sizeB":41},{"type":"rectangle","sizeA":32,"sizeB":95},{"type":"square","size":53},{"type":"circle","diameter":25},{"type":"circle","diameter":73},{"type":"rectangle","sizeA":54,"sizeB":73},{"type":"rectangle","sizeA":71,"sizeB":92},{"type":"rectangle","sizeA":21,"sizeB":8},{"type":"square","size":63},{"type":"circle","diameter":42},{"type":"triangle","sizeA":44,"sizeB":71,"sizeC":60},{"type":"triangle","sizeA":64,"sizeB":59,"sizeC":41},{"type":"rectangle","sizeA":52,"sizeB":34},{"type":"triangle","sizeA":81,"sizeB":28,"sizeC":90},{"type":"circle","diameter":30},{"type":"triangle","sizeA":71,"sizeB":93,"sizeC":125},{"type":"circle","diameter":93},{"type":"rectangle","sizeA":68,"sizeB":72},{"type":"square","size":3},{"type":"triangle","sizeA":12,"sizeB":41,"sizeC":44},{"type":"triangle","sizeA":36,"sizeB":42,"sizeC":66},{"type":"circle","diameter":11},{"type":"rectangle","sizeA":5,"sizeB":62},{"type":"circle","diameter":52},{"type":"square","size":96},{"type":"circle","diameter":49},{"type":"circle","diameter":63},{"type":"rectangle","sizeA":60,"sizeB":95},{"type":"circle","diameter":65},{"type":"square","size":10},{"type":"triangle","sizeA":19,"sizeB":50,"sizeC":36},{"type":"circle","diameter":13},{"type":"square","size":94},{"type":"circle","diameter":78},{"type":"rectangle","sizeA":89,"sizeB":47},{"type":"square","size":96},{"type":"circle","diameter":79},{"type":"triangle","sizeA":76,"sizeB":100,"sizeC":170},{"type":"square","size":51},{"type":"square","size":12},{"type":"circle","diameter":51},{"type":"square","size":63},{"type":"circle","diameter":76},{"type":"circle","diameter":71},{"type":"circle","diameter":80},{"type":"triangle","sizeA":92,"sizeB":78,"sizeC":122},{"type":"rectangle","sizeA":29,"sizeB":13},{"type":"circle","diameter":61},{"type":"square","size":64},{"type":"circle","diameter":76},{"type":"triangle","sizeA":14,"sizeB":84,"sizeC":84},{"type":"square","size":67},{"type":"square","size":66},{"type":"square","size":45},{"type":"rectangle","sizeA":39,"sizeB":64},{"type":"square","size":12},{"type":"circle","diameter":17},{"type":"square","size":80},{"type":"circle","diameter":84},{"type":"circle","diameter":90},{"type":"circle","diameter":75},{"type":"rectangle","sizeA":38,"sizeB":99},{"type":"square","size":39},{"type":"triangle","sizeA":18,"sizeB":98,"sizeC":102},{"type":"circle","diameter":31},{"type":"square","size":35},{"type":"triangle","sizeA":29,"sizeB":53,"sizeC":69},{"type":"triangle","sizeA":92,"sizeB":94,"sizeC":46},{"type":"rectangle","sizeA":45,"sizeB":10},{"type":"square","size":82},{"type":"square","size":23},{"type":"rectangle","sizeA":47,"sizeB":30},{"type":"circle","diameter":57},{"type":"triangle","sizeA":99,"sizeB":68,"sizeC":58},{"type":"rectangle","sizeA":39,"sizeB":9},{"type":"rectangle","sizeA":11,"sizeB":30},{"type":"square","size":34},{"type":"triangle","sizeA":87,"sizeB":50,"sizeC":71},{"type":"triangle","sizeA":48,"sizeB":19,"sizeC":53},{"type":"square","size":70},{"type":"rectangle","sizeA":87,"sizeB":75},{"type":"rectangle","sizeA":87,"sizeB":15},{"type":"circle","diameter":95},{"type":"circle","diameter":9},{"type":"rectangle","sizeA":75,"sizeB":24},{"type":"square","size":78},{"type":"square","size":49},{"type":"triangle","sizeA":64,"sizeB":52,"sizeC":15},{"type":"triangle","sizeA":93,"sizeB":3,"sizeC":92},{"type":"triangle","sizeA":14,"sizeB":42,"sizeC":42},{"type":"square","size":83},{"type":"circle","diameter":61},{"type":"circle","diameter":54},{"type":"triangle","sizeA":87,"sizeB":83,"sizeC":155},{"type":"circle","diameter":72},{"type":"square","size":87},{"type":"triangle","sizeA":5,"sizeB":69,"sizeC":73},{"type":"triangle","sizeA":66,"sizeB":23,"sizeC":72},{"type":"triangle","sizeA":17,"sizeB":88,"sizeC":87},{"type":"rectangle","sizeA":72,"sizeB":98},{"type":"square","size":25},{"type":"triangle","sizeA":43,"sizeB":46,"sizeC":17},{"type":"square","size":85},{"type":"circle","diameter":67},{"type":"square","size":41},{"type":"square","size":79},{"type":"triangle","sizeA":5,"sizeB":14,"sizeC":13},{"type":"triangle","sizeA":34,"sizeB":36,"sizeC":44},{"type":"rectangle","sizeA":34,"sizeB":61},{"type":"circle","diameter":68},{"type":"square","size":84},{"type":"circle","diameter":96},{"type":"circle","diameter":60},{"type":"square","size":23},{"type":"circle","diameter":28},{"type":"triangle","sizeA":77,"sizeB":36,"sizeC":75},{"type":"square","size":26},{"type":"rectangle","sizeA":38,"sizeB":73},{"type":"square","size":24},{"type":"circle","diameter":8},{"type":"triangle","sizeA":4,"sizeB":18,"sizeC":18},{"type":"circle","diameter":16},{"type":"rectangle","sizeA":93,"sizeB":98},{"type":"square","size":39},{"type":"square","size":21},{"type":"triangle","sizeA":85,"sizeB":66,"sizeC":141},{"type":"circle","diameter":74},{"type":"circle","diameter":9},{"type":"rectangle","sizeA":28,"sizeB":66},{"type":"triangle","sizeA":87,"sizeB":62,"sizeC":113},{"type":"rectangle","sizeA":5,"sizeB":45},{"type":"circle","diameter":68},{"type":"triangle","sizeA":55,"sizeB":78,"sizeC":52},{"type":"rectangle","sizeA":36,"sizeB":62},{"type":"rectangle","sizeA":64,"sizeB":72},{"type":"rectangle","sizeA":47,"sizeB":82},{"type":"circle","diameter":17},{"type":"square","size":5},{"type":"square","size":19},{"type":"square","size":24},{"type":"rectangle","sizeA":22,"sizeB":72},{"type":"rectangle","sizeA":53,"sizeB":62},{"type":"rectangle","sizeA":24,"sizeB":33},{"type":"rectangle","sizeA":2,"sizeB":18},{"type":"square","size":53},{"type":"triangle","sizeA":91,"sizeB":72,"sizeC":107},{"type":"circle","diameter":9},{"type":"circle","diameter":14},{"type":"triangle","sizeA":8,"sizeB":50,"sizeC":47},{"type":"circle","diameter":21},{"type":"rectangle","sizeA":29,"sizeB":19},{"type":"circle","diameter":51},{"type":"square","size":92},{"type":"circle","diameter":21},{"type":"square","size":11},{"type":"rectangle","sizeA":36,"sizeB":7},{"type":"rectangle","sizeA":76,"sizeB":57},{"type":"triangle","sizeA":40,"sizeB":8,"sizeC":36},{"type":"square","size":97},{"type":"circle","diameter":37},{"type":"square","size":53},{"type":"circle","diameter":63},{"type":"triangle","sizeA":23,"sizeB":94,"sizeC":96},{"type":"square","size":95},{"type":"triangle","sizeA":63,"sizeB":67,"sizeC":71},{"type":"triangle","sizeA":99,"sizeB":91,"sizeC":139},{"type":"rectangle","sizeA":52,"sizeB":36},{"type":"rectangle","sizeA":73,"sizeB":65},{"type":"square","size":78},{"type":"square","size":51},{"type":"rectangle","sizeA":62,"sizeB":93},{"type":"circle","diameter":20},{"type":"circle","diameter":63},{"type":"triangle","sizeA":58,"sizeB":3,"sizeC":59},{"type":"circle","diameter":92},{"type":"square","size":12},{"type":"circle","diameter":25},{"type":"rectangle","sizeA":75,"sizeB":98},{"type":"circle","diameter":46},{"type":"triangle","sizeA":99,"sizeB":25,"sizeC":93},{"type":"circle","diameter":55},{"type":"rectangle","sizeA":58,"sizeB":93},{"type":"square","size":5},{"type":"triangle","sizeA":24,"sizeB":22,"sizeC":6},{"type":"square","size":65},{"type":"rectangle","sizeA":36,"sizeB":66},{"type":"square","size":83},{"type":"circle","diameter":93},{"type":"square","size":46},{"type":"rectangle","sizeA":44,"sizeB":87},{"type":"triangle","sizeA":44,"sizeB":65,"sizeC":91},{"type":"triangle","sizeA":89,"sizeB":78,"sizeC":109},{"type":"circle","diameter":64},{"type":"square","size":3},{"type":"rectangle","sizeA":81,"sizeB":90},{"type":"circle","diameter":67},{"type":"rectangle","sizeA":86,"sizeB":64},{"type":"circle","diameter":88},{"type":"triangle","sizeA":68,"sizeB":46,"sizeC":79},{"type":"rectangle","sizeA":19,"sizeB":60},{"type":"circle","diameter":49},{"type":"circle","diameter":58},{"type":"circle","diameter":6},{"type":"triangle","sizeA":25,"sizeB":3,"sizeC":25},{"type":"square","size":28},{"type":"square","size":94},{"type":"triangle","sizeA":15,"sizeB":60,"sizeC":67},{"type":"triangle","sizeA":51,"sizeB":77,"sizeC":99},{"type":"circle","diameter":65},{"type":"triangle","sizeA":21,"sizeB":55,"sizeC":72},{"type":"square","size":98},{"type":"triangle","sizeA":27,"sizeB":16,"sizeC":16},{"type":"rectangle","sizeA":27,"sizeB":28},{"type":"triangle","sizeA":10,"sizeB":97,"sizeC":95},{"type":"square","size":8},{"type":"circle","diameter":26},{"type":"triangle","sizeA":33,"sizeB":85,"sizeC":99},{"type":"square","size":18},{"type":"circle","diameter":65},{"type":"rectangle","sizeA":44,"sizeB":50},{"type":"rectangle","sizeA":6,"sizeB":59},{"type":"square","size":94},{"type":"circle","diameter":36},{"type":"square","size":96},{"type":"circle","diameter":34},{"type":"square","size":49},{"type":"rectangle","sizeA":90,"sizeB":57},{"type":"circle","diameter":50},{"type":"triangle","sizeA":76,"sizeB":47,"sizeC":88},{"type":"rectangle","sizeA":29,"sizeB":79},{"type":"rectangle","sizeA":88,"sizeB":10},{"type":"circle","diameter":68},{"type":"circle","diameter":11},{"type":"circle","diameter":81},{"type":"triangle","sizeA":96,"sizeB":81,"sizeC":78},{"type":"triangle","sizeA":77,"sizeB":12,"sizeC":78},{"type":"circle","diameter":61},{"type":"triangle","sizeA":34,"sizeB":72,"sizeC":85},{"type":"rectangle","sizeA":82,"sizeB":60},{"type":"rectangle","sizeA":75,"sizeB":67},{"type":"triangle","sizeA":15,"sizeB":12,"sizeC":11},{"type":"square","size":39},{"type":"circle","diameter":45},{"type":"square","size":48},{"type":"square","size":36},{"type":"triangle","sizeA":62,"sizeB":6,"sizeC":61},{"type":"square","size":64},{"type":"circle","diameter":54},{"type":"circle","diameter":97},{"type":"triangle","sizeA":6,"sizeB":4,"sizeC":5},{"type":"triangle","sizeA":96,"sizeB":32,"sizeC":117},{"type":"triangle","sizeA":27,"sizeB":43,"sizeC":59},{"type":"rectangle","sizeA":75,"sizeB":48},{"type":"circle","diameter":14},{"type":"triangle","sizeA":41,"sizeB":70,"sizeC":51},{"type":"triangle","sizeA":11,"sizeB":98,"sizeC":95},{"type":"square","size":81},{"type":"square","size":56},{"type":"circle","diameter":77},{"type":"square","size":16},{"type":"circle","diameter":79},{"type":"square","size":12},{"type":"rectangle","sizeA":50,"sizeB":11},{"type":"rectangle","sizeA":97,"sizeB":87},{"type":"triangle","sizeA":65,"sizeB":22,"sizeC":50},{"type":"triangle","sizeA":65,"sizeB":80,"sizeC":89},{"type":"square","size":39},{"type":"square","size":55},{"type":"circle","diameter":77},{"type":"triangle","sizeA":93,"sizeB":69,"sizeC":26},{"type":"triangle","sizeA":94,"sizeB":89,"sizeC":68},{"type":"triangle","sizeA":42,"sizeB":12,"sizeC":52},{"type":"circle","diameter":37},{"type":"square","size":20},{"type":"circle","diameter":27},{"type":"square","size":45},{"type":"square","size":68},{"type":"triangle","sizeA":89,"sizeB":39,"sizeC":105},{"type":"circle","diameter":29},{"type":"square","size":78},{"type":"square","size":73},{"type":"triangle","sizeA":28,"sizeB":10,"sizeC":30},{"type":"triangle","sizeA":15,"sizeB":53,"sizeC":56},{"type":"square","size":78},{"type":"circle","diameter":26},{"type":"triangle","sizeA":68,"sizeB":75,"sizeC":87},{"type":"square","size":70},{"type":"triangle","sizeA":24,"sizeB":79,"sizeC":56},{"type":"triangle","sizeA":25,"sizeB":54,"sizeC":51},{"type":"triangle","sizeA":19,"sizeB":83,"sizeC":93},{"type":"circle","diameter":26},{"type":"triangle","sizeA":84,"sizeB":62,"sizeC":143},{"type":"circle","diameter":92},{"type":"square","size":23},{"type":"rectangle","sizeA":27,"sizeB":26},{"type":"rectangle","sizeA":33,"sizeB":32},{"type":"triangle","sizeA":40,"sizeB":17,"sizeC":29},{"type":"circle","diameter":93},{"type":"circle","diameter":28},{"type":"triangle","sizeA":3,"sizeB":42,"sizeC":43},{"type":"circle","diameter":10},{"type":"square","size":60},{"type":"square","size":89},{"type":"circle","diameter":44},{"type":"square","size":30},{"type":"triangle","sizeA":73,"sizeB":44,"sizeC":70},{"type":"circle","diameter":5},{"type":"triangle","sizeA":57,"sizeB":85,"sizeC":45},{"type":"rectangle","sizeA":9,"sizeB":13},{"type":"rectangle","sizeA":18,"sizeB":22},{"type":"square","size":17},{"type":"square","size":27},{"type":"circle","diameter":46},{"type":"square","size":58},{"type":"rectangle","sizeA":26,"sizeB":61},{"type":"rectangle","sizeA":58,"sizeB":88},{"type":"square","size":65},{"type":"square","size":60},{"type":"rectangle","sizeA":100,"sizeB":49},{"type":"circle","diameter":42},{"type":"rectangle","sizeA":95,"sizeB":96},{"type":"square","size":49},{"type":"square","size":3},{"type":"rectangle","sizeA":30,"sizeB":4},{"type":"rectangle","sizeA":34,"sizeB":25},{"type":"square","size":89},{"type":"rectangle","sizeA":5,"sizeB":21},{"type":"triangle","sizeA":58,"sizeB":75,"sizeC":37},{"type":"square","size":87},{"type":"circle","diameter":46},{"type":"rectangle","sizeA":56,"sizeB":28},{"type":"triangle","sizeA":28,"sizeB":65,"sizeC":68},{"type":"rectangle","sizeA":75,"sizeB":55},{"type":"circle","diameter":21},{"type":"rectangle","sizeA":57,"sizeB":17},{"type":"rectangle","sizeA":50,"sizeB":95},{"type":"circle","diameter":12},{"type":"rectangle","sizeA":71,"sizeB":8},{"type":"rectangle","sizeA":36,"sizeB":95},{"type":"rectangle","sizeA":76,"sizeB":39},{"type":"square","size":7},{"type":"circle","diameter":46},{"type":"rectangle","sizeA":18,"sizeB":32},{"type":"circle","diameter":51},{"type":"triangle","sizeA":95,"sizeB":26,"sizeC":116},{"type":"triangle","sizeA":30,"sizeB":78,"sizeC":61},{"type":"triangle","sizeA":43,"sizeB":69,"sizeC":53},{"type":"square","size":76},{"type":"circle","diameter":50},{"type":"rectangle","sizeA":73,"sizeB":39},{"type":"circle","diameter":5},{"type":"circle","diameter":31},{"type":"rectangle","sizeA":70,"sizeB":11},{"type":"rectangle","sizeA":38,"sizeB":73},{"type":"triangle","sizeA":38,"sizeB":96,"sizeC":78},{"type":"square","size":27},{"type":"circle","diameter":74},{"type":"circle","diameter":54},{"type":"square","size":98},{"type":"circle","diameter":51},{"type":"triangle","sizeA":29,"sizeB":57,"sizeC":62},{"type":"circle","diameter":60},{"type":"rectangle","sizeA":97,"sizeB":64},{"type":"circle","diameter":65},{"type":"circle","diameter":86},{"type":"circle","diameter":98},{"type":"rectangle","sizeA":15,"sizeB":21},{"type":"rectangle","sizeA":48,"sizeB":76},{"type":"rectangle","sizeA":73,"sizeB":53},{"type":"rectangle","sizeA":67,"sizeB":36},{"type":"rectangle","sizeA":63,"sizeB":8},{"type":"triangle","sizeA":69,"sizeB":60,"sizeC":17},{"type":"triangle","sizeA":19,"sizeB":95,"sizeC":79},{"type":"circle","diameter":83},{"type":"circle","diameter":63},{"type":"circle","diameter":53},{"type":"square","size":5},{"type":"rectangle","sizeA":99,"sizeB":57},{"type":"triangle","sizeA":36,"sizeB":20,"sizeC":47},{"type":"rectangle","sizeA":100,"sizeB":57},{"type":"circle","diameter":21},{"type":"circle","diameter":6},{"type":"circle","diameter":24},{"type":"circle","diameter":67},{"type":"circle","diameter":14},{"type":"rectangle","sizeA":93,"sizeB":54},{"type":"rectangle","sizeA":52,"sizeB":47},{"type":"square","size":53},{"type":"triangle","sizeA":31,"sizeB":75,"sizeC":53},{"type":"rectangle","sizeA":69,"sizeB":90},{"type":"rectangle","sizeA":59,"sizeB":76},{"type":"rectangle","sizeA":82,"sizeB":84},{"type":"triangle","sizeA":53,"sizeB":72,"sizeC":120},{"type":"circle","diameter":44},{"type":"square","size":37},{"type":"circle","diameter":77},{"type":"circle","diameter":94},{"type":"square","size":84},{"type":"square","size":78},{"type":"square","size":20},{"type":"rectangle","sizeA":54,"sizeB":91},{"type":"square","size":99},{"type":"triangle","sizeA":49,"sizeB":71,"sizeC":75},{"type":"rectangle","sizeA":18,"sizeB":76},{"type":"square","size":68},{"type":"triangle","sizeA":35,"sizeB":86,"sizeC":109},{"type":"triangle","sizeA":38,"sizeB":41,"sizeC":21},{"type":"circle","diameter":94},{"type":"triangle","sizeA":77,"sizeB":73,"sizeC":124},{"type":"rectangle","sizeA":99,"sizeB":11},{"type":"rectangle","sizeA":45,"sizeB":70},{"type":"circle","diameter":88},{"type":"square","size":8},{"type":"triangle","sizeA":55,"sizeB":90,"sizeC":116},{"type":"rectangle","sizeA":20,"sizeB":89},{"type":"square","size":26},{"type":"rectangle","sizeA":95,"sizeB":62},{"type":"rectangle","sizeA":67,"sizeB":72},{"type":"circle","diameter":82},{"type":"square","size":17},{"type":"rectangle","sizeA":3,"sizeB":79},{"type":"triangle","sizeA":100,"sizeB":83,"sizeC":154},{"type":"circle","diameter":52},{"type":"rectangle","sizeA":67,"sizeB":97},{"type":"square","size":34},{"type":"circle","diameter":24},{"type":"rectangle","sizeA":79,"sizeB":61},{"type":"rectangle","sizeA":34,"sizeB":87},{"type":"triangle","sizeA":29,"sizeB":43,"sizeC":35},{"type":"rectangle","sizeA":23,"sizeB":53},{"type":"triangle","sizeA":53,"sizeB":49,"sizeC":16},{"type":"triangle","sizeA":86,"sizeB":32,"sizeC":88},{"type":"circle","diameter":83},{"type":"rectangle","sizeA":87,"sizeB":36},{"type":"circle","diameter":100},{"type":"triangle","sizeA":38,"sizeB":72,"sizeC":108},{"type":"rectangle","sizeA":34,"sizeB":60},{"type":"rectangle","sizeA":63,"sizeB":52},{"type":"rectangle","sizeA":79,"sizeB":92},{"type":"triangle","sizeA":34,"sizeB":38,"sizeC":14},{"type":"triangle","sizeA":67,"sizeB":89,"sizeC":138},{"type":"rectangle","sizeA":13,"sizeB":69},{"type":"circle","diameter":47},{"type":"circle","diameter":67}]'
app = FastAPI()

class Square:
    def __init__(self, size) -> None:
        self.size = size

    def compute_area(self):
        return math.pow(self.size, 2)
    
    def get_type(self): 
        return "square"

class Rectangle:
    def __init__(self, sizeA, sizeB) -> None:
        self.sizeA = sizeA
        self.sizeB = sizeB

    def compute_area(self):
        return self.sizeA * self.sizeB
    
    def get_type(self): 
        return "rectangle"

class Triangle:
    def __init__(self, sizeA, sizeB, sizeC) -> None:
        self.sizeA = sizeA
        self.sizeB = sizeB
        self.sizeC = sizeC

    def compute_area(self):
        s = (self.sizeA + self.sizeB + self.sizeC) / 2
        return math.sqrt(s * (s - self.sizeA) * (s - self.sizeB) * (s - self.sizeC))
    
    def get_type(self): 
        return "triangle"

class Circle:
    def __init__(self, diameter) -> None:
        self.diameter = diameter

    def compute_area(self):
        r = self.diameter / 2
        return math.pi * math.pow(r, 2)
    
    def get_type(self): 
        return "circle"

def load_figures():
    raw = json.loads(DATA)
    figures = []

    for item in raw:
        if item['type'] == 'square':
            figures.append(Square(item["size"]))
        if item['type'] == 'rectangle':
            figures.append(Rectangle(item["sizeA"], item["sizeB"]))
        if item['type'] == 'triangle':
            figures.append(Triangle(item["sizeA"], item["sizeB"], item["sizeC"]))
        if item['type'] == 'circle':
            figures.append(Circle(item["diameter"]))            

    return figures

@app.get("/ping")
def get_ping():
    figures = load_figures()
    min_area = sys.float_info.max
    max_area = sys.float_info.min
    total_area = 0.0

    figure_types = {
        "square": 0,
        "rectangle": 0,
        "triangle": 0,
        "circle": 0,
    }

    for figure in figures:
        area = figure.compute_area()
        min_area = min(min_area, area)
        max_area = max(max_area, area)
        total_area += area
        figure_types[figure.get_type()] += 1

    return {
        "app": "python****", 
        "time": math.floor(time.time()), 
        "min_area": min_area, 
        "max_area": max_area, 
        "total_area": total_area, 
        "figure_types": figure_types
    }

@app.post("/ping")
def post_ping():
    figures = load_figures()
    min_area = sys.float_info.max
    max_area = sys.float_info.min
    total_area = 0.0
    start = time.time()

    for i in range(0, 1_000_000):
        for figure in figures:
            area = figure.compute_area()
            min_area = min(min_area, area)
            max_area = max(max_area, area)
            total_area += area

    return {
        "app": "python****", 
        "time": time.time() - start,
        "min_area": min_area, 
        "max_area": max_area, 
        "total_area": total_area
    }
