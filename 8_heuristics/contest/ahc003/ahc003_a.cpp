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
// const int default_dist = 0;
const int default_dist = 4000;

const ll QUERY_N = 1000; 
int n;

mt19937_64 mt64(0);
// uniform_int_distribution<int> rand_dir4(0, 3);
// uniform_real_distribution<double> rand_01(0, 1);
// uniform_real_distribution<double> rand_05_15(0.5, 1.5);
uniform_int_distribution<int> rand_col_row(0, 1);
uniform_int_distribution<int> rand_lr(0, 1);
uniform_int_distribution<int> rand_hw(0, HW-1);
// uniform_int_distribution<int> rand_d(500, 2000);
uniform_int_distribution<int> rand_d(100, 200);
uniform_int_distribution<int> rand_01(0, 1);
uniform_int_distribution<int> rand_move15(1, 2);
uniform_real_distribution<double> rand_percent(0, 1);
// uniform_real_distribution<double> rand_yuragi(0.9, 1.1);



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
    ll est_dist = default_dist; //最初は0にしておくことで、優先的に使われる？
    int use_cnt=0;
    ll dist_sum=0;
    ll curr_ave_dist=0;
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
    ll g1_dist;
    ll g2_dist;
};

void init_grid_gl(vector<Edge4d> &grid_gl){
    // const int default_dist = 0;
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

// warning!! cont とか使うときは、default_distの設定見直して
// const ll min_dist = 2000;
// const ll max_dist = 8000;
const ll min_dist = 1500;
const ll max_dist = 8500;
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

    // ll est_dist_l = 0; // 最初は0にしておくことで、優先的に使われる？
    // ll est_dist_r = 0; // 最初は0にしておくことで、優先的に使われる？
    ll est_dist_l = default_dist; // 最初は0にしておくことで、優先的に使われる？
    ll est_dist_r = default_dist; // 最初は0にしておくことで、優先的に使われる？

    void add_est_dist(ll dist, int lr){
        if(lr==0) {
            ll next_dist = est_dist_l + dist;
            est_dist_l=max(min_dist, next_dist);
            est_dist_l=min(max_dist, est_dist_l);
        }
        if(lr==1) {
            ll next_dist = est_dist_r + dist;
            est_dist_r=max(min_dist, next_dist);
            est_dist_r=min(max_dist, est_dist_r);
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

    void move_bound(int move){
        bound+=move;
        bound=max(0,bound);
        bound=min((int)HW,bound);
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
    bool use_bound = true;
    int search_cnt;

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

    void remove_bound(){
        use_bound = false;
        for(int i=0 ; i<HW ; i++){
            row_streets[i].bound = HW;
            col_streets[i].bound = HW;
            row_streets[i].est_dist_l = (row_streets[i].est_dist_l+row_streets[i].est_dist_r)/2;
            col_streets[i].est_dist_l = (col_streets[i].est_dist_l+col_streets[i].est_dist_r)/2;
        }
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

struct EdgeUpdateInfo{
    int ind;
    int col_row;
    int lr;
    ll dist_d;
    ll use_cnt = 0;
    // EdgeUpdateInfo(){
    //     ind = rand_hw(mt64);
    //     col_row = rand_col_row(mt64);
    //     lr = rand_lr(mt64);
    //     dist_d = rand_d(mt64);
    //     if(rand_01(mt64)==0) dist_d*=-1;  
    // }
};

void update_route2(State &state, double t01, int mode=0){
    // int ind = rand_hw(mt64);
    // int col_row = rand_col_row(mt64);
    // int lr = rand_lr(mt64);
    // ll dist_d = rand_d(mt64);
    // if(rand_01(mt64)==0) dist_d*=-1;

    int weighted_route_ind = state.search_cnt;
    int update_cnt;
    vector<EdgeUpdateInfo> edge_cands;

    // if(same_street){
    //     update_cnt = 2;
    //     int ind = rand_hw(mt64);
    //     int col_row = rand_col_row(mt64);
    //     ll dist_d = rand_d(mt64);
    //     if(rand_01(mt64)==0) dist_d*=(-1);
    //     REP(i,update_cnt){
    //         EdgeUpdateInfo c_edge_cand;
    //         c_edge_cand.ind = ind;
    //         c_edge_cand.col_row = col_row;
    //         c_edge_cand.lr = i;
    //         c_edge_cand.dist_d = dist_d;
    //         edge_cands.push_back(c_edge_cand);
    //     }   
    // }
    if(mode==0){
        update_cnt = 2;
        int ind = rand_hw(mt64);
        int col_row = rand_col_row(mt64);
        int lr = rand_lr(mt64);
        if(!state.use_bound) lr=0;
        // ll dist_d = rand_d(mt64);
        // if(rand_01(mt64)==0) dist_d*=(-1);
        REP(i,update_cnt){
            EdgeUpdateInfo c_edge_cand;
            c_edge_cand.ind = max(0ll,ind-i);
            c_edge_cand.col_row = col_row;
            // c_edge_cand.lr = (lr+i)%2;
            // // c_edge_cand.lr = lr;
            c_edge_cand.lr = rand_lr(mt64);
            ll dist_d = rand_d(mt64);
            if(rand_01(mt64)==0) dist_d*=(-1);
            c_edge_cand.dist_d = dist_d;
            edge_cands.push_back(c_edge_cand);
        }   
    }
    else if(mode==1){
        update_cnt = 2;
        int ind = rand_hw(mt64);
        int col_row = rand_col_row(mt64);
        ll dist_d = rand_d(mt64);
        if(rand_01(mt64)==0) dist_d*=(-1);
        REP(i,update_cnt){
            EdgeUpdateInfo c_edge_cand;
            c_edge_cand.ind = ind;
            c_edge_cand.col_row = col_row;
            c_edge_cand.lr = i;
            c_edge_cand.dist_d = dist_d;
            edge_cands.push_back(c_edge_cand);
        }   
    }
    else if(mode==2){
        update_cnt = rand_d(mt64)%3 +1;
        // update_cnt = 2;
        REP(i,update_cnt){
            EdgeUpdateInfo c_edge_cand;
            c_edge_cand.ind = rand_hw(mt64);
            c_edge_cand.col_row = rand_col_row(mt64);
            c_edge_cand.lr = rand_lr(mt64);
            if(!state.use_bound) c_edge_cand.lr=0;
            c_edge_cand.dist_d = rand_d(mt64);
            if(rand_01(mt64)==0) c_edge_cand.dist_d*=-1;
            edge_cands.push_back(c_edge_cand);
        }    
    }

    // EdgeUpdateInfo eui = edge_cands[0];

    // ll curr_diff = 0;
    ll kaizen = 0;
    ll edge_cnt = 0;
    // for(RouteInfo &ri : state.routes_info){
    for(int rind=0; rind<state.routes_info.size() ; rind++){
        RouteInfo &ri = state.routes_info[rind];
        ll est_dist=0;
        ll diff=0;
        ll route_len = 0;
        for(Edge &ed : ri.edges){
            route_len++;
            int y=ed.y, x=ed.x;
            if(ed.dir==0){
                est_dist += state.col_streets[x].get_dist(y);
            }
            else{
                est_dist += state.row_streets[y].get_dist(x);
            }
            // EdgeUpdateInfo &eui = edge_cands[0];
            // for(EdgeUpdateInfo &eui : edge_cands){
            REP(i,update_cnt){
                EdgeUpdateInfo &eui = edge_cands[i];
                if(ed.dir==0 && eui.col_row==0 && eui.ind==x && state.col_streets[x].check_lr(y)==eui.lr ){
                    eui.use_cnt++;
                    edge_cnt++;
                    diff+=eui.dist_d;
                }
                if(ed.dir==1 && eui.col_row==1 && eui.ind==y && state.row_streets[y].check_lr(x)==eui.lr ){
                    eui.use_cnt++;
                    edge_cnt++;
                    diff+=eui.dist_d;
                }
            }
        }
        ll curr_error = abs(est_dist-ri.dist);
        ll updated_error = abs(est_dist+diff - ri.dist);
        kaizen+=(curr_error-updated_error)*1;
    }
    if(edge_cnt==0) return;

    kaizen = kaizen/edge_cnt;
    double T0=100;
    double T1=1;
    double tt=pow(T0,1.0-t01)*pow(T1,t01);
    double yaki_prob = rand_percent(mt64);
    if(kaizen>0 || yaki_prob < exp(kaizen/tt) ){
    // if(kaizen>0){
        for(EdgeUpdateInfo &eui : edge_cands){
            if(eui.col_row==0 && eui.lr==0)      state.col_streets[eui.ind].add_est_dist(eui.dist_d,0);
            else if(eui.col_row==0 && eui.lr==1) state.col_streets[eui.ind].add_est_dist(eui.dist_d,1);
            else if(eui.col_row==1 && eui.lr==0) state.row_streets[eui.ind].add_est_dist(eui.dist_d,0);
            else if(eui.col_row==1 && eui.lr==1) state.row_streets[eui.ind].add_est_dist(eui.dist_d,1);
            // DEBUG(eui.col_row);
            // DEBUG(eui.lr);
            // DEBUG(tt);
            // DEBUG(t01);
            // DEBUG(kaizen);
            update_gl_from_est_dist(state, eui.col_row, eui.ind, eui.lr);
        }
    }
}

void update_route(State &state, double t01){
    int ind = rand_hw(mt64);
    int col_row = rand_col_row(mt64);
    int lr = rand_lr(mt64);
    ll dist_d = rand_d(mt64);
    if(rand_01(mt64)==0) dist_d*=-1;
    // if(rand_percent(mt64)<0.95) dist_d*=-1;
    
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
        edge_cnt+=change_cnt;
    }
    if(edge_cnt==0) return;

    // if(dist_d<0 && kaizen<0 && rand_percent(mt64)<0.2 ){
    //     kaizen = 1;
    // }

    kaizen = kaizen/edge_cnt;
    double T0=1;
    double T1=1;
    double tt=pow(T0,1.0-t01)*pow(T1,t01);
    double yaki_prob = rand_percent(mt64);
    if(kaizen>0 || yaki_prob < exp(kaizen/tt) ){
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


void update_bound2(State &state, double t01){
    int ind = rand_hw(mt64);
    int col_row = rand_col_row(mt64);
    int move = rand_move15(mt64);
    if(rand_01(mt64)==0) move*=-1;
    ll dist_d = rand_d(mt64);
    if(rand_01(mt64)==0) dist_d*=-1;
    
    ll dist_diff = 0;
    if(col_row==0 && move>0){
        dist_diff = state.col_streets[ind].get_dist(-1) - state.col_streets[ind].get_dist(HW+1);
    }
    else if(col_row==0 && move<0){
        dist_diff = state.col_streets[ind].get_dist(HW+1) - state.col_streets[ind].get_dist(-1);
    }
    else if(col_row==1 && move>0){
        dist_diff = state.row_streets[ind].get_dist(-1) - state.row_streets[ind].get_dist(HW+1);
    }
    else if(col_row==1 && move<0){
        dist_diff = state.row_streets[ind].get_dist(HW+1) - state.row_streets[ind].get_dist(-1);
    }

    int left = state.row_streets[ind].bound;
    int right = state.row_streets[ind].bound;
    if(move>0){
        right += move;
    }
    else{
        left += move;
    }

    ll kaizen = 0;
    ll edge_cnt = 0;
    for(RouteInfo &ri : state.routes_info){
        ll est_dist=0;
        ll change_cnt=0;
        ll st_cnt=0;
        for(Edge &ed : ri.edges){
            int y=ed.y, x=ed.x;
            if(ed.dir==0){
                est_dist += state.col_streets[x].get_dist(y);
                if(col_row==0 && ind==x && left<=y && y<right){
                    change_cnt++;
                }
                if(col_row==0 && ind==x){
                    st_cnt++;
                }
            }
            else{
                est_dist += state.row_streets[y].get_dist(x);
                if(col_row==1 && ind==y && left<=x && x<right ){
                    change_cnt++;
                }
                if(col_row==1 && ind==y){
                    st_cnt++;
                }
            }
        }
        ll curr_error = abs(est_dist-ri.dist);
        // ll updated_error = abs(est_dist+change_cnt*dist_diff - ri.dist);
        ll updated_error = abs(est_dist+change_cnt*dist_diff+dist_d*st_cnt - ri.dist);
        kaizen+=(curr_error-updated_error);
        edge_cnt+=change_cnt;
    }
    if(edge_cnt==0) return;

    kaizen = kaizen/edge_cnt;
    double T0=10;
    double T1=1;
    double tt=pow(T0,1.0-t01)*pow(T1,t01);
    double yaki_prob = rand_percent(mt64);
    if(kaizen>0 || yaki_prob < exp(kaizen/tt) ){
        if(col_row==0)  {
            state.col_streets[ind].move_bound(move);
            state.col_streets[ind].add_est_dist(dist_d,0);
            state.col_streets[ind].add_est_dist(dist_d,1);
        }
        else{
            state.row_streets[ind].move_bound(move);
            state.row_streets[ind].add_est_dist(dist_d,0);
            state.row_streets[ind].add_est_dist(dist_d,1);
        }
        // if(move<0) update_gl_from_est_dist(state, col_row, ind, 1);
        // else       update_gl_from_est_dist(state, col_row, ind, 0);
        update_gl_from_est_dist(state, col_row, ind, 1);
        update_gl_from_est_dist(state, col_row, ind, 0);
    }
}


void update_bound(State &state, double t01){
    int ind = rand_hw(mt64);
    int col_row = rand_col_row(mt64);
    int move = rand_move15(mt64);
    if(rand_01(mt64)==0) move*=-1;
    
    ll dist_diff = 0;
    if(col_row==0 && move>0){
        dist_diff = state.col_streets[ind].get_dist(-1) - state.col_streets[ind].get_dist(HW+1);
    }
    else if(col_row==0 && move<0){
        dist_diff = state.col_streets[ind].get_dist(HW+1) - state.col_streets[ind].get_dist(-1);
    }
    else if(col_row==1 && move>0){
        dist_diff = state.row_streets[ind].get_dist(-1) - state.row_streets[ind].get_dist(HW+1);
    }
    else if(col_row==1 && move<0){
        dist_diff = state.row_streets[ind].get_dist(HW+1) - state.row_streets[ind].get_dist(-1);
    }

    int left = state.row_streets[ind].bound;
    int right = state.row_streets[ind].bound;
    if(move>0){
        right += move;
    }
    else{
        left += move;
    }

    ll kaizen = 0;
    ll edge_cnt = 0;
    for(RouteInfo &ri : state.routes_info){
        ll est_dist=0;
        ll change_cnt=0;
        for(Edge &ed : ri.edges){
            int y=ed.y, x=ed.x;
            if(ed.dir==0){
                est_dist += state.col_streets[x].get_dist(y);
                if(col_row==0 && ind==x && left<=y && y<right){
                    change_cnt++;
                }
            }
            else{
                est_dist += state.row_streets[y].get_dist(x);
                if(col_row==1 && ind==y && left<=x && x<right ){
                    change_cnt++;
                }
            }
        }
        ll curr_error = abs(est_dist-ri.dist);
        ll updated_error = abs(est_dist+change_cnt*dist_diff - ri.dist);
        kaizen+=(curr_error-updated_error);
        edge_cnt+=change_cnt;
    }
    if(edge_cnt==0) return;

    kaizen = kaizen/edge_cnt;
    double T0=10;
    double T1=1;
    double tt=pow(T0,1.0-t01)*pow(T1,t01);
    double yaki_prob = rand_percent(mt64);
    if(kaizen>0 || yaki_prob < exp(kaizen/tt) ){
        if(col_row==0)  state.col_streets[ind].move_bound(move);
        else            state.row_streets[ind].move_bound(move);
        // if(move<0) update_gl_from_est_dist(state, col_row, ind, 1);
        // else       update_gl_from_est_dist(state, col_row, ind, 0);
        update_gl_from_est_dist(state, col_row, ind, 1);
        update_gl_from_est_dist(state, col_row, ind, 0);
    }
}



void update_bound_swap(State &state, double t01){
    int ind = rand_hw(mt64);
    int col_row = rand_col_row(mt64);
    ll l2r = state.col_streets[ind].get_dist(HW+1) - state.col_streets[ind].get_dist(-1);
    ll r2l = l2r*(-1);

    ll kaizen = 0;
    ll edge_cnt = 0;
    for(RouteInfo &ri : state.routes_info){
        ll est_dist=0;
        ll diff = 0;
        for(Edge &ed : ri.edges){
            int y=ed.y, x=ed.x;
            if(ed.dir==0){
                est_dist += state.col_streets[x].get_dist(y);
                int lr = state.col_streets[x].check_lr(y);
                if(col_row==0 && ind==x && lr==0){
                    diff += l2r; edge_cnt++;
                }
                if(col_row==0 && ind==x && lr==1){
                    diff += r2l; edge_cnt++;
                }
            }
            else{
                est_dist += state.row_streets[y].get_dist(x);
                int lr = state.row_streets[y].check_lr(x);
                if(col_row==1 && ind==y && lr==0){
                    diff += l2r; edge_cnt++;
                }
                if(col_row==1 && ind==y && lr==1){
                    diff += r2l; edge_cnt++;
                }
            }
        }
        ll curr_error = abs(est_dist-ri.dist);
        ll updated_error = abs(est_dist+diff - ri.dist);
        kaizen+=(curr_error-updated_error);
    }
    if(edge_cnt==0) return;

    kaizen = kaizen/edge_cnt;
    double T0=10;
    double T1=1;
    double tt=pow(T0,1.0-t01)*pow(T1,t01);
    double yaki_prob = rand_percent(mt64);
    if(kaizen>0 || yaki_prob < exp(kaizen/tt) ){
        if(col_row==0)  {
            state.col_streets[ind].add_est_dist(l2r,0);
            state.col_streets[ind].add_est_dist(r2l,1);
        }
        else{
            state.row_streets[ind].add_est_dist(l2r,0);
            state.row_streets[ind].add_est_dist(r2l,1);
        }
        update_gl_from_est_dist(state, col_row, ind, 1);
        update_gl_from_est_dist(state, col_row, ind, 0);
    }
}



void DEBUG_GL_OUTPUT(State &state, double t01){
    // double r1 = 1.0-0.3*t01;
    // double r1 = 1.0;
    double r1 = 0.0;
    double r2 = 1.0-r1;
    vector<vector<ll>> hl(HW, vector<ll>(HW-1,0));
    vector<vector<ll>> wl(HW-1, vector<ll>(HW,0));
    for(int y=0; y<HW ; y++){
        for(int x=0; x<HW-1; x++){
            hl[y][x] = state.grid_gl[get_pos_num(y,x)].edges[3].second *r1;
            hl[y][x] += state.grid_gl_v2[get_pos_num(y,x)].edges[3].second *r2;
            cerr << hl[y][x] << " ";
        }
        cerr << endl;
    }
    for(int y=0; y<HW-1 ; y++){
        for(int x=0; x<HW; x++){
            wl[y][x] = state.grid_gl[get_pos_num(y,x)].edges[1].second *r1;
            wl[y][x] += state.grid_gl_v2[get_pos_num(y,x)].edges[1].second *r2;
            cerr << wl[y][x] << " ";
        }
        cerr << endl;
    }
}


void DEBUG_DIFF_OUTPUT(State &state){
    vector<vector<ll>> hl(HW, vector<ll>(HW-1,0));
    vector<vector<ll>> wl(HW-1, vector<ll>(HW,0));
    ll diff_sum = 0;
    for(int y=0; y<HW ; y++){
        ll diff = abs(state.row_streets[y].est_dist_l - state.row_streets[y].est_dist_r);
        diff_sum += diff;
    }
    for(int x=0; x<HW ; x++){
        ll diff = abs(state.col_streets[x].est_dist_l - state.col_streets[x].est_dist_r);
        diff_sum += diff;
    }
    cerr << "diff: " << diff_sum/(HW*2) <<endl;
}

ll get_lr_diff(State &state){
    vector<vector<ll>> hl(HW, vector<ll>(HW-1,0));
    vector<vector<ll>> wl(HW-1, vector<ll>(HW,0));
    ll diff_sum = 0;
    for(int y=0; y<HW ; y++){
        ll diff = abs(state.row_streets[y].est_dist_l - state.row_streets[y].est_dist_r);
        diff_sum += diff;
    }
    for(int x=0; x<HW ; x++){
        ll diff = abs(state.col_streets[x].est_dist_l - state.col_streets[x].est_dist_r);
        diff_sum += diff;
    }
    // cerr << "diff: " << diff_sum/(HW*2) <<endl;
    return diff_sum/(HW*2);
}


void update_edges_from_moveres(State &state, MoveRes move_res){
    int step = move_res.route.size();
    // ll ave_dist = move_res.true_dist / step;

    // ll used_dist = (move_res.dist*0.8+move_res.g2_dist*0.2);
    ll used_dist = move_res.dist;
    ll ave_dist = move_res.true_dist / step;


    ll update_dist = (move_res.true_dist - used_dist)/step;
    // ll update_dist = (move_res.true_dist-move_res.g2_dist)/step;

    // double contribute = 1.0/step;
    // double contribute = 2.0;
    // double contribute = 0.5;
    double contribute = 1.0;
    // contribute*=contribute;
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
        edge_info.use_cnt++;
        edge_info.est_dist += contribute*update_dist;
        edge_info.est_dist = max(min_dist,edge_info.est_dist);
        edge_info.est_dist = min(max_dist,edge_info.est_dist);

        // edge_info.use_cnt++;
        // edge_info.dist_sum += ave_dist;
        // edge_info.curr_ave_dist = edge_info.dist_sum/edge_info.use_cnt;

        state.grid_gl_v2[pos].edges[eind] = { state.grid_gl_v2[pos].edges[eind].first, edge_info.est_dist}; 
        // state.grid_gl_v2[pos].edges[eind] = { state.grid_gl_v2[pos].edges[eind].first, (edge_info.est_dist*0.8+edge_info.curr_ave_dist*0.2) }; 


        int n_pos;
        int n_dir;
        if(eind==0){ n_pos=pos-HW; n_dir=1; }
        if(eind==1){ n_pos=pos+HW; n_dir=0; }
        if(eind==2){ n_pos=pos-1; n_dir=3; }
        if(eind==3){ n_pos=pos+1; n_dir=2; }
        EdgeInfo &edge_info2 = state.grid_gl_v2[n_pos].edges_info[n_dir];
        edge_info2.use_cnt++;
        edge_info2.est_dist += contribute*update_dist;
        edge_info2.est_dist = max(min_dist,edge_info2.est_dist);
        edge_info2.est_dist = min(max_dist,edge_info2.est_dist);

        // edge_info2.use_cnt++;
        // edge_info2.dist_sum += ave_dist;
        // edge_info2.curr_ave_dist = edge_info2.dist_sum/edge_info2.use_cnt;

        // state.grid_gl_v2[n_pos].edges[n_dir] = { state.grid_gl_v2[n_pos].edges[n_dir].first, (edge_info2.est_dist*0.8+edge_info2.curr_ave_dist*0.2) }; 
        state.grid_gl_v2[n_pos].edges[n_dir] = { state.grid_gl_v2[n_pos].edges[n_dir].first, edge_info2.est_dist}; 
    }
}


void update_edges_from_moveres2(State &state, MoveRes move_res){
    int step = move_res.route.size();
    ll ave_dist = move_res.true_dist / step;
    // DEBUG(ave_dist);
    vector<P> used_pos_edges; // P: {pos, edge(0~3)}

    int py=move_res.sy, px=move_res.sx;
    for(char dir : move_res.route){
        used_pos_edges.push_back({get_pos_num(py,px), get_dir_num(dir)});
        if(dir=='U') py--;
        else if(dir=='D') py++;
        else if(dir=='L') px--;
        else px++;
    }

    for(auto &[pos,eind] : used_pos_edges){
        EdgeInfo &edge_info = state.grid_gl_v2[pos].edges_info[eind];
        edge_info.use_cnt++;
        edge_info.dist_sum += ave_dist;
        edge_info.est_dist = edge_info.dist_sum/edge_info.use_cnt;
        edge_info.est_dist+=500;
        state.grid_gl_v2[pos].edges[eind] = { state.grid_gl_v2[pos].edges[eind].first, edge_info.est_dist}; 

        int n_pos;
        int n_dir;
        if(eind==0){ n_pos=pos-HW; n_dir=1; }
        if(eind==1){ n_pos=pos+HW; n_dir=0; }
        if(eind==2){ n_pos=pos-1; n_dir=3; }
        if(eind==3){ n_pos=pos+1; n_dir=2; }
        EdgeInfo &edge_info2 = state.grid_gl_v2[n_pos].edges_info[n_dir];
        edge_info2.use_cnt++;
        edge_info2.dist_sum += ave_dist;
        edge_info2.est_dist = edge_info2.dist_sum/edge_info2.use_cnt;
        edge_info2.est_dist+=500;

        state.grid_gl_v2[n_pos].edges[n_dir] = { state.grid_gl_v2[n_pos].edges[n_dir].first, edge_info2.est_dist}; 
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


void update_streets_from_moveres_2(State &state, MoveRes move_res, bool update_all=false, double rate=1.0){
    int step = move_res.route.size();
    // ll ave_dist = move_res.true_dist / step;


    // ll used_dist = (move_res.dist*0.8+move_res.g1_dist*0.2);
    ll used_dist = move_res.dist;
    // ll used_dist = move_res.g1_dist;
    ll update_dist = (move_res.true_dist-used_dist)/step;
    // ll update_dist = (move_res.true_dist-move_res.g1_dist)/step;

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
            int lr = state.col_streets[px].check_lr(py);
            if(lr==0 || update_all) col_move_cnts_l[px]+=1;
            if(lr==1 || update_all) col_move_cnts_r[px]+=1;
        }
        else{
            int lr = state.row_streets[py].check_lr(px);
            if(lr==0 || update_all) row_move_cnts_l[py]+=1;
            if(lr==1 || update_all) row_move_cnts_r[py]+=1;
        }
        if(dir=='U') py--;
        else if(dir=='D') py++;
        else if(dir=='L') px--;
        else px++;
    }
    // DEBUG(move_res.true_dist);
    // DEBUG(move_res.dist);
    // DEBUG(update_dist);
    for(int y=0 ; y<HW ; y++){
        StreetInfo &street = state.row_streets[y];
        if(row_move_cnts_l[y] > 0){
            double contribute = (1.0) * row_move_cnts_l[y] / step;
            // contribute*=contribute;
            // contribute*=contribute; contribute*=2; 
            // contribute+=0.5; contribute*=contribute; 
            // street.est_dist_l = street.est_dist_l+update_dist*contribute;
            street.add_est_dist(update_dist*contribute*rate, 0);
        }
        if(row_move_cnts_r[y] > 0){
            double contribute = (1.0) * row_move_cnts_r[y] / step;
            // contribute*=contribute;
            // contribute*=contribute; contribute*=2; 
            // contribute+=0.5; contribute*=contribute; 
            // street.est_dist_r = street.est_dist_r+update_dist*contribute*rate;
            street.add_est_dist(update_dist*contribute*rate, 1);
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
            // contribute*=contribute;
            // contribute*=contribute; contribute*=2; 
            // contribute+=0.5; contribute*=contribute; 
            // street.est_dist_l = street.est_dist_l+update_dist*contribute*rate;
            street.add_est_dist(update_dist*contribute*rate, 0);
        }
        if(col_move_cnts_r[x] > 0){
            double contribute = (1.0) * col_move_cnts_r[x] / step;
            // contribute*=contribute;
            // contribute*=contribute; contribute*=2; 
            // contribute+=0.5; contribute*=contribute; 
            // street.est_dist_r = street.est_dist_r+update_dist*contribute*rate;
            street.add_est_dist(update_dist*contribute*rate, 1);
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


// const double street_rate = 0.8;
// double edge_rate = 1.0-street_rate;
MoveRes get_shortest_path_from_grid(State &state, vector<Edge4d> &gl, vector<Edge4d> &gl2, int sy, int sx, int ty, int tx, double t01){
    // TODO: ここのパラメータチューニング
    // if(t01<0.3)t01=0.0;
    // t01*=t01;
    const double street_rate = 1.0-0.3*t01;
    double edge_rate = 1.0-street_rate;
    
    int n = HW*HW;
    vector<ll> d(n,INF);
    vector<ll> d_g1(n,INF);
    vector<ll> d_g2(n,INF);
    vector<ll> d_real(n,INF);
    vector<int> prev_vl(n, -1); // 経路復元用
    int start = get_pos_num(sy,sx);
    int goal = get_pos_num(ty,tx);
    priority_queue<P, vector<P>, greater<P>> q;

    d[start] = 0;
    d_g1[start] = 0;
    d_g2[start] = 0;
    d_real[start] = 0;
    q.push(P(0,start));

    while(!q.empty()){
        auto [dist, v] = q.top(); q.pop();
        if(v == goal) break;
        if( d[v] < dist ) continue;
        // for( auto& [next_v, cost] : gl[v].edges){
        for(int dir : {0,1,2,3}){
            int next_v = gl[v].edges[dir].first;
            // int cost = gl[v].edges[dir].second;
            int use_cnt = state.grid_gl_v2[v].edges_info[dir].use_cnt;
            double g2_rate = min(edge_rate, 5.0*use_cnt/100);
            double g1_rate = 1.0-g2_rate;
            // int cost = (gl[v].edges[dir].second*g1_rate + gl2[v].edges[dir].second*g2_rate);
            int cost1 = gl[v].edges[dir].second;
            int cost2 = gl2[v].edges[dir].second;
            int cost_real = cost1*g1_rate + cost2*g2_rate;
            // int cost = (-1)*(cost_real-8000)*(cost_real-8000)/8000 + 8000;
            int cost = cost_real;
            // int cost = cost_real;
            // int cost = (gl[v].edges[dir].second*street_rate + gl2[v].edges[dir].second*edge_rate);
            // int cost_real = (gl[v].edges[dir].second*street_rate + gl2[v].edges[dir].second*edge_rate);
            // int cost = cost_real*rand_yuragi(mt64);
            if(next_v == -1)continue;
            if( d[next_v] > d[v] + cost ){
                d[next_v] = d[v] + cost;
                d_g1[next_v] = d_g1[v] + cost1;
                d_g2[next_v] = d_g2[v] + cost2;
                d_real[next_v] = d_real[v]+cost_real;
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
    res.dist = d_real[goal];
    // res.dist = d[goal];
    res.g1_dist = d_g1[goal];
    res.g2_dist = d_g2[goal];
    // DEBUG(res.dist); DEBUG(res.g1_dist); DEBUG(res.g2_dist);
    // res.dist = dreal[goal];
    res.route = route_str;
    res.sy=sy; res.sx=sx; res.ty=ty; res.tx=tx;
    return res;
}





// MoveRes get_shortest_path_from_grid(vector<Edge4d> &gl, int sy, int sx, int ty, int tx){
//     int n = HW*HW;
//     vector<ll> d(n,INF);
//     vector<int> prev_vl(n, -1); // 経路復元用
//     int start = get_pos_num(sy,sx);
//     int goal = get_pos_num(ty,tx);
//     priority_queue<P, vector<P>, greater<P>> q;

//     d[start] = 0;
//     q.push(P(0,start));

//     while(!q.empty()){
//         auto [dist, v] = q.top(); q.pop();
//         if(v == goal) break;
//         if( d[v] < dist ) continue;
//         for( auto& [next_v, cost] : gl[v].edges){
//             if(next_v == -1)continue;
//             if( d[next_v] > d[v] + cost ){
//                 d[next_v] = d[v] + cost;
//                 prev_vl[next_v] = v;
//                 q.push(P(d[next_v], next_v));
//             }
//         }
//     }

//     // 経路復元
//     vector<int> route = {goal};
//     string route_str = "";
//     int curr_v = goal;
//     while(true){
//         int prev_v = prev_vl[curr_v];
//         if(prev_v == -1) break;
//         route.push_back(prev_v);

//         int dirnum = curr_v - prev_v;
//         if(dirnum == (-1)*HW) route_str += "U";
//         else if(dirnum == HW) route_str += "D";
//         else if(dirnum == -1) route_str += "L";
//         else route_str += "R";

//         curr_v = prev_v;
//     }
//     reverse(ALL(route_str));
//     MoveRes res;
//     res.dist = d[goal];
//     res.route = route_str;
//     res.sy=sy; res.sx=sx; res.ty=ty; res.tx=tx;
//     return res;
// }



string get_search_route(int sy, int sx, int ty, int tx){
    char row_c;
    if(sx<tx) row_c = 'R';
    else row_c = 'L';
    
    string first_cols = "";
    if(sy<ty) first_cols = string(ty-sy,'D');
    else first_cols = string(sy-ty,'U');

    string second_cols = "";
    if(sy<ty) second_cols = string(ty-sy,'U');
    else second_cols = string(sy-ty,'D');

    string route = first_cols;
    for(int i=0 ; i<abs(tx-sx) ; i++){
        if(i%2==0) {
            route += row_c;
        }
        else {
            route += second_cols;
            route += row_c;
            route += first_cols;
        }
    }
    return route;
}

string get_simple_path(int sy, int sx, int ty, int tx){
    string res = "";
    if(sx<tx) res += string(tx-sx,'R');
    else res += string(sx-tx,'L');

    if(sy<ty) res += string(ty-sy,'D');
    else res += string(sy-ty,'U');

    return res;
}


string get_simple_path2(int sy, int sx, int ty, int tx, int dir){
    string res = "";
    if(dir==0){
        int move1 = abs(tx-sx)/2;
        int move2 = abs(tx-sx)-move1;

        if(sx<tx) res += string(move1,'R');
        else res += string(move1,'L');

        if(sy<ty) res += string(ty-sy,'D');
        else res += string(sy-ty,'U');

        if(sx<tx) res += string(move2,'R');
        else res += string(move2,'L');

        return res;
    }
    else{
        int move1 = abs(ty-sy)/2;
        int move2 = abs(ty-sy)-move1;

        if(sy<ty) res += string(move1,'D');
        else res += string(move1,'U');

        if(sx<tx) res += string(tx-sx,'R');
        else res += string(sx-tx,'L');

        if(sy<ty) res += string(move2,'D');
        else res += string(move2,'U');

        return res;
    }

}

ll get_route_dist(State &state, int sy, int sx, int ty, int tx, string route){
    int py=sy, px=sx;
    ll dist = 0;
    for(char dir : route){
        if(dir=='U') {
            dist += state.grid_gl[get_pos_num(py,px)].edges[0].second;
            py--;
        }
        else if(dir=='D') {
            dist += state.grid_gl[get_pos_num(py,px)].edges[1].second;
            py++;
        }
        else if(dir=='L') {
            dist += state.grid_gl[get_pos_num(py,px)].edges[2].second;
            px--;
        }
        else if(dir=='R') {
            dist += state.grid_gl[get_pos_num(py,px)].edges[3].second;
            px++;
        }
    }
    return dist;
}


// TODO: get_simple_pathをちょっと遠回り。
// ダイクストラで、最初の方は、なるべく直線（曲がりを少なく）する？（直進の場合のコストを少しさげる？）
void solve(){
    TimeManager tm;
    State state;
    //
    //
    const int output_per=10;
    const int search_cnt=50;
    state.search_cnt = search_cnt;
    // const int update_start=150;
    const int update_start=150;
    // const int update_start=0;
    // cerr << QUERY_N/output_per << endl;
    REP(i,QUERY_N){
        ll sy,sx,ty,tx;
        cin>>sy>>sx>>ty>>tx;

        // double t01 = (1.0)*(i-update_start)/(QUERY_N-update_start);
        double t01 = (1.0)*i/QUERY_N;

        MoveRes res; 
        if(i<search_cnt){
            string route;
            route = get_simple_path(sy,sx,ty,tx);
            // if(i<0)route = get_simple_path(sy,sx,ty,tx);
            // else route = get_simple_path2(sy,sx,ty,tx,i%2);
            // route = get_simple_path2(sy,sx,ty,tx,0);
            // if(i<10) route = get_search_route(sy,sx,ty,tx);
            // else route = get_simple_path(sy,sx,ty,tx);
            // string route = get_search_route(sy,sx,ty,tx);
            ll dist = get_route_dist(state,sy,sx,ty,tx,route);
            res.sy=sy; res.sx=sx, res.ty=ty, res.tx=tx;
            res.dist=dist;
            res.route=route;
        }
        else{
            res = get_shortest_path_from_grid(state, state.grid_gl, state.grid_gl_v2, sy,sx,ty,tx, t01);
        }

        cout << res.route << endl;
        ll true_dist; cin>>true_dist;
        res.true_dist = true_dist;
        // DEBUG(true_dist);
        // DEBUG(i);
        state.update_routes_info(res);

        bool flag = false;
        if(rand_percent(mt64)<0.0) flag=true;
        update_streets_from_moveres_2(state, res, flag, 1.0);
        update_edges_from_moveres(state, res);

        // 時間切れなら更新なし
        // if(!tm.check(1950.0, true)) continue;
        // if(!tm.check(8500.0, true)) continue;

        // update_edges_from_moveres2(state, res);

    
        // update_streets_from_moveres_2(state, res, false, 1.0);

        if(i==200){
            ll diff = get_lr_diff(state);
            const ll good_diff = 850;
            if(diff<good_diff){
                state.remove_bound();
                for(int ind=0;ind<HW;ind++){
                    update_gl_from_est_dist(state, 0, ind, 0);
                    update_gl_from_est_dist(state, 1, ind, 0);
                }
            }
            // DEBUG(diff);
        }
        if(i==300 && state.use_bound){
            ll diff = get_lr_diff(state);
            const ll good_diff = 1000;
            if(diff<good_diff){
                state.remove_bound();
                for(int ind=0;ind<HW;ind++){
                    update_gl_from_est_dist(state, 0, ind, 0);
                    update_gl_from_est_dist(state, 1, ind, 0);
                }
            }
            // DEBUG(diff);
        }
        if(i==400 && state.use_bound){
            ll diff = get_lr_diff(state);
            const ll good_diff = 1100;
            if(diff<good_diff){
                state.remove_bound();
                for(int ind=0;ind<HW;ind++){
                    update_gl_from_est_dist(state, 0, ind, 0);
                    update_gl_from_est_dist(state, 1, ind, 0);
                }
            }
            // DEBUG(diff);
        }

        if(i>update_start){
            // int loop = 25-(1.0-t01)*5;
            int loop = 30-t01*10;
            // int loop = 30;
            if(!state.use_bound) loop+=5;
            REP(j,loop){
                int mode=0;
                double p = rand_percent(mt64);
                // if(p<0.25) mode=0;
                if(p<0.0) mode=0;
                // else if(p<0.6) mode=1;
                else mode=2;
                update_route2(state, t01, mode);
                // update_route(state, t01);
            }
            // loop = 15-(1.0-t01)*10;
            if(state.use_bound){
                loop = 5;
                REP(j,loop){
                    // if(rand_percent(mt64)<0.6) update_bound(state, t01);
                    // else update_bound2(state, t01);
                    update_bound(state, t01);
                }
                // loop = 2;
                // REP(j,loop){
                //     update_bound_swap(state, t01);
                // }
            }
        }

        // DEBUG(i);
        if(i%output_per==0){
            // DEBUG_GL_OUTPUT(state, t01);
        }
        //
        // if(i%100==0) DEBUG_DIFF_OUTPUT(state);
    }
    // DEBUG_GL_OUTPUT(state, 1.0);
    // DEBUG_DIFF_OUTPUT(state);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}