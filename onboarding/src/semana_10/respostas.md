# Anotações sobre a leitura

### 2. Leia o capítulo 8 do livro Introduction to Transfer Learning  Algorithms and Practice:

Durante a leitura traga anotações curtas de cada item:

- 8.1 Transferability — camadas baixas = traços gerais; camadas altas = traços específicos (estudo clássico tipo Yosinski et al.).
    > Camadas rasas extraem features gerais (bordas, formas) enquanto camadas profundas capturam features específicas (rostos, pernas). Como as camadas mais rasas são gerais, podemos utilizá-las para outros tipos de problemas, reduzindo o custo de treinamento.
    > **Estudo Yosinski et al. (2014):** Dividiu ImageNet em 2 conjuntos (A e B, 500 classes cada), depois testou transferência camada-por-camada (AlexNet, 8 camadas). Onde AnB (transfere n camadas de A para B e congela), BnB (baseline) e AnB+/BnB+ (com fine-tuning). Pode-se concluir que as primeiras 3 camadas transferem bem diretamente; 4ª-5ª camada têm queda (features mais específicas); Fine-tuning (AnB+) dá melhor performance geral e que a similaridade entre domínios é crítica: quanto mais similar, melhor a transferência.

- 8.2 Pré-treino e Fine-tuning — definição formal; quando congelar vs. ajustar.
    > Definição formal: θ* = arg min L(θ|θ₀, D), onde θ₀ = parâmetros pré-treinados e D = dataset alvo (limitado)
    > Vantagens: Não treinar do zero economiza de tempo/custo, modelos pré-treinados em larga escala aumentam generalização e a implementação é fácil. Tem maior ganho em datasets pequenos (vs. treino do zero)

- 8.3 Regularização no fine-tuning — L2, L2-SP, EWC/Fisher, DELTA (mapas de feature), BSS, co-tuning.
    > Problema: ERM precisa de regularização explícita, forma geral: min L_cls + R(w) 
    Técnicas principais: 
    1. L2: R(w) = (α/2)||w||².
    2. L2-SP (Starting Point): Regulariza distância para pesos pré-treinados w₀: R(w) = (α/2)||w - w₀||²
    3. EWC (Elastic Weight Consolidation) / L2-SP-Fisher: Usa matriz de Fisher para ponderar importância de cada peso: R(w) = (α/2)Σ F̂ⱼⱼ(wⱼ - w₀ⱼ)²
    4. DELTA: Regulariza mapas de features entre rede pré-treinada e fine-tunada: R(w) = Σ ||FM_j(w,x) - FM_j(w₀,x)||²
    5. BSS (Batch Spectral Shrinkage): Restringe k menores valores singulares das features
    6. Co-tuning: Ponte entre espaços semânticos diferentes (teacher vs. student): R = L_CE(P(y_t | y_s))
    7. Outras: Distância de gradientes, re-inicialização de FC layers, thresholds adaptativos por camada

- 8.4 Uso como extrator de features — pipeline “deep features + SVM/ML clássico”.
    > Pipeline clássico: Deep features para ML tradicional (SVM, etc.). Contexto histórico: DeCAF (2014): features de CNNs superaram SIFT/SURF, CNN features + SVM melhorou performance vs. features tradicionais
    > EasyTL (Wang et al. 2019): Abordagem 2 estágios: (1) extrai features com rede fine-tunada; (2) transformação + classificador próprio. Às vezes supera deep transfer learning end-to-end. Usa programação linear para atribuição de labels.
    > 3 opções de uso: Aplicar modelo pré-treinado diretamente, ou pré-treino + fine-tuning, ou pré-treino como extrator + classificador customizado.

- 8.5 O que/onde transferir — abrir a caixa-preta: quantas camadas, para quais blocos (ideias de meta-learning).
" Ainda existem perguntas em aberto, como, quantas camadas transferir? ou quais camadas congelar vs. fine-tunar? " 
    > Abordagem com Meta-Learning (Jang et al. 2019): Tinha como objetivo aprender transferência usando a fórmula: ||r_θ(T^n_θ(x)) - S^m(x)||². Estratégias: Matriz de pesos w^(m,n)_c para selecionar canais importantes e λ^(m,n) como indicador se transferência m→n é benéfica. 3 configurações testadas: **Single**, última camada source → camada específica target, **One-to-one**, cada camada (pré-pooling) para a camada específica target e **All-to-all**, qualquer m para qualquer n.

- 8.6 Prática em PyTorch — função de fine-tuning e extração de features.
    > Função de fine-tuning - Características: 3 fases: source (treino), validation, target (teste), early stopping, salva best model em 'model.pkl'
    > Extração de features: Salva features + labels em arquivo .csv para uso posterior com ML clássico

- 8.7 Sumário — quando pré-treinar ajuda mais (datasets pequenos, robustez, OOD, etc.).
    > Quando pré-treino ajuda mais:
    - Datasets pequenos (alvo)
    - Robustez (adversarial, label noise, classes desbalanceadas)
    - Out-of-distribution (OOD) tasks
    -  Calibração de modelos

### Questão 4 - Compare os resultados no dataset MNIST usando as métricas de acurácia e f1-score no conjunto de teste:

1. Treinamento do zero (Ex 1)
   > A ConvNet apresentou melhor capacidade de generalização, evidenciada pelo menor gap entre acurácia de validação e teste (0.36% vs 1.01%). A ResNet18 demonstrou sinais de overfitting, com acurácia de validação superior (99.27%) mas desempenho inferior no conjunto de teste (98.26%). Portanto a ConvNet demonstrou superioridade em todos os aspectos relevantes: melhor resultado final, menor complexidade, treinamento substancialmente mais rápido e melhor generalização. Sendo observável que o treinamento From Scratch da ResNet18 não foi tão eficiênte quanto uma rede bem mais simples.
   
2. Somente a camada fc (Ex. 3.1)
   > Esta abordagem congela todas as camadas convolucionais, treinando apenas a camada totalmente conectada final. Vantagens: Mínimo custo computacional (apenas 5.130 parâmetros) e treinamento rápido. Desvantagens: Desempenho significativamente inferior (93.84% vs 99.37%) Gap considerável entre treino e validação. Portanto, as features pré-treinadas da ImageNet não se adaptaram adequadamente ao dataset específico.
   
3. Fine tuning parcial (Ex. 3.2)
   > Esta abordagem treina o último bloco convolucional (Layer4) e a camada de classificação. Vantagens: Melhor desempenho no teste: 99.37% (superior a todas as outras abordagens, excelente generalização (gap negativo de -0.12%), F1-Score mais alto e consistente (99.25%), tempo de treinamento eficiente (787s). Portanto, apresentou um equilíbrio ideal entre adaptação e estabilidade.
   
5. Fine tuning total (Ex. 3.3)
   >Esta abordagem treina todos os parâmetros da rede. Vantagens: Segundo melhor desempenho no teste (99.24%), gap zero entre validação e teste. Desvantagens: Maior instabilidade durante treinamento (queda para 97.90% na época 3), tempo de treinamento 32% superior ao fine-tuning parcial, tem maior risco de overfitting com 11.2M parâmetros treináveis.
