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
    ll h,w,n,m; cin >> h >> w >> n >> m;
    vector<vector<bool>> lights(h, vector<bool>(w,false));
    vector<vector<bool>> blocks(h, vector<bool>(w,false));
    vector<vector<bool>> al(h, vector<bool>(w,false));

    REP(i,n){
        ll a,b; cin >> a >> b;
        lights[a-1][b-1] = true;
    }
    REP(i,m){
        ll a,b; cin >> a >> b;
        blocks[a-1][b-1] = true;
    }

    bool light_flag = false;
    REP(hi, h){
        int hatena_start = 0;
        light_flag = false;
        REP(wi,w){
            if(lights[hi][wi]){
                al[hi][wi] = true;
                if(!light_flag){
                    FOR(wwi, hatena_start, wi){
                        al[hi][wwi] = true;
                    }
                    light_flag = true;
                }
                hatena_start = wi;
            }
            else if(blocks[hi][wi]){
                hatena_start = wi+1;
                light_flag = false;
            }
            else{
                if(light_flag){
                    al[hi][wi] = true;
                }
            }
        }
    }


    light_flag = false;
    REP(wi, w){
        int hatena_start = 0;
        light_flag = false;
        REP(hi,h){
            if(lights[hi][wi]){
                al[hi][wi] = true;
                if(!light_flag){
                    FOR(hhi, hatena_start, hi){
                        al[hhi][wi] = true;
                    }
                    light_flag = true;
                }
                hatena_start = hi;
            }
            else if(blocks[hi][wi]){
                hatena_start = hi+1;
                light_flag = false;
            }
            else{
                if(light_flag){
                    al[hi][wi] = true;
                }
            }
        }
    }
    
    int ans = 0;
    REP(hi,h){
        REP(wi,w){
            if(al[hi][wi]) ans++;
        }
    }
    cout << ans << endl;
    // DEBUGLL(al);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}