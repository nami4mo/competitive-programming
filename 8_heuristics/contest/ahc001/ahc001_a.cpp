/*
考慮すべきパラメータ
- 最初に必要面積大きい広告を処理するか。するなら、どれだけ？
- 焼き鈍し温度
- 焼き鈍しループのTL
- 一定ペナ以下は無視する？
- スライドする? するなら確率は？
- 拡大の距離範囲
- 縮小の確率
- ヤバイ時の焼き鈍し確率かえる？
- たまに、余分な部分をカットする？
*/

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

const ll INF = 1'001'001'001'001ll;

const int HW=10000;
const ll PENA_K = 1000000000;
int n;


mt19937_64 mt64(0);
uniform_int_distribution<int> rand_dir4(0, 3);
uniform_real_distribution<double> rand_01(0, 1);
uniform_real_distribution<double> rand_05_15(0.5, 1.5);
uniform_int_distribution<int> rand_hw(0, HW);


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


struct Ad{
    ll tx,ty,r; // target x/y/r
    ll x0,y0,x1,y1; // (x0,y0),(x1,y1)
    ll s; // square (do not use!)
    ll pena;
    int orig_i;

    bool in_place(){
        return (x0<=tx && tx<x1 && y0<=ty && ty<y1);
    }

    bool operator<( const Ad& right ) const {
        if(r!=right.r)return r<right.r;
        if(tx!=right.tx)return tx<right.tx;
        if(ty!=right.ty)return ty<right.ty;
        return false;
    }
    Ad(){};
    Ad(ll x, ll y, ll r, int ind)
    :tx(x),ty(y),r(r),orig_i(ind),x0(x),y0(y),x1(x+1),y1(y+1),s(1){}
    ll get_s(){
        return (x1-x0)*(y1-y0);
    }
};


// const int HW=20;
struct State{
    vector<Ad> ads; // sorted by r
    fenwick_tree<ll> pena_fw;
    ll pena_sum=0;
    State(int n):pena_fw(n){};
};

struct MoveRes{
    ll kaizen;
    int x0,x1,y0,y1;
    int adi;
};

vector<int> get_jyama_inds(State &state, int x0, int x1, int y0, int y1);
ll calc_ad_pena(Ad &ad);
ll calc_ad_pena2(ll x0, ll y0, ll x1, ll y1, ll tx, ll ty, ll r);
void update_pena(State &state, int adi); // 使わん
MoveRes calc_jyama_pena_kaizen(State &state, int jyama_i, int x0, int y0, int x1, int y1);
// bool try_to_expand_4dirs(State &state, int adi, int dx0, int dx1, int dy0, int dy1, double yaki_prob, double tt, ll pre_kaizen=0, bool force=false);


ll calc_ad_pena(Ad &ad){
    if(!ad.in_place()) return PENA_K;
    ll s=ad.get_s();
    ll r=ad.r;
    double c_pena_root;
    if(s<=r) c_pena_root = 1.0-(1.0)*s/r;
    else c_pena_root = 1.0-(1.0)*r/s;
    return (ll)(PENA_K*c_pena_root*c_pena_root);
}

ll calc_ad_pena2(ll x0, ll y0, ll x1, ll y1, ll tx, ll ty, ll r){
    if(tx<x0 || x1<=tx || ty<y0 || y1<=ty ) return PENA_K;
    ll s = (x1-x0)*(y1-y0);
    if(x1-x0<=0 || y1-y0<0) return PENA_K;
    double c_pena_root;
    if(s<=r) c_pena_root = 1.0-(1.0)*s/r;
    else c_pena_root = 1.0-(1.0)*r/s;
    return (ll)(PENA_K*c_pena_root*c_pena_root);
}




void update_pena(State &state, int adi){    
    // ll prev_pena=state.ads[adi].pena;
    // state.ads[adi].pena=calc_ad_pena(state.ads[adi]);
    // state.ads[adi].pena=pow(calc_ad_pena(state.ads[adi]),1.5);
    // ll diff=state.ads[adi].pena - prev_pena; // 改善していたらマイナス
    // state.pena_sum+=diff;
    // state.pena_fw.add(adi,diff);
}


