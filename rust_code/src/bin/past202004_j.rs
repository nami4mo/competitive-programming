#![allow(unused_imports)]

use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve() {
    input! {
        mut s: Chars,
    }
    loop {
        let mut left = 0;
        let mut right = 0;
        for i in 0..s.len() {
            if s[i] == ')' {
                right = i;
                break;
            }
            if s[i] == '(' {
                left = i;
            }
        }
        if right == 0 {
            break;
        }
        let mut new_s: Vec<char> = vec![];
        new_s.extend(s[0..left].iter());
        new_s.extend(s[left + 1..right].iter());
        new_s.extend(s[left + 1..right].iter().rev());
        new_s.extend(s[right + 1..].iter());
        s = new_s;
    }
    let s: String = s.iter().collect();
    println!("{}", s);
}

#[fastout]
fn main() {
    solve();
}
