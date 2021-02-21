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

vector<P> cards(101,{-1,-1});
vector<vector<int>> board(20,vector<int>(20,-1));
deque<int> q;

struct State{
};

int sign(int v){
    if(v>0)return 1;
    else if(v<0)return -1;
    else return 0;
}

void move(int &cy, int &cx, int y, int x, vector<char> &com){
    if(cy<y){
        REP(j,y-cy) com.push_back('D');
    }
    else{
        REP(j,cy-y) com.push_back('U');
    }
    if(cx<x){
        REP(j,x-cx) com.push_back('R');
    }
    else{
        REP(j,cx-x) com.push_back('L');
    }
    cy=y;
    cx=x;
}

P search_empty(int cy, int cx, int y, int x){
    ll dy=y-cy;
    ll dx=x-cx;
    REP(d,abs(dy)+abs(dx)+1){
        REP(i, min(d,abs(dy)+1)){
            // REP(j, min(d,abs(dx)+1)){
            ll j=d-i;
            int yy=y+i*sign(dy)*(-1);
            int xx=x+j*sign(dx)*(-1);
            // DEBUG(yy);
            // DEBUG(xx);
            if(xx<0||20<=xx||yy<0||20<=yy)continue;
            if(board[yy][xx]==-1) return {yy,xx};
            // }
        }
    }
    return {-1,-1};
}

void pre_process(vector<char> &com){
    int cy=0,cx=0;
    if(board[cy][cx]!=-1){
        q.push_back(board[cy][cx]);
        cards[board[cy][cx]]={-1,-1};
        board[cy][cx]=-1;
        com.push_back('I');
    }
    REP(i,20){
        REP(j,19){
            if(i%2==0){
                cx++;
                com.push_back('R');
            }
            else{
                cx--;
                com.push_back('L');
            }
            if(board[cy][cx]!=-1){
                q.push_back(board[cy][cx]);
                cards[board[cy][cx]]={-1,-1};
                board[cy][cx]=-1;
                com.push_back('I');
            }
        }
        if(i!=19) {
            com.push_back('D');
            cy++;
        }
        if(board[cy][cx]!=-1){
            q.push_back(board[cy][cx]);
            cards[board[cy][cx]]={-1,-1};
            board[cy][cx]=-1;
            com.push_back('I');
        }
    }

    // DEBUG(q.size());
    board[cy][cx]=q.back(); 
    cards[q.back()]={cy,cx};
    q.pop_back();
    com.push_back('O');
    REP(i,10){
        REP(j,9){
            if(i%2==0){
                cx++;
                com.push_back('R');
            }
            else{
                cx--;
                com.push_back('L');
            }
            board[cy][cx]=q.back(); 
            cards[q.back()]={cy,cx};
            q.pop_back();
            com.push_back('O');
        }
        if(i!=9){
            cy--;
            com.push_back('U');
            board[cy][cx]=q.back(); 
            cards[q.back()]={cy,cx};
            q.pop_back();
            com.push_back('O');
        }
    }
}


void tsp(){
    
}

void solve(){
    TimeManager tm;
    REP(i,100){
        int x,y;cin>>y>>x;
        cards[i]={y,x};
        board[y][x]=i;
    }

    int cy=0,cx=0;
    vector<char> com;
    // pre_process(com);
    // cy=10;

    REP(i,100){
        if(cards[i].first==-1)continue;
        // DEBUG(i);
        auto&[y,x]=cards[i];
        auto&[y2,x2]=cards[i+1];
        int dy=y-cy;
        int dx=x-cx;
        int dy2=y2-cy;
        int dx2=x2-cx;
        bool go_direct = true;
        // DEBUG(cy);
        // DEBUG(cx);
        // DEBUG(y);
        // DEBUG(x);
        if(sign(dx)*sign(dx2)>=0 && sign(dy)*sign(dy2)>=0 && abs(dy2)<=abs(dy) && abs(dx2)<=abs(dx) && i!=99){
            // DEBUG(y2);
            // DEBUG(x2);
            P em = search_empty(y2,x2,y,x);
            auto&[ey,ex]=em;
            // DEBUG(em);
            if(ey!=-1){
                move(cy,cx,y2,x2,com);
                com.push_back('I');
                board[y2][x2]=-1;
                move(cy,cx,ey,ex,com);
                com.push_back('O');
                board[ey][ex]=i+1;
                move(cy,cx,y,x,com);
                com.push_back('I');
                board[y][x]=-1;
                move(cy,cx,ey,ex,com);
                com.push_back('I');
                board[ey][ex]=-1;
                go_direct=false;
                cards[i]={-1,-1};
                cards[i+1]={-1,-1};
            }
        }
        if(go_direct){ // go to i directly
            move(cy,cx,y,x,com);
            com.push_back('I');
            board[y][x]=-1;
            cards[i]={-1,-1};
        }
    }
    for(char c:com) cout<<c;
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}