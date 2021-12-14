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
const ll HW = 30;
// const ll HW = 5;

const ll QUERY_N = 1000; 
int n;

mt19937_64 mt64(0);
// uniform_int_distribution<int> rand_dir4(0, 3);
// uniform_real_distribution<double> rand_01(0, 1);
// uniform_real_distribution<double> rand_05_15(0.5, 1.5);
uniform_int_distribution<int> rand_col_row(0, 1);
uniform_int_distribution<int> rand_lr(0, 1);
uniform_int_distribution<int> rand_hw(0, HW-1);
uniform_int_distribution<int> rand_d(500, 2000);
uniform_int_distribution<int> rand_01(0, 1);
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

int get_pos_num(int y, int x){ 
    if( y<0 || HW<=y || x<0 || HW<=x ) {return -1;}
    return y*HW+x; 
}

int get_dir_num(char c){
    if(c=='U') return 0;
    if(c=='D') return 1;
    if(c=='L') return 2;
    if(c=='R') return 3;
    return -1;
}

struct EdgeInfo{
    double cont_sum = 0.0;
    vector<double> contributes;
    ll dist_sum = 0.0;
    vector<ll> dists;
    ll cont_dist_sum = 0.0;
    ll est_dist = 0; //最初は0にしておくことで、優先的に使われる？
};


struct Edge4d{
    /*
        UDLR
        0123
    */    
    vector<EdgeInfo> edges_info;
    vector<P> edges;
    Edge4d() : edges(4,{-1,-1}), edges_info(4) {}
};

struct MoveRes{
    int sy,sx,ty,tx;
    ll dist;
    ll true_dist;
    string route;
};

void init_grid_gl(vector<Edge4d> &grid_gl){
    // const int default_dist = 5000;
    const int default_dist = 0;
    for(int y=0; y<HW ; y++){
        for(int x=0; x<HW ; x++){
            int pos = get_pos_num(y,x);
            if(y!=0) grid_gl[pos].edges[0] = {get_pos_num(y-1,x),default_dist};
            if(y!=HW-1) grid_gl[pos].edges[1] = {get_pos_num(y+1,x),default_dist};
            if(x!=0) grid_gl[pos].edges[2] = {get_pos_num(y,x-1),default_dist};
            if(x!=HW-1) grid_gl[pos].edges[3] = {get_pos_num(y,x+1),default_dist};
        }
    }
}

// struct StreetInfo{
//     double cont_sum = 0.0;
//     vector<double> contributes;
//     ll dist_sum = 0.0;
//     vector<ll> dists;
//     ll cont_dist_sum = 0.0;
//     ll est_dist = 0; // 最初は0にしておくことで、優先的に使われる？
// };

struct StreetInfo{
    int bound = 15;

    double cont_sum_l = 0.0;
    double cont_sum_r = 0.0;

    vector<double> contributes_l;
    vector<double> contributes_r;

    ll dist_sum_l = 0.0;
    ll dist_sum_r = 0.0;

    vector<ll> dists_l;
    vector<ll> dists_r;

    ll cont_dist_sum_l = 0.0;
    ll cont_dist_sum_r = 0.0;

    ll est_dist_l = 0; // 最初は0にしておくことで、優先的に使われる？
    ll est_dist_r = 0; // 最初は0にしておくことで、優先的に使われる？

    void add_est_dist(ll dist, int lr){
        if(lr==0) {
            ll next_dist = est_dist_l + dist;
            est_dist_l=max(0ll, next_dist);
        }
        if(lr==1) {
            ll next_dist = est_dist_r + dist;
            est_dist_r = max(0ll, next_dist);
        }
    }

    ll get_dist(int pos){
        if(pos<bound) return est_dist_l;
        else return est_dist_r;
    }
    int check_lr(int pos){
        if(pos<bound) return 0;
        else return 1;
    }
};

struct Edge{
    int y,x; 
    int dir; // 0: D, 1: R 
};

// 一つの移動に関する情報
struct RouteInfo{
    vector<int> row_move_cnts;
    vector<int> col_move_cnts;
    vector<Edge> edges;
    ll dist;
    RouteInfo(){}
};

