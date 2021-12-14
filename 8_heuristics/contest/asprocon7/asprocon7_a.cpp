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
    vector<vector<int>> tl;
    vector<P> tl_sum;
    vector<int> xl; // 各workerの"長さ"に変換。 1-ind. 0は投入前の仮想ベルト（長さ=T*carN）
    vector<int> nl;
    vector<int> nl_orig;
    bool sample=false; // 試作品あり？

    vector<vector<int>> pair_costs;
    vector<vector<int>> pair_costs_2;
    vector<vector<double>> pair_costs_comp;
    
    // 現在位置の計算用
    vector<int> car_first_pos;
    vector<int> xl_pos;
    int move=0;
    vector<P> pos_manager; 

    bool belt=true; // move or stop
    int time; // current time
    vector<P> yk; // car point (何番目のworker, そのworkerの先頭からの距離)
    vector<vector<int>> rkj; // progress
    // vector<int> workers_c_car; // 各workerの作業中のcar. ない時は-1
    vector<deque<int>> workers_car_q; // 各workerのcarのqueue. 
    vector<deque<int>> workers_task_car_q; // 各workerの、作業中の carのqueue. 

    int finished_car_num=0;
    vector<int> cars; // output

    vector<int> cars_mini_1;
    vector<int> cars_mini_2;

    vector<int> bad_cars;
};

/* global vars */
State state;
int M; // num of car types (20 or 40)
int S; // num of workers (40 or 80)
int T; // (= 60) car-input interval 
int L; // time limit (T*1000)
int N=0; // sum of n (= 1000)。 ヤバイglobal変数にしてしまった。後で直す。

/* params (updated by command-line args) */
int MINI_PART=20;
double T0=15.0;
double T1=0.0;
double FIRST_MINI_RATE = 0.95;

int SYOSU_DIV = 3;

const double TL = 20000.0;
// const double TL = 1850.0;



void DEBUG_QUEUE(vector<deque<int>> vq){
    DEBUG("q");
    for(auto q:vq){
        for(int v:q) cout<<v<<" ";
        cout<<endl;
    }
}


void init_pos_manager(){
    state.xl[0]=(T*(N-1)+1); // 0... 投入前ベルト
    state.pos_manager.clear();
    int xi=0;
    for(int x: state.xl){
        REP(i,x){
            state.pos_manager.push_back({xi,i});
        }
        xi++;
    }
}


P get_xi_pos2(int car_i){
    int pos=state.car_first_pos[car_i]+state.move;
    pos+=state.xl[0];
    // DEBUG(state.xl[0]);
    // DEBUG(pos);
    if(pos>=state.pos_manager.size()){
        return {S+1,0};
    }
    else{
        return state.pos_manager[pos];
    }
}

// TODO: xlを1-indに。0は投入前のベルトをおく。
void init_sim(){
    vector<P> yk(N);
    vector<int> car_first_pos(N);
    // int belt0_len=(N-1)*T;
    REP(i,N){
        yk[i]={0,T*(N-1-i)};
        car_first_pos[i]=(-1)*T*i-1;
    }
    // DEBUG(car_first_pos);
    vector<vector<int>> rkj(N, vector<int>(S+1,0));
    vector<deque<int>>  workers_car_q(S+1);
    vector<deque<int>>  workers_task_car_q(S+1);

    REP(i,N) workers_car_q[0].push_back(i);
    workers_task_car_q[0].push_back(0);
    
    state.belt=true;
    state.time=0;
    state.yk=yk;
    state.car_first_pos=car_first_pos;
    state.rkj=rkj;
    state.workers_car_q=workers_car_q;
    state.workers_task_car_q=workers_task_car_q;
    state.finished_car_num=0;
    state.bad_cars.clear();

    state.move=0;
}

enum BeltState{
    WITHOUT_MOVE = 0, 
    WITH_MOVE,
};

struct Event{
    int time_d;
    BeltState belt;
    Event(int time_d, BeltState belt):time_d(time_d),belt(belt){}
};


