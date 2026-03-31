 $$ \lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}=\lim_{\Delta x\to0}\frac{a\Delta x+o(\Delta x)}{\Delta x}=a, $$ 

即 f 在点  $ x_{0} $ 可导且  $ f'(x_{0})=a $.

习惯上，通常将  $ \Delta x $ 写作 dx，从而函数  $ y = f(x) $ 在点 x 处的微分可以改写为

 $$ \mathrm{d}f(x)=f^{\prime}(x)\mathrm{d}x, $$ 

也可以写作：

 $$ \mathrm{d}y=f^{\prime}(x)\mathrm{d}x. $$ 

由此原因，函数  $ y=f(x) $ 在点 x 处的导数  $ f^{\prime}(x) $ 也常常被记作  $ \frac{\mathrm{d}f(x)}{\mathrm{d}x} $ 或  $ \frac{\mathrm{d}y}{\mathrm{d}x} $.

### 习题 3.1

1. 利用导数的定义求下列函数  $ f(x) $ 在指定点  $ x_{0} $ 处的导数.

(1) $ f(x)=\frac{1}{x},x_{0}=-3; $ (2) $ f(x)=2^{-x},x_{0}=0; $

(3) $ f(x)=\tan x,x_{0}=\pi; $ (4) $ f(x)=\cos x,x_{0}=-2. $

2. 研究下列函数在点  $ x_{0}=0 $ 处的连续性与可导性，若可导，求出导数  $ x_{0} $.

(1) $ f(x)=|x-3| $; (2) $ f(x)=|x|+2x $;

(3) $ f(x)=\left\{\begin{aligned}&x,&x<0,\\&\ln(1+x),&x\geqslant0;\end{aligned}\right. $ (4) $ f(x)=\left\{\begin{aligned}&3x^{2}+4x,&x<0,\\&x^{2}-1,&x\geqslant0;\end{aligned}\right. $

(5) $ f(x)=\left\{\begin{aligned}&x\sin\frac{1}{x},&x\neq0,\\&0,&x=0;\end{aligned}\right. $ (6) $ f(x)=\left\{\begin{aligned}&\frac{1}{1+\mathrm{e}^{\frac{1}{x}}},&x\neq0,\\&0,&x=0.\end{aligned}\right. $

3. 设  $ f(x)=\left\{\begin{aligned}&x^{2}+1,&x\leqslant1,\\ &ax+b,&x>1,\end{aligned}\right. $ 问：a,b 取何值时， $ f(x) $ 在 x=1 处可导？

4. 判断下列论述哪些与“ $ f(x) $ 在  $ x_{0} $ 处可导”等价.

(1) $ \lim_{h\to+\infty}h\left[f\left(x_{0}+\frac{1}{h}\right)-f(x_{0})\right] $存在；(2) $ \lim_{h\to0}\frac{f(x_{0}+2h)-f(x_{0})}{h} $存在；

(3) $ \lim_{h\to0}\frac{f(x_0+h)-f(x_0-h)}{h} $存在； $ \lim_{h\to0}\frac{f(x_0)-f(x_0-h)}{h} $存在.

5. 设  $ f(x) $ 在  $ x_{0} $ 处可导，求下列极限.

 $$ \lim_{h\to0}\frac{f(x_{0}+\alpha h)-f(x_{0}-\beta h)}{h}； $$ 

 $$ \lim_{n\to\infty}n\left[f\left(x_{0}+\frac{2}{n}\right)-f\left(x_{0}\right)\right] $$ 

(3) $ \lim_{h\to0}\frac{f(x_0-h)-f(x_0)}{h} $;