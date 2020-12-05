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

int dx[4]={0,0,-1,1};
int dy[4]={1,-1,0,0};


void solve(){
    ll h,w,t; cin >> h >> w >> t;
    vector<string> sl(h);
    REP(i,h){
        cin >> sl[i];
    }

    ll ok = 1;
    ll ng = 1e9+1;

    ll start;
    ll goal;
    while(abs(ok-ng)>1){
        ll mid = (ok+ng)/2;
        bool ok_flag = true;

        vector<vector<ll>> dl(h*w, vector<ll>(h*w, INF));
        REP(y,h){
            REP(x,w){
                ll u = y*w+x;
                if(sl[y][x]=='S') start=u;
                if(sl[y][x]=='G') goal=u;
                REP(di,4){
                    int yy = y+dy[di];
                    int xx = x+dx[di];
                    if(yy<0||h<=yy||xx<0||w<=xx)continue;
                    ll v = yy*w+xx;
                    
                    if(sl[y][x]=='#')dl[v][u] = mid;
                    else dl[v][u] = 1;

                    if(sl[yy][xx]=='#') dl[u][v] = mid;
                    else dl[u][v] = 1;
                }
            }
        }
        // DEBUG
        // DEBUGLL(dl);
        REP(i,h*w){
            REP(j,h*w){
                REP(k,h*w){
                    dl[j][k] = min(dl[j][k], dl[j][i]+dl[i][k]);
                }
            }
        }
        
        if(dl[start][goal]<=t){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}