P get_xi_pos(int car_i){
    int pos=state.car_first_pos[car_i]+state.move;

    auto iter2 = upper_bound(ALL(state.xl_pos), pos);
    int ind2 = iter2 - state.xl_pos.begin();
    if( iter2 == state.xl_pos.end() ){
        ind2 = S+1;
    }
    // int val2 = *iter2;
    if(ind2==0){
        return {0, pos+state.xl[0]};
    }
    else{
        // DEBUG(state.xl_pos);
        // DEBUG(ind2);
        int prev_val=state.xl_pos[ind2-1];
        int dist=pos-prev_val;
        return {ind2, dist};
    }
}


int aaa=0;
int b=0;
Event get_next_event_time(bool debug=false){
    const int inf=1000000;
    int min_time=1000000;
    
    int min_end_but_remain=inf;
    int min_task_done=inf;
    int min_next_belt=inf;

    for(deque<int> &car_q : state.workers_car_q){
        if(car_q.empty()) continue;
        int car_i=car_q.front();
        // DEBUG(car_i);
        // auto [xi, car_pos] = state.yk[car_i]; // どのworkerのどの地点にいるか
        auto [xi, car_pos] = get_xi_pos2(car_i); // どのworkerのどの地点にいるか
        if(debug){DEBUG(car_i); DEBUG(car_pos);}

        int car_type=state.cars[car_i];
        int dist_to_end=state.xl[xi]-1-car_pos; // そのworkerの最後の地点に行くまでの距離
        int rem_work_time=state.tl[car_type][xi]-state.rkj[car_i][xi];
        // DEBUG(dist_to_end);

        // if(dist_to_end==0 && rem_work_time>0) {DEBUG(dist_to_end); DEBUG(rem_work_time);}
        if(dist_to_end<rem_work_time){
            min_end_but_remain=min(min_end_but_remain, dist_to_end);
            state.bad_cars.push_back(car_i);
        }
        if(rem_work_time>0){
            min_task_done=min(min_task_done, rem_work_time);
        }
        min_next_belt=min(min_next_belt, dist_to_end+1);
    }

    if(min_end_but_remain==0){ // 今ベルト停止中なら
        // aaa++;
        return Event(min_task_done, WITHOUT_MOVE);
        // return min_task_done; // 動かないまま、いずれかのタスクが終わるまでの時間
    }
    else{ // いずれかが未完了で終点 or いずれかの先頭タスク完了 or いずれかが次のworker
        // b++;
        // int res_time = min({min_end_but_remain, min_task_done, min_next_belt});
        int res_time = min({min_end_but_remain, min_next_belt});
        return Event(res_time, WITH_MOVE);
    }
}

bool forward_time(Event event, bool debug=false){
    int time_d=event.time_d;
    state.time+=time_d;
    if(state.time>=L-1){ // time-up
        return false;
    }
    
    if(debug) {DEBUG(event.belt);DEBUG(event.time_d);DEBUG_QUEUE(state.workers_car_q); DEBUG_QUEUE(state.workers_task_car_q);}

    if(event.belt==WITHOUT_MOVE){
        for(int xi=1; xi<=S; xi++){
            deque<int> &car_q = state.workers_task_car_q[xi];
            if(car_q.empty()) continue;
            int time_rem=time_d;
            while(!car_q.empty() && time_rem>0){
                int car_i=car_q.front();
                int car_type=state.cars[car_i];
                int need=state.tl[car_type][xi]-state.rkj[car_i][xi];
                if(need<time_rem){
                    state.rkj[car_i][xi]+=need;
                    car_q.pop_front();
                    time_rem-=need;
                }
                else{
                    state.rkj[car_i][xi]+=time_rem;
                    time_rem=0;
                }
            }
        }
    }
    else{
        if(debug) DEBUG("here");
        vector<P> next_cars;
        for(deque<int> &car_q : state.workers_car_q){
            if(car_q.empty()) continue;
            int car_i=car_q.front();
            if(debug){
                DEBUG(car_i);
                DEBUG(time_d);
            }
            auto [xi, car_pos] = get_xi_pos2(car_i); // どのworkerのどの地点にいるか

            int car_type=state.cars[car_i];
            int dist_to_end=state.xl[xi]-1-car_pos; // そのworkerの最後の地点に行くまでの距離
            int rem_work_time=state.tl[car_type][xi]-state.rkj[car_i][xi];

            if(dist_to_end<time_d){ // 次のworkerへ。前のタスク進捗はもう不要。
                car_q.pop_front();
                int next_xi=xi+1;
                if(next_xi==S+1) { // 終わり
                    state.finished_car_num++;
                    continue; 
                }
                next_cars.push_back({next_xi,car_i});
            }

        }
        // タスク進行の更新
        for(int xi=1; xi<=S; xi++){
            deque<int> &car_q2 = state.workers_task_car_q[xi];
            if(car_q2.empty()) continue;
            int time_rem=time_d;
            while(!car_q2.empty() && time_rem>0){
                int car_i=car_q2.front();
                int car_type=state.cars[car_i];
                int need=state.tl[car_type][xi]-state.rkj[car_i][xi];
                if(need<time_rem){
                    state.rkj[car_i][xi]+=need;
                    car_q2.pop_front();
                    time_rem-=need;
                }
                else{
                    state.rkj[car_i][xi]+=time_rem;
                    time_rem=0;
                }
            }
        }

        // 次のworkerに行った車のqueue移動
        for(auto &[next_xi, car_i]:next_cars){
            state.workers_car_q[next_xi].push_back(car_i);
            state.workers_task_car_q[next_xi].push_back(car_i);
        }

        state.move+=time_d;

    }
    return true;
}

