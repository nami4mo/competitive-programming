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
uniform_real_distribution<double> rand_01(0, 1);

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


struct Chair{
    ll e;
    ll x;
    ll y;
    ll power=0;
    int ind; // only used in chairs
    Chair(ll e, ll y, ll x):e(e),y(y),x(x){}
    Chair(){}
    bool operator<( const Chair& right ) const {
        return e<right.e;
    }
};


struct State{
    vector<vector<ll>> el;
    vector<vector<int>> used;
    vector<Chair> chairs;
    vector<vector<Chair>> chairs_2d;
};


/* global vars */
State state;
int N;

vector<P> get_posl(int cy, int cx, int d){
    vector<P> res;
    FOR(dy,(-1)*d,d+1){
        int y=cy+dy;
        int x;
        if(y<0||y>=N) continue;
        int dx=d-abs(dy);
        if(dx==0){
            x=cx;
            res.push_back({y,x});
        }
        else{
            x=cx-dx;
            if(0<=x && x<N) res.push_back({y,x});
            x=cx+dx;
            if(0<=x && x<N) res.push_back({y,x});
        }
    }
    return res;
}

bool check_ok(vector<P> &pl){
    for(auto &[y,x]:pl){
        if(state.used[y][x]!=-1) return false;
    }
    return true;
}



// power変更、変数更新、usedも更新
void update_chair(int ind, int power){
    int prev_p=state.chairs[ind].power;
    state.chairs[ind].power=power;

    int y=state.chairs[ind].y;
    int x=state.chairs[ind].x;
    state.chairs_2d[y][x]=state.chairs[ind];

    if(prev_p<power){
        FOR(d,prev_p+1,power+1){
            vector<P> pl=get_posl(y,x,d);
            for(auto &[y,x]:pl){
                state.used[y][x]++;
            }
        }
    }
    else if(prev_p>power){
        FOR(d,power+1,prev_p+1){
            vector<P> pl=get_posl(y,x,d);
            for(auto &[y,x]:pl){
                state.used[y][x]--;
            }
        }
    }
}


void first_solve(){
    int POWER=1;
    for(Chair &ch:state.chairs){
        if(state.used[ch.y][ch.x]>0) continue;
        // vector<P> noise_pl=get_posl(ch.y, ch.x, POWER);
        // if(check_ok(noise_pl)){
            update_chair(ch.ind, POWER);
        // }
    }
}

bool expand(int ind, int d, double tt){
    d=1;
    Chair &ch=state.chairs[ind];
    int y=ch.y, x=ch.x, power=ch.power;
    if(power==0) return false;
    if(power>=4) return false;
    vector<P> jyama=get_posl(y,x,power+d); // only d=1
    // DEBUG(y); DEBUG(x);
    // DEBUG(jyama);

    vector<ll> jyama_inds;
    int jyama_score=0;
    for(auto &[y,x]:jyama){
        int j_ind=state.chairs_2d[y][x].ind;
        if(state.chairs[j_ind].power>0){
            jyama_inds.push_back(j_ind);
        }
    }

    // int aku=(-4)*(power+1);
    for(int j_ind:jyama_inds){
        jyama_score+=state.chairs[j_ind].power*state.chairs[j_ind].e;
        int pp=state.chairs[j_ind].power;
        // aku+=(pp*pp);
        // aku+=((pp+1)*(pp+1));
    }

    // DEBUG(ch.e);
    // DEBUG(jyama_score);
    int kaizen=ch.e-jyama_score;
    double yaki_prob = rand_01(mt64);
    if(kaizen>0 || yaki_prob<exp(kaizen/tt) ){
        for(int j_ind:jyama_inds){
            update_chair(j_ind,0);
        }
        update_chair(ind,power+1);
        return true;
    }

    return false;
}


void solve(){
    TimeManager tm;
    cin>>N;
    vector<vector<ll>> el(N,vector<ll>(N,0));
    vector<vector<Chair>> c2d(N,vector<Chair>(N));
    vector<vector<int>> used(N,vector<int>(N,0));
    state.chairs.clear();
    REP(i,N){
        REP(j,N){
            cin>>el[i][j];
            state.chairs.push_back(Chair(el[i][j],i,j));
            // c2d[i][j].e=el[i][j];
            // c2d[i][j].x=j;
            // c2d[i][j].y=i;
            // c2d[i][j].power=0;
        }
    }
    state.el=el;
    state.used=used;
    state.chairs_2d=c2d;
    sort(ALL(state.chairs));
    reverse(ALL(state.chairs));
    REP(i,N*N){
        state.chairs[i].ind=i;
        int y=state.chairs[i].y;
        int x=state.chairs[i].x;
        state.chairs_2d[y][x]=state.chairs[i];
    }
    first_solve();

    int loop=0;
    double TL=1850.0;
    double T0=5;
    double T1=0;
    while(tm.check(TL,true)){
        double t01=tm.get_time()/TL;
        double tt=pow(T0,1.0-t01)*pow(T1,t01);

        REP(i,N*N){
            if(!tm.check(TL)) break;
            int ind=i;
            expand(ind,1, tt);
        }
        loop++;
    }
    DEBUG(loop);

    REP(i,N){
        REP(j,N){
            cout<<state.chairs_2d[i][j].power<< " ";
        }
        cout<<endl;
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