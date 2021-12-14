/*
    [memo]
    ENDは1ずらす？
    time_s_vegs は、valの降順にソート？
    近くにあるやつはできるだけとりたい。get_best_veg の 評価関数の設定が大事。これがバグってそう
    行くついでにとりたい。経路単位で最適を探したい（時間で区切って、ここを時間使う？）。

    タイミングがあってないバグがある。
    目指したますに生まれるのが1つさき。

    同じところに固まりがち。いい感じに動けるように。
    3*3の塊とかいらない。そういった塊から優先してとる。

    近い未来のその地点の価値、を考慮する？
    その地点周辺の機械の少なさ、も考慮する
*/

#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
    // typedef pair<ll,ll> P;
    typedef pair<int,int> P;
    typedef tuple<int,int,P> TUPLE;
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

mt19937_64 mt64(0);
uniform_int_distribution<int> rand_col_row(0, 1);
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

enum Dir { ROW = 0, COL, };
vector<P> dir4={{-1,0},{1,0},{0,-1},{0,1}};

/* const */
int N=16;
int M=5000;
int T=1000;

/* args? */
int MAX_MACHINE=45;

/* -------------------- struct -------------------- */

struct Veg{
    int y,x,start,end,val;
    bool remained=true; // 野菜が収穫されずにまだ残っているか。
    Veg(int y, int x, int start, int end, int val)
    : y(y),x(x),start(start),end(end),val(val){}
    Veg():y(-1),x(-1),start(-1),end(-1),val(-1),remained(false){}
    bool operator<( const Veg& right ) const {
        return val>right.val;
    }
};

struct Section{
    int y,x;
    int machine_ind = -1; // machines index. -1: no machine on it
    vector<Veg> vegs;
    int veg_ind=0; // 今いるor次にくるvegのind。時間に応じてこれが変わる。advance_time()で変更。
    Section(){}
    Section(int y, int x) : y(y),x(x){}
    int get_val(int time){ // いまある野菜のvalをget
        if(veg_ind>=vegs.size()) return 0;
        if(time<vegs[veg_ind].start) return 0;
        if(!vegs[veg_ind].remained) return 0;
        return vegs[veg_ind].val;
    }
    Veg get_veg(int time){
        Veg veg;
        int c_ind=veg_ind;
        while(c_ind<vegs.size()){
            if(vegs[c_ind].end<time) c_ind++;
            else break;
            // DEBUG(time); DEBUG(vegs[c_ind].end);
        }
        if(c_ind>=vegs.size()) return veg;
        if(time<=vegs[c_ind].start) return veg;
        if(!vegs[c_ind].remained) return veg;
        return vegs[c_ind];
    }
    int do_harvest_now(int now){
        int val=get_val(now);
        if(val>0){
            vegs[veg_ind].remained=false;
            return val;
        }
        return 0;
    }
};

enum EventType { START = 0, END, };
struct Event{
    int time;
    EventType et;
    Veg veg;
    Event(int time, EventType et, Veg veg) : time(time), et(et), veg(veg){}
    bool operator<( const Event& right ) const {
        if(time==right.time){ // ENDが先にくる（ENDは後ろに1ずらしている）
            if(et==END) return true;
            else return false;
        }
        return time<right.time;
    }
};

struct Machine{
    int y,x;
    int ind;
    Machine(){}
    Machine(int y, int x, int ind) : y(y),x(x),ind(ind){}
};

enum ActionType { MOVE = 0, BUY, NOTHING };
struct Action{
    ActionType at;
    int y=-1, x=-1;
    int to_y=-1, to_x=-1;
    Action(ActionType at, int y, int x, int to_y, int to_x): at(at), y(y),x(x),to_y(to_y),to_x(to_x){}
    Action(ActionType at, int y, int x): at(at), y(y),x(x){}
    Action(ActionType at): at(at){}
};


struct State{
    vector<vector<Section>> grid;
    vector<Machine> machines;
    vector<Action> actions;
    vector<vector<Veg>> time_s_vegs; // start ごとに分けた vegたち (startのeventとみなす)
    vector<vector<Veg>> time_e_vegs; // end ごとに分けた vegたち（endのeventとみなす）

