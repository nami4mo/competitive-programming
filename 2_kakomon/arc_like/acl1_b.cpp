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
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
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

void solve(){
    ll n; cin>>n;
    if(n==1){
        cout<<1<<endl; return;
    }
    vector<P> facs=p_factorization(n);
    if(facs[0].first==2) facs[0]={facs[0].first,facs[0].second+1};
    else facs.push_back({2,1});
    vector<ll> v_facs;
    for(auto &[p,c]:facs){
        v_facs.push_back(pow(p,c));
    }

    ll bits=(1L<<v_facs.size());
    ll ans=INF;
    REP(i,bits){
        ll v1=1;
        ll v2=1;
        REP(j,v_facs.size()){
            if(i&(1L<<j)) v1*=v_facs[j];
            else v2*=v_facs[j];
        }
        vector<ll> r={0,v2-1};
        vector<ll> m={v1,v2};
        P res=crt(r,m);
        if(res.second==0 || res.first==0)continue;
        ans=min(ans, res.first);
        // DEBUG(v1); DEBUG(v2);
        // DEBUG(res);
    }
    cout<<ans<<endl;
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}