struct State{
    // vector<vector<ll>> grid;
    vector<Edge4d> grid_gl; // 行と列ごとに更新
    vector<Edge4d> grid_gl_v2; // 辺ごとに更新
    vector<StreetInfo> row_streets;
    vector<StreetInfo> col_streets;
    vector<RouteInfo> routes_info;
    State() : grid_gl(HW*HW), grid_gl_v2(HW*HW), row_streets(HW), col_streets(HW) {
        init_grid_gl(grid_gl);
        init_grid_gl(grid_gl_v2);
    };
    void update_routes_info(MoveRes move_res){
        vector<int> row_move_cnts(HW,0);
        vector<int> col_move_cnts(HW,0);
        vector<Edge> edges;
        int py=move_res.sy, px=move_res.sx;
        for(char dir : move_res.route){
            Edge ed;
            if(dir == 'U' || dir == 'D') col_move_cnts[px]+=1;
            else row_move_cnts[py]+=1;
            if(dir=='U') {
                py--;
                ed.y=py; ed.x=px; ed.dir=0;
            }
            else if(dir=='D') {
                ed.y=py; ed.x=px; ed.dir=0;
                py++;
            }
            else if(dir=='L') {
                px--;
                ed.y=py; ed.x=px; ed.dir=1;
            }
            else {
                ed.y=py; ed.x=px; ed.dir=1;
                px++;
            }
            edges.push_back(ed);
        }
        RouteInfo ri;
        ri.row_move_cnts=row_move_cnts; 
        ri.col_move_cnts=col_move_cnts;
        ri.edges=edges;
        ri.dist=move_res.true_dist;
        routes_info.push_back(ri);
    }
};

void update_gl_from_est_dist(State &state, int col_row, int ind, int lr){
    if(col_row==0){
        int x = ind;
        StreetInfo &street = state.col_streets[x];
        int bound = street.bound;
        if(lr==0){
            for(int y=0 ; y<bound ; y++){
                int pos = get_pos_num(y,x);
                state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist_l};
                state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist_l};
            }
        }
        else{
            for(int y=bound ; y<HW ; y++){
                int pos = get_pos_num(y,x);
                state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist_r};
                state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist_r};
            }
        }
    }
    else{
        int y = ind;
        StreetInfo &street = state.row_streets[y];
        int bound = street.bound;
        if(lr==0){
            for(int x=0 ; x<bound ; x++){
                int pos = get_pos_num(y,x);
                state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist_l};
                state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist_l};
            }
        }
        else{
            for(int x=bound ; x<HW ; x++){
                int pos = get_pos_num(y,x);
                state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist_r};
                state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist_r};
            }
        }
    }
}


void update_route(State &state, double t01){
    int ind = rand_hw(mt64);
    int col_row = rand_col_row(mt64);
    int lr = rand_lr(mt64);
    ll dist_d = rand_d(mt64);
    if(rand_01(mt64)==0) dist_d*=-1;
    
    // ll curr_diff = 0;
    ll kaizen = 0;
    ll edge_cnt = 0;
    for(RouteInfo &ri : state.routes_info){
        ll est_dist=0;
        ll change_cnt=0;
        for(Edge &ed : ri.edges){
            int y=ed.y, x=ed.x;
            if(ed.dir==0){
                est_dist += state.col_streets[x].get_dist(y);
                if(col_row==0 && ind==x && state.col_streets[x].check_lr(y)==lr ){
                    change_cnt++;
                }
            }
            else{
                est_dist += state.row_streets[y].get_dist(x);
                if(col_row==1 && ind==y && state.row_streets[y].check_lr(x)==lr ){
                    change_cnt++;
                }
            }
        }
        ll curr_error = abs(est_dist-ri.dist);
        ll updated_error = abs(est_dist+change_cnt*dist_d - ri.dist);
        kaizen+=(curr_error-updated_error);
    }

    // kaizen = kaizen/edge_cnt;
    // double T0=abs(dist_d);
    // double T1=abs(dist_d)/10;
    // double tt=pow(T0,1.0-t01)*pow(T1,t01);
    // double yaki_prob = rand_percent(mt64);

    if(kaizen>0){
        if(col_row==0 && lr==0)      state.col_streets[ind].add_est_dist(dist_d,0);
        else if(col_row==0 && lr==1) state.col_streets[ind].add_est_dist(dist_d,1);
        else if(col_row==1 && lr==0) state.row_streets[ind].add_est_dist(dist_d,0);
        else if(col_row==0 && lr==1) state.row_streets[ind].add_est_dist(dist_d,1);
        // DEBUG(col_row);
        // DEBUG(lr);
        // DEBUG(kaizen);
        update_gl_from_est_dist(state, col_row, ind, lr);
    }
}

