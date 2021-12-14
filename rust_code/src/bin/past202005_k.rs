#![allow(unused_imports)]
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque};
use std::mem::swap;

#[derive(Debug, Clone, Copy)]
enum Next {
    Elem(usize),
    Table(usize),
}

fn solve() {
    input! {
        n: usize,
        q: usize,
    }
    let mut nexts: Vec<Next> = (0..n + 1).map(|x| Next::Table(x)).collect();
    let mut tops: Vec<Option<usize>> = (0..n + 1).map(|x| Some(x)).collect();
    for _ in 0..q {
        input! {f: usize, t: usize, x: usize}

        let curr_t_top = tops[t];
        tops[t] = tops[f]; // move top
        let next = nexts[x];
        match next {
            Next::Elem(ind) => {
                tops[f] = Some(ind);
            }
            Next::Table(_) => {
                tops[f] = None;
            }
        }

        match curr_t_top {
            None => {
                nexts[x] = Next::Table(t);
            }
            Some(v) => {
                nexts[x] = Next::Elem(v);
            }
        }
    }
    let mut ans = vec![0; n + 1];
    // eprintln!("{:?}", nexts);
    // eprintln!("{:?}", tops);
    for i in 1..n + 1 {
        let top = tops[i];
        match top {
            None => {}
            Some(ind) => {
                let mut curr = ind;
                ans[ind] = i;
                while let Next::Elem(v) = nexts[curr] {
                    ans[v] = i;
                    curr = v;
                }
            }
        }
    }
    for i in 1..n + 1 {
        println!("{}", ans[i]);
    }
}

#[fastout]
fn main() {
    solve();
}