    int time=0;
    int event_ind=0; // 次くるeventのind。 
    int money=1;
    
    bool add_machine(int y, int x){
        if(grid[y][x].machine_ind!=-1) {
            stringstream ss; 
            ss<<"[add_machine] MACHINE ALREADY EXISTS: " << y << " " << x << endl;
            DEBUG(ss.str());
            return false;
        }
        int machine_ind=machines.size();
        Machine machine(y,x,machine_ind);
        machines.push_back(machine);
        grid[y][x].machine_ind=machine_ind;
        return true;
    }

    bool move_machine(int from_y, int from_x, int to_y, int to_x){
        if(grid[from_y][from_x].machine_ind==-1){
            stringstream ss; 
            ss<<"[move_machine] NO MACHINE HERE: " << from_x << " " << from_x << endl;
            DEBUG(ss.str());
            return false;
        }
        if(grid[to_y][to_x].machine_ind!=-1){
            stringstream ss; 
            ss<<"[move_machine] MACHINE ALREADY EXISTS: " << to_y << " " << to_x << endl;
            DEBUG(ss.str());
            return false;
        }
        int from_ind=grid[from_y][from_x].machine_ind;
        grid[from_y][from_x].machine_ind=-1;
        grid[to_y][to_x].machine_ind=from_ind;
        machines[from_ind].y=to_y; machines[from_ind].x=to_x;
        return true;
    }

