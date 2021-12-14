#![allow(unused_imports)]

use std::mem::swap;

use im_rc::HashSet;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

fn solve2(
    al: &mut Vec<usize>,
    bl: &mut Vec<usize>,
    a0: usize,
    b0: usize,
    rem: usize,
) -> (Vec<usize>, Vec<usize>, usize) {
    al[a0] -= 1;
    bl[b0] -= 1;
    let mut res_a = vec![a0];
    let mut res_b = vec![b0];
    let mut cnt = 0;
    for bi in (1..10).rev() {
        let loop_cnt = bl[bi];
        for _ in 0..loop_cnt {
            for ai in 9 - bi..10 {
                if al[ai] > 0 {
                    al[ai] -= 1;
                    bl[bi] -= 1;
                    res_a.push(ai);
                    res_b.push(bi);
                    cnt += 1;
                    break;
                }
            }
        }
    }
    for _ in 0..al[9].min(rem) {
        al[9] -= 1;
        res_a.push(9);
        // res_b.push(0);
        cnt += 1;
    }
    res_a.reverse();
    res_b.reverse();

    let mut res_a2 = vec![];
    let mut res_a3 = vec![];
    let mut res_b2 = vec![];
    for bi in 1..10 {
        for _ in 0..bl[bi] {
            res_b2.push(bi);
        }
    }
    let mut acnt = 0;
    for ai in 1..10 {
        for _ in 0..al[ai] {
            if acnt >= res_b2.len() {
                acnt += 1;
                res_a3.push(ai);
            } else {
                res_a2.push(ai);
                acnt += 1;
            }
        }
    }

    let res_a = [res_a3, res_a, res_a2].concat();
    let res_b = [res_b, res_b2].concat();

    (res_a, res_b, cnt)
}

fn solve() {
    input! {
        mut a: Chars,
        mut b: Chars,
    }
    let mut swapped = false;
    if a.len() < b.len() {
        swap(&mut a, &mut b);
        swapped = true;
    }
    let mut al = vec![0; 10];
    let mut bl = vec![0; 10];
    for &ac in &a {
        let ai = ac.to_digit(10).unwrap() as usize;
        al[ai] += 1;
    }
    for &bc in &b {
        let bi = bc.to_digit(10).unwrap() as usize;
        bl[bi] += 1;
    }

    let mut ans_cnt = 0;
    let mut ans_al = vec![];
    let mut ans_bl = vec![];

    for a0 in 1..10 {
        for b0 in 1..10 {
            if a0 + b0 < 10 {
                continue;
            }
            if al[a0] == 0 || bl[b0] == 0 {
                continue;
            }

            let (res_a, res_b, cnt) =
                solve2(&mut al.clone(), &mut bl.clone(), a0, b0, a.len() - b.len());

            if cnt > ans_cnt {
                ans_al = res_a;
                ans_bl = res_b;
                ans_cnt = cnt;
            }
        }
    }
    if ans_cnt == 0 {
        if swapped {
            swap(&mut a, &mut b);
        }
        println!("{}", a.iter().collect::<String>());
        println!("{}", b.iter().collect::<String>());
        return;
    }

    if swapped {
        swap(&mut ans_al, &mut ans_bl);
    }
    println!(
        "{}",
        ans_al
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join("")
    );
    println!(
        "{}",
        ans_bl
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join("")
    );
}

#[fastout]
fn main() {
    solve();
}
