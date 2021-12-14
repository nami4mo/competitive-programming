#![allow(unused_imports)]
use proconio::marker::Chars;
use proconio::{fastout, input};
use std::collections::HashMap;

fn solve() {
    let num_s = vec![
        String::from(".###..#..###.###.#.#.###.###.###.###.###."),
        String::from(".#.#.##....#...#.#.#.#...#.....#.#.#.#.#."),
        String::from(".#.#..#..###.###.###.###.###...#.###.###."),
        String::from(".#.#..#..#.....#...#...#.#.#...#.#.#...#."),
        String::from(".###.###.###.###...#.###.###...#.###.###."),
    ];
    input! {
        n: usize,
        s: [String; 5],
    }
    let mut ans = String::from("");
    for i in 0..n {
        for num in 0..10 {
            let mut ok = true;
            for row in 0..5 {
                if s[row][i * 4..i * 4 + 4] != num_s[row][num * 4..num * 4 + 4] {
                    ok = false;
                    break;
                }
            }
            if ok {
                ans += &num.to_string();
            }
        }
    }
    println!("{}", ans);
}

#[fastout]
fn main() {
    solve();
}
