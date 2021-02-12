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

int d;

struct UDInfo{
    ll updated_val;
    ll new_cost;
    ll old_cost;
};

ll calc(vector<ll> &tl, vector<ll> &cl, vector<vector<ll>> &dl, vector<ll> &costs){
    ll ans = 0;
    vector<ll> last_di(26,-1);
    REP(i,d){
        int t = tl[i];
        ans += dl[i][t];
        last_di[t] = i;
        REP(m,26){
            costs[m] += cl[m]*(i-last_di[m]);
        }
    }
    REP(m,26){
        ans -= costs[m];
    }
    return ans;
}

UDInfo update(vector<ll> &tl, vector<ll> &cl, vector<vector<ll>> &dl, vector<ll> &costs, int old_q, int new_q, int new_d){
    vector<ll> last_di(26,-1);
    ll old_cost = costs[old_q];
    ll new_cost = costs[new_q];
    ll updated_old_cost = 0;
    ll updated_new_cost = 0;
    REP(i,d){
        int t = tl[i];
        if(i==new_d) t=new_q;
        last_di[t] = i;
        updated_old_cost += cl[old_q]*(i-last_di[old_q]);
        updated_new_cost += cl[new_q]*(i-last_di[new_q]);
    }
    ll updated = updated_old_cost + updated_new_cost - old_cost - new_cost;
    UDInfo udinfo;
    udinfo.updated_val = updated*(-1);
    udinfo.new_cost = updated_new_cost;
    udinfo.old_cost = updated_old_cost;
    return udinfo;
}

void solve(){
    cin >> d;
    vector<ll> cl(26); REP(i,26) cin >> cl[i];
    vector<vector<ll>> dl(d,vector<ll>(26,0));
    REP(i,d){
        REP(j,26){
            cin>>dl[i][j];
        }
    }
    vector<ll> last_di(26,-1);
    vector<ll> tl(d,-1);
    REP(i,d){
        ll t; cin>>t;
        t-=1;
        tl[i] = t;
    }

    vector<ll> costs(26,0);
    ll ans = calc(tl,cl,dl,costs);

    int m; cin>>m;
    REP(i,m){
        ll d,q; cin >> d >> q;
        d-=1;q-=1;
        int old_q = tl[d];
        UDInfo ud = update(tl,cl,dl,costs,old_q,q,d);

        ans += ud.updated_val;
        ans -= dl[d][old_q];
        ans += dl[d][q];

        costs[old_q] = ud.old_cost;
        costs[q] = ud.new_cost;
        tl[d]=q;

        cout<<ans<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}