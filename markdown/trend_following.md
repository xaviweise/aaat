# Introduction

# Exercises

$$\begin{pmatrix}I_{t}\\I_{t-1}\\...\\I_{t-N+1}\\I_{t-N}\\r_{1,t}\\r_{2,t}\end{pmatrix}=\begin{pmatrix}\alpha_0+\sum_{M=1}^{11}\beta_{s,M}1_{M(t)=M}\\0\\...\\0\\0\\0\\0\end{pmatrix}+\begin{pmatrix}\alpha_1&\alpha _2&...&\alpha_{N-1}&\alpha_N&0&0\\1&0&...&0&0&0&0\\0&1&...&0&0&0&0\\...&...&...&...&...&...&...\\0&0&...&1&0&0&0\\0&0&...&0&0&0&0\\0&0&...&0&0&0&0\end{pmatrix}\begin{pmatrix}I_{t-1}\\I_{t-2}\\...\\I_{t-N}\\I_{t-N-1}\\r_{1,t-1}\\r_{2,t-1}\end{pmatrix} + \vec{\eta_t}$$

$$Q = 
    \begin{pmatrix}
    \sigma_I^2& 0 &...& 0 & \rho_{I,1} \sigma_I \sigma_1 & \rho_{I,1} \sigma_I \sigma_2 \\ 
    0 & 0 & ... & 0 & 0 & 0 \\
    ... & ... & ... & ... & ... & ... \\
     \rho_{I,1} \sigma_I \sigma_1 & 0 & ... & 0 & \sigma_1^2  & \rho_{1,2} \sigma_1 \sigma_2 \\
    \rho_{I,1} \sigma_I \sigma_2 & 0 & ... & 0 &  \rho_{1,2} \sigma_1 \sigma_2 & \sigma_2^2
    \end{pmatrix}$$

$$L = 
    \begin{pmatrix}
    l_{11}& l_{21} & l_{31} \\
    0     & l_{22} & l_{32} \\
    0     &    0   & l_{33}
    \end{pmatrix}$$

$$\begin{pmatrix} 
    \eta_1 \\
    \eta_2 \\
    \eta_3 
    \end{pmatrix}
    = 
    \begin{pmatrix}
    l_{11}& l_{21} & l_{31} \\
    0     & l_{22} & l_{32} \\
    0     &    0   & l_{33}
    \end{pmatrix}
    \begin{pmatrix} 
    \epsilon_1 \\
    \epsilon_2 \\
    \epsilon_3 
    \end{pmatrix}
    = 
    \begin{pmatrix} 
    l_{11} \epsilon_1 + l_{21} \epsilon_2 + l_{31} \epsilon_3  \\
    l_{22} \epsilon_2 + l_{32} \epsilon_3\\
    l_{33} \epsilon_3 
    \end{pmatrix}$$

$$\begin{aligned}
    \begin{pmatrix}
    l_{11}& l_{21} & l_{31} \\
    0     & l_{22} & l_{32} \\
    0     &    0   & l_{33}
    \end{pmatrix}
    \begin{pmatrix}
    l_{11} & 0 & 0 \\
    l_{21} & l_{22} & 0 \\
    l_{31} & l_{32} & l_{33}
    \end{pmatrix}
    \nonumber \\
    =
     \begin{pmatrix}
    l_{11}^2 + l_{21}^2 + l_{31}^2  & l_{21} l_{22} + l_{31} l_{32} & l_{31} l_{33} \\
    l_{21} l_{22} + l_{31} l_{32}  & l_{22}^2 + l_{32}^2 & l_{32} l_{33} \\
    l_{33} l_{31} & l_{33} l_{32} & l_{33}^2
    \end{pmatrix}
    = 
     \begin{pmatrix}
    \sigma_I^2  & \rho_{I,1} \sigma_I \sigma_1  & \rho_{32} \sigma_I \sigma_2 \\
    \rho_{I,1} \sigma_I \sigma_1  & \sigma_1^2 & \rho_{12} \sigma_1 \sigma_2 \\
    \rho_{32} \sigma_I \sigma_2 & \rho_{12} \sigma_1 \sigma_2 & \sigma_2^2
    \end{pmatrix}
    \nonumber
\end{aligned}$$
