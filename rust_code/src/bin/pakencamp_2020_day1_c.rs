#![allow(unused_imports)]

use im_rc::HashMap;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        n: usize,
    }
    let mut mp = HashMap::<String, usize>::new();
    for _ in 0..n {
        input! {
            k: usize,
            sl: [String; k],
        }
        for s in &sl {
            let ss = s.clone();
            *mp.entry(ss).or_insert(0) += 1;
        }
    }
    let mut ans = 0;
    for &(_, v) in &mp {
        if v == n {
            ans += 1;
        }
    }
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
