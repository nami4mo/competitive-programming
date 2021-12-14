/*
    UDLR
    0123
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

namespace visgen{
class Graphics {
public:
	double screenW;
	double screenH;
	ostringstream data;

	double sr;
	double sg;
	double sb;
	double sa;
	double fr;
	double fg;
	double fb;
	double fa;

	Graphics() : screenW(1), screenH(1), sr(0), sg(0), sb(0), sa(1), fr(1), fg(1), fb(1), fa(1) {
	}

	void screen(int width, int height) {
		screenW = width;
		screenH = height;
	}

	void clear() {
		data.str("");
		data.clear(stringstream::goodbit);
	}

	void stroke(double r, double g, double b) {
		stroke(r, g, b, 1);
	}

	void stroke(double r, double g, double b, double a) {
		sr = r;
		sg = g;
		sb = b;
		sa = a;
	}

	void noStroke() {
		stroke(0, 0, 0, 0);
	}

	void fill(double r, double g, double b) {
		fill(r, g, b, 1);
	}

	void fill(double r, double g, double b, double a) {
		fr = r;
		fg = g;
		fb = b;
		fa = a;
	}

	void noFill() {
		fill(0, 0, 0, 0);
	}

	void line(double x1, double y1, double x2, double y2) {
		data << "<line x1=\"" << x1 << "\" y1=\"" << y1 << "\" x2=\"" << x2 << "\" y2=\"" << y2 << "\" " << stroke() << "/>\n";
	}

	void rect(double x, double y, double w, double h) {
		data << "<rect x=\"" << x << "\" y=\"" << y << "\" width=\"" << w << "\" height=\"" << h << "\" " << stroke() << " " + fill() << "/>\n";
	}

	void text(string str, double x, double y, double size = 16) {
		data << "<text text-anchor=\"middle\" x=\"" << x << "\" y=\"" << y << "\" font-size=\"" << size << "\" " << fill() << " >" << str << "</text>\n";
	}

	string dump(string id = "", string style = "", int widthPx = -1, int heightPx = -1) const {
		ostringstream res;
		res << "<svg ";
		if (id != "") res << "id=\"" + id + "\" ";
		if (style != "") res << "style=\"" + style + "\" ";
		if (widthPx != -1) res << "width=\"" << widthPx << "\" ";
		if (heightPx != -1) res << "height=\"" << heightPx << "\" ";
		res << "viewBox=\"-1 -1 " << screenW + 2 << " " << screenH + 2 << "\" xmlns=\"http://www.w3.org/2000/svg\">\n" << data.str() << "</svg>";
		return res.str();
	}

private:
	string stroke() const {
		return "stroke=\"" + rgb(sr, sg, sb) + "\" stroke-opacity=\"" + s(sa) + "\"";
	}

	string fill() const {
		return "fill=\"" + rgb(fr, fg, fb) + "\" fill-opacity=\"" + s(fa) + "\"";
	}

	string rgb(double r, double g, double b) const {
		return "rgb(" + s(lround(r * 255)) + "," + s(lround(g * 255)) + "," + s(lround(b * 255)) + ")";
	}

	string s(double x) const {
		return to_string(x);
	}
};

class Movie {
public:
	vector<string> svgs;

	Movie() {
	}

	void clear() {
		svgs.clear();
	}

	void addFrame(Graphics& g) {
		svgs.push_back(g.dump("f" + to_string(svgs.size()), "display:none;pointer-events:none;user-select:none;"));
	}

	string dumpHtml(int fps) {
		ostringstream res;
		res << "<html><body><div id=\"text\">loading...</div>" << endl;
		for (string& svg : svgs) {
			res << svg << endl;
		}

		res << "<script>\nlet numFrames = " << svgs.size() << ", fps = " << fps << ";";
		res << R"(
	let text = document.getElementById("text");
	let frames = [];
	for (let i = 0; i < numFrames; i++) {
		let f = document.getElementById("f" + i);
		frames.push(f);
		f.style.display = "none";
	}
	let currentFrame = 0;
	let playing = true;
	setInterval(() => {
		if (!playing) return;
		text.innerText = (currentFrame + 1) + " / " + numFrames;
		frames[(currentFrame - 1 + numFrames) % numFrames].style.display = "none";
		frames[currentFrame].style.display = null;
		currentFrame = (currentFrame + 1) % numFrames;
		if (currentFrame == 0) playing = false;
	}, 1000 / fps);
	window.onmousedown = e => { if (e.button == 0) playing = true; };
;)";
		res << "</script>" << endl;
		res << "</body></html>" << endl;
		return res.str();
	}
private:
};

}
using namespace visgen;

const int HW=30;
void solve(){
    vector<vector<ll>> hl(HW, vector<ll>(HW-1,0));
    vector<vector<ll>> vl(HW-1, vector<ll>(HW,0));
    REP(y,HW){
        REP(x,HW-1){
            cin>>hl[y][x];
        }
    }
    REP(y,HW-1){
        REP(x,HW){
            cin>>vl[y][x];
        }
    }
    
    //
	Graphics g;
	Movie mov;
	int w = 600;
	int h = 600;
    g.screen(w, h);
    //
    int qn; cin>>qn;
    REP(i,qn){
        vector<vector<ll>> chl(HW, vector<ll>(HW-1,0));
        vector<vector<ll>> cvl(HW-1, vector<ll>(HW,0));

        vector<vector<ll>> dhl(HW, vector<ll>(HW-1,0));
        vector<vector<ll>> dvl(HW-1, vector<ll>(HW,0));

        g.clear();

		g.stroke(0.5, 0.0, 0.0, 0.7);
		g.fill(0.5, 0.0, 0.0, 0.7);
		g.rect(300, 10, 3, 10);
		
		g.stroke(0.25, 0.0, 0.0, 0.45);
		g.fill(0.25, 0.0, 0.0, 0.45);
		g.rect(300, 20, 3, 10);

		g.stroke(0.0, 0.0, 0.25, 0.45);
		g.fill(0.0, 0.0, 0.25, 0.45);
		g.rect(300, 30, 3, 10);

		g.stroke(0.0, 0.0, 0.5, 0.7);
		g.fill(0.0, 0.0, 0.5, 0.7);
		g.rect(300, 40, 3, 10);

		g.noFill();
        const int gc=8;
        REP(y,HW){
            REP(x,HW-1){
                cin>>chl[y][x];
                dhl[y][x]=hl[y][x]-chl[y][x];
				ll dabs=abs(dhl[y][x]);
				double color_b = dhl[y][x]/2500.0;
				double color_r = (-1)*dhl[y][x]/2500.0;
                double opacity = dabs/2500.0;
                g.fill(color_r,0.0,color_b,opacity+0.2);
                g.stroke(color_r,0.0,color_b,opacity+0.2);
                g.rect(x*gc, y*gc, gc, 0.5);
            }
        }
        REP(y,HW-1){
            REP(x,HW){
                cin>>cvl[y][x];
                dvl[y][x]=vl[y][x]-cvl[y][x];
				ll dabs=abs(dvl[y][x]);
				double color_b = dvl[y][x]/2500.0;
				double color_r = (-1)*dvl[y][x]/2500.0;
                double opacity = dabs/2500.0;
                g.fill(color_r,0.0,color_b,opacity+0.2);
                g.stroke(color_r,0.0,color_b,opacity+0.2);
                g.rect(x*gc, y*gc, 0.5, gc);
            }
        }
        mov.addFrame(g);
		// DEBUG(i);
    }
    string html = mov.dumpHtml(10);
	// 動画を保存
	ofstream fout;
	fout.open("movie2.html", ios::out);
	fout << html << endl;
	fout.close();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}