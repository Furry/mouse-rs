#[derive(Debug)]
pub struct Path {
    start: i32,
    stop: i32,
    start_padding: i32, // Room for positional error in the starting position.
    stop_padding: i32, // Room for positional error in the stop destination.
    points: i32, // The frequency for generated mouse polling events.
    positions: Vec<Position>
}

#[derive(Debug)]
pub struct Position {
    x: i32,
    y: i32
}

pub struct PathOptions {
    start_padding: i32,
    stop_padding: i32,
    points: i32
}

impl PathOptions {
    pub fn new(start_padding: i32, stop_padding: i32, points: i32) -> Self {
        Self {
            start_padding: start_padding,
            stop_padding: stop_padding,
            points: points
        }
    }

    pub fn default() -> Self {
        Self::new(0, 0, 60)
    }
}

// Implementations

impl Path {
    pub fn new(start: i32, stop: i32, options: PathOptions) -> Self {
        Self {
            start: start,
            stop: stop,
            start_padding: options.start_padding,
            stop_padding: options.stop_padding,
            points: options.points,
            positions: Vec::new()
        }
    }
}