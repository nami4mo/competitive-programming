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

    /* for debug print */
    #define DEBUG(x) cerr << #x << ": " << x << '\n'
    #define DEBUGP(x) cerr << #x << ": (" << x.first << ", " << x.second << ")" << '\n' 
    #define DEBUGL(xl) dbgl_f(#xl,xl)
    #define DEBUGLP(xl) dbglp_f(#xl,xl)
    #define DEBUGLL(xll) dbgll_f(#xll,xll)
    #define DEBUGM(xl) dbgm_f(#xl,xl)
    template<class T> void dbgl_f(string name, vector<T> xl){cerr<<name<<": "; for(T x: xl) cerr<<x<<" "; cerr << '\n';}
    template<class T, class U> void dbgm_f(string name, map<T,U> xl){cerr<<name<<": ";for(auto x: xl)cerr<<"("<<x.first<<": "<<x.second<<") ";cerr<<'\n';}
    template<class T> void dbglp_f(string name, vector<T> xl){cerr<<name<<": ";for(T x: xl)cerr<<"("<<x.first<<", "<< x.second<<") ";cerr<<'\n';}
    template<class T> void dbgll_f(string name, vector<vector<T>> xll){
        cerr<< name << ": " << '\n'; 
        for(vector<T> xl: xll){
            for(T x : xl) cerr << x << " ";
            cerr << '\n';
        }
    }
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;

int rhcnt[100001][4];

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};


void solve(){
    ll h,w; cin >> h >> w;
    char sl[h][w];
    P start, goal;
    REP(i,h){
        REP(j,w){
            cin >> sl[i][j];
            if(sl[i][j] == 's') start = P(i,j);
            if(sl[i][j] == 'g') goal = P(i,j);
        }
    }

    vector<vector<int>> break_cnts(h,vector<int>(w,4));
    deque<P> q;
    q.push_back(start);
    break_cnts[start.first][start.second] = 0;
    bool ans = false;
    while(!q.empty()){
        auto [y,x] = q.front(); q.pop_front();
        REP(i,4){
            int yy = y+dy[i];
            int xx = x+dx[i];
            if( yy < 0 || h <= yy || xx < 0 || w <= xx ){
                continue;
            }
            if( sl[yy][xx] == '.' && break_cnts[yy][xx] > break_cnts[y][x] ){
                break_cnts[yy][xx] = break_cnts[y][x];
                q.push_back(P(yy,xx));
            }
            else if( sl[yy][xx] == '#' && break_cnts[yy][xx] > break_cnts[y][x]+1 && break_cnts[y][x] < 2){
                break_cnts[yy][xx] = break_cnts[y][x]+1;
                q.push_back(P(yy,xx));
            }
            else if( sl[yy][xx] == 'g' ){
                ans = true;
            }
        }
    }
    if(ans)cout<<"YES"<<'\n';
    else cout<<"NO"<<'\n';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}