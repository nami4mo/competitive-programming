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

int M;

struct TimeManager
{
    chrono::system_clock::time_point start;
    double time=0.0;
    int loop_per_measure, loop_cnt;
    TimeManager(int loop_per_measure=50): start(chrono::system_clock::now()),loop_cnt(0),loop_per_measure(loop_per_measure){};
    bool check(double limit, bool force=false){
        loop_cnt++;
        if(force || loop_cnt>=loop_per_measure){
            auto c_time=chrono::system_clock::now();
            time = chrono::duration_cast<chrono::milliseconds>(c_time-start).count();
            loop_cnt=0;
            return (time<limit);
        }
        else return (time<limit);
    }
    double get_time(bool force=false){
        if(force) check(0.0,true);
        return time;
    }
};

int get_sim(string s, string t){
    int sn=s.size(), tn=t.size();
    vector<vector<int>> dp(sn+1, vector<int>(tn+1,(-1)*IINF));
    dp[0][0]=0;
    REP(i,sn+1){
        REP(j,tn+1){
            int score=1;
            if(s[i]!=t[j]) score=-3;
            int curr=dp[i][j];
            if(i<sn && j<tn) dp[i+1][j+1]=max(dp[i+1][j+1], curr+score);
            if(i<sn) dp[i+1][j]=max(dp[i+1][j], curr-5);
            if(j<tn) dp[i][j+1]=max(dp[i][j+1], curr-5);
        }
    }
    return dp[sn][tn];
}


struct Col{
    int a=0;
    int t=0;
    int c=0;
    int g=0;
    int hy=0;
    bool new_hy=false;
    vector<int> inds;
    Col operator+(const Col &other) {
        Col ret;
        ret.a=a+other.a;
        ret.t=t+other.t;
        ret.c=c+other.c;
        ret.g=g+other.g;
        ret.hy=hy+other.hy;
        return ret;
    }
};

struct ColData{
    vector<Col> cols;
    vector<int> inds;
};

// char get_max_c(Col col){
//     char c='.';
//     int ma=-1;
//     if(col.a>ma){c='A'; ma=col.a;}
//     if(col.t>ma){c='T'; ma=col.t;}
//     if(col.c>ma){c='C'; ma=col.c;}
//     if(col.g>ma){c='G'; ma=col.g;}
//     if(col.hy>ma){c='-'; ma=col.hy;}
//     return c;
// }

vector<char> get_max_cs(Col col){
    int DIST=12;
    if(M<=10) DIST=2;

    int ma=-1;
    char c='.';

    if(col.a>ma){c='A'; ma=col.a;}
    if(col.t>ma){c='T'; ma=col.t;}
    if(col.c>ma){c='C'; ma=col.c;}
    if(col.g>ma){c='G'; ma=col.g;}
    if(col.hy>ma){c='-'; ma=col.hy;}
    vector<char> res={c};
    if(col.a>=ma-DIST && c!='A'){res.push_back('A');}
    if(col.t>=ma-DIST && c!='T'){res.push_back('T');}
    if(col.c>=ma-DIST && c!='C'){res.push_back('C');}
    if(col.g>=ma-DIST && c!='G'){res.push_back('G');}
    if(col.hy>=ma-DIST && c!='-'){res.push_back('-');}
    return res;
}

int get_cost(Col &u, Col &v){
    // DEBUG(u.a);
    int a=u.a+v.a;
    int t=u.t+v.t;
    int c=u.c+v.c;
    int g=u.g+v.g;
    int hy=u.hy+v.hy;
    int cnt=a+t+c+g+hy;
    int res=cnt-max({a,t,c,g,hy});
    // if(hy>=cnt/2) res+=cnt/10;
    // if(u.new_hy||v.new_hy) res+=cnt/15;
    return res;
}

vector<Col> s2col(string s){
    vector<Col> res;
    for(char c:s){
        Col col;
        if(c=='A') col.a=1;
        if(c=='T') col.t=1;
        if(c=='C') col.c=1;
        if(c=='G') col.g=1;
        if(c=='-') col.hy=1;
        res.push_back(col);
        // DEBUG(col.a);
    }
    return res;
}
 

