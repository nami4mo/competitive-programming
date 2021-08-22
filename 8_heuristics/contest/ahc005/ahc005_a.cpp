#include <bits/stdc++.h>
// #include <time.h>
// #include <iomanip>
// #include <iostream>
// #include <map>
// #include <algorithm>
// #include <queue>
// #include <set>
// #include <vector>
// #include <iomanip>
// #include <bitset>
// #include <string>
// #include <random>
// #include <unordered_set>
// // #include <unordered_multiset>
// #include <unordered_map>
// #include <sstream>
// #include <chrono>


// #define PENA 100
int PENA=-100;
int YUGU=5;


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
int N;

mt19937_64 mt64(0);
uniform_int_distribution<int> rand_col_row(0, 1);
uniform_int_distribution<int> rand_lr(0, 1);
uniform_int_distribution<int> rand_lrd(-5, 5);

// uniform_int_distribution<int> rand_n(0, N-1);
uniform_int_distribution<int> rand_c(0, 7);

uniform_int_distribution<int> rand_d(100, 200);
uniform_int_distribution<int> rand_num(0, 1000);
uniform_int_distribution<int> rand_01(0, 1);
uniform_int_distribution<int> rand_move15(1, 2);
uniform_real_distribution<double> rand_percent(0, 1);

enum Dir { HOR = 0, VER, };


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

struct Road{
    Dir dir;
    int sy,sx,gy,gx;
    bool used=false;
    Road(Dir dir, int sy, int sx, int gy, int gx):dir(dir),sy(sy),sx(sx),gy(gy),gx(gx){}
};

struct Point{
    int y,x;
    bool used=false;
    Point(){}
    Point(int y, int x) : y(y),x(x){}
};


struct State{
    vector<string> city;
    vector<Road> roads;
    vector<Point> crosses;
    vector<vector<bool>> hor_used;
    vector<vector<bool>> ver_used;
    vector<vector<int>> road_gl;
    vector<vector<int>> road_dist;
    int y,x;
    int current_road;
    string ans;
    int sy,sx;
    State() : hor_used(N,vector<bool>(N,false)), ver_used(N,vector<bool>(N,false)), road_gl(4*N){}
    bool check_mass(int y, int x){
        if(y<0||y>=N||x<0||x>=N) return false;
        if(city[y][x]=='#') return false;
        return true;
    }
};

bool check_road_cross(Road &rh, Road &rv){
    bool ok=true;
    if(rv.sx<rh.sx || rh.gx<rv.gx ) return false;
    if(rh.sy<rv.sy || rv.gy<rh.gy ) return false;
    return true;
}

Point get_cross(Road &rh, Road &rv){
    // bool ok=true;
    // if(rv.sx<rh.sx || rh.gx<rv.gx ) return false;
    // if(rh.sy<rv.sy || rv.gy<rh.gy ) return false;
    // return true;
    return Point(rh.sy, rv.sx);
}

void check_roads(State &state){
    REP(x,N-1){
        REP(y,N){
            // DEBUG(y);DEBUG(x);
            // DEBUG(state.hor_used[y][x]);
            // DEBUG(state.city[y][x]);
            // DEBUG(state.city[y][x+1]);
            if(state.hor_used[y][x]) continue;
            if(state.city[y][x]=='#') continue;
            if(state.city[y][x+1]=='#') continue;
            int sy=y;
            int sx=x;
            int gy=y;
            int gx;
            for(int xx=x; xx<N ; xx++){
                // if(y==54&&x==53) {DEBUG(xx);}
                if(state.city[y][xx]=='#') break;
                state.hor_used[y][xx]=true;
                gx=xx;
            }
            Road road(HOR,sy,sx,gy,gx);
            state.roads.push_back(road);
        }
    }
    REP(y,N-1){
        REP(x,N){
            // DEBUG(y);DEBUG(x);
            // DEBUG(state.hor_used[y][x]);
            // DEBUG(state.city[y][x]);
            // DEBUG(state.city[y][x+1]);
            if(state.ver_used[y][x]) continue;
            if(state.city[y][x]=='#') continue;
            if(state.city[y+1][x]=='#') continue;
            int sy=y;
            int sx=x;
            int gy;
            int gx=x;
            for(int yy=y; yy<N ; yy++){
                if(state.city[yy][x]=='#') break;
                state.ver_used[yy][x]=true;
                gy=yy;
            }
            Road road(VER,sy,sx,gy,gx);
            state.roads.push_back(road);

            int road_ind = state.roads.size()-1;
            REP(i, state.roads.size()){
                Road &rh=state.roads[i];
                if(rh.dir==VER) continue;
                if(check_road_cross(rh,road)){
                    state.road_gl[road_ind].push_back(i);
                    state.road_gl[i].push_back(road_ind);
                }
            }
        }
    }
}

