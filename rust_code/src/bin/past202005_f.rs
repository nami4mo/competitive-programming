#![allow(unused_imports)]
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque};

fn solve() {
    input! {
        n: usize, x: i64, y: i64,
        xyl: [(i64, i64); n],
    }
    const OFFSET: i64 = 300;
    let goal_x = (x + OFFSET) as usize;
    let goal_y = (y + OFFSET) as usize;
    let mut ok = vec![vec![true; 1000]; 1000];
    for &(xx, yy) in &xyl {
        let xxx = (xx + OFFSET) as usize;
        let yyy = (yy + OFFSET) as usize;
        ok[xxx][yyy] = false;
    }
    let mut q = VecDeque::new();
    let inf = 1e9 as usize;
    let mut dists = vec![vec![inf; 1000]; 1000];
    q.push_back((OFFSET, OFFSET));
    dists[OFFSET as usize][OFFSET as usize] = 0;
    while let Some(cxy) = q.pop_front() {
        // eprintln!("{:?}", q);
        let (cx, cy) = cxy;
        for &dx in [-1, 0, 1].iter() {
            for &dy in [-1, 0, 1].iter() {
                if (dx, dy) == (0, 0) || (dx, dy) == (-1, -1) || (dx, dy) == (1, -1) {
                    continue;
                }
                let nx = (cx + dx) as usize;
                let ny = (cy + dy) as usize;
                if nx < 1 || nx >= 1000 || ny < 1 || ny >= 1000 {
                    continue;
                }
                if !ok[nx][ny] {
                    continue;
                }
                if dists[nx][ny] > dists[cx as usize][cy as usize] + 1 {
                    dists[nx][ny] = dists[cx as usize][cy as usize] + 1;
                    q.push_back((nx as i64, ny as i64));
                }
            }
        }
    }
    if dists[goal_x][goal_y] == inf {
        println!("-1");
    } else {
        println!("{}", dists[goal_x][goal_y]);
    }
}

#[fastout]
fn main() {
    solve();
}