void DEBUG_STATE(){
    // return;
    DEBUG(state.cars);
    DEBUG("-----");
    reverse(ALL(state.yk));
    DEBUG(state.yk);
    reverse(ALL(state.yk));
    // DEBUG("yk");
    // REP(i,N){
        // DEBUG(get_xi_pos(i));
    // }
    DEBUG(state.rkj);
    DEBUG(state.time);
}

void simulate(bool debug=false){
    // init_sim();
    // DEBUG_STATE();
    int cnt=0;
    while(state.finished_car_num<N){
        Event next_event=get_next_event_time(debug);
        bool ret = forward_time(next_event,debug);
        // DEBUG(state.time);
        // DEBUG_STATE();
        if(debug) DEBUG_STATE();
        // if((cnt++)%10==0) DEBUG_STATE();
        if(!ret)break;
        // DEBUG(cnt++);
        cnt++;
    }
    // DEBUG(cnt);
}

void make_initial_cars(){
    state.cars.clear();
    vector<int> cars_rem=state.nl;
    if(state.nl_orig[M-1]==1){
        state.cars.push_back(M-1);
        cars_rem[M-1]--;
    }
    REP(i,N){
        double max_v=0.0;
        int max_i=0;
        REP(j,M){
            double rate=(1.0)*cars_rem[j]/state.nl[j];
            if(rate>max_v){
                max_v=rate;
                max_i=j;
            }
        }
        cars_rem[max_i]--;
        state.cars.push_back(max_i);
    }
}

void make_initial_cars2(){
    state.cars.clear();
    vector<double> bads(M);
    double best=0.0;
    REP(i,M){
        double worst=10000;
        REP(j,S){
            double d=state.xl[j+1]-state.tl[i][j+1];
            worst=min(worst,d);
        }
        DEBUG(worst);
        best=max(best,worst);
        bads[i]=worst;
    }

    REP(i,M){
        bads[i]/=best;
        bads[i]*=bads[i];
    }

    vector<int> cars_rem=state.nl;
    REP(i,N){
        double max_v=0.0;
        int max_i=0;
        REP(j,M){
            double rate=(1.0)*cars_rem[j]/state.nl[j];
            rate*=bads[j];
            if(rate>max_v){
                max_v=rate;
                max_i=j;
            }
        }
        cars_rem[max_i]--;
        state.cars.push_back(max_i);
    }
}


void make_initial_cars3(){
    state.cars.clear();
    vector<int> cars_rem=state.nl;
    bool top=true;
    int cnt=0;
    REP(i,N){
        REP(j,M){
            int ind;
            // if(top) ind=j;
            if(cnt!=2) ind=j;
            else ind=M-j-1;
            auto [tsum, car_i] = state.tl_sum[ind];
            if(cars_rem[car_i]>0){
                cars_rem[car_i]--;
                state.cars.push_back(car_i);
                break;
            }
        }
        cnt++;
        cnt%=3;
        top = !top;
    }
}