void DEBUG_ROADS(State &state){
    int i=0;
    for(Road r : state.roads){
        cout << i << " :" << r.dir << "(" << r.sy << "," << r.sx << ") -> "  <<  "(" << r.gy << "," << r.gx << ")" << endl;
        i++;
    }
}

void DEBUG_CROSS(State &state){
    for(Point p : state.crosses){
        cout << "(" << p.y << "," << p.x << ")" << endl;
    }
}


void check_cross(State &state){
    REP(y,N){
        REP(x,N){
            if(state.city[y][x]=='#') continue;
            int c1=0;
            int c2=0;
            if(state.check_mass(y-1,x)) c1++;
            if(state.check_mass(y+1,x)) c1++;
            if(state.check_mass(y,x-1)) c2++;
            if(state.check_mass(y,x+1)) c2++;
            if(c1>=1 && c2>=1){
                state.crosses.push_back(Point(y,x));
            }
        }
    }
}



// void make_road_dist(State &state){
//     const int inf=1000000;
//     int rn=state.roads.size();
//     vector<vector<int>> dists(rn, inf);
//     REP(i,rn){
//         for(int neib:state.road_gl[i]){
//             dists[i][neib]=1;
//             dists[neib][i]=1;
//         }
//     }
//     REP(k,rn){
//         REP(i,rn){
//             REP(j,rn){
//                 dists[i][j]=min(d[i][j], d[i][k] + d[k][j]);
//             }
//         }
//     }
// }

string get_p2p(Point &p1, Point &p2){
    if(p1.x==p2.x){
        int d=p2.y-p1.y;
        if(d>0) return string(d,'D');
        if(d<0) return string(abs(d),'U');
    }
    if(p1.y==p2.y){
        int d=p2.x-p1.x;
        if(d>0) return string(d,'R');
        if(d<0) return string(abs(d),'L');
    }
    return "";
}


Point get_cross2(int ri, int rj, State &state){
    Road &c_road=state.roads[ri];
    Road &next_road=state.roads[rj];
    Point cross_p;
    if(c_road.dir==HOR){
        cross_p=get_cross(c_road,next_road);
    }
    else{
        cross_p=get_cross(next_road,c_road);
    } 
    return cross_p;
}

int get_real_dist(State &state, Point &p1, Point &p2){
    int res=0;
    if(p1.y==p2.y){
        int y=p1.y;
        int sx=p1.x;
        int gx=p2.x;
        if(sx>gx) swap(sx,gx);
        for(int x=sx+1; x<=gx ; x++){
            char c = state.city[y][x];
            int val = c-'0';
            res+=val;
        }
    }
    else{
        int x=p1.x;
        int sy=p1.y;
        int gy=p2.y;
        if(sy>gy) swap(sy,gy);
        for(int y=sy+1;y<=gy ; y++){
            char c = state.city[y][x];
            int val = c-'0';
            res+=val;
        }
    }
    return res;
}

int calc_penalty(Point start, Point p){
    // int dist = abs(start.x-p.x)+abs(start.y-p.y);
    int dist = abs(N/2-p.x)+abs(N/2-p.y);
    // DEBUG(start.x);
    // DEBUG(p.x);
    // DEBUG(start.y);
    // DEBUG(p.y);
    // DEBUG(dist*PENA);
    return dist*PENA;

    // return (N-dist)*PENA;
}


int calc_yugu(Point p){
    int dist = abs(N/2-p.x)+abs(N/2-p.y);
    return dist*YUGU;
}

