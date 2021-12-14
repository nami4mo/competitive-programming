use libm::pow;
use mytool::MyRng;
use nalgebra::Point;
use num::{abs, range};
use proconio::input;
use proconio::marker::Usize1;
use std::cmp::max;
use std::collections::{HashSet, VecDeque};
use std::fmt::Debug;
use std::mem::swap;
use std::vec;

const TL1: u64 = 1920;
const TL: u64 = 1920;

const AC_POS: Pos = Pos {
    x: 400,
    y: 400,
    id: 11111,
    picked: false,
};
/* --------------------- enum --------------------- */
#[derive(Debug, PartialEq, Clone, Copy)]
enum Progress {
    Pending,
    OnRoad,
    Finish,
}
impl Default for Progress {
    fn default() -> Self {
        Progress::Pending
    }
}

// #[derive(Default, Debug, PartialEq, Clone, Copy)]
#[derive(Default, Debug, PartialEq, Clone)]
pub struct State {
    orders: Vec<Order>,
    ans_pos_rest: Vec<Pos>,  // start from AC_POS
    ans_pos_house: Vec<Pos>, // end by AC_POS
    ans_order: Vec<usize>,
    ans_pos: Vec<Pos>,
    orders_by_rest_d: Vec<Order>,
    pos: Pos,
    dist_sum: usize,
}

impl State {}

#[derive(Default, Debug, PartialEq, Clone, Copy)]
pub struct Pos {
    x: usize,
    y: usize,
    id: usize, // order_id
    picked: bool,
}

#[derive(Default, Debug, PartialEq, Clone, Copy)]
pub struct Order {
    id: usize,
    rest: Pos,
    house: Pos,
    progress: Progress,
    rest_d_from_ac: usize,
}

fn yaki_prob(top: usize, bottom: usize, ther0: f64, ther1: f64, kaizen: i64) -> f64 {
    let time01 = (top as f64) / (bottom as f64);
    let mut tt = pow(ther0, 1.0 - time01) * pow(ther1, time01);
    tt *= kaizen as f64;
    tt.exp()
}

fn init_state(vl: &Vec<Vec<usize>>) -> State {
    let mut orders = vec![];
    let mut id = 0;
    for row in vl {
        let rest = Pos {
            x: row[0],
            y: row[1],
            id,
            picked: true,
        };
        let house = Pos {
            x: row[2],
            y: row[3],
            id,
            picked: false,
        };
        let rest_d_from_ac = get_dist(&rest, &AC_POS);
        orders.push(Order {
            id,
            rest,
            house,
            progress: Progress::Pending,
            rest_d_from_ac,
        });
        id += 1;
    }

    let mut orders_by_rest_d = orders.clone();
    orders_by_rest_d.sort_by_key(|x| x.rest_d_from_ac);

    // for i in 0..50 {
    //     eprintln!("{:?}", orders_by_rest_d[i]);
    // }

    State {
        orders,
        ans_pos: vec![AC_POS],
        ans_pos_rest: vec![AC_POS],
        ans_pos_house: vec![],
        ans_order: vec![],
        orders_by_rest_d,
        pos: AC_POS,
        dist_sum: 0,
    }
}

fn get_dist(p1: &Pos, p2: &Pos) -> usize {
    let x1 = p1.x as i64;
    let y1 = p1.y as i64;
    let x2 = p2.x as i64;
    let y2 = p2.y as i64;
    let res = abs(x1 - x2) + abs(y1 - y2);
    res as usize
}

fn in_area(x0: usize, x1: usize, y0: usize, y1: usize, pos: &Pos) -> bool {
    let res = x0 <= pos.x && pos.x <= x1 && y0 <= pos.y && pos.y <= y1;
    res
}

fn get_greedy_rest_range(state: &mut State, x0: usize, x1: usize, y0: usize, y1: usize) {
    for _ in 0..50 {
        let mut nearest_i_d = (None, 1000000);
        for order in &state.orders {
            if order.progress != Progress::Pending {
                continue;
            }
            if !in_area(x0, x1, y0, y1, &order.house) {
                continue;
            }
            let d = get_dist(&state.pos, &order.rest);
            if d < nearest_i_d.1 {
                nearest_i_d = (Some(order.id), d);
            }
        }
        match nearest_i_d.0 {
            None => return,
            Some(o_id) => {
                state.orders[o_id].progress = Progress::OnRoad;
                state.pos = state.orders[o_id].rest;
                state.ans_order.push(o_id);
                state.ans_pos.push(state.orders[o_id].rest);
                state.ans_pos_rest.push(state.orders[o_id].rest);
                state.dist_sum += nearest_i_d.1;
            }
        }
    }
}

