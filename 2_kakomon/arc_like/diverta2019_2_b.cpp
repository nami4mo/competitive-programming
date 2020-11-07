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
    ll n; cin >> n;
    vector<P> xyl;
    REP(i,n){
        ll x,y; cin >> x >> y;
        xyl.push_back(P(x,y));
    }

    sort(ALL(xyl));

    int ans = n;
    FOR(i,0,n){
        FOR(j,i+1,n){
            ll p = xyl[i].first - xyl[j].first;
            ll q = xyl[i].second - xyl[j].second;
            // if(p == 0 && q == 0) continue; 
            int cnt = 0;
            vector<bool> used(n,false);
            REP(k,n){
                // DEBUGL(used);
                if(used[k]) continue;
                used[k] = true;
                cnt++;
                int curr_dist = 0;
                FOR(m,k+1,n){
                    ll dx = xyl[k].first - xyl[m].first;
                    ll dy = xyl[k].second - xyl[m].second;
                    // DEBUG(dx%p);
                    // DEBUG(dy%q);
                    // DEBUG(dx/p);
                    // DEBUG(dy/q);
                    if( p == 0 ) {
                        if(dx==0 && dy%q == 0 && dy/q == curr_dist+1) {
                            used[m] = true;
                            curr_dist++;
                        }
                    }
                    else if( q == 0 ){
                        if(dy==0 && dx%p == 0 && dx/p == curr_dist+1) {
                            used[m] = true; 
                            curr_dist++;
                        }
                    }
                    else if( dx%p==0 && dy%q==0 && dx/p == dy/q && dx/p == curr_dist+1) {
                        used[m] = true; 
                        curr_dist++;
                    }
                }
                // DEBUGL(used);

            }
            // cout << endl;
            // DEBUG(p);
            // DEBUG(q);
            // DEBUG(cnt);
            ans = min(ans, cnt);
        }
    }
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}