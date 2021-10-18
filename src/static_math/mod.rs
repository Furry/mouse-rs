use super::structures::point::Point;

pub fn linear_bezier(start: Point, stop: Point, hook1: Point, hook2: Point) -> Vec<Point> {
    let points: i32 = 500;
    
    let b: i32 = 2;
    let c: i32 = 3;
    let f: i32 = 1;

    let mut x: i32;
    let mut y: i32;
    let mut point_col: Vec<Point> = Vec::new();

    for t in 0..points {
        x = start.x * (f - t) ^ c + hook1.x * c * t * (f - t) ^ b;
        point_col.push(Point { x: x, y: y });
    }
    point_col
}