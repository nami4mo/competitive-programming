#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
#endif
using namespace std;
using namespace atcoder;
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
    ll n,m,v,p; cin >> n >> m >> v >> p;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    // sort()
    // vector<ll> cumsums(n+1,0);
    // ll c = 0;
    // REP(i,n){
    //     c+=min(al[i],m);
    //     cumsums[i+1]=c;
    // }
    sort(ALL(al), greater<ll>());
    // DEBUGL(al);
    
    ll ok = 0;
    ll ng = n;
    while(abs(ok-ng)>1){
        ll mid = (ok+ng)/2;
        bool ok_flag = false;
        // DEBUG(mid);
        if(mid < p){
            ok_flag = true;
        }
        else{
            vector<ll> rivals;
            bool break_f = false;
            FOR(i,p-1,mid){
                ll val = min(al[mid]+m-al[i], m);
                if(val < 0) {
                    break_f = true;
                    break;
                }
                rivals.push_back(val);
            }
            if(break_f){
                
            }
            else{
                // DEBUGL(rivals);
                ll rems = v-(n-rivals.size());
                ll rems_cnt = rems*m;
                // DEBUG(rems_cnt);
                ll rivals_rem = accumulate(ALL(rivals), 0LL);
                if(rems_cnt<=rivals_rem){
                    ok_flag = true;
                }
            }
        }
        if(ok_flag){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok+1 << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}

