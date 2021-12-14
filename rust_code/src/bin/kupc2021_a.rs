use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: i64,
        sl: [i64; n],
        t: i64,
    }
    let mut set = HashSet::new();
    for s in &sl {
        set.insert(s / t);
    }
    let ans = set.len();
    println!("{}", ans);
}