void make_initial_cars4(){
    vector<int> rems=state.nl;
    state.cars.clear();
    int curr_pos=M-1;
    rems[curr_pos]--;
    bool flag=false;
    state.cars.push_back(curr_pos);
    REP(loop_,1000){
        int min_d=1000000;
        int min_i=-1;
        REP(i,M){
            int ind=i;
            if(flag) ind=M-1-i;
            int d=state.pair_costs[curr_pos][ind];
            if(d<min_d && rems[ind]>0){
                min_d=d;
                min_i=ind;
            }
        }
        if(min_i!=-1){
            rems[min_i]--;
            curr_pos=min_i;
            state.cars.push_back(curr_pos);
        }
        flag = !flag;
    }
    return;
}


void swap_cars(int u, int v){
    int tmp=state.cars[u];
    state.cars[u]=state.cars[v];
    state.cars[v]=tmp;
}

void reverse_cars(int u, int v){
    reverse(state.cars.begin()+u, state.cars.begin()+v+1);
}

void insert_cars(int u, int v){
    int poped=state.cars[u];
    state.cars.erase(state.cars.begin()+u);
    state.cars.insert(state.cars.begin()+v, poped);
}


enum CarOp {SWAP = 0, REVERSE, INSERT, SWAP2};

int try_update(double tt, uniform_int_distribution<int> &rand_mini_n){
    int prev_time=state.time;

    double yaki_prob = rand_percent(mt64);
    double prob=rand_percent(mt64);

    int u,v, u2,v2;
    CarOp op;
    u=rand_mini_n(mt64);
    v=rand_mini_n(mt64);

    u2=rand_mini_n(mt64);
    v2=rand_mini_n(mt64);

    if(prob<0.4){
        op=SWAP;
        swap_cars(u,v);
    }
    else if(prob<=0.7){
        op=REVERSE;
        reverse_cars(u,v);
    }
    else{
        op=SWAP2;
        swap_cars(u,v);
        swap_cars(u2,v2);
        // op=INSERT;
        // insert_cars(u,v);
    }

    init_sim();
    simulate();
    int kaizen=prev_time-state.time;
    if(kaizen>0 || yaki_prob < exp(kaizen/tt)){
        return true;
    }
    else{
        if(op==SWAP) swap_cars(u,v);
        if(op==REVERSE) reverse_cars(u,v);
        if(op==INSERT) insert_cars(v,u);
        if(op==SWAP2){
            swap_cars(u2,v2);
            swap_cars(u,v);
        }
        state.bad_cars.clear();
        state.time=prev_time;
        return false;
    }
}



void solve_mini(TimeManager &tm, int time_limit, int combine=1){
    // 小さくする
    N=0;
    if(combine==1){ // 一つのパーツからなる時。
        REP(i,M){
            // double val=state.nl_orig[i]*(1.0)/MINI_PART;
            // int val2=round(val);
            // if(val2==0) val2=1;
            // state.nl[i]=val2;

            state.nl[i]=(state.nl_orig[i]-1)/MINI_PART +1;
            N+=state.nl[i];

            // state.nl[i]=state.nl[i]/MINI_PART;
            //// state.nl[i]=max(1, state.nl[i]);
            // N+=state.nl[i];
        }
        // make_initial_cars();
        make_initial_cars3();
        // shuffle(ALL(state.cars), mt64);
        init_pos_manager();
    }
    else if(combine==-1){
        N=state.cars.size();
        init_pos_manager();
    }
    else{ // 今のパーツを "combine"個くっつける
        vector<int> cars=state.cars;
        REP(i,combine-1){
            state.cars.insert(state.cars.end(), cars.begin(), cars.end());
        }
        N=state.cars.size();
        init_pos_manager();
    }

    // DEBUG(N);
    // DEBUG(state.cars);


    init_sim();
    simulate();

    // DEBUG(state.time);

    uniform_int_distribution<int> rand_mini_n(0, N-1);
    uniform_int_distribution<int> rand_mini_half(1, N/2-1);
    uniform_int_distribution<int> rand_d(1,5);

    int prev_time=state.time;
    int loop=0;

    // double T0=50;
    // double T1=2;
    int use_bad_cnt=0;
    int use_bad_ok_cnt=0;
    int use_swap_ok_cnt=0;
    int use_reverse_ok_cnt=0;
    int use_insert_ok_cnt=0;
    int ok_cnt=0;

    while(tm.check(time_limit,true)){
    // DEBUG(tm.get_time());
        bool use_bad=false;

        double t01 = tm.get_time()/time_limit;
        double tt=pow(T0,1.0-t01)*pow(T1,t01);
        double yaki_prob = rand_percent(mt64);

        try_update(tt, rand_mini_n);
    }
}