void DEBUG_GL_OUTPUT(State &state){
    vector<vector<ll>> hl(HW, vector<ll>(HW-1,0));
    vector<vector<ll>> wl(HW-1, vector<ll>(HW,0));
    for(int y=0; y<HW ; y++){
        for(int x=0; x<HW-1; x++){
            hl[y][x] = state.grid_gl[get_pos_num(y,x)].edges[3].second;
            // hl[y][x] = state.grid_gl_v2[get_pos_num(y,x)].edges[3].second;
            cerr << hl[y][x] << " ";
        }
        cerr << endl;
    }
    for(int y=0; y<HW-1 ; y++){
        for(int x=0; x<HW; x++){
            hl[y][x] = state.grid_gl[get_pos_num(y,x)].edges[1].second;
            // hl[y][x] = state.grid_gl_v2[get_pos_num(y,x)].edges[1].second;
            cerr << hl[y][x] << " ";
        }
        cerr << endl;
    }
}

void update_edges_from_moveres(State &state, MoveRes move_res){
    int step = move_res.route.size()-1;
    ll ave_dist = move_res.true_dist / step;
    double contribute = 1.0/step;
    contribute*=contribute;
    // vector<int> row_move_cnts(HW,0);
    // vector<int> col_move_cnts(HW,0);
    vector<P> used_pos_edges; // P: {pos, edge(0~3)}

    int py=move_res.sy, px=move_res.sx;
    for(char dir : move_res.route){
        // if(dir == 'U' || dir == 'D') col_move_cnts[px]+=1;
        // else row_move_cnts[py]+=1;
        used_pos_edges.push_back({get_pos_num(py,px), get_dir_num(dir)});
        if(dir=='U') py--;
        else if(dir=='D') py++;
        else if(dir=='L') px--;
        else px++;
    }

    for(auto &[pos,eind] : used_pos_edges){
        EdgeInfo &edge_info = state.grid_gl_v2[pos].edges_info[eind];
        edge_info.contributes.push_back(contribute);
        edge_info.cont_sum += contribute;
        edge_info.dists.push_back(ave_dist);
        edge_info.cont_dist_sum += ave_dist*contribute;
        edge_info.est_dist = edge_info.cont_dist_sum/edge_info.cont_sum;
        state.grid_gl_v2[pos].edges[eind] = { state.grid_gl_v2[pos].edges[eind].first, edge_info.est_dist};
    }
}



