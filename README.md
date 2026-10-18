# QualityShop — QA Portfolio

## Sobre o projeto

Este projeto apresenta um portefólio prático de Quality Assurance (QA), desenvolvido para aplicar conhecimentos de testes de software através de atividades de análise de requisitos, identificação de riscos, elaboração e execução de casos de teste e registo de defeitos.

Os testes foram realizados no [SauceDemo](https://www.saucedemo.com/), um ambiente de demonstração utilizado para praticar testes de aplicações web.

## Objetivos

- Analisar e organizar requisitos funcionais.
- Identificar e avaliar riscos associados às funcionalidades.
- Elaborar e executar casos de teste.
- Verificar funcionalidades de autenticação, produtos, carrinho e checkout.
- Registar defeitos com passos para reprodução, resultado esperado e resultado obtido.
- Documentar evidências dos testes realizados.

## Documentação do projeto

O projeto inclui quatro áreas principais:

- **Requirements:** requisitos funcionais e respetiva associação aos casos de teste.
- **Risk Matrix:** identificação de riscos, impacto, probabilidade e prioridade.
- **Test Cases:** casos de teste com pré-condições, passos e resultados.
- **Bugs:** registo dos defeitos identificados durante os testes.
  
### Evidências de teste

As capturas de ecrã abaixo documentam a investigação do defeito visual BUG-001 no ambiente de demonstração SauceDemo.

- [Mensagem de erro cortada](TC-005_mensagem-de-erro-cortada.png)
- [Altura original do elemento no DevTools (45 px)](TC-005_devtools-height-original-45px.png)
- [Teste temporário com a mensagem sem cortes no DevTools](TC-005_mensagem-de-erro-sem-cortes-teste-DevTools-temporario.png)

**Nota:** a alteração de altura foi apenas um teste temporário no Chrome DevTools, não uma correção permanente da aplicação.
## Ferramentas e técnicas

- Testes manuais e funcionais
- Análise de requisitos
- Matriz de riscos
- Elaboração e execução de casos de teste
- Registo e análise de defeitos
- Google Sheets
- Chrome DevTools

## Resultados e observações

Durante os testes, foi identificado um problema visual na apresentação da mensagem de erro do login: parte do texto aparece cortada. O comportamento foi documentado no registo de defeitos como BUG-001.

A investigação com o Chrome DevTools permitiu observar o comportamento do elemento e testar temporariamente uma alteração de altura. Esta observação sustenta uma hipótese para a causa do problema, mas não confirma definitivamente a sua causa técnica.

## Metodologia e limitações

A matriz de riscos utiliza uma escala de impacto e probabilidade definida para este projeto. As probabilidades são estimativas iniciais e não se baseiam em dados estatísticos ou históricos de incidentes.

Os testes foram realizados num ambiente de demonstração. Os resultados não devem ser interpretados como uma avaliação de um sistema de produção.

## Sobre mim

Estou a desenvolver competências na área de Quality Assurance, com foco em testes manuais, testes de API, bases de dados e automação de testes.

Este projeto faz parte do meu portefólio de aprendizagem prática em QA.

---

**Projeto de aprendizagem prática — Quality Assurance (QA).**

## Automação de testes

Até ao momento, foram automatizados dez casos de teste: sete da funcionalidade de login (TC-001 a TC-007) e três de produtos e carrinho (TC-011 a TC-013), utilizando Python, Selenium, pytest e Google Chrome.
Para executar os testes, abre o terminal na pasta principal do projeto e executa:

```text
python -m pytest tests -v
```
