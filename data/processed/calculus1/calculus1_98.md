n=m成立，即有

 $$ (f\bullet g)^{(m)}=\sum_{k=0}^{m}\mathrm{C}_{m}^{k}f^{(k)}g^{(m-k)}, $$ 

两端再求导数，得到

 $$ \begin{align*}(f\bullet g)^{(m+1)}&=\sum_{k=0}^{m}\mathrm{C}_{m}^{k}(f^{(k)}g^{(m+1-k)}+f^{(k+1)}g^{(m-k)})\\&=\sum_{k=0}^{m}\mathrm{C}_{m}^{k} f^{(k)}g^{(m+1-k)}+\sum_{k=0}^{m}\mathrm{C}_{m}^{k} f^{(k+1)}g^{(m-k)}\\&=\sum_{k=0}^{m}\mathrm{C}_{m}^{k} f^{(k)}g^{(m+1-k)}+\sum_{k=1}^{m+1}\mathrm{C}_{m}^{k-1}f^{(k)}g^{(m+1-k)}\\&=\sum_{k=1}^{m}(\mathrm{C}_{m}^{k}+\mathrm{C}_{m}^{k-1})f^{(k)}g^{(m+1-k)}+\mathrm{C}_{m}^{0}\bullet g^{(m+1)}+\mathrm{C}_{m}^{m} f^{(m+1)}g\\&=\sum_{k=1}^{m}\mathrm{C}_{m+1}^{k} f^{(k)}g^{(m+1-k)}+\mathrm{C}_{m+1}^{0}f\bullet g^{(m+1)}+\mathrm{C}_{m+1}^{m+1}f^{(m+1)}g\\&=\sum_{k=0}^{m+1}\mathrm{C}_{m+1}^{k} f^{(k)}g^{(m+1-k)},\end{align*} $$ 

其中用到等式： $ C_{m}^{k}+C_{m}^{k-1}=C_{m+1}^{k} $。所以(3)对 $ n=m+1 $亦成立。由数学归纳法，

(3) 对任何正整数 n 成立.

 $ y=\frac{1}{x^{2}-x-2} $，求 $ y^{(n)} $

解  $ y=\frac{1}{3}\left(\frac{1}{x-2}-\frac{1}{x+1}\right) $.

所以

 $$ \begin{align*}\boldsymbol{y}^{(n)}&=\frac{1}{3}\left(\frac{1}{x-2}\right)^{(n)}-\frac{1}{3}\left(\frac{1}{x+1}\right)^{(n)}\\&=\frac{1}{3}\left(-1\right)^{n}n!(x-2)^{-(n+1)}-\frac{1}{3}\left(-1\right)^{n}n!(x+1)^{-(n+1)}.\end{align*} $$ 

 $ y=x^{2}\sin x $，求  $ y^{(20)} $

解 在莱布尼茨公式中取  $ f(x)=x^{2} $， $ g(x)=\sin x $，便得到

 $$ \begin{aligned}(\boldsymbol{x}^{2}\sin\boldsymbol{x})^{(20)}&=\boldsymbol{x}^{2}(\sin\boldsymbol{x})^{(20)}+\mathrm{C}_{20}^{1}2\boldsymbol{x}(\sin\boldsymbol{x})^{(19)}+\mathrm{C}_{20}^{2}2(\sin\boldsymbol{x})^{(18)}\\&=\boldsymbol{x}^{2}\sin\left(\boldsymbol{x}+\frac{20\pi}{2}\right)+40x\sin\left(\boldsymbol{x}+\frac{19}{2}\pi\right)+380\sin\left(\boldsymbol{x}+\frac{18}{2}\pi\right)\\&=\boldsymbol{x}^{2}\sin\boldsymbol{x}-40x\cos\boldsymbol{x}-380\sin\boldsymbol{x}.\end{aligned} $$ 