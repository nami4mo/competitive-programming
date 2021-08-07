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
// using mint = modint1000000007;
// using mint = modint998244353;



void solve(){
    ll n;cin>>n;
    vector<vector<P>> gl(n,vector<P>());
    REP(i,n-1){
        ll u,v,w; cin >> u >> v >> w; u--;v--;
        gl[u].push_back({v,w});
        gl[v].push_back({u,w});
    }

    vector<ll> order = {0};
    vector<P> pare(n,{-1,-1});
    deque<ll> q; q.push_back(0);
    while(!q.empty()){
        ll ped=q.front(); q.pop_front();
        for(auto &[neib,w] : gl[ped]){
            if(pare[neib].first!=-1 || neib==0) continue;
            pare[neib]={ped,w};
            order.push_back(neib);
            q.push_back(neib);
        }
    }

    const ll MAX=61;
    vector<vector<ll>> dp0(MAX, vector<ll>(n,0));
    vector<vector<ll>> dp1(MAX, vector<ll>(n,0));
    reverse(ALL(order));
    for(ll v :order){
        if(pare[v].first==-1)continue;
        ll parent =pare[v].first;
        ll w =pare[v].second;
        REP(i,MAX){
            if(w&(1L<<i)){
                dp0[i][parent]+=dp1[i][v];
                dp1[i][parent]+=(dp0[i][v]+1);
            }
            else{
                dp0[i][parent]+=(dp0[i][v]+1);
                dp1[i][parent]+=dp1[i][v];
            }
        }
    }

    ll ans=0;
    deque<ll> qq; qq.push_back(0);
    vector<bool> used(n,false);
    used[0]=true;
    
    while(!qq.empty()){
        ll poped=qq.front(); qq.pop_front();
        for(auto &[neib,w]:gl[poped]){
            if(used[neib])continue;

            vector<ll> cnt(MAX,0);
            REP(i,MAX){
                ll sum0=dp0[i][poped];
                ll sum1=dp1[i][poped];
                ll c0=dp0[i][neib];
                ll c1=dp1[i][neib];
                if(w&(1L<<i)){
                    ll tmp=c0;
                    c0=c1;
                    c1=tmp+1;
                }
                else{
                    c0++;
                }
                cnt[i]+=c0*(sum1-c1);
                cnt[i]+=c1;
            }
            REP(i,MAX){
                ans+=cnt[i]*((1L<<i)%MOD);
                ans%=MOD;
            }
            qq.push_back(neib);
            used[neib]=true;
        }
    }
    cout<<ans<<endl;


}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}