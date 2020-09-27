#ifndef ATCODER_INTERNAL_BITOP_HPP
#define ATCODER_INTERNAL_BITOP_HPP 1
#ifdef _MSC_VER
#include <intrin.h>
#endif
namespace atcoder
{
    namespace internal
    {
        // @param n `0 <= n`
        // @return minimum non-negative `x` s.t. `n <= 2**x`
        int ceil_pow2(int n)
        {
            int x = 0;
            while ((1U << x) < (unsigned int)(n))
                x++;
            return x;
        }
        // @param n `1 <= n`
        // @return minimum non-negative `x` s.t. `(n & (1 << x)) != 0`
        int bsf(unsigned int n)
        {
#ifdef _MSC_VER
            unsigned long index;
            _BitScanForward(&index, n);
            return index;
#else
            return __builtin_ctz(n);
#endif
        }
    } // namespace internal
} // namespace atcoder
#endif // ATCODER_INTERNAL_BITOP_HPP
#ifndef ATCODER_LAZYSEGTREE_HPP
#define ATCODER_LAZYSEGTREE_HPP 1
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
namespace atcoder
{
    template <class S,
              S (*op)(S, S),
              S (*e)(),
              class F,
              S (*mapping)(F, S),
              F (*composition)(F, F),
              F (*id)()>
    struct lazy_segtree
    {
    public:
        lazy_segtree() : lazy_segtree(0) {}
        lazy_segtree(int n) : lazy_segtree(std::vector<S>(n, e())) {}
        lazy_segtree(const std::vector<S> &v) : _n(int(v.size()))
        {
            log = internal::ceil_pow2(_n);
            size = 1 << log;
            d = std::vector<S>(2 * size, e());
            lz = std::vector<F>(size, id());
            for (int i = 0; i < _n; i++)
                d[size + i] = v[i];
            for (int i = size - 1; i >= 1; i--)
            {
                update(i);
            }
        }

        void set(int p, S x)
        {
            assert(0 <= p && p < _n);
            p += size;
            for (int i = log; i >= 1; i--)
                push(p >> i);
            d[p] = x;
            for (int i = 1; i <= log; i++)
                update(p >> i);
        }

        S get(int p)
        {
            assert(0 <= p && p < _n);
            p += size;
            for (int i = log; i >= 1; i--)
                push(p >> i);
            return d[p];
        }

        S prod(int l, int r)
        {
            assert(0 <= l && l <= r && r <= _n);
            if (l == r)
                return e();

            l += size;
            r += size;

            for (int i = log; i >= 1; i--)
            {
                if (((l >> i) << i) != l)
                    push(l >> i);
                if (((r >> i) << i) != r)
                    push(r >> i);
            }

            S sml = e(), smr = e();
            while (l < r)
            {
                if (l & 1)
                    sml = op(sml, d[l++]);
                if (r & 1)
                    smr = op(d[--r], smr);
                l >>= 1;
                r >>= 1;
            }

            return op(sml, smr);
        }

        S all_prod() { return d[1]; }

        void apply(int p, F f)
        {
            assert(0 <= p && p < _n);
            p += size;
            for (int i = log; i >= 1; i--)
                push(p >> i);
            d[p] = mapping(f, d[p]);
            for (int i = 1; i <= log; i++)
                update(p >> i);
        }
        void apply(int l, int r, F f)
        {
            assert(0 <= l && l <= r && r <= _n);
            if (l == r)
                return;

            l += size;
            r += size;

            for (int i = log; i >= 1; i--)
            {
                if (((l >> i) << i) != l)
                    push(l >> i);
                if (((r >> i) << i) != r)
                    push((r - 1) >> i);
            }

            {
                int l2 = l, r2 = r;
                while (l < r)
                {
                    if (l & 1)
                        all_apply(l++, f);
                    if (r & 1)
                        all_apply(--r, f);
                    l >>= 1;
                    r >>= 1;
                }
                l = l2;
                r = r2;
            }

            for (int i = 1; i <= log; i++)
            {
                if (((l >> i) << i) != l)
                    update(l >> i);
                if (((r >> i) << i) != r)
                    update((r - 1) >> i);
            }
        }

        template <bool (*g)(S)>
        int max_right(int l)
        {
            return max_right(l, [](S x) { return g(x); });
        }
        template <class G>
        int max_right(int l, G g)
        {
            assert(0 <= l && l <= _n);
            assert(g(e()));
            if (l == _n)
                return _n;
            l += size;
            for (int i = log; i >= 1; i--)
                push(l >> i);
            S sm = e();
            do
            {
                while (l % 2 == 0)
                    l >>= 1;
                if (!g(op(sm, d[l])))
                {
                    while (l < size)
                    {
                        push(l);
                        l = (2 * l);
                        if (g(op(sm, d[l])))
                        {
                            sm = op(sm, d[l]);
                            l++;
                        }
                    }
                    return l - size;
                }
                sm = op(sm, d[l]);
                l++;
            } while ((l & -l) != l);
            return _n;
        }