void solve_mini2(TimeManager &tm, int time_limit){
    N=0;
    double syosu_per=1.0/SYOSU_DIV;
    REP(i,M){
        // state.nl[i]=state.nl_orig[i]/MINI_PART;
        // N+=state.nl[i];
        int rem=state.nl_orig[i]%MINI_PART;
        double c_syosu=(1.0)*rem/MINI_PART;
        bool flag=false;
        REP(j,SYOSU_DIV){
            if(c_syosu<(j+1)*syosu_per){
                state.nl[i]=j;
                // state.nl[i]=j+1;
                flag=true;
                break;
            }
        }
        if(!flag) state.nl[i]=SYOSU_DIV-1;
        if(state.nl_orig[i]<MINI_PART && state.nl[i]==0) state.nl[i]=1; // 両方0はNG
        // if(!flag) state.nl[i]=SYOSU_DIV;
        N+=state.nl[i];
    }

    // N=0;
    // REP(i,M){
    //     state.nl[i]=(state.nl_orig[i]-1)/MINI_PART +1;
    //     N+=state.nl[i];
    // }


    // DEBUG(N);
    // DEBUG(state.nl);
    make_initial_cars3();
    // DEBUG(state.cars);
    // DEBUG(N);
    // DEBUG(state.cars.size());
    N=state.cars.size();
    init_pos_manager();

    init_sim();
    simulate();

    // DEBUG(state.time);

    uniform_int_distribution<int> rand_mini_n(0, N-1);
    uniform_int_distribution<int> rand_mini_half(1, N/2-1);
    uniform_int_distribution<int> rand_d(1,5);

    int prev_time=state.time;
    int loop=0;
    double start_time=tm.get_time(true);

    while(tm.check(time_limit,true)){

        double t01 = (tm.get_time()-start_time)/(time_limit-start_time);
        double tt=pow(T0,1.0-t01)*pow(T1,t01);
        double yaki_prob = rand_percent(mt64);

        double prob=rand_percent(mt64);

        int u,v;
        CarOp op;
        u=rand_mini_n(mt64);
        v=rand_mini_n(mt64);

        // int bad_size=state.bad_cars.size();
        // if(bad_size>=2 && rand_percent(mt64)<0.2){
        //     // DEBUG(state.bad_cars);
        //     int uu=state.bad_cars[rand_10e5(mt64)%bad_size];
        //     int vv=state.bad_cars[rand_10e5(mt64)%bad_size];
        //     if(uu!=vv){
        //         u=uu; v=vv;
        //     }
        // }

        if(prob<0.4){
            op=SWAP;
            swap_cars(u,v);
        }
        else if(prob<=0.7){
            op=REVERSE;
            reverse_cars(u,v);
        }
        else{
            op=INSERT;
            insert_cars(u,v);
        }

        init_sim();
        simulate();
        int kaizen=prev_time-state.time;
        if(kaizen>0 || yaki_prob < exp(kaizen/tt)){
            prev_time=state.time;
            // DEBUG(prev_time);
        }
        else{
            if(op==SWAP) swap_cars(u,v);
            if(op==REVERSE) reverse_cars(u,v);
            if(op==INSERT) insert_cars(v,u);
            state.bad_cars.clear();
        }
        loop++;
    }
    // DEBUG(prev_time);
    // int loss=prev_time-(T*(N-1)+state.xl_pos[S]);
    // DEBUG(loss);
}



