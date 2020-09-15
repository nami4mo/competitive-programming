#include <bits/stdc++.h>
#include <cmath>

using namespace std;
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