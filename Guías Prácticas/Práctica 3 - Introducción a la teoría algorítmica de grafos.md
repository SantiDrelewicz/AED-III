# Demostración de propiedades simples sobre grafos

## Equilibrio Digrafo
1. ⋆ Demostrar, usando inducción en la cantidad de aristas, que todo digrafo D satisface 

$$\sum_{v ∈ V(D)} d_{in}(v) = \sum_{v ∈ V(D)} d_{out}(v) = |E(D)|$$

>- **Caso base:** Tomo $m = |E(D)| = 0$ y por lo tanto tenemos a todos los vertices desconectados, de forma que
>
  >$$ \sum_{v ∈ V(D)} d_{in}(v) = 0 = \sum_{v ∈ V(D)} d_{out}(v) $$
>
> - **Paso Inductivo:**
>   - **HI**: $|E(D)| ≤ m - 1$ vale $$\sum_{v ∈ V(D)} d_{in}(v) = \sum_{v ∈ V(D)} d_{out}(v) = |E(D)|$$
>   - Qvq vale para $|E(D)| = m$
>   - Sea $(i → j) ∈ E(D)$, y llamemos $D' = (V(D), E(D) ∖ \{(i → j)\})$. De esta forma
  $|E(D)| = |E(D') \oplus (i → j)| = |E(D')| + |\{(i → j)\}| = |E(D')|+1 = m-1 + 1 = m$
>
> $$\begin{align*}
      ⟹\sum_{v ∈ V(D)} d_{in}(v) & =
          \sum_{v ∈ V(D) ∖ \{(i→j)\}} d_{in}(v) + d_{in}^D(j)\\
      & = \sum_{v ∈ V(D) ∖ \{(i→j)\}} d_{in}(v)  + d_{in}^{D'}(j) + 1 \\
      & =  \sum_{v ∈ V(D')} d_{in}(v) + 1 = |E(D')| + 1 = |E(D)|
\end{align*}$$
>
>$$\begin{align*}
      ⟹\sum_{v ∈ V(D)} d_{out}(v) & =
          \sum_{v ∈ V(D) ∖ \{(i→j)\}} d_{out}(v) + d_{out}^D(i)\\
      & = \sum_{v ∈ V(D) ∖ \{(i→j)\}} d_{out}(v)  + d_{out}^{D'}(i) + 1 \\
      & =  \sum_{v ∈ V(D')} d_{out}(v) + 1 = m-1 + 1 = m
\end{align*}$$
>
> - $ ⟹ \sum_{v ∈ V(D)} d_{in}(v) = \sum_{v ∈ V(D)} d_{out}(v) = m_{ \; \blacksquare}$