void solve_mini_half(TimeManager &tm, int time_limit, double rate=0.45){
    // 小さくする
    N=0;
    REP(i,M){
        state.nl[i]=(state.nl_orig[i]-1)/MINI_PART +1;
        N+=state.nl[i];
    }
    // make_initial_cars3();
    make_initial_cars4();
    init_pos_manager();


    vector<int> second_cars;
    REP(i,N/2){
        int poped=state.cars.back() ; state.cars.pop_back();
        second_cars.push_back(poped);
    }
    N=state.cars.size();

    // DEBUG(state.cars);
    // DEBUG(second_cars);

    init_sim();
    simulate();

    uniform_int_distribution<int> rand_mini_n(0, N-1);
    uniform_int_distribution<int> rand_mini_half(1, N/2-1);
    uniform_int_distribution<int> rand_d(1,5);

    int prev_time=state.time;
    int loop=0;

    init_sim();
    simulate();
    double start_time=tm.get_time(true);
    double time_limit_1=time_limit*rate;
    while(tm.check(time_limit_1,true)){
        double t01 = (tm.get_time()-start_time)/(time_limit_1-start_time);
        double tt=pow(T0,1.0-t01)*pow(T1,t01);

        try_update(tt, rand_mini_n);
    }

    // DEBUG(state.cars);

    vector<int> finished_cars_1=state.cars;
    state.cars=second_cars;
    N=state.cars.size();

    // DEBUG(state.time);
    uniform_int_distribution<int> rand_mini_n2(0, N-1);

    start_time=tm.get_time(true);
    double time_limit_2=time_limit*rate*2;
    init_sim();
    simulate();
    while(tm.check(time_limit_2,true)){
        double t01 = (tm.get_time()-start_time)/(time_limit_2-start_time);
        double tt=pow(T0,1.0-t01)*pow(T1,t01);

        try_update(tt, rand_mini_n2);
    }

    // DEBUG(state.cars);

    state.cars.insert(state.cars.end(), finished_cars_1.begin(), finished_cars_1.end());
    N=state.cars.size();
    uniform_int_distribution<int> rand_mini_n3(0, N-1);

    // DEBUG(state.cars);

    init_sim();
    simulate();
    start_time=tm.get_time(true);
    double time_limit_3=time_limit;
    while(tm.check(time_limit_3,true)){
        double t01 = (tm.get_time()-start_time)/(time_limit_3-start_time);
        double tt=pow(T0,1.0-t01)*pow(T1,t01);

        try_update(tt, rand_mini_n3);
    }

    // DEBUG(state.cars);

}




void make_ans(){
    vector<int> cars_rem=state.nl_orig;
    vector<int> all_cars;
    int finish_cnt=0;
    REP(i, MINI_PART+50){
        for(int car : state.cars){
            if(cars_rem[car]>0){
                cars_rem[car]--;
                all_cars.push_back(car);
                if(cars_rem[car]==0) finish_cnt++;
            }
        }
        if(finish_cnt==M) break;
    }
    N=all_cars.size();
    // DEBUG(N);
    state.cars=all_cars;
    // make_initial_cars();
    
    init_pos_manager();
    init_sim();

    simulate();
}

void combine_mini_cars(){
    state.cars.clear();
    state.cars.insert(state.cars.end(), state.cars_mini_2.begin(), state.cars_mini_2.end());
    REP(i,SYOSU_DIV){
        state.cars.insert(state.cars.end(), state.cars_mini_1.begin(), state.cars_mini_1.end());
    }
    N=state.cars.size();
}


void calc_pair_cost(){
    vector<vector<int>> costs(M,vector<int>(M,0));
    state.pair_costs_2=costs;
    REP(i,M){
        REP(j,M){
            vector<int> cars={(int)i,(int)j};
            state.cars=cars;
            N=2;
            init_pos_manager();
            init_sim();
            simulate();
            int cost=state.time-(T*(N-1)+state.xl_pos[S]);
            state.pair_costs_2[i][j]=cost;
        }
    }


    const int COEF=1000;
    // vector<vector<int>> costs(M,vector<int>(M,0));
    state.pair_costs=costs;
    REP(i,M){
        REP(j,M){
            int worst=0;
            int val=0;
            vector<int> vals;
            REP(k,S){
                int si=k+1;
                double r1=(1.0)*state.tl[i][si]/state.xl[si];
                double r2=(1.0)*state.tl[j][si]/state.xl[si];
                int cost=pow(r1*r2,2.5)*COEF;
                vals.push_back(cost);
                worst=max(worst,cost);
                val+=cost;
            }
            sort(ALL(vals), std::greater<>());
            // DEBUG(vals);
            int vsum=0;
            const int CNT=10;
            REP(k,CNT){
                // vsum+=vals[k]*(5-k);
                vsum+=vals[k];
            }
            state.pair_costs[i][j]=vsum/CNT;
            state.pair_costs[i][j]+=(state.pair_costs_2[i][j]-1)*(state.pair_costs_2[i][j]-1)/1000;
            // state.pair_costs[i][j]=worst;
            // state.pair_costs[i][j]=val/S;
        }
    }

    vector<vector<double>> dcosts(M,vector<double>(M,0.0));
    state.pair_costs_comp=dcosts;
    REP(i,M){
        int dsum=0;
        REP(j,M){
            dsum+=state.pair_costs[i][j];
        }
        int d_ave=dsum/M;
        REP(j,M){
            state.pair_costs_comp[i][j]=(1.0)*state.pair_costs[i][j]/d_ave;
        }
    }
    // DEBUG(state.pair_costs);
    // DEBUG(state.pair_costs_2);
}