ColData align_cols(ColData &sdata, ColData &tdata, vector<string> &dl){
    vector<Col> &s=sdata.cols;
    vector<Col> &t=tdata.cols;
    vector<int> &sinds=sdata.inds;
    vector<int> &tinds=tdata.inds;

    int sn=s.size(), tn=t.size();
    Col s_hy; s_hy.hy=sinds.size(); s_hy.new_hy=true;
    Col t_hy; t_hy.hy=tinds.size(); t_hy.new_hy=true;
    vector<vector<int>> dp(sn+1, vector<int>(tn+1,IINF)); // cost
    dp[0][0]=0;
    REP(i,sn+1){
        REP(j,tn+1){
            int curr=dp[i][j];
            if(i<sn && j<tn) dp[i+1][j+1]=min(dp[i+1][j+1], curr+get_cost(s[i],t[j]));
            if(i<sn) dp[i+1][j]=min(dp[i+1][j], curr+get_cost(s[i],t_hy));
            if(j<tn) dp[i][j+1]=min(dp[i][j+1], curr+get_cost(s_hy,t[j]));
        }
    }
    int i=sn, j=tn;
    vector<Col> ss;
    vector<Col> tt;
    vector<string> new_dl(M, "");
    // DEBUG(dp);
    while(i>0 || j>0){
        // DEBUG(i); DEBUG(j);
        int score;
        int curr=dp[i][j];
        if(i>0 && j>0){
            score=get_cost(s[i-1],t[j-1]);
            if(dp[i-1][j-1]+score==curr){
                ss.push_back(s[i-1]);
                tt.push_back(t[j-1]);
                i--; j--;
                continue;
            }
        }
        if(i>0){
            score=get_cost(s[i-1],t_hy);
            if(dp[i-1][j]+score==curr){
                ss.push_back(s[i-1]);
                tt.push_back(t_hy);
                i--;
                continue;
            }
        }
        ss.push_back(s_hy);
        tt.push_back(t[j-1]);
        j--;
    }
    reverse(ALL(ss));
    reverse(ALL(tt));
    vector<Col> res;
    int curr_si=0;
    int curr_ti=0;
    REP(i,ss.size()){
        // DEBUG(i);
        res.push_back(ss[i]+tt[i]);
        // DEBUG(i);
        if(ss[i].new_hy){
            for(int ind:sinds){
                new_dl[ind]+="-";
            }
        }
        else{
            for(int ind:sinds){
                new_dl[ind]+=dl[ind][curr_si];
            }
            curr_si++;
        }
        if(tt[i].new_hy){
            for(int ind:tinds){
                new_dl[ind]+="-";
            }
        }
        else{
            for(int ind:tinds){
                new_dl[ind]+=dl[ind][curr_ti];
            }
            curr_ti++;
        }
    }

    ColData resdata;
    resdata.cols=res;
    for(int ind:sinds) {dl[ind]=new_dl[ind]; resdata.inds.push_back(ind);}
    for(int ind:tinds) {dl[ind]=new_dl[ind]; resdata.inds.push_back(ind);}

    return resdata;
}


int DEBUG_SCORE(ColData cd){
    int pena=0;
    for(Col col:cd.cols){
        int ma=max({col.a, col.t, col.c, col.g, col.hy});
        pena+=(M-ma);
    }
    DEBUG(700-pena*0.1);
    return 700-pena*0.1;
}

