### 1、攻击的基本原理

**零相关性**：零相关线性分析由Bogdanov等人[<sup>[1]</sup>](#r1)在2012年提出。主要原理是在零相关性掩码下，在整个的$2^{n}$个明密文空间上，该掩码下的相关性必然为0。而对于一个随机的置换，在整个明密文空间上零相关性成立的概率是$\frac{1}{\sqrt{2\pi}}2^{\frac{4-n}{2}}$,具体证明参见[<sup>[1]</sup>](#r1)Proposition.3[<sup>[2,3]</sup>](#r2)。因为零相关线性攻击所需的明密文为$2^{n}$,限制了零相关性的攻击。所以在同年Bogdanov又提出了多重零相关攻击[<sup>[4]</sup>](#r4)，这是一种统计攻击方法，主要原理是：在一组明密文下，这组明文在$l$个零相关线性掩码下的相关性的分布和随机的一组明密文在该组零相关性掩码下的分布不同，从而区分出正确密钥下的一组明密文和随机的一组明密文。在2012年的亚密会上，Bogdanov又提出了多维零相关分析[<sup>[5]</sup>](#r5) 。





## 参考文献

1. <div id="r1">Bogdanov, A. and V. Rijmen, Linear hulls with correlation zero and linear cryptanalysis of block ciphers. Designs, codes and cryptography. 70(3): p. 369-383 2014. </div>

2. <div id="r2">O'Connor, L. Properties of linear approximation tables. in:Fast Software Encryption: Second International Workshop Leuven.  1994.</div>

3. <div id="r3">Daemen, J. and V.J.J.o.M.C. Rijmen, Probability distributions of correlation and differentials in block ciphers. 1(3): p. 221-242 2007. </div>

4. <div id="r4">Bogdanov, A. and M. Wang. Zero correlation linear cryptanalysis with reduced data complexity. in:International Workshop on Fast Software Encryption. Springer 2012.</div>

5. <div id="r5">Bogdanov, A., et al. Integral and multidimensional linear distinguishers with correlation zero. in:International Conference on the Theory and Application of Cryptology and Information Security. Springer 2012.</div>
