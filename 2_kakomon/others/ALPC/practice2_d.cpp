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

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void solve(){
    int n,m; cin >> n >> m;
    vector<string> grid(n);
    REP(i,n){
        cin >> grid[i];
    }
    mf_graph<int> mg(n*m+2); // s: n*m, t: n*m+1
    REP(i,n){
        REP(j,m){
            int pos_v = i*m+j;
            if(grid[i][j] == '#'){
                continue;
            }

            if((i+j)%2==0){
                mg.add_edge(n*m, pos_v, 1);
                for(int k = 0 ; k < 4; k++){
                int cy = i+dy[k];
                int cx = j+dx[k];
                if( cy < 0 || n <= cy || cx < 0 || m <= cx ){
                    continue;
                }
                if(grid[cy][cx] == '#'){
                    continue;
                }
                mg.add_edge(pos_v, cy*m+cx, 1);
            }
            }
            else{
                mg.add_edge(pos_v, n*m+1, 1);
            }
        
        }
    }

    int ans = mg.flow(n*m,n*m+1);
    cout<<ans<<endl;

    vector<mf_graph<int>::edge> edges = mg.edges();
    for(auto e : edges){
        if(e.flow <= 0 || e.from==n*m || e.to==n*m+1)continue;
        ll u,v;
        u = e.from;
        v = e.to;
        if(u>v) swap(u,v);
        int uy = u/m, ux = u%m;
        int vy = v/m, vx = v%m;
        // DEBUG(u);
        // DEBUG(v);
        if(uy+1==vy){
            grid[uy][ux] = 'v';
            grid[vy][vx] = '^';
        }
        else{
            grid[uy][ux] = '>';
            grid[vy][vx] = '<';
        }
        // if(v-u==1){
        //     if( m!=1){
        //         grid[row][col] = '>';
        //         grid[row][col+1] = '<';
        //     }
        //     else{
        //         grid[row][col] = 'v';
        //         grid[row+1][col] = '^';
        //     }
        // }
        // else{
        //     if( n!=1){
        //         grid[row][col] = 'v';
        //         grid[row+1][col] = '^';
        //     }
        //     else{
        //         grid[row][col] = '>';
        //         grid[row][col+1] = '<';
        //     }
        // }
    }
    REP(i,n){
        cout<<grid[i]<<'\n';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}