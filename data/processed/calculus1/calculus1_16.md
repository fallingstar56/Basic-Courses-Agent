7. 设 A, B 均为非空有界数集，且  $ A \cap B $ 非空，证明：

 $$ \left(1\right)\inf(A\cup B)=\min\left\{\inf A,\inf B\right\};\quad\left(2\right)\sup(A\cup B)=\max\left\{\sup A,\sup B\right\}; $$ 

 $$ \left(3\right)\inf(A\cap B)\geqslant\max\{\inf A,\inf B\}\text{；}\left(4\right)\sup(A\cap B)\leqslant\min\{\sup A,\sup B\}\text{．} $$ 

8. 设 A, B 均为非空有界数集，定义  $ A + B = \{x + y \mid x \in A, y \in B\} $， $ AB = \{xy \mid x \in A, y \in B\} $。证明：(1)  $ \inf(A + B) = \inf A + \inf B $；(2)  $ \sup(A + B) = \sup A + \sup B $；(3) 当  $ A, B \subseteq \{x \mid x \geqslant 0\} $ 时，有  $ \inf AB = \inf A \inf B $， $ \sup AB = \sup A \sup B $。

9. 证明下列命题：(1) 设 A 为有上界的非空数集，则  $ \xi = \sup A $ 的充分必要条件是： $ \xi $ 为 A 的上界，并且  $ \forall \varepsilon > 0 $，存在  $ x \in A $，使得  $ x > \xi - \varepsilon $.

(2) 设 A 为有下界的非空数集，则  $ \eta = \inf A $ 的充分必要条件是： $ \eta $ 为 A 的下界，并且  $ \forall \varepsilon > 0 $，存在  $ x \in A $，使得  $ x < \eta + \varepsilon $.

### 1.2 数列极限的基本概念

以正整数 1,2, $ \cdots $,n, $ \cdots $ 为下标的一列实数按照下标的大小顺序排成一列

 $$ a_{1},a_{2},\cdots,a_{n},\cdots $$ 

称为一个(实)数列，也可以记为 $ \{a_{n}\} $。 $ a_{n} $称为数列的第n项或通项。例如，

 $$ (1)\left\{2n-1\right\};(2)\left\{(-1)^{n}\right\};(3)\left\{2+2^{-n}\right\};(4)\left\{\frac{2-(-1)^{n}}{n}\right\}. $$ 

考察上面几个数列的例子可以发现，当项数 n 由小变大时，数列  $ \{2+2^{-n}\} $ 的项  $ 2+2^{-n} $ 越来越接近实数 2，即数列  $ \{2+2^{-n}\} $ 的项越来越靠后时，这些项会朝着固定值 2 变化并无限接近 2，我们称数列  $ \{2+2^{-n}\} $ 有“极限” 2。同样地，数列  $ \left\{\frac{2-(-1)^{n}}{n}\right\} $ 的项越来越靠后时，这些项会朝着固定值 0 变化并无限接近 0，即数列  $ \left\{\frac{2-(-1)^{n}}{n}\right\} $ 有极限 0。但是  $ \{2n-1\} $ 与  $ \{(-1)^{n}\} $ 则没有这样的性质。

我们需要把这种关于数列极限的直观描述用符合逻辑的语言表达出来。

定义 1.2.1

对于数列  $ \{a_n\} $ 及常数 A，如果  $ \forall \varepsilon > 0, \exists N \in \mathbb{N} $，使得当  $ n > N $ 时，就有  $ |a_n - A| < \varepsilon $。则称数列  $ \{a_n\} $ 有极限 A，也称  $ \{a_n\} $ 收敛于 A，记为  $ \lim_{n \to \infty} a_n = A $ 或  $ a_n \to A(n \to \infty) $。

若数列 $ \{a_{n}\} $没有极限，则称 $ \{a_{n}\} $发散.

上述定义精确地表达了当数列  $ \{a_{n}\} $ 的项越来越靠后时，这些项会朝着 A 变化并“无限接近”A，因为无论对于多么小的正数  $ \varepsilon $，都可以找到相应（依赖于  $ \varepsilon $）的自然数  $ N=N(\varepsilon) $，使得数列  $ \{a_{n}\} $ 中第 N 项后面的每一项与 A 的距离