// もし移動不可なら、 -INFを返す
// 邪魔な広告を縮小させた時の改善値を返す（悪化するので、マイナスになる）
MoveRes calc_jyama_pena_kaizen(State &state, int jyama_i, int x0, int y0, int x1, int y1){
    Ad &ad = state.ads[jyama_i];
    ll new_pena = PENA_K-1;
    ll prev_pena = calc_ad_pena(state.ads[jyama_i]);
    ll c_pena;
    int ax0=-1,ax1=-1,ay0=-1,ay1=-1;
    c_pena = calc_ad_pena2(ad.x0,ad.y0, x0,ad.y1, ad.tx, ad.ty, ad.r);
    if(c_pena < new_pena){
        new_pena = c_pena;
        ax0=ad.x0, ay0=ad.y0, ax1=x0, ay1=ad.y1;
    }
    c_pena = calc_ad_pena2(x1,ad.y0, ad.x1,ad.y1, ad.tx, ad.ty, ad.r);
    if(c_pena < new_pena){
        new_pena = c_pena;
        ax0=x1, ay0=ad.y0, ax1=ad.x1, ay1=ad.y1;
    }
    c_pena = calc_ad_pena2(ad.x0,ad.y0, ad.x1,y0, ad.tx, ad.ty, ad.r);
    if(c_pena < new_pena){
        new_pena = c_pena;
        ax0=ad.x0, ay0=ad.y0, ax1=ad.x1, ay1=y0;
    }
    c_pena = calc_ad_pena2(ad.x0,y1, ad.x1,ad.y1, ad.tx, ad.ty, ad.r);
    if(c_pena < new_pena){
        new_pena = c_pena;
        ax0=ad.x0, ay0=y1, ax1=ad.x1, ay1=ad.y1;
    }
    
    MoveRes res;
    res.adi = jyama_i;
    if(new_pena>=PENA_K-1){
        res.kaizen= -INF;
        return res;
    }
    res.kaizen = prev_pena - new_pena; // 絶対にマイナス
    res.x0=ax0, res.x1=ax1, res.y0=ay0, res.y1=ay1;
    return res;
}



bool try_to_expand_4dirs(State &state, int adi, int dx0, int dx1, int dy0, int dy1, double yaki_prob, double tt, ll pre_kaizen=0, bool force=false){
    Ad &ad = state.ads[adi];
    if(ad.get_s()>=ad.r && !force) return false;
 
    ll kaizen = pre_kaizen;
    ll prev_ad_pena = calc_ad_pena(ad);
    vector<int> jyama_ads;
    vector<MoveRes> jyama_move_resl;
 
    if(dx0>ad.x0) dx0=ad.x0;
    if(dx1>HW-ad.x1) dx1=HW-ad.x1;
    if(dy0>ad.y0) dy0=ad.y0;
    if(dy1>HW-ad.y1) dy1=HW-ad.y1;
    int x0=ad.x0-dx0, x1=ad.x1+dx1, y0=ad.y0-dy0, y1=ad.y1+dy1;
    if(x1<=x0 || y1<=y0) return false;
    
    ll new_ad_pena = calc_ad_pena2(x0,y0, x1,y1, ad.tx,ad.ty, ad.r);
    if(new_ad_pena==PENA_K) return false;
    
    kaizen+=(prev_ad_pena-new_ad_pena);
    jyama_ads = get_jyama_inds(state, x0, x1, y0, y1);
    for(int jyama_i:jyama_ads){
        if(jyama_i==adi) continue;
        MoveRes res=calc_jyama_pena_kaizen(state, jyama_i, x0,y0, x1,y1);
        if(res.kaizen == -INF) return false;
        jyama_move_resl.push_back(res);
        kaizen+=res.kaizen;
    }
    // if(force)DEBUG(kaizen);
    if(kaizen>0 || yaki_prob<exp(kaizen/tt) ){
        ad.x0=x0, ad.x1=x1, ad.y0=y0, ad.y1=y1;
        update_pena(state,adi);
        for(MoveRes res:jyama_move_resl){
            Ad &c_ad=state.ads[res.adi];
            c_ad.x0=res.x0, c_ad.x1=res.x1, c_ad.y0=res.y0, c_ad.y1=res.y1;
            update_pena(state,res.adi);
        }
        return true;
    }
    return false;
}