bool to_near_road(State &state){
    int inf=10000000;
    int rn=state.roads.size();
    vector<int> vis(rn,inf);
    vector<Point> pos(rn, Point(0,0));
    // Point start = Point(state.y,state.x);
    Point start = Point(state.sy,state.sx);
    vector<vector<int>> routes(rn, vector<int>(1,state.current_road));
    // deque<int> q;
    priority_queue<P, vector<P>, greater<P>> q;
    q.push(P(0,state.current_road));
    vis[state.current_road]=0;
    pos[state.current_road]=Point(state.y,state.x);
    int goal=-1;

    int loop=0;
    while(!(q.empty())){
        loop++;
        auto [dist,poped]=q.top(); q.pop();
        // DEBUG(poped);
        if(!state.roads[poped].used){
            state.roads[poped].used=true;
            goal=poped;
            break;
        }
        vector<int> c_route=routes[poped];
        // int pppppppppppppppppp=poped;
        // DEBUG(pppppppppppppppppp);
        for(int neib: state.road_gl[poped]){
            if(vis[neib] < dist)continue;
            Point cross_p=get_cross2(poped,neib,state);
            int cost = get_real_dist(state, pos[poped], cross_p);  
            int pena=max(0, calc_penalty(start, cross_p)-calc_penalty(start, pos[neib]));
            int yugu = calc_yugu(cross_p);
            // cost-=yugu;
            cost=max(0,cost);
            // cost-=calc_penalty(start, pos[neib]);
            // cost+=calc_penalty(start, cross_p);
            cost+=pena;
            // cost+=1;
            // DEBUG(pena); DEBUG(cost);
            // cost+=10;          
            // DEBUG(neib);DEBUG(cost);DEBUG(vis[neib]);
            if( vis[neib] > vis[poped] + cost ){    
                vis[neib] = vis[poped] + cost;
                q.push(P(vis[neib], neib));
                routes[neib]=c_route;
                routes[neib].push_back(neib);
                pos[neib]=cross_p;
            }
        }
        // vis[poped]=true;
    }
    // DEBUG(loop);
    if(goal==-1) return false;

    int route_len=routes[goal].size();
    for(int i=0; i<route_len-1; i++){
        Point c_point=Point(state.y,state.x);
        Road &c_road=state.roads[routes[goal][i]];
        Road &next_road=state.roads[routes[goal][i+1]];
        Point cross_p;
        if(c_road.dir==HOR){
            cross_p=get_cross(c_road,next_road);
        }
        else{
            cross_p=get_cross(next_road,c_road);
        }
        string route_str=get_p2p(c_point,cross_p);
        // string route_str="aa";
        state.ans+=route_str;

        state.y=cross_p.y;
        state.x=cross_p.x;
        state.current_road=routes[goal][i+1];
    }

    return true;
}


int check_current_road(State &state){
    REP(i, state.roads.size()){
        Road &r=state.roads[i];
        if(r.dir==HOR){
            if(r.sy!=state.y) continue;
            if(r.sx<=state.x && state.x<=r.gx) return i;
        }
        if(r.dir==VER){
            if(r.sx!=state.x) continue;
            if(r.sy<=state.y && state.y<=r.gy) return i;
        }
    }
    return -1;
}

int calc_score(State &state){
    int res=0;
    int y=state.sy;
    int x=state.sx;
    // DEBUG(state.ans);
    for(char c:state.ans){
        // DEBUG(c); DEBUG(y); DEBUG(x);
        if(c=='U')y--;
        if(c=='D')y++;
        if(c=='R')x++;
        if(c=='L')x--;
        res+=(state.city[y][x]-'0');
    }
    return res;
}

struct AnsInfo{
    int score;
    string ans;
};

void solve(){

    TimeManager tm;

    cin>>N;
    int sy,sx; cin>>sy>>sx;

    State state;
    state.y=sy;
    state.x=sx;

    state.sy=sy;
    state.sx=sx;

    AnsInfo c_ans;
    c_ans.score=10000000;

    REP(i,N){
        string s; cin>>s;
        state.city.push_back(s);
    }

    State state_orig=state;

    int loop=0;
    double TL = 2500.0;
    while(tm.check(TL, true)){
        if(!tm.check(TL)) break;

        check_roads(state);
        // check_cross(state);
        // DEBUG_ROADS(state);
        // DEBUG_CROSS(state);
        // DEBUG(state.road_gl);

        int first_road_i = check_current_road(state);
        state.roads[first_road_i].used=true;
        state.current_road=first_road_i;

        while(true){
            bool ret = to_near_road(state);
            if(!ret) break;
            // loop+=1;
        }
        state.roads[first_road_i].used=false;
        to_near_road(state);
        Point c_point=Point(state.y,state.x);
        Point goal=Point(sy,sx);
        string last_route = get_p2p(c_point, goal);
        state.ans+=last_route;

        // DEBUG(state.ans);


        int score=calc_score(state);
        // DEBUG(score);
        if(score<c_ans.score){
            c_ans.score=score;
            c_ans.ans=state.ans;
        }
        state=state_orig;
        PENA+=3;
        // break;
        loop++;
    }

    DEBUG(loop);
    // cout<<state.ans<<endl;
    cout<<c_ans.ans<<endl;

    // double TL = 2500.0;
    // while(tm.check(TL)){
    //     if(!tm.check(TL)) break;
        // double t01 = tm.get_time()/TL;
        // double tt=pow(T0,1.0-t01)*pow(T1,t01);
        // if(kaizen > 0 || yaki_prob < exp(kaizen/tt) )
    // }
    // state.output();
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}