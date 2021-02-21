#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
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

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;

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
        else return true;
    }
    double get_time(bool force=false){
        if(force) check(true);
        return time;
    }
};

int D=365;
vector<ll> cl(26,0ll);
vector<vector<ll>> sl(D, vector<ll>(26,0ll));

struct State{
    ll score;
    vector<ll> tl;
    // vector<vecotr<ll>> c_days;
    State(){};
    // ll change(int day, int c){
    // }
    ll calc(){
        score=0;
        vector<ll> last_ds(26,-1);
        REP(i,D){
            ll c=tl[i];
            last_ds[c]=i;
            score+=sl[i][c];
            REP(cc,26){
                score-=cl[cc]*(i-last_ds[cc]);
            }
        }
        return score;
    }
};



void solve(){
    TimeManager tm;

    cin>>D;
    REP(i,26) cin>>cl[i];
    REP(i,D)REP(j,26)cin>>sl[i][j];

    vector<ll> last_ds(26,-1);
    vector<ll> first_tl;
    ll score=0;
    REP(i,D){
        ll next_v= -INF;
        ll real_v=-INF;
        ll next_c= -1;
        REP(c,26){
            ll dist=i-last_ds[c];
            score-=cl[c]*dist;
            //// ---- eval func ------
            // ll v=sl[i][c]+cl[c]*(dist)*(dist+1)/2;
            ll v=sl[i][c]+cl[c]*dist*3;
            ll vv=sl[i][c]+cl[c]*dist;
            //// ---------------------
            if(next_v<v){
                next_v=v;
                next_c=c;
                real_v=vv;
            }
        }
        score+=real_v;
        last_ds[next_c]=i;
        first_tl.push_back(next_c);    
    }
    // DEBUG(first_tl);
    // DEBUG(score);
    State state;
    state.tl=first_tl;
    state.score=score;
    
    mt19937_64 mt64(0);
    uniform_int_distribution<int> rand_day(0, D-1);
    uniform_int_distribution<int> rand_type(0, 26-1);
    uniform_int_distribution<int> rand_16(1, 16);
    uniform_real_distribution<double> rand_01(0, 1);

    double T0 = 2000.0;
    double T1 = 600.0;
    double TL = 1900.0;
    while(tm.check(TL)){

        double t01=tm.get_time()/TL;
        double tt=pow(T0,1.0-t01)*pow(T1,t01);
        
        int day = rand_day(mt64);
        int c = rand_type(mt64);

        ll prev_score=state.score;
        int prev_c=state.tl[day];
        
        state.tl[day]=c;
        ll new_score=state.calc();

        ll delta=new_score-prev_score;
        if( prev_score>new_score && rand_01(mt64)>exp(delta/tt) ){
            state.tl[day]=prev_c;
            state.score=prev_score;
        }
    }
    for(ll t:state.tl) cout<<t+1<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}