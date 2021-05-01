#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<int,int> P;
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

const ll HW=50;
vector<P> dirs={{-1,0},{1,0},{0,-1},{0,1}};
vector<char> d2c={'U','D','L','R'};

mt19937_64 mt64(0);
uniform_int_distribution<int> rand_dir4(0, 3);
uniform_real_distribution<double> rand_01(0, 1);
uniform_real_distribution<double> rand_05_15(0.5, 1.5);
// uniform_int_distribution<int> rand_hw(0, HW);
// uniform_int_distribution<int> rand_ad(0, n-1);
// int next_adi=rand_ad(mt64);

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
    // ll pena_sum=0;
    // State(int n):pena_sum(n){};
    vector<bool> used;
    vector<vector<int>> tl;
    vector<vector<int>> pl;
    int y,x;
    State():used(2510,false), tl(HW, vector<int>(HW,-1)), pl(HW, vector<int>(HW,-1)){};
};

// ll dfs(P node, State &state){
//     for(int )
// }

ll step_k(int k, State &state){
    vector<bool> used_orig;
}


string greedy(State &state, int si, int sj){
    string res=""; 
    int y=si,x=sj;
    state.used[ state.tl[y][x]]=true;
    const int loop=3;
    while(true){
        for(int lc=0 ; lc<loop ; lc++){
            
        }

        vector<int> vals(4,-1);
        for(int i=0 ; i<4 ; i++){
            auto &[dy,dx]=dirs[i];
            int yy=y+dy,xx=x+dx;
            if(yy<0||HW<=yy||xx<0||HW<=xx) continue;
            int tnum=state.tl[yy][xx];
            if(state.used[tnum]) continue;
            vals[i]=state.pl[yy][xx];
        }
        int maxd=-1;
        int maxv=-1;
        for(int i=0 ; i<4 ; i++){
            if(maxv<vals[i]){
                maxd=i, maxv=vals[i];
            }
        }
        if(maxd==-1)break;
        res+=d2c[maxd];
        auto &[dy,dx]=dirs[maxd];
        y+=dy, x+=dx;
        state.used[ state.tl[y][x] ]=true;
    }
    return res;
}

int cnt_good_tiles(State &state, int y, int x, int sz=3){
    int res=0;
    for(int dy=sz*(-1) ; dy<=sz ; dy++){
        for(int dx=sz*(-1) ; dx<=sz ; dx++){
            int yy=y+dy, xx=x+dx;
            // if(yy<0||HW<=yy||xx<0||HW<=xx) continue;
            if(yy<0||HW<=yy||xx<0||HW<=xx) {
                res++;
                continue;
            }
            if(!state.used[state.tl[yy][xx]]) res++;
        }
    }
    return res;
}

int calc_kakomare(State &state, int y, int x, int sz=3){
    int res=0;
    for(int dy=1 ; y-dy>=0 ; dy++){
        int yy=y-dy;
        if(state.used[state.tl[yy][x]]){
            res+=dy;
            break;
        }
        if(y-dy==0) res+=dy;
    }
    for(int dy=1 ; y+dy<HW ; dy++){
        int yy=y+dy;
        if(state.used[state.tl[yy][x]]){
            res+=dy;
            break;
        }
        if(y+dy==HW-1) res+=dy;
    }
    for(int dx=1 ; x-dx>=0 ; dx++){
        int xx=x-dx;
        if(state.used[state.tl[y][xx]]){
            res+=dx;
            break;
        }
        if(x-dx==0) res+=dx;
    }
    for(int dx=1 ; x+dx<HW ; dx++){
        int xx=x+dx;
        if(state.used[state.tl[y][xx]]){
            res+=dx;
            break;
        }
        if(x+dx==HW-1) res+=dx;
    }
    return res;
}

