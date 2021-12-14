/*
    UDLR
    0123
*/

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

const ll INF = 1'001'001'001'001ll;
const ll HW = 30;
const ll QUERY_N = 1000; 
int n;

mt19937_64 mt64(0);
uniform_int_distribution<int> rand_dir4(0, 3);
uniform_real_distribution<double> rand_01(0, 1);
uniform_real_distribution<double> rand_05_15(0.5, 1.5);
uniform_int_distribution<int> rand_hw(0, HW);


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

int get_pos_num(int y, int x){ 
    if( y<0 || HW<=y || x<0 || HW<=x ) {return -1;}
    return y*HW+x; 
}

struct Edge4d{
    /*
        UDLR
        0123
    */
   vector<P> edges;
   Edge4d() : edges(4,{-1,-1}) {}
};

struct MoveRes{
    int sy,sx,ty,tx;
    ll dist;
    ll true_dist;
    string route;
};

void init_grid_gl(vector<Edge4d> &grid_gl){
    const int default_dist = 5000;
    for(int y=0; y<HW ; y++){
        for(int x=0; x<HW ; x++){
            int pos = get_pos_num(y,x);
            if(y!=0) grid_gl[pos].edges[0] = {get_pos_num(y-1,x),5000};
            if(y!=HW-1) grid_gl[pos].edges[1] = {get_pos_num(y+1,x),5000};
            if(x!=0) grid_gl[pos].edges[2] = {get_pos_num(y,x-1),5000};
            if(x!=HW-1) grid_gl[pos].edges[3] = {get_pos_num(y,x+1),5000};
        }
    }
}

struct StreetInfo{
    double cont_sum = 0.0;
    vector<double> contributes;
    ll dist_sum = 0.0;
    vector<ll> dists;
    ll cont_dist_sum = 0.0;
    ll est_dist = 0;
};

struct State{
    // vector<vector<ll>> grid;
    vector<Edge4d> grid_gl;
    vector<StreetInfo> row_streets;
    vector<StreetInfo> col_streets;
    State() : grid_gl(HW*HW), row_streets(HW), col_streets(HW) {
        init_grid_gl(grid_gl);
    };
};

void update_streets_from_moveres(State &state, MoveRes move_res){
    int step = move_res.route.size()-1;
    ll ave_dist = move_res.true_dist / step;
    vector<int> row_move_cnts(HW,0);
    vector<int> col_move_cnts(HW,0);
    int py=move_res.sy, px=move_res.sx;
    for(char dir : move_res.route){
        if(dir == 'U' || dir == 'D') col_move_cnts[px]+=1;
        else row_move_cnts[py]+=1;

        if(dir=='U') py--;
        else if(dir=='D') py++;
        else if(dir=='L') px--;
        else px++;
    }

    for(int y=0 ; y<HW ; y++){
        if(row_move_cnts[y] == 0) continue;
        double contribute = (1.0) * row_move_cnts[y] / step;
        contribute*=contribute;
        // DEBUG(contribute);
        StreetInfo &street = state.row_streets[y];
        street.contributes.push_back(contribute);
        street.cont_sum += contribute;
        street.dists.push_back(ave_dist);
        street.cont_dist_sum += ave_dist*contribute;
        street.est_dist = street.cont_dist_sum/street.cont_sum;
        for(int x=0 ; x<HW ; x++){
            int pos = get_pos_num(y,x);
            if(x!=0) state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist};
            if(x!=HW-1) state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist};
            // DEBUG(state.grid_gl[pos].edges[2]);
        }
    }

    for(int x=0 ; x<HW ; x++){
        if(col_move_cnts[x] == 0) continue;
        double contribute = (1.0) * col_move_cnts[x] / step;
        contribute*=contribute;
        StreetInfo &street = state.col_streets[x];
        street.contributes.push_back(contribute);
        street.cont_sum += contribute;
        street.dists.push_back(ave_dist);
        street.cont_dist_sum += ave_dist*contribute;
        street.est_dist = street.cont_dist_sum/street.cont_sum;
        for(int y=0 ; y<HW ; y++){
            int pos = get_pos_num(y,x);
            if(y!=0) state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist};
            if(y!=HW-1) state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist};
            // DEBUG(state.grid_gl[pos].edges[0]);
        }
    }
}

MoveRes get_shortest_path_from_grid(vector<Edge4d> &gl, int sy, int sx, int ty, int tx){
    int n = HW*HW;
    vector<ll> d(n,INF);
    vector<int> prev_vl(n, -1); // 経路復元用
    int start = get_pos_num(sy,sx);
    int goal = get_pos_num(ty,tx);
    priority_queue<P, vector<P>, greater<P>> q;

    d[start] = 0;
    q.push(P(0,start));

    while(!q.empty()){
        auto [dist, v] = q.top(); q.pop();
        if(v == goal) break;
        if( d[v] < dist ) continue;
        for( auto& [next_v, cost] : gl[v].edges){
            if(next_v == -1)continue;
            if( d[next_v] > d[v] + cost ){
                d[next_v] = d[v] + cost;
                prev_vl[next_v] = v;
                q.push(P(d[next_v], next_v));
            }
        }
    }

    // 経路復元
    vector<int> route = {goal};
    string route_str = "";
    int curr_v = goal;
    while(true){
        int prev_v = prev_vl[curr_v];
        if(prev_v == -1) break;
        route.push_back(prev_v);

        int dirnum = curr_v - prev_v;
        if(dirnum == (-1)*HW) route_str += "U";
        else if(dirnum == HW) route_str += "D";
        else if(dirnum == -1) route_str += "L";
        else route_str += "R";

        curr_v = prev_v;
    }
    reverse(ALL(route_str));
    MoveRes res;
    res.dist = d[goal];
    res.route = route_str;
    res.sy=sy; res.sx=sx; res.ty=ty; res.tx=tx;
    return res;
}



string get_simple_path(int sy, int sx, int ty, int tx){
    string res = "";
    if(sx<tx) res += string(tx-sx,'R');
    else res += string(sx-tx,'L');

    if(sy<ty) res += string(ty-sy,'D');
    else res += string(sy-ty,'U');

    return res;
}

void solve(){
    TimeManager tm;
    State state;

    REP(i,QUERY_N){
        ll sy,sx,ty,tx;
        cin>>sy>>sx>>ty>>tx;
        // string res = get_simple_path(sy,sx,ty,tx);
        MoveRes res = get_shortest_path_from_grid(state.grid_gl, sy,sx,ty,tx);
        // DEBUG(res.dist);
        cout << res.route << endl;
        ll true_dist; cin>>true_dist;
        res.true_dist = true_dist;
        update_streets_from_moveres(state, res);
    }

    // REP(y,HW){
    //     REP(x,HW){
    //         DEBUG(state.grid_gl[get_pos_num(y,x)].edges[3].second);
    //     }
    // }
    // cin>>n;
    // uniform_int_distribution<int> rand_ad(0, n-1);

    // double T0=2e8 *n;
    // double T1=1e4 *n;
    // double TL = 4900.0;

    // while(tm.check(TL)){    
        // double t01=tm.get_time()/TL;
        // double tt=pow(T0,1.0-t01)*pow(T1,t01);
    // }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}