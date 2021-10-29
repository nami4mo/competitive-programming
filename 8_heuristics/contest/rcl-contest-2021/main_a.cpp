#include <bits/stdc++.h>
// #if __has_include(<atcoder/all>)
//     #include <atcoder/all>
//     using namespace atcoder;
// #endif
using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<int,int> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()
    // template<class T> vector<T> make_vec(size_t a){return vector<T>(a);}
    // template<class T, class... Ts> auto make_vec(size_t a, Ts... ts){ return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...));}
    // template<typename A, size_t N, typename T> void Fill(A (&array)[N], const T &val){std::fill( (T*)array, (T*)(array+N), val );}

    // /* for debug */
    #define DEBUG(x) dbg(#x,x)
    template<class T> void dbg(string name, T x){cerr<<name<<": "<<x<<"\n";}
    template<> void dbg<P>(string name, P x){cerr<<name<<": ("<<x.first<<","<<x.second<<")\n";}
    template<class T> void dbg(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr<<'\n';}
    template<> void dbg<P>(string name, vector<P> xl){cerr<<name<<": "; for(P x:xl){cerr<<"("<<x.first<<","<<x.second<<"), ";}cerr<<"\n";}
    template<class T> void dbg(string name, vector<vector<T>> xl){ cerr<<name<<": \n"; int ml=1;for(vector<T> row: xl){for(T x:row){stringstream sstm; sstm<<x; ml=max(ml,(int)sstm.str().size());}}; for(vector<T> row: xl){{for(T x:row) cerr<<std::right<<std::setw(ml+1)<<x;} cerr << '\n';}}
    // template<class T> void dbg(string name, set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    // template<class T> void dbg(string name, multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    // template<class T> void dbg(string name, unordered_set<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x<<" ";cerr<<'\n';}
    // template<class T> void dbg(string name, unordered_multiset<T> xl){cerr<<name<<": "; for(T x:xl)cerr<<x;cerr<<'\n';}
    // template<class T, class U> void dbg(string name, map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
    // template<class T, class U> void dbg(string name, unordered_map<T,U> xl){cerr<<name<<": \n"; for(auto &[k,v]:xl)cerr<<"  "<<k<<": "<<v<<'\n';}
}
using namespace defines;

const ll INF = 1'001'001'001'001ll;

mt19937_64 mt64(0);
uniform_int_distribution<int> rand_col_row(0, 1);
uniform_int_distribution<int> rand_n(0, 999);
uniform_int_distribution<int> rand_10e5(0, 100000);
uniform_real_distribution<double> rand_percent(0, 1);

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
    vector<ll> al;
    vector<P> alp;
};

/* global vars */
State state;
int N,M,K;
double logk;

int calc_score(){
    double res=0;
    for(ll a:state.al){
        res+=(logk-log2(a+1));
        // DEBUG(res);
    }
    int resi=ceil(res);
    return resi;
}

void solve(){
    TimeManager tm;
    cin>>N>>M>>K;
    logk=log2(K);
    vector<ll> al(N);
    vector<P> alp(N);
    REP(i,N){
        cin>>al[i];
        alp[i]={al[i],i};
    }
    sort(ALL(alp));
    state.al=al;
    state.alp=alp;
    // DEBUG(calc_score());
    while(tm.check(1850.0)){
         
    }
    return;
}


int main(int argc, char* argv[]){

    // if(argc>=2){
    //     MINI_PART = atoi(argv[1]);
    //     T0 = atof(argv[2]);
    //     T1 = atof(argv[3]);
    //     FIRST_MINI_RATE = atof(argv[4]);
    // }

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}