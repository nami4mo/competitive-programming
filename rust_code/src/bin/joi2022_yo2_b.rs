#![allow(unused_imports)]

use std::collections::VecDeque;

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

// #[fastout]
fn solve() {
    input! {
        h: usize, w: usize,
        sl: [Chars; h],
    }
    let mut dist = vec![vec![-1; w]; h];
    let mut q = VecDeque::<(usize, usize)>::new();
    q.push_back((0, 0));
    dist[0][0] = 0;
    while let Some(yx) = q.pop_front() {
        let (y, x) = yx;
        for &(dy, dx) in &[(-1, 0), (1, 0), (0, -1), (0, 1)] {
            let yy = y as i64 + dy;
            let xx = x as i64 + dx;
            if yy < 0 || h <= yy as usize || xx < 0 || w <= xx as usize {
                continue;
            }
            let yy = yy as usize;
            let xx = xx as usize;

            if dist[yy][xx] != -1 {
                continue;
            }
            if sl[y][x] == sl[yy][xx] {
                continue;
            }
            dist[yy][xx] = dist[y][x] + 1;
            q.push_back((yy, xx));
        }
    }
    println!("{}", dist[h - 1][w - 1]);
}

fn main() {
    solve();
}