    int get_connected_machine_cnt(int y, int x){
        int mn=machines.size();
        vector<bool> vis(mn,false);
        deque<int> q;
        int start=grid[y][x].machine_ind;
        q.push_back(start); vis[start]=true;
        int res=0;
        while(!q.empty()){
            res++;
            int poped=q.front(); q.pop_front();
            Machine &mc=machines[poped];
            int cy=mc.y, cx=mc.x;
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;
                int mi=grid[yy][xx].machine_ind;
                if(mi==-1) continue;
                if(vis[mi]) continue;
                q.push_back(mi);
                vis[mi]=true;
            }
        }
        return res;
    }

    int get_machine_price(){
        int x=machines.size();
        return (x+1)*(x+1)*(x+1);
    }

    int do_harvest(){
        int vsum=0;
        for(Machine &mc:machines){
            int y=mc.y, x=mc.x;
            int val=grid[y][x].do_harvest_now(time);
            if(val>0){
                vsum+=val*get_connected_machine_cnt(y,x);
            }
        }
        return vsum;
    }

    void advance_time(){ 
        /*
            1. 現時刻のeventのうち END のものを処理（veg_indを進める）
            2. 現時刻のeventのうち START のものを処理（???）
            3. Actionを処理
            4. 収穫 　
        */
        if(time>=T) return;

        for(Veg &veg:time_e_vegs[time]){
            int y=veg.y;
            int x=veg.x;
            grid[y][x].veg_ind+=1;
        }
        for(Veg &veg:time_s_vegs[time]){
        }

        Action &ac=actions[time];
        // DEBUG(ac.at);DEBUG(time);
        if(ac.at==NOTHING) {}
        if(ac.at==BUY){
            int price = get_machine_price();
            money-=price;
            add_machine(ac.y, ac.x);
            // TODO: エラー処理
        }
        else if(ac.at==MOVE){
            move_machine(ac.y, ac.x, ac.to_y, ac.to_x);
        }
        int veg_vals=do_harvest();
        money+=veg_vals;
        time++;
    }

    // 距離が近い方を優先したいがための係数
    int dist_coef(int d, bool use_far_dist=false){
        // if(time>750) {
        //     if(d==0) return machines.size();
        //     return machines.size()/(d+2);
        // }
        if(!use_far_dist){
            if(d==0) return machines.size();
            return machines.size()/d;
        }
        else{ //あえて遠くを狙う
            return d;
        }

        int v=max((int)machines.size()-d, 1);
        // return v* (4.0)*T/(time+T) ;
        // return v*pow(2,(4.0)*T/(time+T));
        return pow(v, (4.0)*T/(time+T) )/100;
    }

    int count_around_machines(int y, int x){w
        int cnt=0;
        for(int dy:{-2,-1,0,1,2}){for(int dx:{-2,-1,0,1,2}){
            int yy=y+dy, xx=x+dx;
            if(yy<0||yy>=N||xx<0||xx>=N) {
                // cnt++;
                continue;
            }
            if(grid[yy][xx].machine_ind!=-1) cnt++;
        }}
        return cnt;
    }

    int eval_target_veg(Veg &veg, int c_time, int dist, bool use_far_dist=false){
        int dc=dist_coef(dist, use_far_dist);
        int yoyu=veg.end-(c_time+dist); // 消えるまでどれくらい余裕があるか
        int yoyu_c=30-yoyu; // もうすぐ消えそうなやつは評価高め
        int y=veg.y, x=veg.x;
        int res=0;
        res+=veg.val*8;
        for(int dy:{-1,0,1}){for(int dx:{-1,0,1}){
        // for(auto &[dy,dx]:dir4){
        // for(int dy:{-2,-1,0,1,2}){for(int dx:{-2,-1,0,1,2}){
            int yy=y+dy, xx=x+dx;
            if(yy<0||yy>=N||xx<0||xx>=N) continue;
            // res+=get_future_val(yy,xx,c_time+dist,3)/5;
            // if(abs(dy)+abs(dx)>=2)continue;
            res+=grid[yy][xx].get_val(c_time+dist+abs(dy)+abs(dx));
            res+=grid[yy][xx].get_val(c_time+dist+abs(dy)+abs(dx)+5)/10;
        // }
        }}   
        // return res*dc*pow(yoyu_c,1.5);

        // int around_machine_coef=10-count_around_machines(y,x);
        // around_machine_coef=max(around_machine_coef,1);
        return res*dc*yoyu_c;
    }
    

    int get_future_val(int y, int x, int c_time, int time_d){
        return grid[y][x].get_val(c_time+time_d);
    }

    // 次の最適なルートを返す
    vector<P> get_best_veg_2(int c_time){
        Veg veg(-1,-1,-1,-1,-1);
        int mn=machines.size();
        vector<vector<TUPLE>> dist(N, vector<TUPLE>(N, {-1,-1,{-1,-1}} )); // <dist, val, 前の点(Pair)>

        deque<P> q;
        for(Machine &mc:machines){
            dist[mc.y][mc.x]={0, 0, {-1,-1} };
            q.push_back({mc.y,mc.x});
        }
        bool use_far_dist=false;
        while(!q.empty()){
            auto &[cy,cx]=q.front(); q.pop_front();
            auto &[c_d, c_val, c_prev_yx]=dist[cy][cx];
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;

                auto &[d,val,prev_yx]=dist[yy][xx];
                if(d!=-1 && c_d+1>d) continue;

                bool first_vis=true;
                if(c_d+1==d) first_vis=false;

                // if(time==816 && yy==11 && xx==0){
                //     DEBUG(c_time+c_d+1);
                //     DEBUG(grid[yy][xx].get_val(c_time+c_d+1));
                // }
                // int c_veg_val=grid[yy][xx].get_val(c_time+c_d);
                Veg c_veg=grid[yy][xx].get_veg(c_time+c_d);
                int c_veg_val = max(c_veg.val,0);
                // int yoyu=c_veg.end-(c_time+c_d);
                // c_veg_val*=(20-yoyu);
                // int c_veg_val = 0;
                // if(c_veg.val>0){
                //     c_veg_val=eval_target_veg(c_veg, c_time, c_d, use_far_dist);
                // }


                // if(813<=c_time && c_time<=815 && yy==14 && xx==4){
                //     DEBUG(yy);
                //     DEBUG(xx);
                //     DEBUG(c_time+c_d);
                //     DEBUG(grid[yy][xx].get_val(c_time+c_d));
                // }  

                if(c_val+c_veg_val>val){
                    dist[yy][xx]={c_d+1, c_val+c_veg_val, {cy,cx}};
                }
                if(first_vis) q.push_back({yy,xx});
            }
        }


        P best_yx={-1,-1};
        int best_val=-1;

        REP(y,N){
            REP(x,N){
                auto &[c_d, c_val, c_prev_yx]=dist[y][x];
                if(c_d<=0) continue;

                Veg c_veg=grid[y][x].get_veg(c_time+ max(c_d-1,0) );
                if(c_veg.val<=0) continue;

                int eval_val=eval_target_veg(c_veg, c_time, c_d, use_far_dist);
                // int eval_coef = eval_val/c_veg.val;
                // int vv = eval_coef*c_val;
                int vv= (c_val-c_veg.val) + eval_val;
                // int vv=c_val/max(c_d+5,1);
                // vv/=max(c_d+5,1);
                if(vv>best_val){
                    best_yx={y,x};
                    best_val=vv;
                }
            }
        }
        if(best_yx.first==-1){
            return {};
        }

        vector<P> res={best_yx};
        int cy=best_yx.first, cx=best_yx.second;
        while(true){
            auto &[c_d, c_val, c_prev_yx]=dist[cy][cx];
            cy=c_prev_yx.first;
            cx=c_prev_yx.second;
            if(cy==-1)break;
            res.push_back({cy,cx});
        }
        // res.pop_back(); // 最後は出発点


        reverse(ALL(res));
        //         if(810<=c_time && c_time<=815){
        //     DEBUG(c_time);
        //     DEBUG(res);
        // }
        return res;
    }


    Veg get_best_veg(int c_time){
        // if(820<=c_time && c_time<=830)DEBUG("-----");
        Veg veg(-1,-1,-1,-1,-1);
        int best_val=-1;
        int mn=machines.size();
        vector<vector<int>> dist(N, vector<int>(N,-1));
        deque<P> q;
        for(Machine &mc:machines){
            dist[mc.y][mc.x]=0;
            q.push_back({mc.y,mc.x});
        }
        bool use_far_dist=false;
        // if(rand_percent(mt64)<0.00){
        //     use_far_dist=true;
        // }
        while(!q.empty()){
            auto &[cy,cx]=q.front(); q.pop_front();
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;
                if(dist[yy][xx]!=-1) continue;
 
                int c_dist=min(dist[cy][cx]+1, mn);
                Veg c_veg=grid[yy][xx].get_veg(c_time+c_dist-1);
 
                if(c_veg.val>0){
                    int c_val=eval_target_veg(c_veg, c_time, c_dist, use_far_dist);
                    if( best_val < c_val){
                        veg=c_veg;
                        best_val=c_val;
                    }
                }
                q.push_back({yy,xx});
                dist[yy][xx]=c_dist;
            }
        }
        // DEBUG(c_time);
        // DEBUG(best_val);
        return veg;
    }

    void shuffle_machine(){
        shuffle(ALL(machines), mt64);
        REP(new_ind,machines.size()){
            Machine &mc=machines[new_ind]; 
            int old_ind=mc.ind;
            grid[mc.y][mc.x].machine_ind=new_ind;
            mc.ind=new_ind;
        }
    }

    // (y,x)にあるマシンから近い順のリストで連結したマシンの(y,x)を返す
    vector<P> get_machines_by_order(int y, int x){
        int mn=machines.size();
        vector<bool> vis(mn,false);
        deque<int> q;
        vector<P> res={{y,x}};
        int start=grid[y][x].machine_ind;
        q.push_back(start); vis[start]=true;
        while(!q.empty()){
            int poped=q.front(); q.pop_front();
            Machine &mc=machines[poped];
            int cy=mc.y, cx=mc.x;
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;
                int mi=grid[yy][xx].machine_ind;
                if(mi==-1) continue;
                if(vis[mi]) continue;
                q.push_back(mi);
                res.push_back({yy,xx});
                vis[mi]=true;
            }
        }
        return res;
    }

    bool judge_connection(int start_mi, vector<int> &not_mis){
        int mn=machines.size();
        vector<bool> vis(mn,false);
        for(int mi:not_mis){
            vis[mi]=true;
        }
        deque<int> q;
        q.push_back(start_mi); vis[start_mi]=true;
        int cnt=0;
        while(!q.empty()){
            cnt++;
            int poped=q.front(); q.pop_front();
            Machine &mc=machines[poped];
            int cy=mc.y, cx=mc.x;
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;
                int mi=grid[yy][xx].machine_ind;
                if(mi==-1) continue;
                if(vis[mi]) continue;
                q.push_back(mi);
                vis[mi]=true;
            }
        }
        if(cnt==machines.size()-not_mis.size()) return true;
        else return false;
    }

    // (y,x)にあるマシンから近い順のリストで連結したマシンの(y,x)を返す
    // 十字の塊の中央のmachineは、優先的にとる。
    vector<P> get_machines_by_order_2(int y, int x){
        int mn=machines.size();
        int start=grid[y][x].machine_ind;
        vector<bool> vis(mn,false);
        deque<int> q;
        vector<P> res={{y,x}};
        vector<P> res_back={};
        
        for(Machine &mc:machines){
            int cy=mc.y, cx=mc.x;
            int cnt=0;
            // for(auto &[dy,dx]:dir4){
            for(int dy:{-1,0,1}){for(int dx:{-1,0,1}){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) cnt++;
                else if(grid[yy][xx].machine_ind!=-1) cnt++;
            }}
            if(cnt==9){
                int mi=mc.ind;
                if(mi==start) continue;
                vis[mi]=true;
                res_back.push_back({cy,cx});
            }
        }

        q.push_back(start); vis[start]=true;
        while(!q.empty()){
            int poped=q.front(); q.pop_front();
            Machine &mc=machines[poped];
            int cy=mc.y, cx=mc.x;
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;
                int mi=grid[yy][xx].machine_ind;
                if(mi==-1) continue;
                if(vis[mi]) continue;
                q.push_back(mi);
                res.push_back({yy,xx});
                vis[mi]=true;
            }
        }
        for(P yx:res_back){
            res.push_back(yx);
        }
        return res;
    }


    vector<P> get_machines_by_order_3(int y, int x){
        int mn=machines.size();
        int start=grid[y][x].machine_ind;

        vector<P> mis;
        for(Machine &mc:machines){
            double cnt=0;
            int y=mc.y, x=mc.x;
            // for(int dy:{-1,0,1}){for(int dx:{-1,0,1}){
            for(int dy:{-2,-1,0,1,2}){for(int dx:{-2,-1,0,1,2}){
                // if(abs(dy)+abs(dx)>2)continue;
                int yy=y+dy, xx=x+dx;
                if(yy<0||yy>=N||xx<0||xx>=N) {
                    cnt+=1.0;
                    continue;
                }
                if(grid[yy][xx].machine_ind!=-1) cnt+=1.0;
                if(grid[yy][xx].machine_ind!=-1 && abs(dy)+abs(dx)==1) cnt+=1.0;
                if(abs(dy)+abs(dx)<=2 && grid[yy][xx].get_val(time+100)>750) cnt-=2;
            }}
            // if(grid[y][x].get_val(time+20)>700) cnt-=10;
            mis.push_back({(int)cnt,mc.ind});
        }
        sort(ALL(mis), greater<P>{});

        vector<bool> vis(mn,false);
        deque<int> q;
        vector<P> res={{y,x}};
        vector<P> res_back={};
        vector<int> not_mis={};
        for(auto &[v_,mi]:mis){
            Machine &mc=machines[mi];
        // for(Machine &mc:machines){
            if(start==mc.ind) continue;
            not_mis.push_back(mc.ind);
            bool ret=judge_connection(start, not_mis);
            if(!ret){
                not_mis.pop_back();
            }
            else{
                res_back.push_back({mc.y, mc.x});
                vis[mc.ind]=true;
            }
        }

        // DEBUG(not_mis);

        q.push_back(start); vis[start]=true;
        while(!q.empty()){
            int poped=q.front(); q.pop_front();
            Machine &mc=machines[poped];
            int cy=mc.y, cx=mc.x;
            for(auto &[dy, dx]:dir4){
                int yy=cy+dy, xx=cx+dx;
                if(yy<0||N<=yy||xx<0||N<=xx) continue;
                int mi=grid[yy][xx].machine_ind;
                if(mi==-1) continue;
                if(vis[mi]) continue;
                q.push_back(mi);
                res.push_back({yy,xx});
                vis[mi]=true;
            }
        }
        reverse(ALL(res_back));
        for(P yx:res_back){
            res.push_back(yx);
        }
        return res;
    }


    void output_actions(){
        REP(i,T){
        // for(Action &ac:actions){
            Action &ac=actions[i];
            if(ac.at==NOTHING) cout<<-1<<'\n';
            else if(ac.at==BUY){
                cout<<ac.y<<" "<<ac.x<<'\n';
            }
            else if(ac.at==MOVE){
                cout<<ac.y<<" "<<ac.x<<" "<<ac.to_y<<" "<<ac.to_x<<'\n';
            }
        }
    }

    void DEBUG_VEG_OUTPUT(){
        cout<<"s,e,v,used"<<endl;
        REP(y,N){
            REP(x,N){
                vector<Veg> &vegs=grid[y][x].vegs;
                for(Veg &veg:vegs){
                    int used=1;
                    if(veg.remained) used=0;
                    cout<<veg.start<<","<<veg.end<<","<<veg.val<<","<<used<<'\n';
                }
            }
        }
    }
};
State state; // global
/* -------------------- struct -------------------- */




