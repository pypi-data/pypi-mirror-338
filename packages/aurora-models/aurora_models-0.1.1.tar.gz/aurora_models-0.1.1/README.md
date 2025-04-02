<p align="center">
  <img src="/auroralogo.png" width="400"/>
</p>

<p align="center">
        🤗 <a href="https://huggingface.co/scrumlaltda/sl-aurora-01KG"> Models on Hugging Face</a>&nbsp | <a href="https://desenvolvimento.scrumlab.com.br/aurora/blog/"> Blog</a>&nbsp |  <a href="https://desenvolvimento.scrumlab.com.br/aurora/">Website</a>&nbsp | <a href="https://desenvolvimento.scrumlab.com.br/aurora/get-started/">Get Started</a>&nbsp
<br>

---

# SL-Aurora-01KG

SL-Aurora-01KG é um modelo avançado baseado na arquitetura Llama 3.1-8B, desenvolvido e treinado pela Scrumlab com foco em aplicações avançadas de IA generativa. Este modelo foi ajustado para fornecer respostas contextuais detalhadas e realizar tarefas complexas de geração de texto.

## Objetivos

1. **Acessibilidade Aberta:** Disponível para desenvolvedores e pesquisadores da comunidade para promover avanços e colaborações.
2. **Treinamento Especializado:** Ajustado para tarefas de geração de texto específicas da Scrumlab, visando aplicações em áreas como processamento de linguagem natural, análise de dados, e interfaces conversacionais inteligentes.
3. **Confiabilidade e Segurança:** Construído seguindo rigorosos padrões de ética e segurança, com ênfase na utilização responsável da IA.

---

## Modelos Disponíveis

|  **Modelo** | **Data de Lançamento** | **Tamanhos Disponíveis** | **Comprimento do Contexto** | **Tokenizer** | **Política de Uso Aceitável**  |  **Licença** | **Model Card** |
| :----: | :----: | :----: | :----:|:----:|:----:|:----:|:----:|
| SL-Aurora-01KG | 4/1/2025 | 8B | 128K | TikToken-based | [Política de Uso](models/sl-aurora/USE_POLICY.md) | [Licença](models/sl-aurora/LICENSE) | [Model Card](models/sl-aurora/MODEL_CARD.md) |

---

## Download

Para baixar os pesos do modelo e o tokenizador:

1. Visite a página do modelo no [Hugging Face](https://huggingface.co/scrumlaltda/sl-aurora-01KG).
2. Leia e aceite a licença.
3. Instale o [Hugging Face CLI](https://github.com/huggingface/transformers): `pip install huggingface-hub`.
4. Faça o login com seu token: `huggingface-cli login`.
5. Faça o download do modelo:
```bash
huggingface-cli download scrumlaltda/sl-aurora-01KG --include "original/*" --local-dir scrumlab-aurora
```

---

## Rodando o Modelo

Você precisa instalar o pacote `transformers` e suas dependências:
```bash
pip install transformers torch
```

Agora você pode usar o seguinte script para carregar e utilizar o modelo:

```python
import transformers
import torch

model_id = "scrumlaltda/sl-aurora-01KG"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
)
```

---

## Treinamento e Ajustes

Para treinar ou ajustar o modelo, utilize o seguinte comando (certifique-se de ter os dados preparados em formato apropriado):

```bash
python train.py --model_name_or_path scrumlaltda/sl-aurora-01KG --dataset your_dataset --output_dir ./output
```

---

## Uso Responsável

A SL-Aurora-01KG é uma tecnologia poderosa que deve ser utilizada de forma responsável. É importante seguir as diretrizes estabelecidas pela [Política de Uso Aceitável](models/sl-aurora/USE_POLICY.md) e garantir que o uso do modelo não cause danos ou viole direitos de terceiros.

---

## Problemas e Feedback

Relate problemas ou bugs através dos seguintes meios:

- [Issues na Scrumlab](https://github.com/scrumlaltda/sl-aurora-01KG/issues)
- Feedback sobre conteúdo gerado: [desenvolvimento.scrumlab.com.br/aurora/output_feedback](https://desenvolvimento.scrumlab.com.br/aurora/output_feedback)
- Preocupações de segurança: [desenvolvimento.scrumlab.com.br/aurora/whitehat/info](https://desenvolvimento.scrumlab.com.br/aurora/whitehat/info)

---

## Perguntas Frequentes

Para perguntas comuns, consulte a [FAQ](https://desenvolvimento.scrumlab.com.br/aurora/faq). Esse documento será atualizado regularmente para cobrir novos tópicos e dúvidas que possam surgir.

---