// もうこれいらないのでは？ try_to_expand でdist指定
bool try_to_expand_large(State &state, int adi, int dir, ll dist, bool debug=false){
    Ad &ad = state.ads[adi];
    if(ad.get_s()>=ad.r) {
        // DEBUG(adi);
        return false;
    }

    vector<int> jyama_ads;
    if(dir==0){
        if(ad.x0==0)return false; 
        dist=min(dist, ad.x0);
        jyama_ads = get_jyama_inds(state, ad.x0-dist, ad.x0, ad.y0, ad.y1);
        if(!jyama_ads.empty()) return false;
        ad.x0-=dist;
        update_pena(state,adi);
        return true;
    }
    //x+1
    else if(dir==1){
        if(ad.x1==HW)return false; 
        dist=min(dist, HW-ad.x1);
        jyama_ads = get_jyama_inds(state, ad.x1, ad.x1+dist, ad.y0, ad.y1);
        if(!jyama_ads.empty()) return false;
        ad.x1+=dist;
        update_pena(state,adi);
        return true;
    }
    else if(dir==2){
        if(ad.y0==0)return false; 
        dist=min(dist, ad.y0);
        jyama_ads = get_jyama_inds(state, ad.x0, ad.x1, ad.y0-dist, ad.y0);
        if(!jyama_ads.empty()) return false;
        ad.y0-=dist;
        update_pena(state,adi);
        return true;  
    }
    //y+1
    else if(dir==3){
        if(ad.y1==HW)return false; 
        dist=min(dist, HW-ad.y1);
        jyama_ads = get_jyama_inds(state, ad.x0, ad.x1, ad.y1, ad.y1+dist);
        if(!jyama_ads.empty()) return false;
        ad.y1+=dist;
        update_pena(state,adi);
        return true;
    }
    return false;
}


void DEBUG_AD(Ad &ad){
    DEBUG(ad.x0);
    DEBUG(ad.x1);
    DEBUG(ad.y0);
    DEBUG(ad.y1);
    DEBUG(ad.tx);
    DEBUG(ad.ty);
}

ll DEBUG_SCORE(State &state){
    ll score=0;
    for(Ad ad : state.ads){
        // TODO: 必要なら、広告の位置を確認（今は全ての広告の初期位置は所望の位置） 
        double c_pena_root = 1.0-(1.0)*ad.get_s()/ad.r;
        if(ad.get_s()>ad.r){
            c_pena_root = 1.0-(1.0)*ad.r/ad.get_s();
        }
        double c_score=1-(c_pena_root*c_pena_root);
        score+=PENA_K*c_score;
    }
    return score/state.ads.size();
}

// ペナの改善値を返す（悪化するので、マイナス） 0のときは、何もなし
ll shrink_ad(State &state, int adi, int dir, int dist=1){
    Ad &ad = state.ads[adi];
    ll prev_pena=calc_ad_pena(ad);
    if(dir==0 && ad.x1-ad.x0>dist){
        if(ad.tx<ad.x0+dist)return 0ll;
        ad.x0+=dist;
        ll new_pena=calc_ad_pena(ad);
        update_pena(state,adi);
        return (prev_pena-new_pena);
    }
    if(dir==1 && ad.x1-ad.x0>dist){
        if(ad.x1-dist<=ad.tx)return 0ll;
        ad.x1-=dist;
        ll new_pena=calc_ad_pena(ad);
        update_pena(state,adi);
        return (prev_pena-new_pena);
    }
    if(dir==2 && ad.y1-ad.y0>dist){
        if(ad.ty<ad.y0+dist)return 0ll;
        ad.y0+=dist;
        ll new_pena=calc_ad_pena(ad);
        update_pena(state,adi);
        return (prev_pena-new_pena);
    }
    if(dir==3 && ad.y1-ad.y0>1){
        if(ad.y1-dist<=ad.ty)return 0ll;
        ad.y1-=dist;
        ll new_pena=calc_ad_pena(ad);
        update_pena(state,adi);
        return (prev_pena-new_pena);
    }
    return 0;
}


