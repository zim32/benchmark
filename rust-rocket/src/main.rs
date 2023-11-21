mod data;

#[macro_use] extern crate rocket;

use rocket::serde::{json::Json, Serialize, Deserialize};
use std::collections::{HashMap};
use std::time::{Instant};

trait FigureTrait {
    fn compute_area(&self) -> f64;
    fn get_type(&self) -> &str;
}

#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
pub struct Square {
    size: u32,
}

#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
pub struct Rectangle {
    #[serde(rename = "sizeA")]
    size_a: u32,
    #[serde(rename = "sizeB")]
    size_b: u32,
}

#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
pub struct Triangle {
    size_a: u32,
    size_b: u32,
    size_c: u32,
}

#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
pub struct Circle {
    diameter: u32,
}

impl FigureTrait for Square {
    fn compute_area(&self) -> f64 {
        self.size.pow(2) as f64
    }

    fn get_type(&self) -> &str {
        "square"
    }
}

impl FigureTrait for Rectangle {
    fn compute_area(&self) -> f64 {
        (self.size_a * self.size_b) as f64
    }

    fn get_type(&self) -> &str {
        "rectangle"
    }
}

impl FigureTrait for Triangle {
    fn compute_area(&self) -> f64 {
        let a = self.size_a as f64;
        let b = self.size_b as f64;
        let c = self.size_c as f64;

        let s = (a + b + c) / 2.0;
        (s * (s - a) * (s - b) * (s - c)).sqrt()
    }

    fn get_type(&self) -> &str {
        "triangle"
    }
}

impl FigureTrait for Circle {
    fn compute_area(&self) -> f64 {
        let r: f64 = self.diameter as f64 / 2.0;
        std::f64::consts::PI * r.powi(2)
    }

    fn get_type(&self) -> &str {
        "circle"
    }
}

#[derive(Deserialize, Debug)]
#[serde(tag = "type")]
#[serde(rename = "Diameter")]
#[serde(rename_all = "camelCase")]
pub enum Figure {
    Square(Square),
    Rectangle(Rectangle),
    Triangle(Triangle),
    Circle(Circle),
}

impl FigureTrait for Figure {
    fn compute_area(&self) -> f64 {
        match self {
            Figure::Square(f) => f.compute_area(),
            Figure::Rectangle(f) => f.compute_area(),
            Figure::Triangle(f) => f.compute_area(),
            Figure::Circle(f) => f.compute_area(),
        }
    }

    fn get_type(&self) -> &str {
        match self {
            Figure::Square(f) => f.get_type(),
            Figure::Rectangle(f) => f.get_type(),
            Figure::Triangle(f) => f.get_type(),
            Figure::Circle(f) => f.get_type(),
        }
    }
}

#[derive(Debug, Serialize)]
#[serde(crate = "rocket::serde")]
struct Response {
    app: &'static str,
    time: u64,
    min_area: f64,
    max_area: f64,
    total_area: f64,
    figure_type: HashMap<String, u32>
}

#[derive(Debug, Serialize)]
#[serde(crate = "rocket::serde")]
struct PostResponse {
    app: &'static str,
    time: u128,
    min_area: f64,
    max_area: f64,
    total_area: f64,
}

impl Default for Response {
    fn default() -> Self {
        Self {
            app: "rust-rocke",
            time: std::time::UNIX_EPOCH.elapsed().unwrap().as_secs(),
            min_area: f64::MAX,
            max_area: f64::MIN,
            total_area: 0.0,
            figure_type: HashMap::from([
                ("square".to_owned(), 0),
                ("rectangle".to_owned(), 0),
                ("triangle".to_owned(), 0),
                ("circle".to_owned(), 0),
            ])
        }
    }
}

impl Default for PostResponse {
    fn default() -> Self {
        Self {
            app: "rust-rocke",
            min_area: f64::MAX,
            max_area: f64::MIN,
            total_area: 0.0,
            time: 0,
        }
    }
}

#[get("/ping")]
fn ping_get() -> Json<Response> {
    let figures = load_figures();
    let mut response = Response::default();

    for figure in figures.iter() {
        let area = figure.compute_area();
        response.min_area = response.min_area.min(area);
        response.max_area = response.max_area.max(area);
        response.total_area += area;
        let count = response.figure_type.get(figure.get_type()).unwrap();
        response.figure_type.insert(figure.get_type().to_owned(), count + 1);
    }

    Json(response)
}

#[post("/ping")]
fn ping_post() -> Json<PostResponse> {
    let figures = load_figures();
    let mut response = PostResponse::default();
    let start = Instant::now();

    for _ in 1..1_000_000 {
        for figure in figures.iter() {
            let area = figure.compute_area();
            response.min_area = response.min_area.min(area);
            response.max_area = response.max_area.max(area);
            response.total_area += area;
        }
    }

    response.time = start.elapsed().as_millis();

    Json(response)
}

fn load_figures() -> Vec<Figure> {
    serde_json::from_str(data::DATA).unwrap()
}

#[rocket::main]
async fn main() {
    rocket::build().mount("/", routes![ping_get, ping_post]).launch().await.unwrap();
}
