#![allow(unused_imports)]
use im_rc::HashMap;
use num_integer::Roots;
use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

// ただの累積和でごまかした簡潔ビットベクトル
// そのうちちゃんと作る
pub struct SuccinctBitVectorDummy {
    size: usize,
    bits: Vec<u8>,
    cumsum: Vec<u32>,
}

impl SuccinctBitVectorDummy {
    pub fn new(size: usize) -> Self {
        SuccinctBitVectorDummy {
            size,
            bits: vec![0; size],
            cumsum: vec![0; size + 1],
        }
    }
    pub fn set(&mut self, ind: usize, bit: u8) {
        self.bits[ind] = bit;
    }
    pub fn build(&mut self) {
        let mut c_sum = 0;
        for i in 0..self.size {
            if self.bits[i] > 0 {
                c_sum += 1;
            }
            self.cumsum[i + 1] = c_sum;
        }
    }
    pub fn access(&self, ind: usize) -> u8 {
        self.bits[ind]
    }
    pub fn rank1(&self, ind: usize) -> u32 {
        // [0, ind)
        self.cumsum[ind]
    }
    pub fn rank0(&self, ind: usize) -> u32 {
        ind as u32 - self.rank1(ind)
    }
    pub fn select(&self, x: u32) -> usize {
        // x番目の1
        assert!(x > 0, "rank must be >0");
        let mut ng = 0;
        let mut ok = self.size + 1;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if self.cumsum[mid] < x {
                ng = mid;
            } else {
                ok = mid;
            }
        }
        // if ok == self.size -> no such ind
        ok - 1
    }
    pub fn print_bits(&self) {
        println!("{:?}", self.bits);
    }
}

pub struct WaveletMatrix {
    size: usize,
    bit_len: usize,
    bit_arrays: Vec<SuccinctBitVectorDummy>,
    bit_arrays_zero_cnts: Vec<usize>,
    bit_last_begins: HashMap<u64, usize>,
    bit_last_zero_cnt: usize,
}

impl WaveletMatrix {
    pub fn new(vals: &Vec<u64>) -> Self {
        let size = vals.len();
        let &max_v = vals.iter().max().unwrap();
        let mut bit_val = 2;
        let mut bit_len = 1;
        while max_v > bit_val - 1 {
            bit_val *= 2;
            bit_len += 1;
        }

        let mut bit_arrays = vec![];
        let mut bit_arrays_zero_cnts = vec![];
        let mut c_vals = vals.clone();
        for bit_i in (0..bit_len).rev() {
            let mut sbv = SuccinctBitVectorDummy::new(size);
            let mut zero_vals = vec![];
            let mut one_vals = vec![];
            for (i, &v) in c_vals.iter().enumerate() {
                if v & (1 << bit_i) > 0 {
                    sbv.set(i, 1);
                    one_vals.push(v);
                } else {
                    zero_vals.push(v);
                }
            }
            sbv.build();
            bit_arrays.push(sbv);
            bit_arrays_zero_cnts.push(zero_vals.len());
            c_vals = [zero_vals, one_vals].concat();
        }

        let mut bit_last_begins = HashMap::new();
        let bit_last_zero_cnt = bit_arrays_zero_cnts[bit_len - 1];
        for (i, &v) in c_vals.iter().enumerate() {
            bit_last_begins.entry(v).or_insert(i);
        }

        WaveletMatrix {
            size,
            bit_len,
            bit_arrays,
            bit_arrays_zero_cnts,
            bit_last_begins,
            bit_last_zero_cnt,
        }
    }

    pub fn access(&self, ind: usize) -> u64 {
        let mut r_ind = ind;
        let mut c_val = 0;
        for i in 0..self.bit_len {
            let bit = self.bit_arrays[i].access(r_ind);
            if bit == 1 {
                r_ind =
                    self.bit_arrays_zero_cnts[i] + self.bit_arrays[i].rank1(r_ind + 1) as usize - 1;
                c_val |= 1 << (self.bit_len - i - 1);
            } else {
                r_ind = self.bit_arrays[i].rank0(r_ind + 1) as usize - 1;
            }
        }
        c_val
    }

    pub fn rank(&self, ind: usize, x: u64) -> usize {
        // # of x in [0, ind)
        if !self.bit_last_begins.contains_key(&x) || ind == 0 {
            return 0;
        }
        let begin_ind = match self.bit_last_begins.get(&x) {
            Some(v) => v,
            None => return 0,
        };
        let mut r_ind = ind;
        for i in 0..self.bit_len {
            let bit = x & (1 << (self.bit_len - i - 1));
            if bit >= 1 {
                r_ind = self.bit_arrays_zero_cnts[i] + self.bit_arrays[i].rank1(r_ind) as usize;
            } else {
                r_ind = self.bit_arrays[i].rank0(r_ind) as usize;
            }
            // println!("r_ind: {}", r_ind);
        }
        r_ind - begin_ind
    }
}

// #[fastout]
fn main() {
    let vals = vec![5, 4, 5, 5, 2, 1, 5, 6, 1, 3, 5, 0];
    let wm = WaveletMatrix::new(&vals);
    for b in &wm.bit_arrays {
        b.print_bits();
    }
    println!("{:?}", wm.bit_arrays_zero_cnts);
    println!("{:?}", wm.bit_last_begins);
    println!("{:?}", wm.bit_last_zero_cnt);

    println!("{} : {}", 6, wm.access(6));
    println!("{} : {}", 4, wm.access(4));
    println!("{}", wm.rank(9, 5));

    // for i in 0..vals.len() + 1 {
    //     println!("--- {} --- ", i);
    //     println!("{}", wm.rank(i, 1));
    // }

    for l in 0..vals.len() {
        for r in l + 1..vals.len() {
            for &x in &vals {
                let cnt = wm.rank(r, x) - wm.rank(l, x);
                let mut cnt2 = 0;
                for k in l..r {
                    if vals[k] == x {
                        cnt2 += 1;
                    }
                }
                assert!(cnt == cnt2);
            }
        }
    }
}