void PRINT_OUTPUT(State &state, int n){
    vector<Ad> ansl(n);
    for(Ad ad:state.ads){
        ansl[ad.orig_i] = ad;
    }
    cout<<n<<endl;
    for(Ad ad:ansl){
        cout << ad.x0 << " " << ad.y0 << " " << ad.x1 << " " << ad.y1 << endl;
    }
}

// 2分探索で早くなる　（必要？）
bool slide_ad_max(State &state, int adi, int dir, int dmax=10000){
    Ad &ad=state.ads[adi];
    int x0=ad.x0, x1=ad.x1, y0=ad.y0, y1=ad.y1;
    int xy=x0*y0;
    int move_cnt=0;
    vector<int> jyama_ads;
    if(dir==0 && x0!=0){
        int max_d=min(ad.x1-ad.tx-1, ad.x0);
        max_d=min(max_d,dmax);
        for(int dx=1; dx<=max_d; dx++){
            jyama_ads = get_jyama_inds(state, x0-dx, x0-dx+1, y0, y1);
            if(jyama_ads.empty()){
                move_cnt++;
                ad.x0-=1; ad.x1-=1;
            }
            else break;
        }
    }
    if(dir==1 && x1!=HW){
        int max_d=min(ad.tx-ad.x0, HW-ad.x1);
        max_d=min(max_d,dmax);
        for(int dx=1; dx<=max_d; dx++){
            bool ok=true;
            jyama_ads = get_jyama_inds(state, x1-1+dx, x1+dx, y0, y1);
            if(jyama_ads.empty()){
                move_cnt++;
                ad.x0+=1; ad.x1+=1;
            }
            else break;
        }
    }
    if(dir==2 && y0!=0){
        int max_d=min(ad.y1-ad.ty-1, ad.y0);
        max_d=min(max_d,dmax);
        for(int dy=1; dy<=max_d; dy++){
            bool ok=true;
            jyama_ads = get_jyama_inds(state, x0, x1, y0-dy, y0-dy+1);
            if(jyama_ads.empty()){
                move_cnt++;
                ad.y0-=1; ad.y1-=1;
            }
            else break;
        }
    }
    if(dir==3 && y1!=HW){
        int max_d=min(ad.ty-ad.y0, HW-ad.y1);
        max_d=min(max_d,dmax);
        for(int dy=1; dy<=max_d; dy++){
            bool ok=true;
            jyama_ads = get_jyama_inds(state, x0, x1, y1-1+dy, y1+dy);
            if(jyama_ads.empty()){
                move_cnt++;
                ad.y0+=1; ad.y1+=1;
            }
            else break;
        }
    }
    if(move_cnt==0)return false;
    else return true;
}

bool check_overlap(int xa0, int xa1, int xb0, int xb1){
    if(xa1<=xb0) return false;
    if(xb1<=xa0) return false;
    return true;
}

