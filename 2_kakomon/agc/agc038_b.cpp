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
    template<typename A, size_t N, typename T> void Fill(A (&array)[N], const T &val){std::fill( (T*)array, (T*)(array+N), val );}
}
using namespace defines;

const int IINF = 1'001'001'001;
const ll INF = 1'001'001'001'001'001'001ll;
const int MOD = 1'000'000'007;
// const int MOD = 998244353;
// using mint = modint1000000007;
// using mint = modint998244353;


void solve(){
    ll n,k; cin >> n >> k;
    vector<ll> al(n); REP(i,n) cin >> al[i];
    ll inc_cnt = 0;
    deque<ll> rems_q(ALL(al));
    deque<ll> curr_q;
    set<ll> st;

    ll notchange = 0;
    ll allinc = 0;
    REP(i,k){
        ll new_a = rems_q.front(); rems_q.pop_front();
        if(i!=0){
            if(new_a > curr_q.back()) inc_cnt+=1;
        }
        curr_q.push_back(new_a);
        st.insert(new_a);
    }
    if(inc_cnt==k-1) allinc++;

    REP(i,n-k){
        if(curr_q[0]<curr_q[1]) inc_cnt--;

        ll poped = curr_q.front(); curr_q.pop_front();
        ll new_a = rems_q.front(); rems_q.pop_front();

        if(curr_q.back()<new_a){
            inc_cnt++;
        }
        // DEBUG(poped);
        // DEBUG(new_a);
        // DEBUG(curr_q.back());
        // DEBUG(inc_cnt);

        bool ng_flag = false;
        ll prev_st_min = *(st.begin());
        st.erase(poped);
        ll prev_st_max = *(st.rbegin());

        // DEBUG(prev_st_min);
        // DEBUG(prev_st_max);
        // cout<<endl;

        
        if(inc_cnt==k-1){
            // ng_flag = true;
            allinc++;
        }
        else if(prev_st_min==poped && prev_st_max<new_a){
            notchange++;
        }

        st.insert(new_a);
        curr_q.push_back(new_a);

    }
    allinc = max(allinc-1,0ll);
    cout<<n-k+1-allinc-notchange<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}