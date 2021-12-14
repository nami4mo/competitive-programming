/*
    UDLR
    0123
*/

#include <bits/stdc++.h>
// #if __has_include(<atcoder/all>)
//     #include <atcoder/all>
//     using namespace atcoder;
// #endif
using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<ll,ll> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()
    template<class T> vector<T> make_vec(size_t a){return vector<T>(a);}
    template<class T, class... Ts> auto make_vec(size_t a, Ts... ts){ return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...));}
    template<typename A, size_t N, typename T> void Fill(A (&array)[N], const T &val){std::fill( (T*)array, (T*)(array+N), val );}

    /* for debug */
    #define DEBUG(x) dbg(#x,x)
    template<class T> void dbg(string name, T x){cerr<<name<<": "<<x<<"\n";}
    template<> void dbg<P>(string name, P x){cerr<<name<<": ("<<x.first<<","<<x.second<<")\n";}
    template<class T> void dbg(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr<<'\n';}
    template<> void dbg<P>(string name, vector<P> xl){cerr<<name<<": "; for(P x:xl){cerr<<"("<<x.first<<","<<x.second<<"), ";}cerr<<"\n";}
    template<class T> void dbg(string name, vector<vector<T>> xl){ cerr<<name<<": \n"; int ml=1;for(vector<T> row: xl){for(T x:row){stringstream sstm; sstm<<x; ml=max(ml,(int)sstm.str().size());}}; for(vector<T> row: xl){{for(T x:row) cerr<<std::right<<std::setw(ml+1)<<x;} cerr << '\n';}}
    template<class T> void dbg(string name, set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, unordered_set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    template<class T> void dbg(string name, unordered_multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x;cerr<<'\n';}
    template<class T, class U> void dbg(string name, map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
    template<class T, class U> void dbg(string name, unordered_map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
}
using namespace defines;

const ll INF = 1'001'001'001'001ll;
const int N=20;
// const int N = 5;
int m;

mt19937_64 mt64(0);
uniform_int_distribution<int> rand_col_row(0, 1);
uniform_int_distribution<int> rand_lr(0, 1);
uniform_int_distribution<int> rand_lrd(-5, 5);

uniform_int_distribution<int> rand_n(0, N-1);
uniform_int_distribution<int> rand_c(0, 7);

uniform_int_distribution<int> rand_d(100, 200);
uniform_int_distribution<int> rand_num(0, 1000);
uniform_int_distribution<int> rand_01(0, 1);
uniform_int_distribution<int> rand_move15(1, 2);
uniform_real_distribution<double> rand_percent(0, 1);

enum Dir { ROW = 0, COL, };


struct TimeManager
{
    chrono::system_clock::time_point start;
    double time=0.0;
    int loop_per_measure, loop_cnt;
    TimeManager(int loop_per_measure=50): start(chrono::system_clock::now()),loop_cnt(0),loop_per_measure(loop_per_measure){};
    bool check(double limit, bool force=false){
        loop_cnt++;
        if(force || loop_cnt>=loop_per_measure){
            auto c_time=chrono::system_clock::now();
            time = chrono::duration_cast<chrono::milliseconds>(c_time-start).count();
            loop_cnt=0;
            return (time<limit);
        }
        else return (time<limit);
    }
    double get_time(bool force=false){
        if(force) check(0.0,true);
        return time;
    }
};

struct State{
    vector<vector<char>> mat;
    vector<int> row_lens;
    // vector<string> sl;
    vector<string> sl;
    vector<bool> sl_used;
    vector<int> row_ls;
    vector<int> row_rs;

    int used_cnt = 0;
    int max_len = 0;
    State() : mat(N, vector<char>(N,'.')), row_lens(N, 0), row_ls(N, 0), row_rs(N, 0){
    }

    string get_row_str(int i, int j, int len){
        string s = "";
        REP(d,len){
            s += mat[i][(j+d)%N];
        }
        return s;
    }

    void update_s(Dir dir, string s, int i, int j){
        int len = s.length();
        if(dir==ROW){
            REP(d, len){
                mat[i][(j+d)%N] = s[d];
            }
        }
        if(dir==COL){
            REP(d, len){
                mat[(i+d)%N][j] = s[d];
            }
        }
    }

    P get_row_max_empty(int ind){
        int cmax = 0;
        int ci = 0;
        int cc = 0;
        REP(i,N){
            if(mat[ind][i]=='.'){
                cc++;
            }
            else{
                if(cc>cmax){
                    ci = i-cc;
                    cmax = cc;
                }
            }
        }
        if(cc>cmax){
            ci = N-cc;
            cmax = cc;
        }
        return {ci,cmax};
    }

    void output(){
        REP(i,N){
            REP(j,N){
                cout<<mat[i][j];
            }
            cout<<'\n';
        }
    }
};

void check_all_sl(State &state){
    // for(string s)
}

bool exist_s(State &state, string s){
    int len=s.length();
    REP(row, N){
        REP(j, N){
            bool ok=true;
            REP(d, len){
                if(s[d]!=state.mat[row][(j+d)%N]){ok=false; break;}
            }
            if(ok) return true;
        }
    }
    REP(col, N){
        REP(i, N){
            bool ok=true;
            REP(d, len){
                if(s[d]!=state.mat[(i+d)%N][col]){ok=false; break;}
            }
            if(ok) return true;
        }
    }
    return false;
}

void use_by_min(State &state){
    for(string s : state.sl){
        int len = s.length();
        if(exist_s(state, s)) continue;
        REP(row, N){
            auto [start_ind, emp_max] = state.get_row_max_empty(row);
            if(emp_max>=len){
                state.update_s(ROW, s, row, start_ind);
                break;
            }
        }
    }
}

int check_cnt(State &state){
    int res=0;
    for(string s: state.sl){
        // DEBUG(s);
        if(exist_s(state, s))res++;
    }
    return res;
}

void slide_mat(State &state, int dir, int lr, int ind){
    if(dir==ROW){
        vector<char> new_vec(N);
        REP(i, N){
            char c = state.mat[ind][i];
            int ni = i+lr;
            if(ni>=N) ni-=N;
            if(ni<0) ni+=N;
            new_vec[ni] = c;
        }
        REP(i, N){
            state.mat[ind][i] = new_vec[i];
        }
    }
    if(dir==COL){
        vector<char> new_vec(N);
        REP(i, N){
            char c = state.mat[i][ind];
            int ni = i+lr;
            if(ni>=N) ni-=N;
            if(ni<0) ni+=N;
            new_vec[ni] = c;
        }
        REP(i, N){
            state.mat[i][ind] = new_vec[i];
        }
    }
}

void rand_slide(State &state){
    // int dir = rand_col_row(mt64);
    int dir = ROW;
    int ind = rand_n(mt64);
    int lr = rand_lrd(mt64);
    if(lr==0) return;

    slide_mat(state, dir, lr, ind);
    int new_cnt = check_cnt(state);

    if(new_cnt < state.used_cnt){
        slide_mat(state, dir, lr*(-1), ind);
    }
    else{
        state.used_cnt = new_cnt;
    }
}

void rand_slide_n(State &state){
    vector<pair<int,int>> prevs;
    // int dir = rand_col_row(mt64);
    int cnt = rand_num(mt64)%5+1;
    int lr = rand_lrd(mt64);
    int start_i = rand_n(mt64);
    int dir = ROW;
    REP(i,cnt){
        int ind = start_i+i;
        if(ind>=N) ind-=N;
        slide_mat(state, dir, lr, ind);
        prevs.push_back({lr,ind});
    }

    int new_cnt = check_cnt(state);

    if(new_cnt < state.used_cnt){
        for(auto &[lr,ind]:prevs){
            slide_mat(state, dir, lr*(-1), ind);
        }
    }
    else{
        state.used_cnt = new_cnt;
    }
}


void rand_change(State &state){
    int row = rand_n(mt64);
    int col = rand_n(mt64);
    char new_c = 'A' + rand_c(mt64);
    char prev_c = state.mat[row][col];
    state.mat[row][col] = new_c;
    
    int new_cnt = check_cnt(state);
    if(new_cnt < state.used_cnt){
        state.mat[row][col] = prev_c;
    }
    else{
        state.used_cnt = new_cnt;
    }
}


void init_mat(State &state){
    REP(row,N){
        while(true){
            int max_suf = min(state.max_len, state.row_lens[row]);
            int right = state.row_lens[row];
            bool updated = false;
            for(int len=max_suf; len>=0; len--){
                bool ok = false;
                string suf_s = state.get_row_str(row, right-len, len);
                // DEBUG(suf_s);
                for(string s : state.sl){
                    if(exist_s(state, s)) continue;
                    if(s.length()<=len) continue;
                    if(suf_s != s.substr(0,len)) continue;
                    string rem_s = s.substr(len);
                    if(right+rem_s.length()>N)continue;
                    // if(right+rem_s.length()>N)break;
                    state.update_s(ROW, rem_s, row, right);
                    state.row_lens[row] += rem_s.length();
                    ok = true;
                    break;
                }
                if(ok){updated=true; break;}
            }
            if(!updated) break;
        }
    }
    for(string s : state.sl){
        int len = s.length();
        if(exist_s(state, s)) continue;
        REP(row, N){
            auto [start_ind, emp_max] = state.get_row_max_empty(row);
            if(emp_max>=len){
                state.update_s(ROW, s, row, start_ind);
                break;
            }
        }
    }
}



void init_mat2(State &state){
    vector<bool> used_s(m, false);
    REP(row,N){
        while(true){
            int rc = state.row_rs[row];
            int lc = state.row_ls[row];
            int emp_c = N-rc-lc;
            int max_suf = min(state.max_len, rc+lc);
            bool updated = false;
            for(int len=max_suf; len>=0; len--){
                // DEBUG(row); DEBUG(len);
                bool ok = false;
                //　右側に伸ばす
                int start_i = lc-len;
                if(start_i<0) start_i+=N;
                string suf_s = state.get_row_str(row, start_i, len);
                // for(string s : state.sl){
                REP(si,m){
                    if(used_s[si]) continue;
                    string s = state.sl[si];
                    if(exist_s(state, s)) {used_s[si]=true; continue;}
                    if(s.length()<=len) continue;
                    if(suf_s != s.substr(0,len)) continue;
                    string rem_s = s.substr(len);
                    if(rem_s.length() > emp_c) continue;
                    state.update_s(ROW, rem_s, row, lc);
                    state.row_ls[row] += rem_s.length();
                    ok = true;
                    break;
                }
                // if(ok) continue;
                if(ok){updated=true; break;}
                // 左側に伸ばす
                rc = state.row_rs[row];
                lc = state.row_ls[row];
                emp_c = N-rc-lc;

                start_i = N-rc;
                if(start_i>=N) start_i-=N;
                string pre_s = state.get_row_str(row, start_i, len);
                // for(string s : state.sl){
                REP(si,m){
                    if(used_s[si]) continue;
                    string s = state.sl[si];
                    int slen = s.length();
                    if(exist_s(state, s)) continue;
                    if(slen<=len) continue;
                    if(pre_s != s.substr(slen-len)) continue;
                    string rem_s = s.substr(0,slen-len);
                    if(rem_s.length() > emp_c) continue;
                    // DEBUG(rem_s);
                    state.update_s(ROW, rem_s, row, N-rc-rem_s.length());
                    state.row_rs[row] += rem_s.length();
                    ok = true;
                    break;
                }

                if(ok){updated=true; break;}
            }
            if(!updated) break;
        }
    }
    for(string s : state.sl){
        int len = s.length();
        if(exist_s(state, s)) continue;
        REP(row, N){
            auto [start_ind, emp_max] = state.get_row_max_empty(row);
            if(emp_max>=len){
                state.update_s(ROW, s, row, start_ind);
                break;
            }
        }
    }
}



void rand_change_n(State &state, int loop, double t01){

    vector<tuple<int,int,int>> prevs;
    REP(i, loop){
        int row = rand_n(mt64);
        int col = rand_n(mt64);
        char new_c = 'A' + rand_c(mt64);
        char prev_c = state.mat[row][col];
        state.mat[row][col] = new_c;
        prevs.push_back({row,col,prev_c});
    }
    int new_cnt = check_cnt(state);
    int kaizen = new_cnt - state.used_cnt;
    // double T0=3;
    // double T1=0;
    // double tt=pow(T0,1.0-t01)*pow(T1,t01);
    // double yaki_prob = rand_percent(mt64);
    // if(kaizen > 0 || yaki_prob < exp(kaizen/tt) ){
    if(kaizen > 0){
        state.used_cnt = new_cnt;
    }
    else{
        for(auto &[row,col,prev_c] : prevs){
            state.mat[row][col] = prev_c;
        }
    }
}

void swap_rows(State &state){
    int ind1 = rand_n(mt64);
    int ind2 = rand_n(mt64);
    swap(state.mat[ind1], state.mat[ind2]);

    int new_cnt = check_cnt(state);
    if(new_cnt < state.used_cnt){
        swap(state.mat[ind1], state.mat[ind2]);
    }
    else{
        state.used_cnt = new_cnt;
    }
}

void solve(){
    TimeManager tm;
    State state;
    int n_dummy;
    cin >> n_dummy >> m;
    REP(i,m){
        string s; cin>>s;
        // state.sl.push_back(s);
        state.sl.push_back(s);
        state.sl_used.push_back(false);
        state.max_len = max(state.max_len, (int)s.length());
    }
    // shuffle(state.sl.begin(), state.sl.end(), mt64);
    // sort(state.sl.begin(), state.sl.end(), [] (string &s1, string &s2) { return s1.size() > s2.size(); });
    sort(state.sl.begin(), state.sl.end(), [] (string &s1, string &s2) { return s1.size() < s2.size(); });

    DEBUG(tm.get_time(true));
    // init_mat(state);
    init_mat2(state);
    state.used_cnt = check_cnt(state);
    DEBUG(tm.get_time(true));

    double TL = 2800.0;
    while(tm.check(TL)){
        if(!tm.check(TL)) break;
        double t01 = tm.get_time()/TL;

        if(rand_percent(mt64)<0.5) rand_slide(state);
        else{
            int cnt = rand_num(mt64)%2+1;
            rand_change_n(state,cnt,t01);
        }
        if(rand_percent(mt64)<0.5) swap_rows(state);
    }
    state.output();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}