int get_x_percent_adi(State &state, double percent){
    ll ok=1, ng=n+1;
    while(abs(ok-ng)>1){
        ll mid = (ok+ng)/2;
        bool ok_flag = true;
        double val=(1.0)*state.pena_fw.sum(0,mid)/state.pena_sum;
        if(val<percent){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    int res=ok-1;
    if(res>=n) res=n-1;
    return res;
}


vector<int> get_jyama_inds(State &state, int x0, int x1, int y0, int y1){
    vector<int> jyama_inds;
    for(int i=0 ; i<n ;i++){
        Ad &ad=state.ads[i];
        if( check_overlap(x0,x1, ad.x0,ad.x1) && check_overlap(y0,y1, ad.y0,ad.y1)){
            jyama_inds.push_back(i);
        }
    }
    return jyama_inds;
}

// ll transform(State &state, int adi, int dir){

// }

struct MoveCom{
    int adi;
    int dx0,dx1,dy0,dy1;
    MoveCom(int adi,int dx0,int dx1,int dy0,int dy1)
    :adi(adi),dx0(dx0),dx1(dx1),dy0(dy0),dy1(dy1){};
};

struct AdInfo{
    int adi;
    int x0,x1,y0,y1;
    AdInfo(int adi, int x0, int y0, int x1, int y1):adi(adi),x0(x0),x1(x1),y0(y0),y1(y1){};
};
bool try_to_expand_4dirs_multi(State &state, vector<MoveCom> move_coms, double yaki_prob, double tt){
    vector<AdInfo> orig_adinfos; //失敗した元のに戻す
 
    ll kaizen=0;
    for(MoveCom mc:move_coms){
        Ad &ad = state.ads[mc.adi];
        orig_adinfos.push_back(AdInfo(mc.adi, ad.x0, ad.y0, ad.x1, ad.y1));
        int dx0=mc.dx0, dx1=mc.dx1, dy0=mc.dy0, dy1=mc.dy1;
        ll prev_ad_pena = calc_ad_pena(ad);
        vector<int> jyama_ads;
        vector<MoveRes> jyama_move_resl;
 
        if(dx0>ad.x0) dx0=ad.x0;
        if(dx1>HW-ad.x1) dx1=HW-ad.x1;
        if(dy0>ad.y0) dy0=ad.y0;
        if(dy1>HW-ad.y1) dy1=HW-ad.y1;
        int x0=ad.x0-dx0, x1=ad.x1+dx1, y0=ad.y0-dy0, y1=ad.y1+dy1;
        if(x1<=x0 || y1<=y0) continue;
        
        ll new_ad_pena = calc_ad_pena2(x0,y0, x1,y1, ad.tx,ad.ty, ad.r);
        if(new_ad_pena==PENA_K) continue;
        
        kaizen+=(prev_ad_pena-new_ad_pena);
        jyama_ads = get_jyama_inds(state, x0, x1, y0, y1);
        bool success=true;
        for(int jyama_i:jyama_ads){
            if(jyama_i==mc.adi) continue;
            Ad &c_ad=state.ads[jyama_i];
            orig_adinfos.push_back(AdInfo(jyama_i, c_ad.x0, c_ad.y0, c_ad.x1, c_ad.y1));
            MoveRes res=calc_jyama_pena_kaizen(state, jyama_i, x0,y0, x1,y1);
            if(res.kaizen == -INF){
                success=false; break;
            }
            jyama_move_resl.push_back(res);
            kaizen+=res.kaizen;
        }
        if(success){
            ad.x0=x0, ad.x1=x1, ad.y0=y0, ad.y1=y1;
            for(MoveRes res:jyama_move_resl){
                Ad &c_ad=state.ads[res.adi];
                c_ad.x0=res.x0, c_ad.x1=res.x1, c_ad.y0=res.y0, c_ad.y1=res.y1;
            }
        }
    }
    // if(kaizen>0 || yaki_prob<exp(kaizen/tt) ){
    if(kaizen>0 || yaki_prob<exp(kaizen/tt) ){
        return true;
    }
    else{
        reverse(ALL(orig_adinfos));
        for(AdInfo &adinfo:orig_adinfos){
            Ad &c_ad=state.ads[adinfo.adi];
            c_ad.x0=adinfo.x0, c_ad.x1=adinfo.x1, c_ad.y0=adinfo.y0, c_ad.y1=adinfo.y1;
        }
        return false;
    }
}





bool try_to_transform(State &state, int adi){
    int shrink_dir;
    int shrink_kaizen=0;
    bool shrink=true;
    Ad &ad = state.ads[adi];

    // shrink_dir=rand_dir4(mt64);

    // double xyratio = (1.0)*(ad.x1-ad.x0)/((ad.x1-ad.x0)+(ad.y1-ad.y0));
    double xyratio=0.5;
    if(rand_01(mt64)<xyratio) shrink_dir=0;
    else shrink_dir=2;
    shrink_dir+=rand_dir4(mt64)%2;

    int shrink_dist_max;
    if(shrink_dir==0)      shrink_dist_max=ad.tx-ad.x0;
    else if(shrink_dir==1) shrink_dist_max=ad.x1-ad.tx-1;
    else if(shrink_dir==2) shrink_dist_max=ad.ty-ad.y0;
    else if(shrink_dir==3) shrink_dist_max=ad.y1-ad.ty-1;
    
    // dist_max を 0〜500 で適当に選んだ方が精度良かった...?
    // shrink_dist_max=2*shrink_dist_max/4;
    // shrink_dist_max=2*shrink_dist_max/3;
    shrink_dist_max=3*shrink_dist_max/5;
    // shrink_dist_max=2*shrink_dist_max/2;

    if(shrink_dist_max<=0) return false;
    ll shrink_dist=1+rand_hw(mt64)%shrink_dist_max;
    // if(shrink_dist<shrink_dist_max/3) shrink_dist+=shrink_dist_max/3;

    // if(ad.get_s()>ad.r)DEBUG(ad.get_s());
    shrink_kaizen=shrink_ad(state,adi,shrink_dir,shrink_dist);
    if(shrink_kaizen==0) shrink=false;
    // if(ad.get_s()>ad.r)DEBUG(ad.get_s());
    
    ll need_dist;
    if(shrink_dir<=1) need_dist=shrink_dist*(ad.y1-ad.y0)/(ad.x1-ad.x0);
    else need_dist=shrink_dist*(ad.x1-ad.x0)/(ad.y1-ad.y0);

    int dir=rand_dir4(mt64);
    if(shrink_dir<=1) dir=2+dir%2;
    else dir=dir%2;
    bool ret = try_to_expand_large(state, adi, dir, need_dist );
    if(!ret && shrink){
        ret = try_to_expand_large(state, adi, shrink_dir, shrink_dist, true); // shrinkを戻す
        // if(!ret) DEBUG(ret); // なぜかこれになる。なぜ？
    }
    update_pena(state,adi);
    return ret;
}


void cut_over_area(State &state){
    for(Ad &ad:state.ads){
        if(ad.r<ad.get_s()){
            bool ret;
            ll rem=ad.get_s()-ad.r;
            ll xd=(ad.x1-ad.x0);
            ll yneed=rem/xd;
            ll yd=(ad.y1-ad.y0);
            ll xneed=rem/yd;
            xneed*=-1;
            yneed*=-1;

            for(int dir=0;dir<4;dir++){
                // int dir=rand_dir4(mt64);
                if(dir==0) ret = try_to_expand_4dirs(state, ad.orig_i, 0,0, yneed,0, 1.0, 1.0, 0, true);
                else if(dir==1) ret = try_to_expand_4dirs(state, ad.orig_i, 0,0, 0,yneed, 1.0, 1.0, 0, true);
                else if(dir==2) ret = try_to_expand_4dirs(state, ad.orig_i, xneed,0, 0,0, 1.0, 1.0, 0, true);
                else if(dir==3) ret = try_to_expand_4dirs(state, ad.orig_i, 0,xneed, 0,0, 1.0, 1.0, 0, true);
                if(ret)break;
            }            
        }
    }
}

void solve(){
    TimeManager tm;
    cin>>n;
    uniform_int_distribution<int> rand_ad(0, n-1);
    State state(n);
    REP(i,n){
        int x,y,r; cin>>x>>y>>r;
        state.ads.push_back(Ad(x,y,r,i));
    }

    /////// これ、むしろないほうが良いかも？いや、ある方が良いかも...
    /////// 高いやつはちょっと低くなる、低いやつはちょっと高くなる？
    // vector<P> ad_t_ind_vec;
    // for(int i=0;i<n;i++) ad_t_ind_vec.push_back({state.ads[i].r, i});
    // sort(ALL(ad_t_ind_vec), greater<>());
    // int loops=0;
    // int FIRST_LOOP = 2000;
    // for(double thre:{0.7,0.5,0.25}){
    //     for(auto&[r,adi]:ad_t_ind_vec){
    //         int dists[4]={0,0,0,0};
    //         for(int j=0;j<FIRST_LOOP;j++){
    //             for(int i=0;i<4;i++){
    //                 dists[i]=rand_hw(mt64)%1250-0; dists[i]=max(dists[i],0); //無難
    //                 if(rand_01(mt64)<0.2) dists[i]*=(-1);
    //             }
    //             bool ret = try_to_expand_4dirs(state, adi, dists[0], dists[1], dists[2], dists[3], 1.0, PENA_K, 0, false);
    //             if(calc_ad_pena(state.ads[adi])<PENA_K*thre) {break;}
    //         }
    //         if((loops++)>n/5)break;
    //     }
    // }
    // DEBUG(tm.get_time(true));

    double T0=2e8 *n;
    // double T1=5e3 *n;
    double T1=1e4 *n;
    double TL = 4900.0;
    TL*=2;
    
    // for(int i=0;i<n;i++)update_pena(state,i);

    int cnt=0;
    int dists[4]={0,0,0,0};
    int adi;
    int next_adi=rand_ad(mt64);
    int same_cnt=0;
    while(tm.check(TL)){
        cnt++;
        
        double t01=tm.get_time()/TL;
        double tt=pow(T0,1.0-t01)*pow(T1,t01);

        // if(t01<0.01) adi = get_x_percent_adi(state,rand_01(mt64));
        // adi = rand_ad(mt64);
        adi = next_adi;

        //// もうこれはない方が精度高そう？
        if(t01<0.3 && state.ads[adi].pena<0.1*PENA_K)continue;
        // if(state.ads[adi].pena<0.5*(1.0-t01)*PENA_K)continue;

        int dir = rand_dir4(mt64);

        //// たまにスライドさせてみる。縮小&拡大ができた今、要る？
        if(rand_01(mt64)<0.0001*t01*t01){
            int slide_dir=rand_dir4(mt64);
            slide_ad_max(state, adi, slide_dir);
        }

        // 4方向に拡大。ランダムで、たまに縮む方向もある。
        double yaki_prob = rand_01(mt64);
        for(int i=0;i<4;i++){
            // dists[i]=rand_hw(mt64)%1250-400; dists[i]=max(dists[i],0);
            // dists[i]*=50; dists[i]/=n;
            // dists[i]=rand_hw(mt64)%1000-250; dists[i]=max(dists[i],0); //無難

            dists[i]=rand_hw(mt64)%1000-500; dists[i]=max(dists[i],0);
            dists[i]*=(t01*t01+1.0);

            // dists[i]=rand_hw(mt64)%1000-500; dists[i]=max(dists[i],0);
            // if(t01>0.8){
            //     dists[i]=rand_hw(mt64)%2000-1000; dists[i]=max(dists[i],0);
            // }

            // if(t01>0.7)dists[i]=rand_hw(mt64)%1500-500; dists[i]=max(dists[i],0);
            // if(rand_01(mt64)<0.1) dists[i]*=(-1); //0.3がbest?
            if(rand_01(mt64)<0.2) dists[i]*=(-1); //0.3がbest?
        }
        // まだペナがでかい広告は、無理やりでも拡大するために 焼き鈍し確率をあげる
        if(0.5<t01 && t01<0.8 && calc_ad_pena(state.ads[adi])>0.5*PENA_K ){
            // yaki_prob*=(5.0*calc_ad_pena(state.ads[adi])/PENA_K);
            // yaki_prob*=5; // 無難に結構良い。（追記）これ、yaki_probを大きくではなく小さくするのでは？間違い。
            // yaki_prob=0.0;
            yaki_prob/=5000.0;
        }
        bool ret = try_to_expand_4dirs(state, adi, dists[0], dists[1], dists[2], dists[3], yaki_prob, tt, 0);


        //// たまに、何個も動かしてみる？ なんかバグあるかも？
        if(rand_01(mt64)<0.01){
            vector<MoveCom> coms;
            for(int j=0;j<10;j++){
                adi = rand_ad(mt64);
                for(int i=0;i<4;i++){
                    // dists[i]=rand_hw(mt64)%500-250; dists[i]=max(dists[i],0);
                    dists[i]=rand_hw(mt64)%250-125; dists[i]=max(dists[i],0);
                    if(rand_01(mt64)<0.3*t01) dists[i]*=(-1); //0.3がbest?
                }
                coms.push_back(MoveCom(adi, dists[0], dists[1], dists[2], dists[3]));
            }
            bool ret2 = try_to_expand_4dirs_multi(state, coms, yaki_prob, tt);
        }

        ////たまに消してみる？
        if(t01<0.75 && rand_01(mt64)<0.00001){
            Ad &ad=state.ads[adi];
            if(calc_ad_pena(ad)<0.02*PENA_K){
                ad.x0=ad.tx, ad.y0=ad.ty, ad.x1=ad.x0+1, ad.y1=ad.y0+1;
                update_pena(state, adi);
            }
        }
        if(t01<0.75 && rand_01(mt64)<0.001){
            int adii=rand_ad(mt64);
            Ad &ad=state.ads[adii];
            if(calc_ad_pena(ad)>0.5*PENA_K){
                int ddir=rand_dir4(mt64);
                if(dir==0) ad.x0=ad.tx;
                else if(dir==1) ad.x1=ad.tx+1;
                else if(dir==2) ad.y0=ad.ty;
                else if(dir==3) ad.y1=ad.ty+1;
            }
            // if(calc_ad_pena(ad)<0.02*PENA_K){
                // ad.x0=ad.tx, ad.y0=ad.ty, ad.x1=ad.x0+1, ad.y1=ad.y0+1;
                // update_pena(state, adi);
            // }
        }

        //// ヤバイやつは続けて選んでみる
        if(t01>0.8 && same_cnt<1000 &&calc_ad_pena(state.ads[adi])>PENA_K*0.6){
            next_adi=adi;
            same_cnt++;
        }
        else{
            next_adi=rand_ad(mt64);
            same_cnt=0;
        }


      
        // if(cnt%200000==0){
        //     PRINT_OUTPUT(state,n);
        // }
    }

    // ll prev=DEBUG_SCORE(state);
    // 余分な部分をカット
    cut_over_area(state);
    // DEBUG(DEBUG_SCORE(state)-prev);


    TL=4950.0;
    TL*=2;
    ll lastcnt=0;

    ll prev=DEBUG_SCORE(state);
    while(tm.check(TL)){ 
        for(int adi=0 ; adi<n ; adi++){
            while(tm.check(TL)){
                int retcnt=0;
                for(int dir=0; dir<4 ; dir++){
                    ll dist = rand_hw(mt64)%20 + 1;
                    bool ret;
                    if(dir==0) ret = try_to_expand_4dirs(state, adi, dist, 0, 0, 0, 1.1, PENA_K, 0);
                    if(dir==1) ret = try_to_expand_4dirs(state, adi, 0, dist, 0, 0, 1.1, PENA_K, 0);
                    if(dir==2) ret = try_to_expand_4dirs(state, adi, 0, 0, dist, 0, 1.1, PENA_K, 0);
                    if(dir==3) ret = try_to_expand_4dirs(state, adi, 0, 0, 0, dist, 1.1, PENA_K, 0);
                    if(ret) retcnt++;
                }
                if(retcnt==0) break;
            }
            if(!tm.check(TL)) {
                break;
            }
        }
        for(int adi=0 ; adi<n ; adi++){
            int dir = rand_dir4(mt64);
            int dmax=rand_hw(mt64)%10000;
            slide_ad_max(state, adi, dir, dmax);
            // try_to_transform(state, adi);
            if(!tm.check(TL)) break;
        }
        if(!tm.check(TL)) break;
        // lastcnt++;
        // DEBUG(DEBUG_SCORE(state)-prev);
        // prev=DEBUG_SCORE(state);
        // DEBUG(lastcnt);
    }



    for(Ad &ad:state.ads){
        // if(ad.r<ad.get_s()){DEBUG(ad.get_s()*1.0/ad.r); DEBUG(ad.get_s());}
        // DEBUG((PENA_K-calc_ad_pena(ad))*PENA_K);
        cout << ad.x0 << " " << ad.y0 << " " << ad.x1 << " " << ad.y1 << endl;
    }

    DEBUG(DEBUG_SCORE(state));
    DEBUG(cnt);
    // DEBUG(shrink_success);
    // DEBUG(expand_success);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}