void DEBUG_GRID(){
    REP(y,N){
        REP(x,N){
            cout<<state.grid[y][x].get_val(state.time)<<" ";
        }
        cout<<endl;
    }
}

void valid_machines(){
    REP(i, state.machines.size()){
        Machine &mac=state.machines[i];
        int y=mac.y, x=mac.x;
        if(state.grid[y][x].machine_ind!=i){
            stringstream ss; 
            ss<<"[valid_machines] ERROR: " << i << endl;
            DEBUG(ss.str()); 
        }
    }
}

/* 最初の8円を集める */
int first_solve(){
    int csum=0;
    int cy=0, cx=0;
    int time=0;
    REP(i,T){
        time++;
        if(!state.time_s_vegs[i].empty()){
            Veg &veg=state.time_s_vegs[i][0];
            if(csum==0) {
                state.actions[i]=Action(BUY,veg.y,veg.x);
                cy=veg.y, cx=veg.x;
            }
            else {
                state.actions[i]=Action(MOVE,cy,cx,veg.y,veg.x);
                cy=veg.y, cx=veg.x;
            }
            csum+=veg.val;
            if(csum>=8) break;
        }
    }
    return time;
}

// /* 2台目購入 ~ 27円まで */
// int second_solve(){
// }

Machine get_nearest_machine(int y, int x){
    Machine res;
    int dist=10000;
    for(Machine &mc:state.machines){
        int d=abs(mc.y-y)+abs(mc.x-x);
        if(d<dist){
            dist=d;
            res=mc;
        }
    }
    return res;
}