void make_initial_cars5(){
    vector<int> rems=state.nl;
    int nn=0;
    for(int v:rems)nn+=v;

    state.cars.clear();
    int curr_pos=M-1;
    rems[curr_pos]--;
    bool flag=false;
    state.cars.push_back(curr_pos);
    REP(loop,nn-1){
        double min_d=1000000;
        int min_i=-1;
        REP(i,M){
            int ind=i;
            // if(flag) ind=M-1-i;
            double d=state.pair_costs_comp[ind][curr_pos];
            if(loop>=1){
                if(ind==state.cars[loop-1]) continue;
                // DEBUG(loop);
                // DEBUG(state.cars[loop-1]);
            }
            if(d<min_d && rems[ind]>0){
                min_d=d;
                min_i=ind;
            }
        }
        if(min_i==-1){
            min_i=state.cars[loop-1];
        }
        rems[min_i]--;
        curr_pos=min_i;
        state.cars.push_back(curr_pos);
        flag = !flag;
    }
    return;
}


void solve_like_tsp(TimeManager &tm, double time_limit){ 
    // N=1000;
    // make_initial_cars4();

    N=0;
    REP(i,M){
        // if(state.nl[i]>1000/M){
            // state.nl[i]=state.nl_orig[i]/MINI_PART;
        // }
        // else{
            state.nl[i]=(state.nl_orig[i]-1)/MINI_PART +1;
        // }
        N+=state.nl[i];
    }
    // make_initial_cars4();
    // DEBUG(state.pair_costs_comp);
    make_initial_cars5();
    DEBUG(state.cars);
    init_pos_manager();

    uniform_int_distribution<int> rand_mini_n(1, N-2);
    double start_time=tm.get_time(true);
    double time_limit_2=time_limit*0.5;
    while(tm.check(time_limit_2, true)){
        int a=rand_mini_n(mt64);
        int b=rand_mini_n(mt64);
        if(a>b) swap(a,b);
        int d=a+1;
        int c=b+1;
        int a_car=state.cars[a];
        int b_car=state.cars[b];
        int c_car=state.cars[c];
        int d_car=state.cars[d];
        int c_cost=state.pair_costs[a_car][d_car]+state.pair_costs[b_car][c_car];
        int new_cost=state.pair_costs[a_car][b_car]+state.pair_costs[d_car][c_car];
        // DEBUG(c_cost);

        double t01 = (tm.get_time()-start_time)/(time_limit_2-start_time);
        double tt=pow(T0,1.0-t01)*pow(T1,t01);
        double yaki_prob = rand_percent(mt64);

        int kaizen=c_cost-new_cost;
        if(kaizen>0 || yaki_prob < exp(kaizen/tt)){
            reverse(state.cars.begin()+d, state.cars.begin()+c);
            // int kaizen=c_cost-new_cost;
            // DEBUG(kaizen);
        }

        int a1=rand_mini_n(mt64);
        int b1=rand_mini_n(mt64);
        if(a1>b1) swap(a1,b1);
        int a0=a1-1;
        int a2=a1+1;
        int b0=b1-1;
        int b2=b1+1;
        int a0_car=state.cars[a0];
        int a1_car=state.cars[a1];
        int a2_car=state.cars[a2];
        int b0_car=state.cars[b0];
        int b1_car=state.cars[b1];
        int b2_car=state.cars[b2];
        int c_cost2=0;
        c_cost2+=state.pair_costs[a0_car][a1_car]+state.pair_costs[a1_car][a2_car];
        c_cost2+=state.pair_costs[b0_car][b1_car]+state.pair_costs[b1_car][b2_car];

        int new_cost2=0;
        new_cost2+=state.pair_costs[a0_car][b1_car]+state.pair_costs[b1_car][a2_car];
        new_cost2+=state.pair_costs[b0_car][a1_car]+state.pair_costs[a1_car][b2_car];
        // DEBUG(c_cost);

        t01 = (tm.get_time()-start_time)/(time_limit_2-start_time);
        tt=pow(T0,1.0-t01)*pow(T1,t01);
        yaki_prob = rand_percent(mt64);

        kaizen=c_cost-new_cost;
        if(kaizen>0 || yaki_prob < exp(kaizen/tt)){
            swap_cars(a1,b1);
            // reverse(state.cars.begin()+d, state.cars.begin()+c);
            // int kaizen=c_cost-new_cost;
            // DEBUG(kaizen);
        }
    }

    // DEBUG(state.cars.size());
    init_sim();
    simulate();
    start_time=tm.get_time(true);
    double time_limit_3=time_limit;
    while(tm.check(time_limit_3,true)){
        double t01 = (tm.get_time()-start_time)/(time_limit_3-start_time);
        double tt=pow(T0,1.0-t01)*pow(T1,t01);
        try_update(tt, rand_mini_n);
    }
    // DEBUG(state.cars.size());

}


