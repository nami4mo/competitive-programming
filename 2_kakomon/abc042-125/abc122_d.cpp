#include <bits/stdc++.h>

using namespace std;
namespace defines{
    typedef long long ll;
    typedef pair<ll,ll> P;
    #define FOR(i,a,b) for(ll i = a ; i < b ; i++) // for i in range(a,b)
    #define REP(i,n) for(ll i = 0 ; i < n ; i++) // for i in range(b)
    #define FORD(i,a,b) for(ll i = a ; i > b ; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(),x.end()

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
    template<class T> vector<T> make_vec(size_t a){return vector<T>(a);}
    template<class T, class... Ts> auto make_vec(size_t a, Ts... ts){ return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...));}
}

using namespace defines;
const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;




void solve(){
    int n; cin >> n;
    auto dp = make_vec<ll>(n+1, 4, 4, 4);
    ll dp[101][4][4][4] = {0};
    ll a=0,g=1,c=2,t=3;

    REP(i,n+1){
        REP(s3,4){
            REP(s2,4){
                REP(s1,4){
                    if(dp[i][s3][s2][s1]!=0){
                        cout << i << s3 << s2 << s1 << endl;
                    }
                    if(i!=3){
                        dp[i][s3][s2][s1] = 0;
                    }
                    else{
                        if(s3==a&&s2==g&&s1==c){
                            dp[3][s3][s2][s1] = 0;
                        }
                        else if(s3==g&&s2==a&&s1==c){
                            dp[3][s3][s2][s1] = 0;
                        }
                        else if(s3==a&&s2==c&&s1==g){
                            dp[3][s3][s2][s1] = 0;
                        }
                        else{
                            dp[3][s3][s2][s1] = 1;
                        }
                    }
                }
            }
        }
    }


    FOR(i,4,n+1){
        REP(s3,4){
            REP(s2,4){
                REP(s1,4){
                    REP(s,4){
                        if(s==c){
                            if(s2==a && s1==g) continue;
                            if(s3==a && s1==g) continue;
                            if(s2==g && s1==a) continue;
                            if(s3==a && s2==g) continue;
                        }
                        if(s2==a && s1==c && s==g) continue;
                        dp[i][s2][s1][s] += dp[i-1][s3][s2][s1];
                        dp[i][s2][s1][s]%=MOD;
                    }
                }
            }
        }
    }
    ll ans = 0;
    REP(s3,4){
        REP(s2,4){
            REP(s1,4){
                // cout << s3 << s2 << s1 << endl;
                // cout << dp[n][s3][s2][s1] << endl << endl;
            
                ans += dp[n][s3][s2][s1];
                ans%=MOD;
            }
        }
    }
    cout << ans << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}