fn get_greedy_rest_range_2(state: &mut State, x0: usize, x1: usize, y0: usize, y1: usize) {
    let cx = (x0 + x1) / 2;
    let cy = (y0 + y1) / 2;
    let cpos = Pos {
        x: cx,
        y: cy,
        id: 99999,
        picked: false,
    };

    let mut sum_x = cx;
    let mut sum_y = cy;
    let mut ave_p = Pos {
        x: cx,
        y: cy,
        id: 11111111,
        picked: false,
    };

    for i in 0..50 {
        let mut nearest_i_d = (None, 1000000);
        for order in &state.orders {
            if order.progress != Progress::Pending {
                continue;
            }
            if !in_area(x0, x1, y0, y1, &order.house) {
                continue;
            }
            let d = get_dist(&state.pos, &order.rest) + get_dist(&ave_p, &order.house);
            if d < nearest_i_d.1 {
                nearest_i_d = (Some(order.id), d);
            }
        }
        match nearest_i_d.0 {
            None => return,
            Some(v) => {
                let o_id = v;
                state.orders[o_id].progress = Progress::OnRoad;
                state.pos = state.orders[o_id].rest;
                state.ans_order.push(o_id);
                state.ans_pos.push(state.orders[o_id].rest);
                state.ans_pos_rest.push(state.orders[o_id].rest);
                state.dist_sum += nearest_i_d.1;
                sum_x += state.orders[o_id].house.x;
                sum_y += state.orders[o_id].house.y;
                ave_p.x = sum_x / (i + 1);
                ave_p.y = sum_y / (i + 1);
            }
        }
    }
}

fn get_greedy_house(state: &mut State) {
    for _ in 0..50 {
        let mut nearest_i_d = (100000, 1000000);
        for order in &state.orders {
            if order.progress != Progress::OnRoad {
                continue;
            }
            let d = get_dist(&state.pos, &order.house);
            if d < nearest_i_d.1 {
                nearest_i_d = (order.id, d);
            }
        }
        let o_id = nearest_i_d.0;
        state.orders[o_id].progress = Progress::Finish;
        state.pos = state.orders[o_id].house;
        state.ans_pos.push(state.orders[o_id].house);
        state.ans_pos_house.push(state.orders[o_id].house);
        state.dist_sum += nearest_i_d.1;
    }
}

fn go_ac(state: &mut State) {
    let d = get_dist(&state.pos, &AC_POS);
    state.dist_sum += d;
    state.pos = AC_POS;
    state.ans_pos.push(AC_POS);
    state.ans_pos_house.push(AC_POS);
}

fn calc_delivery_dist(state: &State, pl: &Vec<Pos>) -> usize {
    let mut d = 0;
    d += get_dist(&state.ans_pos_rest[50], &pl[0]);
    for i in 0..50 {
        d += get_dist(&pl[i], &pl[i + 1]);
    }
    d
}

fn calc_rest_dist(state: &State, pl: &Vec<Pos>) -> usize {
    let mut d = 0;
    for i in 0..50 {
        d += get_dist(&pl[i], &pl[i + 1]);
    }
    d += get_dist(&state.ans_pos_house[0], &pl[50]);
    d
}

fn make_reverse_vec(pl: &Vec<Pos>, a: usize, b: usize) -> Vec<Pos> {
    let n = pl.len();
    let mut res = vec![AC_POS; n];
    for i in 0..n {
        if i < a || b < i {
            res[i] = pl[i];
        } else {
            let d = i - a;
            res[i] = pl[b - d];
        }
    }
    res
}

fn calc_total_dist(pl: &Vec<Pos>) -> usize {
    let mut res = 0;
    for i in 0..pl.len() - 1 {
        res += get_dist(&pl[i], &pl[i + 1]);
    }
    res
}

