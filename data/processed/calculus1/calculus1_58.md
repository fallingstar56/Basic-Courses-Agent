证明： $ \lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=\lim_{t\to0}(1+t)^{\frac{1}{t}}=\mathrm{e}. $

证明 注意到当  $ x \geqslant 1 $ 时，

 $$ \left(1+\frac{1}{\left\lbrack x\right\rbrack+1}\right)^{\left\lbrack x\right\rbrack}\leqslant\left(1+\frac{1}{x}\right)^{x}\leqslant\left(1+\frac{1}{\left\lbrack x\right\rbrack}\right)^{\left\lbrack x\right\rbrack+1}. $$ 

由于 $ \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e $，易见 $ \lim_{x\to+\infty}\left(1+\frac{1}{\left\lfloor x\right\rfloor}\right)^{|x|}=e $。运用极限的四则运算可得

 $ \lim_{x\to+\infty}\left(1+\frac{1}{\left\lfloor x\right\rfloor}\right)^{[x]+1}=\lim_{x\to+\infty}\left(1+\frac{1}{\left\lfloor x\right\rfloor}\right)^{[x]}\cdot\lim_{x\to+\infty}\left(1+\frac{1}{\left\lfloor x\right\rfloor}\right)=e, $

 $ \lim_{x\to+\infty}\left(1+\frac{1}{\left\lfloor x\right\rfloor+1}\right)^{[x]}=\lim_{x\to+\infty}\left(1+\frac{1}{\left\lfloor x\right\rfloor+1}\right)^{[x]+1}\cdot\left(1+\frac{1}{\left\lfloor x\right\rfloor+1}\right)^{-1}=e. $

于是由夹逼原理得到

 $$ \lim_{x\to+\infty}\left(1+\frac{1}{x}\right)^{x}=e. $$ 

还需要证明  $ \lim_{x\to-\infty}\left(1+\frac{1}{x}\right)^x= $ e. 由于  $ \lim_{x\to+\infty}\left(1+\frac{1}{x}\right)^x= $ e，故  $ \forall\varepsilon>0,\exists M>0 $ 使得当 x>M 时有

 $$ \left|\left(1+\frac{1}{x}\right)^{x}-\mathrm{e}\right|<\varepsilon, $$ 

注意到 $ \left(1+\frac{1}{x}\right)^{x+1}=\left(1+\frac{1}{-x-1}\right)^{-x-1} $，于是当 $ x<-(M+1) $时有

 $$ \left|\left(1+\frac{1}{x}\right)^{x+1}-\mathrm{e}\right|=\left|\left(1+\frac{1}{-x-1}\right)^{-x-1}-\mathrm{e}\right|<\varepsilon, $$ 

因此  $ \lim_{x\to-\infty}\left(1+\frac{1}{x}\right)^{x+1}= $ e. 进而知

 $$ \lim_{x\to-\infty}\left(1+\frac{1}{x}\right)^{x}=\lim_{x\to-\infty}\left(1+\frac{1}{x}\right)^{x+1}\cdot\left(1+\frac{1}{x}\right)^{-1}=e. $$ 

所以 $ \lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=\mathrm{e}. $

最后，由于 $ \lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e,\forall\varepsilon>0,\exists M>0 $，使得当 $ |x|>M $时有

 $$ \left|\left(1+\frac{1}{x}\right)^{x}-\mathrm{e}\right|<\varepsilon. $$ 

于是当  $ 0 < |t| < \delta = \frac{1}{M} $ 时有

 $$ \left|\left(1+t\right)^{\frac{1}{t}}-e\right|<\varepsilon. $$ 

所以 $ \lim_{t\to0}(1+t)^{\frac{1}{t}}=\mathrm{e}. $