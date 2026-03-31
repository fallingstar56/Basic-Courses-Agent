证明 令  $ y_{1}=0, y_{n}=\sum_{k=1}^{n-1}|x_{k+1}-x_{k}| $  $ (n=2,3,\cdots) $，则  $ \{y_{n}\} $ 单调递增且有上界 M，所以  $ \{y_{n}\} $ 收敛，从而是柯西列。于是  $ \forall\varepsilon>0,\exists N\in\mathbb{N} $，当 n>N 时， $ \forall p\in\mathbb{N} $，有

 $$ 0\leqslant y_{n+p}-y_{n}<\varepsilon. $$ 

进而得

 $$ \left|x_{n+p}-x_{n}\right|=\left|\sum_{k=n}^{n+p-1}(x_{k+1}-x_{k})\right|\leqslant\sum_{k=n}^{n+p-1}\mid x_{k+1}-x_{k}\mid=y_{n+p}-y_{n}<\epsilon. $$ 

即  $ \{x_{n}\} $ 是柯西列。应用柯西收敛原理便知  $ \{x_{n}\} $ 收敛。

需要指出的是，上面这四个定理是相互等价的。也就是说，如果假设其中任意一个成立，则可推出其他所有定理。实际上，我们已经给出的逻辑关系如下：

 $$  定理 A\Rightarrow 定理 B\Rightarrow 定理 1.5.1\Rightarrow 定理 1.5.2. $$ 

只要再证明：定理 1.5.2  $ \Rightarrow $ 定理 A，便得到这四个定理的相互等价性。证明如下：

定理 1.5.2  $ \Rightarrow $ 定理 A

设数集 E 非空且有上界 b. 任取  $ a \in E $，则  $ a \leqslant b $。当 a = b 时 b 即为 E 的上确界。下面设 a < b。

将闭区间  $ [a,b] $ 两等分，若分点  $ \frac{a+b}{2} $ 是 E 的上界，则取  $ [a_{1},b_{1}]=\left[a,\frac{a+b}{2}\right] $，若分点  $ \frac{a+b}{2} $ 不是 E 的上界，则取  $ [a_{1},b_{1}]=\left[\frac{a+b}{2},b_{1}\right] $。再重复上面步骤将  $ [a_{1},b_{1}] $ 两等分，……，如此作下去，可以得到一列闭区间  $ [a_{n},b_{n}] $  $ (n=1,2,\cdots) $ 满足下列条件：

(1)  $ b_{n} $ 是 E 的上界，且  $ [a_{n}, b_{n}] \cap E \neq \varnothing $;

(2)  $ [a_n, b_n] \supseteq [a_{n+1}, b_{n+1}] $;

(3) $ b_{n}-a_{n}=2^{-n}(b-a). $

由(2)与(3)，任取 $ n\in\mathbb{N}^{*} $及 $ \forall m>n,0\leqslant b_{n}-b_{m}\leqslant b_{n}-a_{n}=2^{-n}(b-a) $，根据柯西列的定义，易见 $ \{b_{n}\} $为柯西列。应用定理1.5.2即得 $ \{b_{n}\} $收敛： $ \lim_{n\to\infty}b_{n}=\xi $。再由(3)， $ \lim_{n\to\infty}a_{n}=\lim_{n\to\infty}b_{n}=\xi $。下证 $ \xi=\sup E $。

 $ \forall x\in E, $ 由(1)，每个 $ b_{n} $ 都是E的上界，故 $ x\leqslant b_{n},\forall n\in N^{*} $。由极限的保序性可得 $ x\leqslant\xi=\lim_{n\to\infty}b_{n} $，所以 $ \xi $ 是E的上界。另一方面，若 $ \eta $ 也是E的上界且 $ \eta<\xi $，则 $ \varepsilon=\xi-\eta>0 $，由于 $ \lim_{n\to\infty}a_{n}=\xi $，故 $ \exists N\in N^{*} $ 使得 $ a_{N}>\xi-\varepsilon=\eta $。再由(1)， $ \exists x\in E\cap[a_{n},b_{n}] $，从而 $ x\geqslant a_{n}>\eta $，这与 $ \eta $ 是E的上界矛盾。所以 $ \xi=\sup E $。

### 习题 1.5

1. 用  $ \varepsilon-N $ 语言叙述：“数列  $ \{a_{n}\} $ 不是柯西列”.