int sig(int v){
    if(v<0) return -1;
    // if(v==0) return 0;
    else return 1;
}

void DEBUG_MACHINE(){
    cerr<<"car"<<endl;
    for(Machine &mc:state.machines){
        cerr<<mc.y<<" "<<mc.x<<endl;
    }
}



/* machine が少ないうちの戦略。マシンは（遠くにワープしている最中を除いて）常に連結！ */
bool flip=false;
int mini_solve(){
    // ターゲットのvegを決定
    int c_time=state.time;
    Veg target_veg=state.get_best_veg(c_time);
    if(target_veg.y<0){
        return 1;
    }
    // その野菜から最も近いmachine
    Machine kiten_mc=get_nearest_machine(target_veg.y, target_veg.x);
    // その距離（端点含む）
    int dx=target_veg.x-kiten_mc.x;
    int dy=target_veg.y-kiten_mc.y;
    int dist=abs(dy)+abs(dx)+1;
    // if(dist==0){
    //     DEBUG(dist);
    // }
    // DEBUG(dist);
    // if(state.time>650){
    // DEBUG(kiten_mc.y);
    // DEBUG(kiten_mc.x);

    // DEBUG(target_veg.y);
    // DEBUG(target_veg.x);}
    // DEBUG(target_veg.val);

    // y方向、x方向のどちらから伸ばすか（できるだけまっすぐしたい）
    int con_x=0;
    int cx=kiten_mc.x;
    while(cx>=0){
        if(state.grid[kiten_mc.y][cx].machine_ind==-1)break;
        con_x++;
        cx--;
    }
    cx=kiten_mc.x;
    while(cx<N){
        if(state.grid[kiten_mc.y][cx].machine_ind==-1)break;
        con_x++;
        cx++;
    }
    int con_y=0;
    int cy=kiten_mc.y;
    while(cy>=0){
        if(state.grid[kiten_mc.y][cy].machine_ind==-1)break;
        con_y++;
        cy--;
    }
    cy=kiten_mc.y;
    while(cy<N){
        if(state.grid[kiten_mc.y][cy].machine_ind==-1)break;
        con_y++;
        cy++;
    }

    if(con_y==con_x && rand_percent(mt64)<0.5){
        con_x++;
    }

    // このマシンを後ろからとっていけば、連結が維持される
    // vector<P> mc_yxs=state.get_machines_by_order(kiten_mc.y, kiten_mc.x);
    // vector<P> mc_yxs=state.get_machines_by_order_2(kiten_mc.y, kiten_mc.x);
    vector<P> mc_yxs=state.get_machines_by_order_3(kiten_mc.y, kiten_mc.x);
    // DEBUG(kiten_mc.y);
    // DEBUG(kiten_mc.x);
    // DEBUG(mc_yxs);

    if(state.machines.size()<MAX_MACHINE && state.money>=state.get_machine_price()){
        mc_yxs.push_back({-1,-1}); // 新しいmachine
    }

    if(dist==0){ //止まる
        state.actions[c_time]=Action(NOTHING);
        return 1;
    }

    if(dist<=mc_yxs.size()){
        int cy=kiten_mc.y, cx=kiten_mc.x;
        int mi=mc_yxs.size()-1;
        int sigy=sig(dy);
        int sigx=sig(dx);
        if(con_y>=con_x){
            REP(i,abs(dy)){
                cy+=sigy;
                if(mc_yxs[mi].first==-1) state.actions[c_time]=Action(BUY, cy, cx);
                else {
                    state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, cy, cx);
                }
                mi--; c_time++;
            }
            REP(i,abs(dx)){
                cx+=sigx;
                if(mc_yxs[mi].first==-1) state.actions[c_time]=Action(BUY, cy, cx);
                else {
                    state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, cy, cx);
                }
                mi--; c_time++;
            }   
        }
        else{
            REP(i,abs(dx)){
                cx+=sigx;
                if(mc_yxs[mi].first==-1) state.actions[c_time]=Action(BUY, cy, cx);
                else {
                    state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, cy, cx);
                }
                mi--; c_time++;
            }   
            REP(i,abs(dy)){
                cy+=sigy;
                if(mc_yxs[mi].first==-1) state.actions[c_time]=Action(BUY, cy, cx);
                else {
                    state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, cy, cx);
                }
                mi--; c_time++;
            }
        }
    }
    else{
        dist=mc_yxs.size();
        int cy=target_veg.y, cx=target_veg.x;
        int sigx=sig(N/2-cx), sigy=sig(N/2-cy);
        int dx=(dist-1)/2;
        int dy=dist-1-dx;

        // DEBUG(dy);
        // DEBUG(dx);
        // DEBUG(mc_yxs.size());
        // DEBUG(state.machines.size());

        int mi=mc_yxs.size()-1;
        REP(i,dy){
            // DEBUG(c_time);

            cy+=sigy;
            if(mc_yxs[mi].first==-1) state.actions[c_time]=Action(BUY, cy, cx);
            else state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, cy, cx);
            mi--; c_time++;
        }
        REP(i,dx){
            cx+=sigx;
            if(mc_yxs[mi].first==-1) state.actions[c_time]=Action(BUY, cy, cx);
            else state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, cy, cx);
            mi--; c_time++;
        }
        state.actions[c_time]=Action(MOVE, mc_yxs[mi].first, mc_yxs[mi].second, target_veg.y, target_veg.x);
        mi--; c_time++;
    }
    return c_time-state.time;
}


