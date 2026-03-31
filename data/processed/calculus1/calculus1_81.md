 $$ \left(\sin x\right)^{\prime}=\lim_{\Delta x\rightarrow0}\frac{\sin\left(x+\Delta x\right)-\sin x}{\Delta x}=\cos x. $$ 

类似地，可得 $ \left(\cos x\right)^{\prime}=-\sin x. $

▶ 例 3.1.3 ……

设 a>0，且  $ a\neq1 $， $ f(x)=a^{x} $， $ g(x)=\log_{a}x $，求  $ f'(x) $ 与  $ g'(x) $.

解 (1) $ f'(x)=\lim_{\Delta x\to0}\frac{a^{x+\Delta x}-a^{x}}{\Delta x}=a^{x}\lim_{\Delta x\to0}\frac{a^{\Delta x}-1}{\Delta x}=a^{x}\ln a. $

(2) 当 x > 0 时，

 $$ \begin{aligned}g^{^{\prime}}(x)&=\lim_{\Delta x\to0}\frac{\log_{a}(x+\Delta x)-\log_{a}x}{\Delta x}=\lim_{\Delta x\to0}\frac{1}{x}\log_{a}\left(1+\frac{\Delta x}{x}\right)^{\frac{x}{\Delta x}}\\&=\frac{1}{x}\log_{a}e=\frac{1}{x\ln a}.\end{aligned} $$ 

特别地，当 a=e 时，导数的表达式最简单：

 $$ \left(\mathrm{e}^{x}\right)^{\prime}=\mathrm{e}^{x},\quad\left(\ln x\right)^{\prime}=\frac{1}{x}. $$ 

这正是以 e 为底数的指数函数与对数函数被广泛使用的重要原因。

▶ 例 3.1.4

设  $ f(x)=x^{a} $，求  $ f'(x) $.

解 当  $ x \neq 0 $ 时，

 $$ f^{\prime}(x)=\lim_{\Delta x\to0}\frac{(x+\Delta x)^{*}-x^{a}}{\Delta x}=x^{a-1}\lim_{\Delta x\to0}\frac{\left(1+\frac{\Delta x}{x}\right)^{a}-1}{\frac{\Delta x}{x}}=\alpha x^{a-1}. $$ 

上面等式中只需要求 x 使得运算过程中各个表达式都有意义即可。所以，

(1) 若 a=k 为正整数，则  $ f(x)=x^{k} $ 在 x=0 点的导数也存在：

 $$ f^{\prime}(0)=\lim_{\Delta x\to0}\frac{(\Delta x)^{k}-0^{k}}{\Delta x}=\left\{\begin{aligned}1,\quad k=1,\\ 0,\quad k\neq1,\end{aligned}\right. $$ 

即

 $$ (x^{k})^{\prime}=k x^{k-1}\quad(x\in\mathbb{R}); $$ 

(2) 若 a=k 为负整数，则

 $$ (x^{k})^{\prime}=kx^{k-1}\quad(x\neq0)\;; $$ 

(3) 若  $ \alpha $ 为非零实数，则

 $$ (x^{a})^{\prime}=ax^{a-1}\quad(x>0). $$ 

从导数定义不难看出