void update_streets_from_moveres(State &state, MoveRes move_res){
    int step = move_res.route.size()-1;
    ll ave_dist = move_res.true_dist / step;
    vector<int> row_move_cnts_l(HW,0);
    vector<int> col_move_cnts_l(HW,0);
    vector<int> row_move_cnts_r(HW,0);
    vector<int> col_move_cnts_r(HW,0);
    double error_rate = (1.0)+abs(move_res.true_dist-move_res.dist)/move_res.true_dist;
    error_rate*=error_rate;
    error_rate*=error_rate;
    const double weight = 0.95;

    int py=move_res.sy, px=move_res.sx;
    for(char dir : move_res.route){
        if(dir == 'U' || dir == 'D') {
            if(py < state.col_streets[px].bound) col_move_cnts_l[px]+=1;
            else col_move_cnts_r[px]+=1;
        }
        else{
            if(px < state.row_streets[py].bound) row_move_cnts_l[py]+=1;
            else row_move_cnts_r[py]+=1;
        }
        if(dir=='U') py--;
        else if(dir=='D') py++;
        else if(dir=='L') px--;
        else px++;
    }

    for(int y=0 ; y<HW ; y++){
        StreetInfo &street = state.row_streets[y];
        if(row_move_cnts_l[y] > 0){
            double contribute = (1.0) * row_move_cnts_l[y] / step;
            contribute*=contribute; // pow2
            contribute*=error_rate;
            street.contributes_l.push_back(contribute);
            street.cont_sum_l += contribute;
            street.dists_l.push_back(ave_dist);
            street.cont_dist_sum_l += ave_dist*contribute;
            street.est_dist_l = street.cont_dist_sum_l/street.cont_sum_l;
        }
        if(row_move_cnts_r[y] > 0){
            double contribute = (1.0) * row_move_cnts_r[y] / step;
            contribute*=contribute; // pow2
            contribute*=error_rate;
            street.contributes_r.push_back(contribute);
            street.cont_sum_r += contribute;
            street.dists_r.push_back(ave_dist);
            street.cont_dist_sum_r += ave_dist*contribute;
            street.est_dist_r = street.cont_dist_sum_r/street.cont_sum_r;
        }
        if(row_move_cnts_l[y] > 0 || row_move_cnts_r[y] > 0){
            for(int x=0 ; x<HW ; x++){
                int pos = get_pos_num(y,x);
                if(x < street.bound){
                    state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist_l};
                    state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist_l};
                }
                else{
                    state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist_r};
                    state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist_r};
                }
                // if(x!=0) state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist};
                // if(x!=HW-1) state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist};
                // DEBUG(state.grid_gl[pos].edges[2]);
            }
        }
    }
    // DEBUG(py);
    for(int x=0 ; x<HW ; x++){
        StreetInfo &street = state.col_streets[x];
        if(col_move_cnts_l[x] > 0){
            double contribute = (1.0) * col_move_cnts_l[x] / step;
            contribute*=contribute; // pow2
            contribute*=error_rate;
            street.contributes_l.push_back(contribute);
            street.cont_sum_l += contribute;
            street.dists_l.push_back(ave_dist);
            street.cont_dist_sum_l += ave_dist*contribute;
            street.est_dist_l = street.cont_dist_sum_l/street.cont_sum_l;
        }
        if(col_move_cnts_r[x] > 0){
            double contribute = (1.0) * col_move_cnts_r[x] / step;
            contribute*=contribute; // pow2
            contribute*=error_rate;
            street.contributes_r.push_back(contribute);
            street.cont_sum_r += contribute;
            street.dists_r.push_back(ave_dist);
            street.cont_dist_sum_r += ave_dist*contribute;
            street.est_dist_r = street.cont_dist_sum_r/street.cont_sum_r;
        }
        if(col_move_cnts_l[x] > 0 || col_move_cnts_r[x] > 0){
            for(int y=0 ; y<HW ; y++){
                int pos = get_pos_num(y,x);
                if(y < street.bound){
                    state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist_l};
                    state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist_l};
                }
                else{
                    state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist_r};
                    state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist_r};
                }
                // if(x!=0) state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist};
                // if(x!=HW-1) state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist};
                // DEBUG(state.grid_gl[pos].edges[2]);
            }
        }
    }
}



