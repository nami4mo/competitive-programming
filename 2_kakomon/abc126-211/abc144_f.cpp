#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
    #include <atcoder/all>
    using namespace atcoder;
#endif
using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<ll,int> P;
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
    template<typename A, size_t N, typename T>
    void Fill(A (&array)[N], const T &val){
        std::fill( (T*)array, (T*)(array+N), val );
    }
}
using namespace defines;

const int IINF = 10000;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;

int n;
double dp[620];
vector<vector<int>> gl(601);

void solve(){
    int m;
    cin >> n >> m;
    Fill(dp, 0.0);
    REP(i,m){
        ll s,t; cin >> s >> t;
        s-=1;
        t-=1;
        gl[s].push_back(t);
    }

    double ans = IINF;
    REP(blocked, n){ // blocked node
        // Fill(dp, 0.0);
        Fill(dp, IINF);
        bool ng_flag = false;
        dp[n-1] = 0.0;
        for(int i = n-2 ; i >= 0 ; i--){
            if( i != blocked ){
                for(int neib : gl[i]){
                    dp[i] += dp[neib]/gl[i].size();
                }
                dp[i] += 1.0;
            }
            else{
                int largest = 0;
                double largest_val = 0;
                if(gl[i].size()<2){
                    // continue; //0.0
                    ng_flag = true;
                    continue;
                }
                for(int neib : gl[i]){
                    double v = dp[neib];
                    if(v > largest_val){
                        largest = neib;
                        largest_val = v;
                    }
                }
                for(int neib : gl[i]){
                    if(neib == largest) continue;
                    dp[i] += dp[neib]/(gl[i].size()-1);
                }
                dp[i] += 1.0;
            }
        }
        if(!ng_flag){
            ans = min(ans, dp[0]);

        }
        // DEBUG(blocked);
        // for(double v:dp){
        //     cout << v <<" ";
        // }
        // cout<<'\n';
    }
    printf("%.8f\n",ans);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}