        template <bool (*g)(S)>
        int min_left(int r)
        {
            return min_left(r, [](S x) { return g(x); });
        }
        template <class G>
        int min_left(int r, G g)
        {
            assert(0 <= r && r <= _n);
            assert(g(e()));
            if (r == 0)
                return 0;
            r += size;
            for (int i = log; i >= 1; i--)
                push((r - 1) >> i);
            S sm = e();
            do
            {
                r--;
                while (r > 1 && (r % 2))
                    r >>= 1;
                if (!g(op(d[r], sm)))
                {
                    while (r < size)
                    {
                        push(r);
                        r = (2 * r + 1);
                        if (g(op(d[r], sm)))
                        {
                            sm = op(d[r], sm);
                            r--;
                        }
                    }
                    return r + 1 - size;
                }
                sm = op(d[r], sm);
            } while ((r & -r) != r);
            return 0;
        }

    private:
        int _n, size, log;
        std::vector<S> d;
        std::vector<F> lz;

        void update(int k) { d[k] = op(d[2 * k], d[2 * k + 1]); }
        void all_apply(int k, F f)
        {
            d[k] = mapping(f, d[k]);
            if (k < size)
                lz[k] = composition(f, lz[k]);
        }
        void push(int k)
        {
            all_apply(2 * k, lz[k]);
            all_apply(2 * k + 1, lz[k]);
            lz[k] = id();
        }
    };

} // namespace atcoder

#endif // ATCODER_LAZYSEGTREE_HPP

#include <bits/stdc++.h>
#if __has_include(<atcoder/all>)
#include <atcoder/all>
#endif
using namespace std;
using namespace atcoder;
namespace defines
{
    typedef long long ll;
    typedef pair<ll, ll> P;
    #define FOR(i, a, b) for (ll i = a; i < b; i++)  // for i in range(a,b)
    #define REP(i, n) for (ll i = 0; i < n; i++)     // for i in range(b)
    #define FORD(i, a, b) for (ll i = a; i > b; i--) // for i in range(a,b,-1)
    #define ALL(x) x.begin(), x.end()
    template <class T>
    vector<T> make_vec(size_t a)
    {
        return vector<T>(a);
    }
    template <class T, class... Ts>
    auto make_vec(size_t a, Ts... ts) { return vector<decltype(make_vec<T>(ts...))>(a, make_vec<T>(ts...)); }

/* for debug print */
#define DEBUG(x) cerr << #x << ": " << x << '\n'
#define DEBUGP(x) cerr << #x << ": (" << x.first << ", " << x.second << ")" << '\n'
#define DEBUGL(xl) dbgl_f(#xl, xl)
#define DEBUGLP(xl) dbglp_f(#xl, xl)
#define DEBUGLL(xll) dbgll_f(#xll, xll)
#define DEBUGM(xl) dbgm_f(#xl, xl)
    template <class T>
    void dbgl_f(string name, vector<T> xl)
    {
        cerr << name << ": ";
        for (T x : xl)
            cerr << x << " ";
        cerr << '\n';
    }
    template <class T, class U>
    void dbgm_f(string name, map<T, U> xl)
    {
        cerr << name << ": ";
        for (auto x : xl)
            cerr << "(" << x.first << ": " << x.second << ") ";
        cerr << '\n';
    }
    template <class T>
    void dbglp_f(string name, vector<T> xl)
    {
        cerr << name << ": ";
        for (T x : xl)
            cerr << "(" << x.first << ", " << x.second << ") ";
        cerr << '\n';
    }
    template <class T>
    void dbgll_f(string name, vector<vector<T>> xll)
    {
        cerr << name << ": " << '\n';
        for (vector<T> xl : xll)
        {
            for (T x : xl)
                cerr << x << " ";
            cerr << '\n';
        }
    }
} // namespace defines
using namespace defines;

using S = int;
using F = int;
const S INF = 1e8;

S op(S a, S b) { return std::min(a, b); }
S e() { return INF; }
S mapping(F f, S x) { return f + x; }
F composition(F f, F g) { return f + g; }
F id() { return 0; }

void solve()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n, 0);
    lazy_segtree<S, op, e, F, mapping, composition, id> seg(a);
    vector<P> ranges(m);
    REP(i, m)
    {
        int s, t;
        cin >> s >> t;
        s -= 1;
        t -= 1;
        seg.apply(s, t + 1, 1);
        ranges[i] = P(s, t);
    }
    vector<int> ans;
    REP(i, m)
    {
        if (i != 0)
        {
            int s = ranges[i - 1].first;
            int t = ranges[i - 1].second;
            seg.apply(s, t + 1, 1);
        }
        int del_s = ranges[i].first;
        int del_t = ranges[i].second;
        seg.apply(del_s, del_t + 1, -1);
        if (seg.all_prod() > 0)
        {
            ans.push_back(i + 1);
            // cout << i+1 << endl;
            // DEBUG(seg.all_prod());
        }
    }
    cout << ans.size() << endl;
    for (int a : ans)
        cout << a << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}