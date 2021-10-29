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
const ll MOD = 1'000'000'007;
// const int MOD = 998244353;
using mint = modint1000000007;
// using mint = modint998244353;

vector<P> p_factorization(ll n){
    vector<P> facs;
    if(n == 1) return facs;
    ll curr_n = n;
    for(ll i = 2 ; i*i <= n ; i++){
        if(curr_n%i == 0){
            ll cnt = 0;
            while(curr_n%i == 0){
                cnt += 1;
                curr_n /= i;
            }
            facs.push_back(P(i,cnt));
        }
    }
    if(curr_n != 1) facs.push_back(P(curr_n,1));
    return facs;
}

long long pow_mod(long long x, long long n, long long mod){
    if(n == 0) { return 1; }
    ll xx = x;
    ll nn = n;
    ll k = 1;
    while(nn > 1){
        if(nn%2 != 0){ k *= xx; }
        xx *= xx;
        nn = nn/2;
        xx%=mod;
    }
    return k * xx;
}

mint ans=0;
vector<P> c_pl;
vector<P> c_pl2;
vector<P> ps;
ll n,k; 
void solve_dfs2(int ind, ll val){
    if(ind==ps.size()){
        ll nmax=n/val;
        ll v2=1;
        ll cnt=0;
        for(auto &[p,c]:c_pl2){
            v2*=pow_mod(p,c,MOD);
            cnt+=c;
        }
        ll icnt=nmax/v2;
        ll csum=icnt*(icnt+1)/2;
        // csum*=(k);
        csum*=v2;
        if(cnt%2==1) ans-=csum;
        else ans+=csum;
        return;
    }

    auto &[prime,pcnt]=ps[ind];
    REP(i, min(pcnt+1-c_pl[ind].second, 2ll)){
        c_pl2.push_back({prime,i});
        solve_dfs2(ind+1, val);
        c_pl2.pop_back();
    }
}

void solve_dfs(int ind){
    if(ind==ps.size()){
        ll val=1;
        for(auto &[p,c]:c_pl){
            val*=pow_mod(p,c,MOD);
        }
        solve_dfs2(0,val);
        return;
    }
    auto &[prime,cnt]=ps[ind];
    REP(i, cnt+1){
        c_pl.push_back({prime,i});
        solve_dfs(ind+1);
        c_pl.pop_back();
    }
}

void solve(){
    cin>>n>>k;
    ps=p_factorization(k);
    solve_dfs(0);
    ans*=k;
    cout<<ans.val()<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}