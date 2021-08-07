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

struct S{
    double a,b;
    S(double a, double b):a(a),b(b){}
};

vector<S> dp(200200,S(0.0,0.0));

S op(S l, S r){return S(l.a+r.a,l.b+r.b);}
S e(){return S(0,0);}


void solve(){
    ll n,m,k; cin>>n>>m>>k;
    vector<ll> al(k); REP(i,k) cin >> al[i];
    vector<bool> akl(n+2,false);
    segtree<S, op, e> seg(n+m+10);
    for(ll a:al){
        akl[a]=true;
    }
    for(int i=n-1 ; i>=0 ; i--){
        if(akl[i]){
            seg.set(i,S(0.0,1.0));
        }
        else{
            S c_val=seg.prod(i+1,i+1+m);
            c_val.a/=m;
            c_val.a+=1;
            c_val.b/=m;
            seg.set(i,c_val);
        }
    }
    S top=seg.prod(0,1);
    if(top.b>=1.0){
        cout<<-1<<endl;
        return;
    }
    double div=1.0-top.b;
    double ans=top.a/div;
    printf("%f\n",ans);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}