fn opt2_deli(state: &mut State, my_rng: &mut MyRng) {
    let mut a = my_rng.get_int(0, 49) as usize; // NOTICE: 50: AC_POS
    let mut b = my_rng.get_int(0, 49) as usize;
    if a == b {
        return;
    }
    if a > b {
        swap(&mut a, &mut b);
    }
    // let curr_pl = state.ans_pos_house.clone();
    let new_pl = make_reverse_vec(&state.ans_pos_house, a, b);
    let current_deli_d = calc_delivery_dist(&state, &state.ans_pos_house);
    let new_deli_d = calc_delivery_dist(&state, &new_pl);
    if new_deli_d < current_deli_d {
        state.ans_pos_house = new_pl.clone();
    }
}

fn opt2_rest(state: &mut State, my_rng: &mut MyRng) {
    let mut a = my_rng.get_int(1, 50) as usize; // NOTICE: 0: AC_POS
    let mut b = my_rng.get_int(1, 50) as usize; // NOTICE: 0: AC_POS
    if a == b {
        return;
    }
    if a > b {
        swap(&mut a, &mut b);
    }
    // let curr_pl = state.ans_pos_house.clone();
    let new_pl = make_reverse_vec(&state.ans_pos_rest, a, b);
    let current_rest_d = calc_rest_dist(&state, &state.ans_pos_rest);
    let new_rest_d = calc_rest_dist(&state, &new_pl);
    if new_rest_d < current_rest_d {
        state.ans_pos_rest = new_pl.clone();
    }
}

fn make_insert_vec(pl: &Vec<Pos>, a: usize, b: usize) -> Vec<Pos> {
    let n = pl.len();
    let mut res = vec![AC_POS; n];
    for i in 0..n {
        if i < a || b < i {
            res[i] = pl[i];
        } else if i == a {
            res[i] = pl[b];
        } else {
            res[i] = pl[i - 1];
        }
    }
    res
}

fn opt2_all(state: &mut State, my_rng: &mut MyRng) {
    let n = state.ans_pos.len();
    let mut a = my_rng.get_int(1, (n - 2) as i64) as usize; // NOTICE: 0 and n-1: AC_POS
    let mut b = my_rng.get_int(1, (n - 2) as i64) as usize; // NOTICE: 0: AC_POS
    if a == b {
        return;
    }
    if a > b {
        swap(&mut a, &mut b);
    }
    if state.ans_pos[a].id >= 50 || state.ans_pos[b].id >= 50 {
        return;
    }
    // let curr_pl = state.ans_pos_house.clone();
    let new_pl = make_insert_vec(&state.ans_pos, a, b);
    let mut ok = true;
    let mut picked = vec![false; 50];
    for pos in &new_pl {
        if pos.id >= 50 {
            continue;
        }
        if pos.picked {
            picked[pos.id] = true;
        } else {
            if !picked[pos.id] {
                ok = false;
                break;
            }
        }
    }
    if !ok {
        return;
    }
    let current_d = calc_total_dist(&state.ans_pos);
    let new_d = calc_total_dist(&new_pl);
    if new_d < current_d {
        state.ans_pos = new_pl.clone();
        eprintln!("up: {}", current_d - new_d);
    }
}