string align_one_fixed(string s, string t){
    int sn=s.size(), tn=t.size();
    int hyn=tn-sn;
    vector<vector<int>> dp(sn+1, vector<int>(hyn+1,(-1)*IINF));
    dp[0][0]=0;
    REP(i,sn+1){
        REP(j,hyn+1){
            char ti=t[i+j];
            int curr=dp[i][j];
            if(i<sn) {
                int score=1;
                if(s[i]!=ti) score=-1;
                dp[i+1][j]=max(dp[i+1][j], curr+score);
            }
            if(j<hyn) {
                int score=1;
                if(ti!='-') score=-1;
                dp[i][j+1]=max(dp[i][j+1], curr+score);
            }
        }
    }
    int i=sn, j=hyn;
    string ss;
    while(i>0 || j>0){
        int curr=dp[i][j];
        char ti=t[i+j-1];
        if(i>0){
            int score=1;
            if(ti!=s[i-1]) score=-1;
            if(dp[i-1][j]+score==curr){
                ss+=s[i-1];
                i--;
                continue;
            }
        }
        ss+='-';
        j--;
        continue;
    }
    reverse(ALL(ss));
    return ss;
}

vector<Col> dl2cols(vector<string> dl){
    vector<Col> cols(dl[0].size());
    REP(i,dl.size()){
        REP(j, dl[i].size()){
            if(dl[i][j]=='A') cols[j].a++;
            if(dl[i][j]=='T') cols[j].t++;
            if(dl[i][j]=='C') cols[j].c++;
            if(dl[i][j]=='G') cols[j].g++;
            if(dl[i][j]=='-') cols[j].hy++;
        }
    }
    return cols;
}

const int LIMIT=100;
vector<string> get_s_orig_cands(ColData col_data){
    vector<string> s_origs={""};
    for(Col col : col_data.cols){
        vector<string> new_s_origs;
        vector<char> cs=get_max_cs(col);
        for(string s:s_origs){
            for(char c:cs){
                if(new_s_origs.size()>=LIMIT) break;
                new_s_origs.push_back(s+c);
            }
        }
        s_origs=new_s_origs;
    }
    return s_origs;
}

void solve(){
    TimeManager tm;
    cin>>M;
    vector<string> dl;
    vector<string> dl_orig;
    REP(i,M){
        string s; cin>>s; dl.push_back(s);
    }
    dl_orig=dl;
    vector<vector<int>> sims(M,vector<int>(M,0));
    REP(i,M){
        FOR(j,i+1,M){
            sims[i][j]=get_sim(dl[i],dl[j]);
            sims[j][i]=sims[i][j];
        }
    }
    // DEBUG(sims);
    vector<bool> used(M,false);
    vector<int> order;
    order.push_back(0);
    used[0]=true;
    REP(i,M-1){
        int c_ind=-1;
        int ma=-10000000;
        int ci=order.back();
        REP(j,M){
            if(used[j]) continue;
            if(sims[ci][j]>ma){
                c_ind=j;
                ma=sims[ci][j];
            }
        }
        // DEBUG(c_ind);
        used[c_ind]=true;
        order.push_back(c_ind);
    }
    DEBUG(order);
    deque<ColData> q;
    for(int i=0 ; i<M ; i++){
        // int ind=i;
        int ind=order[i];
        ColData col_data;
        col_data.inds={ind};
        col_data.cols=s2col(dl[ind]);
        q.push_back(col_data);
    }

    while(q.size()>1){
        ColData u=q.front(); q.pop_front();
        ColData v=q.front(); q.pop_front();
        ColData merged=align_cols(u,v,dl);
        // q.push_back(merged);
        q.push_front(merged);
    }

    // string s_orig="";
    // for(Col col : q.back().cols){
    //     s_orig+=get_max_cs(col)[0];
    // }

    vector<string> s_cands=get_s_orig_cands(q.back());
    vector<string> ans;
    int score=-1;

    for(string s_orig:s_cands){
        if(!tm.check(9000,true)) break;

        // string s_orig=s_cands[0];
        vector<string> dll;

        for(string s:dl_orig){
            string ressss=align_one_fixed(s,s_orig);
            dll.push_back(ressss);
        }

        ColData col_data;
        col_data.cols=dl2cols(dll);
        int res=DEBUG_SCORE(col_data);
        if(res>score){
            ans=dll;
            score=res;
        }
    }
    for(string s:ans){
        cout<<s<<endl;
    }


}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}