int mini_solve2(){
    // ターゲットのvegを決定
    int c_time=state.time;
    // DEBUG(state.time);

    vector<P> routes=state.get_best_veg_2(c_time);
        if(routes.empty()){ //止まる
        // DEBUG(state.time);
        state.actions[c_time]=Action(NOTHING);
        return 1;
    }
    // if(target_veg.y<0){
    //     return 1;
    // }
    // DEBUG(routes);
    int ty=routes.back().first;
    int tx=routes.back().second;

    // その野菜から最も近いmachine
    // Machine kiten_mc=get_nearest_machine(ty, tx);
    auto &[sy, sx]=routes.front();
    // このマシンを後ろからとっていけば、連結が維持される
    // vector<P> mc_yxs=state.get_machines_by_order_3(kiten_mc.y, kiten_mc.x);
    vector<P> mc_yxs=state.get_machines_by_order_3(sy,sx);

    if(state.machines.size()<MAX_MACHINE && state.money>=state.get_machine_price()){
        mc_yxs.push_back({-1,-1}); // 新しいmachine
    }



    int msize=mc_yxs.size();
    // DEBUG(msize);
    REP(i, routes.size()-1){
        int moved_mi=msize-i-1;
        int cy=mc_yxs[moved_mi].first;
        int cx=mc_yxs[moved_mi].second; 
        auto &[to_y,to_x]=routes[i+1];
        if(cy==-1) state.actions[c_time+i]=Action(BUY, to_y, to_x);
        else {
            state.actions[c_time+i]=Action(MOVE, cy,cx, to_y,to_x);
        }
    }
    // DEBUG(routes.size());
    return routes.size()-1;
}


