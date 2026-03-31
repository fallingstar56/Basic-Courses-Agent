求证：(1) $ \lim_{x\to+\infty}\frac{x}{a^{x}}=0(a>1) $; (2) $ \lim_{x\to+\infty}\frac{\log_{a}x}{x}=0(a>0,a\neq1) $.

证明 （1）由例 1.4.3， $ \lim_{n\to\infty}\frac{n}{a^n}=0 $，易知  $ \lim_{x\to+\infty}\frac{\left[x\right]}{a^{\left[x\right]}}=0 $。而

 $$ 0<\frac{x}{a^{x}}\leqslant\frac{2\left\lbrack x\right\rbrack}{a^{\left\lbrack x\right\rbrack}}\quad(x\geqslant1), $$ 

于是由夹逼原理推出  $ \lim_{x\to+\infty}\frac{x}{a^{x}}=0. $

(2) 由例 1.2.4, $ \lim_{n\to\infty}\frac{\ln n}{n}=0 $，于是 $ \lim_{x\to+\infty}\frac{\ln[x]}{[x]}=0 $。而当 x>1 时，

 $$ 0<\frac{\ln x}{x}\leqslant\frac{\ln(2[x])}{x}\leqslant\frac{\ln2}{x}+\frac{\ln[x]}{[x]}. $$ 

从而由夹逼原理可得  $ \lim_{x\to+\infty}\frac{\ln x}{x}=0 $ ，进而得

 $$ \lim_{x\to+\infty}\frac{\log_{a}x}{x}=\frac{1}{\ln a}\lim_{x\to+\infty}\frac{\ln x}{x}=0. $$ 

设函数 f 在  $ U(x_{0},\rho) $ 内定义. 则下列命题等价:

(1)  $ \forall \varepsilon > 0, \exists \delta > 0 $, 当  $ x_{1}, x_{2} \in U(x_{0}, \delta) $ 时, 就有  $ \left|f(x_{1}) - f(x_{2})\right| < \varepsilon $.

(2)  $ \exists A \in \mathbb{R} $，对于  $ U(x_0, \rho) $ 内任意一个收敛于  $ x_0 $ 的点列  $ \{x_n\} $，有  $ \lim_{n \to \infty} f(x_n) = A $.

(3)  $ \lim_{x\to x_0}f(x)=A. $

定理 2.3.4 中(1)与(3)的等价性称为函数极限的柯西收敛原理。

证明 (1) $ \Rightarrow(2) $ 由(1)， $ \forall\varepsilon>0,\exists\delta>0 $，当 $ x,y\in U(x_{0},\delta) $时，就有

 $$ \left|f(x)-f(y)\right|<\varepsilon. $$ 

若  $ \{x_{n}\} $ 为  $ U(x_{0},\rho) $ 内任一个收敛于  $ x_{0} $ 的点列，则对上面  $ \delta>0,\exists N\in\mathbb{N} $，使得当 n>N 时，有  $ 0<\left|x_{n}-x_{0}\right|<\delta $，即  $ x_{n}\in U(x_{0},\delta) $。所以当 m,n>N 时，有  $ \left|f(x_{m})-f(x_{n})\right|<\varepsilon $。于是  $ \{f(x_{n})\} $ 为柯西列，从而收敛： $ \lim_{n\to\infty}f(x_{n})=A $。

又设点列 $ \{y_{n}\}\subseteq U(x_{0},\rho) $且收敛于 $ x_{0} $，同理， $ \lim_{n\to\infty}f(y_{n})=B $存在。只需再证明B=A即可。令 $ z_{2n-1}=x_{n},z_{2n}=y_{n}(n=1,2,\cdots) $，则点列 $ \{z_{n}\}\subseteq U(x_{0},\rho) $且收敛于 $ x_{0} $，从而 $ \{f(z_{n})\} $必收敛，所以 $ B=\lim_{n\to\infty}f(z_{2n})=\lim_{n\to\infty}f(z_{2n-1})=A. $

(2) $ \Rightarrow(3) $ 假定  $ \lim_{x\to0}f(x)=A $ 不成立. 由极限定义, 存在正数  $ \varepsilon_{0} $, 使得  $ \forall\delta>0 $, 总