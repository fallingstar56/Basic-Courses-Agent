▶ 例 3.3.5

设由方程  $ x^{2}+xy+y^{2}=1 $ 确定了隐函数  $ y=y(x) $，求  $ y''(x) $.

解 方程两端对 x 求导得

 $$ 2x+y+xy^{\prime}+2yy^{\prime}=0, $$ 

故

 $$ y^{\prime}=-\frac{2x+y}{x+2y}. $$ 

进而有

 $$ \begin{aligned}y^{\prime \prime}&=-\frac{(2+y^{\prime})(x+2y)-(2x+y)(1+2y^{\prime})}{(x+2y)^{2}}=3\frac{xy^{\prime}-y}{(x+2y)^{2}}\\&=3\frac{-x\cdot\frac{2x+y}{x+2y}-y}{(x+2y)^{2}}=-6\frac{x^{2}+xy+y^{2}}{(2x+y)^{3}}=\frac{-6}{(2x+y)^{3}}.\end{aligned} $$ 

▶ 例 3.3.6

设  $ y=y(x) $ 由参数方程  $ \left\{\begin{aligned}x=a(t-\sin t),\\ y=a(1-\cos t)\end{aligned}\right. $ 确定，试求  $ \frac{dy}{dx} $ 与  $ \frac{d^{2}y}{dx^{2}} $.

解

$$\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{y'(t)}{x'(t)}=\frac{a\sin t}{a(1-\cos t)}=\frac{\sin t}{1-\cos t},$$

 $$ \begin{aligned}\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}&=\frac{\mathrm{d}}{\mathrm{d}x}\Big(\frac{\mathrm{d}y}{\mathrm{d}x}\Big)=\frac{\mathrm{d}}{\mathrm{d}x}\Big(\frac{\sin t}{(1-\cos t)}\Big)=\frac{\frac{\mathrm{d}}{\mathrm{d}t}\Big(\frac{\sin t}{1-\cos t}\Big)}{\frac{\mathrm{d}x}{\mathrm{d}t}}\\&=\frac{\frac{(1-\cos t)\cos t-\sin^{2}t}{(1-\cos t)^{2}}}{a(1-\cos t)}=\frac{-1}{a(1-\cos t)^{2}}.\end{aligned} $$ 

习题 3.3

1. 求下列函数的二阶导数.

(1)

 $$ y=\mathrm{e}^{x^{2}} $$ 

(2)

 $$ y=\frac{x-1}{(x+1)^{2}} $$ 

(3)

 $$ y=x\arcsin^{2}x； $$ 

(4)

 $$ y=\frac{x^{2}}{\sqrt{1-x^{2}}}; $$ 

(5) $ y=x\left[\sin(\ln x)+\cos(\ln x)\right]; $ (6) $ y=\ln f(x) $，其中 $ f(x) $

2. 已知  $ f(x) $ 三阶可导，求  $ y'', y'' $

(1)  $ y = f(x^{2}) $; (2)  $ y = f(e^{x}) $; (3)  $ y = f(\ln x) $.

3. 求下列函数的指定阶数的导数.

(1) $ y=\sqrt{x} $，求 $ y^{(10)} $;

(2) $ y=e^{x}x^{4} $，求 $ y^{(4)} $;