use rand::prelude::*;
use std::time::Instant;

const TL: u64 = 500; // ms

struct TimeManager {
    count: u64,
    start: Instant,
    last_time: u64,
}

impl TimeManager {
    const COUNT_PER_MEASURE: u64 = 1000;
    fn new() -> Self {
        TimeManager {
            count: 0,
            start: Instant::now(),
            last_time: 0,
        }
    }
    fn check_time(&mut self, time: u64, force: bool) -> bool {
        self.count += 1;
        if force || self.count > Self::COUNT_PER_MEASURE {
            self.count = 0;
            self.last_time = self.start.elapsed().as_millis() as u64;
        }
        self.last_time < time
    }
    fn get_time(&self) -> u64 {
        self.start.elapsed().as_millis() as u64
    }
}

struct MyRng {
    rng: SmallRng,
}

impl MyRng {
    fn new() -> Self {
        MyRng {
            rng: SmallRng::seed_from_u64(4445),
        }
    }
    fn get_int(&mut self, left: i64, right: i64) -> i64 {
        //! get [left, right] ( not [left, right)  )
        self.rng.gen_range(left, right + 1)
    }
    fn get_percent(&mut self) -> f64 {
        self.rng.gen::<f64>()
    }
}

fn main() {
    let mut tm = TimeManager::new();
    let mut myrng = MyRng::new();
    let mut cnt = 0;
    while tm.check_time(TL, false) {
        cnt += 1;
        myrng.get_percent();
        myrng.get_int(1,10);
    }
    println!("{}", cnt);
    println!("{:?}", tm.get_time());
}