void update_streets_from_moveres_2(State &state, MoveRes move_res){
    int step = move_res.route.size()-1;
    // ll ave_dist = move_res.true_dist / step;
    ll update_dist = (move_res.true_dist-move_res.dist)/step;
    vector<int> row_move_cnts_l(HW,0);
    vector<int> col_move_cnts_l(HW,0);
    vector<int> row_move_cnts_r(HW,0);
    vector<int> col_move_cnts_r(HW,0);
    // double error_rate = (1.0)+abs(move_res.true_dist-move_res.dist)/move_res.true_dist;
    // error_rate*=error_rate;
    // error_rate*=error_rate;
    // const double weight = 0.95;

    int py=move_res.sy, px=move_res.sx;
    for(char dir : move_res.route){
        if(dir == 'U' || dir == 'D') {
            if(py < state.col_streets[px].bound) col_move_cnts_l[px]+=1;
            else col_move_cnts_r[px]+=1;
        }
        else{
            if(px < state.row_streets[py].bound) row_move_cnts_l[py]+=1;
            else row_move_cnts_r[py]+=1;
        }
        if(dir=='U') py--;
        else if(dir=='D') py++;
        else if(dir=='L') px--;
        else px++;
    }

    for(int y=0 ; y<HW ; y++){
        StreetInfo &street = state.row_streets[y];
        if(row_move_cnts_l[y] > 0){
            double contribute = (1.0) * row_move_cnts_l[y] / step;
            street.est_dist_l = street.est_dist_l+update_dist*contribute;
            if(street.est_dist_l<0) street.est_dist_l=0;
        }
        if(row_move_cnts_r[y] > 0){
            double contribute = (1.0) * row_move_cnts_r[y] / step;
            street.est_dist_r = street.est_dist_r+update_dist*contribute;
            if(street.est_dist_r<0) street.est_dist_r=0;
        }
        if(row_move_cnts_l[y] > 0 || row_move_cnts_r[y] > 0){
            for(int x=0 ; x<HW ; x++){
                int pos = get_pos_num(y,x);
                if(x < street.bound){
                    state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist_l};
                    state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist_l};
                }
                else{
                    state.grid_gl[pos].edges[2]={get_pos_num(y,x-1), street.est_dist_r};
                    state.grid_gl[pos].edges[3]={get_pos_num(y,x+1), street.est_dist_r};
                }
            }
        }
    }
    // DEBUG(py);
    for(int x=0 ; x<HW ; x++){
        StreetInfo &street = state.col_streets[x];
        if(col_move_cnts_l[x] > 0){
            double contribute = (1.0) * col_move_cnts_l[x] / step;
            street.est_dist_l = street.est_dist_l+update_dist*contribute;
            if(street.est_dist_l<0) street.est_dist_l=0;
        }
        if(col_move_cnts_r[x] > 0){
            double contribute = (1.0) * col_move_cnts_r[x] / step;
            street.est_dist_r = street.est_dist_r+update_dist*contribute;
            if(street.est_dist_r<0) street.est_dist_r=0;
        }
        if(col_move_cnts_l[x] > 0 || col_move_cnts_r[x] > 0){
            for(int y=0 ; y<HW ; y++){
                int pos = get_pos_num(y,x);
                if(y < street.bound){
                    state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist_l};
                    state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist_l};
                }
                else{
                    state.grid_gl[pos].edges[0]={get_pos_num(y-1,x), street.est_dist_r};
                    state.grid_gl[pos].edges[1]={get_pos_num(y+1,x), street.est_dist_r};
                }
            }
        }
    }

}


MoveRes get_shortest_path_from_grid(vector<Edge4d> &gl, vector<Edge4d> &gl2, int sy, int sx, int ty, int tx){
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
        // for( auto& [next_v, cost] : gl[v].edges){
        for(int dir : {0,1,2,3}){
            int next_v = gl[v].edges[dir].first;
            // int cost = gl[v].edges[dir].second;
            int cost = (gl[v].edges[dir].second*0.9 + gl2[v].edges[dir].second*0.1);
            if(next_v == -1)continue;
            if( d[next_v] > d[v] + cost ){
                d[next_v] = d[v] + cost;
                prev_vl[next_v] = v;
                q.push(P(d[next_v], next_v));
            }
        }
    }

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

    //
    //
    const int output_per=10;
    // cerr << QUERY_N/output_per << endl;
    REP(i,QUERY_N){
        ll sy,sx,ty,tx;
        cin>>sy>>sx>>ty>>tx;
        // string res = get_simple_path(sy,sx,ty,tx);
        // MoveRes res = get_shortest_path_from_grid(state.grid_gl, sy,sx,ty,tx);
        MoveRes res = get_shortest_path_from_grid(state.grid_gl, state.grid_gl_v2, sy,sx,ty,tx);
        // DEBUG(res.dist);
        cout << res.route << endl;
        ll true_dist; cin>>true_dist;
        res.true_dist = true_dist;

        state.update_routes_info(res);
        if(i<300){
            // update_streets_from_moveres(state, res);
            update_streets_from_moveres_2(state, res);
        }
        else{
            double t01 = (1.0)*i/QUERY_N;
            update_streets_from_moveres_2(state, res);
            REP(j,20){
                update_route(state, t01);
            }
        }
        if(i%output_per==0){
            // DEBUG_GL_OUTPUT(state);
        }
        //
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}