const double TL2=1600;
void dfs(State &state, int y, int x, int dist, int maxdist, int score, string res, vector<pair<int,string>> &cands, vector<pair<int,string>> &stop_cands, TimeManager &tm){ //score, res
    // DEBUG(y);
    // DEBUG(x);
    if(tm.get_time(true)>TL2) {
        cands.push_back({score,res});
        return;
    }
    if(dist==maxdist){
        // int dirscore=0;
        // int dx=abs(state.x-x);
        // int dy=abs(state.y-y);
        // dirscore=abs(dx-dy)+(dx+dy);
        // cands.push_back({score,res});
        // cands.push_back({dirscore,res});
        // DEBUG(dirscore);
        // int good_ts=cnt_good_tiles(state,y,x);
        // cands.push_back({good_ts,res});
        int kakomare=calc_kakomare(state,y,x);
        // DEBUG(kakomare);
        cands.push_back({kakomare,res});
        // DEBUG(good_ts);
        return;
    }
    bool moved;
    for(int i=0 ; i<4 ; i++){
        auto &[dy,dx]=dirs[i];
        int yy=y+dy,xx=x+dx;
        if(yy<0||HW<=yy||xx<0||HW<=xx) continue;
        int tnum=state.tl[yy][xx];
        if(state.used[tnum]) continue;

        int val=state.pl[yy][xx];
        state.used[tnum]=true;
        dfs(state,yy,xx,dist+1, maxdist, score+val, res+d2c[i], cands,stop_cands,tm);

        state.used[tnum]=false;
        moved=true;
    }
    if(!moved){
        stop_cands.push_back({score,res});
    }
}

void do_step(State &state, int &y, int &x, string res){
    state.used[ state.tl[y][x]]=true;
    for(char c:res){
        if(c=='U')y--;
        else if(c=='D')y++;
        else if(c=='L')x--;
        else if(c=='R')x++;
        state.used[ state.tl[y][x]]=true;
        // DEBUG(y);
        // DEBUG(x);
        state.y=y;
        state.x=x;
    }
}

const double TL = 1500.0;
string dfs_loop(State &state, int y, int x, int maxdist, TimeManager &tm, int max_loop=-1){
    string all_res="";
    int loop=0;
    while(true){
        if(max_loop>0 && max_loop==loop){
            return all_res;
        }
        if(tm.get_time(true)>TL) {
            return all_res;
        }

        double t01=tm.get_time()/TL;
        int distup=(loop/10);

        vector<pair<int,string>> cands;
        vector<pair<int,string>> stop_cands;
// void dfs(State &state, int y, int x, int dist, int maxdist, int score, string res, vector<pair<int,string>> &cands, vector<pair<int,string>> &stop_cands){ //score, res
        dfs(state,y,x,0,maxdist+distup,0,"",cands,stop_cands,tm);
        // for(auto &[score,res]:cands){
        //     // DEBUG(score);
        //     // DEBUG(res);
        // }
        if(!cands.empty()){
            string max_res="";
            int maxv=-1;
            for(auto &[score,res]:cands){
                if(score>maxv){
                    maxv=score, max_res=res;
                }
            }
            do_step(state,y,x,max_res);
            all_res+=max_res;
            // DEBUG(all_res);
        }

        else{
            if(stop_cands.empty()){
                return all_res;
            }
            else{
                string max_res="";
                int maxv=-1;
                for(auto &[score,res]:stop_cands){
                    if(score>maxv){
                        maxv=score, max_res=res;
                    }
                } 
                all_res+=max_res;
                return all_res;
            }
        }
    }


    // state.used[ state.tl[si][sj]]=true;
}

void solve(){
    TimeManager tm;
    State state;

    // double TL = 4900.0;
    int si,sj;cin>>si>>sj;
    REP(i,HW)REP(j,HW)cin>>state.tl[i][j];
    REP(i,HW)REP(j,HW)cin>>state.pl[i][j];
    
    // string res=greedy(state, si,sj);
    // cout<<res<<endl;

    vector<pair<int,string>> cands;
    vector<pair<int,string>> stop_cands;

    state.y=si, state.x=sj;
    state.used[ state.tl[si][sj]]=true;
    const int DIST=15;
    string res=dfs_loop(state,si,sj,DIST,tm,-1);

    // cout<<res<<endl;

    string res2=greedy(state, state.y,state.x);
    DEBUG(res2);

    res+=res2;
    cout<<res<<endl;


    // dfs(state,si,sj,0,15,0,"",cands,stop_cands);
    // string res=cands[0].second;
    // cout<<res<<endl;
    // DEBUG(cands);
    // DEBUG(stop_cands);
    // for(auto &[score,res]:cands){
    //     DEBUG(score);
    //     DEBUG(res);
    // }

    // while(tm.check(TL)){
    //     // double t01=tm.get_time()/TL;
    //     // double tt=pow(T0,1.0-t01)*pow(T1,t01);

    //     // yaki_prob<exp(kaizen/tt)
    // }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}