void init_state(){
    cin >> N >> M >> T;

    vector<vector<Section>> grid(N, vector<Section>(N));
    REP(y,N){REP(x,N){ grid[y][x].y=y; grid[y][x].x=x; }}
    state.grid=grid;

    vector<vector<Veg>> time_s_vegs(T);
    vector<vector<Veg>> time_e_vegs(T+2);

    REP(i,M){
        int r,c,s,e,v;
        cin >> r >> c >> s >> e >> v;
        Veg veg(r,c,s,e,v);
        // if(s>800 && v<300) continue;
        state.grid[r][c].vegs.push_back(veg);
        time_s_vegs[s].push_back(veg);
        time_e_vegs[e+1].push_back(veg);
    }

    REP(i,T){
        sort(ALL(time_s_vegs[i]));
    }

    vector<Action> actions(T+100,Action(NOTHING));
    state.actions=actions;
    state.time_s_vegs=time_s_vegs;
    state.time_e_vegs=time_e_vegs;
}




void solve(){
    TimeManager tm;
    init_state(); // 10ms

    // state.actions[0]=Action(BUY,5,5);
    // state.actions[1]=Action(BUY,5,6);
    // state.actions[2]=Action(BUY,6,5);
    // state.advance_time();
    // state.advance_time();
    // state.advance_time();
    // DEBUG(state.get_machines_by_order_3(6,5));

    // return;

    int first_time=first_solve();

    State state_orig=state;
    int mmax_orig=MAX_MACHINE;
    vector<Action> ans;
    int best_val=0;
    int best_mm=0;
    // T=50;
    REP(loop,20){
        if(loop%2==0) MAX_MACHINE=mmax_orig+(loop/2);
        else MAX_MACHINE=mmax_orig-(loop/2);
        state=state_orig;
        REP(i,first_time){
            state.advance_time();
        }

        bool flag=true;
        while(state.time<T){
            // DEBUG("---");
            // DEBUG(state.time);
            // DEBUG_MACHINE();
            // if(rand_percent(mt64)<0.3)state.shuffle_machine();
            // if(flag&&state.machines.size()==MAX_MACHINE){
            //     flag=false;
            //     DEBUG(MAX_MACHINE);
            //     DEBUG(state.time);
            // }
            // state.shuffle_machine();
            int dt;
            if(state.time<900){
                // if(state.time>650) {DEBUG(state.time);}
                dt=mini_solve();
            }
            else{
                dt=mini_solve2();
            }
            REP(i,dt){
                state.advance_time();
            }
        }
        if(best_val<state.money){
            best_val=state.money;
            ans=state.actions;
            best_mm=MAX_MACHINE;
        }

    }
    state.actions=ans;
    DEBUG(best_val);
    DEBUG(best_mm);
    // DEBUG(state.money);


    // double TL = 2800.0;
    // while(tm.check(TL)){
    //     double t01 = tm.get_time()/TL;
    // }
    state.output_actions();
    // state.DEBUG_VEG_OUTPUT();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}