void solve(){
    TimeManager tm;
    cin>>M>>S>>T>>L;

    if(M==20){
        // MINI_PART*=2;
    }
    // MINI_PART=1000/M;

    REP(i,M){
        int tsum=0;
        vector<int> row(S+1); // 0 は投入前ベルト (必要作業=0)
        row[0]=0;
        REP(j,S) {
            cin>>row[j+1];
            tsum+=row[j+1];
        }
        state.tl_sum.push_back({tsum,i});
        state.tl.push_back(row);
    }
    sort(ALL(state.tl_sum));

    state.xl.push_back(-1); // 0... 投入前ベルト。後で更新
    state.xl_pos.push_back(0);
    int prev_x=0;
    REP(i,S){
        int x; cin>>x; 
        state.xl.push_back(x-prev_x);
        state.xl_pos.push_back(x);
        prev_x=x;
    }

    REP(i,M){
        int n; cin>>n; state.nl.push_back(n);
        N+=n;
    }
    state.nl_orig=state.nl;

    // DEBUG(tm.get_time(true));
    calc_pair_cost();
    solve_like_tsp(tm,TL*1.0);
    // DEBUG(tm.get_time(true));

    // solve_mini(tm, TL*FIRST_MINI_RATE*0.8, 1);
    // solve_mini_half(tm, TL*FIRST_MINI_RATE*2.0, 0.2);
    // solve_mini(tm, TL*FIRST_MINI_RATE*2.0, 1);
    // state.cars_mini_1=state.cars;
    // DEBUG(state.cars.size());
    // DEBUG(state.nl);
    // DEBUG(state.cars);

    // solve_mini2(tm, TL*FIRST_MINI_RATE*2.0);
    // state.cars_mini_2=state.cars;
    // DEBUG(state.cars.size());
    // DEBUG(state.nl);
    // DEBUG(state.cars);

    // combine_mini_cars(); // ここで mini_1 と mini_2 が結合されて state.cars に

    // solve_mini(tm, TL*FIRST_MINI_RATE*3.0, -1);
    // solve_mini(tm, TL, -1); // ここで state.cars が combine個に合体
    make_ans(); // 最終的な答えを作成
    // DEBUG(state.cars);

    cout<<state.finished_car_num<<endl;
    REP(i,state.finished_car_num){
        cout << state.cars[i]+1 << " ";
    }
    // cout<<N<<endl;
    // REP(i,N){
    //     cout << state.cars[i]+1 << " ";
    // }
    cout<<'\n';

    return;
}


int main(int argc, char* argv[]){

    if(argc>=2){
        MINI_PART = atoi(argv[1]);
        T0 = atof(argv[2]);
        T1 = atof(argv[3]);
        FIRST_MINI_RATE = atof(argv[4]);
    }

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}