/* ------------------------------------------------------------------------
    solve!
------------------------------------------------------------------------ */
fn solve() {
    /* ------------ ready ------------ */
    let mut tm = mytool::TimeManager::new();
    let mut myrng = mytool::MyRng::new();

    input! {
        vl: [[usize; 4]; 1000],
    }

    let mut state = init_state(&vl);
    // let mut ans_state = state.clone();
    let state_orig = state.clone();

    let mut areas = vec![
        // (0, 400, 0, 400),
        // (0, 400, 400, 800),
        // (400, 800, 0, 400),
        // (400, 800, 400, 800),
        (250, 550, 250, 550),
    ];
    // for i in 0..4 {
    //     for j in 0..4 {
    //         let x0 = i * 200;
    //         let x1 = (i + 1) * 200;
    //         let y0 = j * 200;
    //         let y1 = (j + 1) * 200;
    //         areas.push((x0, x1, y0, y1));
    //     }
    // }
    for i in 0..3 {
        for j in 0..3 {
            let x0 = i * 200;
            let x1 = x0 + 400;
            let y0 = j * 200;
            let y1 = y0 + 400;
            areas.push((x0, x1, y0, y1));
        }
    }
    // for i in 0..3 {
    //     for j in 0..3 {
    //         let x0 = i * 200;
    //         let x1 = x0 + 267;
    //         let y0 = j * 200;
    //         let y1 = y0 + 267;
    //         areas.push((x0, x1, y0, y1));
    //     }
    // }

    let mut cnt = 0;
    for (x0, x1, y0, y1) in &areas {
        let mut curr_state = state_orig.clone();
        get_greedy_rest_range(&mut curr_state, *x0, *x1, *y0, *y1);
        // get_greedy_rest_range_2(&mut curr_state, *x0, *x1, *y0, *y1);
        if curr_state.ans_order.len() != 50 {
            continue;
        }
        get_greedy_house(&mut curr_state);
        go_ac(&mut curr_state);

        while tm.check_time((cnt + 1) * TL1 / areas.len() as u64, false) {
            if myrng.get_percent() < 0.3 {
                opt2_rest(&mut curr_state, &mut myrng);
            }
            opt2_deli(&mut curr_state, &mut myrng);
        }
        curr_state.ans_pos = [
            curr_state.ans_pos_rest.clone(),
            curr_state.ans_pos_house.clone(),
        ]
        .concat();
        curr_state.dist_sum = calc_total_dist(&curr_state.ans_pos);

        if state.dist_sum == 0 || curr_state.dist_sum < state.dist_sum {
            state = curr_state;
        }
        cnt += 1;
    }

    assert_eq!(state.ans_pos_rest.len(), 51);
    assert_eq!(state.ans_pos_house.len(), 51);

    // while tm.check_time(TL / 2, false) {
    //     opt2_rest(&mut state, &mut myrng);
    // }

    // while tm.check_time(TL, false) {
    //     opt2_rest(&mut state, &mut myrng);
    //     opt2_deli(&mut state, &mut myrng);
    // }

    while tm.check_time(TL, false) {
        opt2_all(&mut state, &mut myrng);
    }

    /* ------------ output ------------ */

    // state.ans_pos = [state.ans_pos_rest, state.ans_pos_house].concat();

    print!("{} ", state.ans_order.len());
    for v in &state.ans_order {
        print!("{} ", v + 1);
    }
    println!();
    print!("{} ", state.ans_pos.len());
    for v in &state.ans_pos {
        print!("{} {} ", v.x, v.y);
    }
    println!();
    // while tm.check_time(TL, false) {}
    eprintln!("score: {}", 1e8 as usize / (1000 + state.dist_sum));
    eprintln!("dist : {}", state.dist_sum);
}

/* ------------------------------------------------------------------------
    need not change below
------------------------------------------------------------------------ */
fn main() {
    solve();
}

pub mod mytool {
    use rand::prelude::*;
    use std::fmt;
    use std::time::Instant;
    pub struct TimeManager {
        count: u64,
        start: Instant,
        last_time: u64,
    }
    impl fmt::Display for TimeManager {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "{}", self.count)
        }
    }
    impl TimeManager {
        const COUNT_PER_MEASURE: u64 = 1000;
        pub fn new() -> Self {
            TimeManager {
                count: 0,
                start: Instant::now(),
                last_time: 0,
            }
        }
        pub fn check_time(&mut self, time: u64, force: bool) -> bool {
            self.count += 1;
            if force || self.count > Self::COUNT_PER_MEASURE {
                self.count = 0;
                self.last_time = self.start.elapsed().as_millis() as u64;
            }
            self.last_time < time
        }
        pub fn get_time(&self) -> u64 {
            self.start.elapsed().as_millis() as u64
        }
    }
    pub struct MyRng {
        rng: SmallRng,
    }
    impl MyRng {
        pub fn new() -> Self {
            MyRng {
                rng: SmallRng::seed_from_u64(4445),
            }
        }
        pub fn get_int(&mut self, left: i64, right: i64) -> i64 {
            //! get [left, right] ( not [left, right)  )
            self.rng.gen_range(left, right + 1)
        }
        pub fn get_percent(&mut self) -> f64 {
            self.rng.gen::<f64>()
        }
        pub fn shuffle<T>(&mut self, v: &mut [T]) {
            v.shuffle(&mut self.rng);
        }
        pub fn choose<T: Copy>(&mut self, v: &[T]) -> T {
            *v.choose(&mut self.rng).unwrap()
        }
    }
}
