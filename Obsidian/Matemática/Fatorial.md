
# Fatorial

### O que é fatorial?

O fatorial de um número inteiro positivo é o produto de todos os números inteiros positivos de 1 até esse número. Ele é representado pelo símbolo "!".

Por exemplo, o fatorial de 5 (escrito como `5!`) é calculado assim:

5!=5×4×3×2×15!=5×4×3×2×1

Fazendo as multiplicações:

5!=5×4=20
20×3=60
60×2=120
120×1=120

Então, **`5! = 120`**.

---

### Para que serve o fatorial?

O fatorial é muito usado em matemática, especialmente em áreas como combinatória (que estuda combinações e permutações) e probabilidade. Ele ajuda a calcular, por exemplo:

1. **Permutações**: Quantas maneiras diferentes podemos organizar um conjunto de objetos.
    
    - Exemplo: Se você tem 3 livros, de quantas maneiras diferentes pode organizá-los na prateleira?
        
    - Resposta: `3! = 3 × 2 × 1 = 6` maneiras.
        
2. **Combinações**: Quantos grupos diferentes podemos formar a partir de um conjunto de objetos.
    
    - Exemplo: Quantos grupos de 2 pessoas podemos formar com 4 pessoas?
        
    - Resposta: Usamos fatorial na fórmula de combinação:
        
        C(n,k)=n!k!×(n−k)!C(n,k)=k!×(n−k)!n!​
        
        Onde:
        
        - `n = 4` (total de pessoas),
            
        - `k = 2` (tamanho do grupo).
            
        - Substituindo na fórmula:
            
            C(4,2)=4!2!×(4−2)!=242×2=244=6C(4,2)=2!×(4−2)!4!​=2×224​=424​=6
        - Então, **6 grupos** de 2 pessoas podem ser formados com 4 pessoas.
            

---

### Casos especiais

- **Fatorial de 0**: Por definição, `0! = 1`. Isso pode parecer estranho, mas é útil em fórmulas matemáticas.
    
- **Fatorial de 1**: `1! = 1`.
    

---

### Resumindo

- O fatorial de um número `n` é o produto de todos os números de 1 até `n`.
    
- É representado por `n!`.
    
- Exemplo: `4! = 4 × 3 × 2 × 1 = 24`.
    
- Usado em permutações, combinações e probabilidade.