
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


void solve(){
    ll r,c; cin >> r >> c;
    ll sy,sx; cin >> sy >> sx;
    sy--; sx--;
    ll gy,gx; cin >> gy >> gx;
    gy--; gx--;
    vector<vector<char>> sl(r, vector<char>(c,'#'));
    REP(i,r){
        REP(j,c){
            char c; cin >> c;
            sl[i][j] = c;
        }
    }
    // vector<vector<int>> dists(r, vector<int>(c, -1));
    int dists[55][55];
    REP(i,55){
        REP(j,55){
            dists[i][j] = -1;
        }
    }
    deque<P> q;
    q.push_back(P(sy,sx));
    dists[sy][sx] = 0;
    while(!q.empty()){
        P pos = q.front();
        int y = pos.first;
        int x = pos.second;
        if( y == gy && x == gx ){
            break;
        }
        q.pop_front();
        for( int dy : {-1,0,1} ){
            for( int dx : {-1,0,1} ){
                int cy = y+dy;
                int cx = x+dx;
                if(abs(dy)+abs(dx) > 1) continue;
                if(cy < 0 || r <= cy || cx < 0 || c <= cx ) continue;
                if(dists[cy][cx] != -1) continue;
                if(sl[cy][cx] == '#') continue;
                dists[cy][cx] = dists[y][x] + 1;
                q.push_back(P(cy,cx));
            }
        }
    }
    cout << dists[gy][gx] << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}