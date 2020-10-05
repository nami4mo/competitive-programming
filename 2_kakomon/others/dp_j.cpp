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

int n;
double dp[301][301][301];
bool dp_flag[301][301][301];

double rec(int c1, int c2, int c3){
    if(dp_flag[c1][c2][c3]){
        return dp[c1][c2][c3];
    }
    double ans = 1.0;
    if(c1>0) ans += rec(c1-1,c2,c3)*(1.0*c1/n);
    if(c2>0) ans += rec(c1+1,c2-1,c3)*(1.0*c2/n);
    if(c3>0) ans += rec(c1,c2+1,c3-1)*(1.0*c3/n);
    ans /= 1.0-1.0*(n-c1-c2-c3)/n;
    dp_flag[c1][c2][c3] = true;
    return dp[c1][c2][c3] = ans;
}


void solve(){
    cin >> n;
    REP(i1,n+1){
        REP(i2,n+1){
            REP(i3,n+1){
                dp[i1][i2][i3] = 0;
                dp_flag[i1][i2][i3] = false;
            }
        }
    }
    dp[0][0][0] = 0;
    dp_flag[0][0][0] = true;
    vector<int> cl(3,0);
    REP(i,n){
        int a; cin >> a;
        cl[a-1]++;
    }
    double ans = rec(cl[0],cl[1],cl[2]);
    // cout << ans << endl;
    printf("%.9f\n",ans);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}