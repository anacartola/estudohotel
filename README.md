![hotel](https://github.com/anacartola/estudohotel/assets/136506553/0ab5a94c-3ec6-429b-8c53-c5e843adfaf9)
# Data Science Study Room - Hotel Operations Analysis
At our esteemed ApartHotel, guest satisfaction is paramount. Lately, however, we've heard murmurs of discontent regarding the frequency of room cleanings. As these concerns grow, the management faces a critical decision: should we hire more cleaning staff, or can we optimize our current operations?

This case study leverages data analysis to provide insights into cleaning operations, using various Python libraries and tools to facilitate a comprehensive evaluation.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#)

## Table of Contents
- [English](#english)
  - [Introduction](#introduction)
  - [Tools and Libraries Used](#tools-and-libraries-used)
  - [Data Dictionary](#data-dictionary)
  - [Curiosities](#curiosities)
  - [Objectives](#objectives)
  - [License](#license)
  - [Contact](#contact)
- [Português](#português)
  - [Introdução](#introdução)
  - [Ferramentas e Bibliotecas Utilizadas](#ferramentas-e-bibliotecas-utilizadas)
  - [Curiosidades](#curiosidades)
  - [Objetivos](#objetivos)
  - [Licença](#licença)
  - [Contato](#contato)

## English

### Introduction

At our esteemed ApartHotel, guest satisfaction is paramount. Lately, however, we've heard murmurs of discontent regarding the frequency of room cleanings. As these concerns grow, the management faces a critical decision: should we hire more cleaning staff, or can we optimize our current operations?

This case study leverages data analysis to provide insights into cleaning operations, using various Python libraries and tools to facilitate a comprehensive evaluation.

### Tools and Libraries Used

- **Pandas**: Utilized for data manipulation and analysis, enabling efficient handling and transformation of Excel data.
- **Matplotlib and Seaborn**: Used for creating informative visualizations, with Seaborn adding aesthetically pleasing statistical graphics.
- **Plotly Express**: Enhanced data visualization with interactive and high-quality plots.
- **NumPy and SciPy**: Employed for numerical computations and statistical analysis.

# Data Dictionary

This document describes the structure and content of the DataFrames used for generating visualizations in the hotel operations analysis project.

## Main DataFrames (used to generate Graphics)

### 1. `df_notas`
- **Description**: Comprehensive DataFrame combining cleanliness scores, occupancy, and cleaning data. Used for plotting monthly notes and average cleanings per room.
- **Columns**:
  - `Mes`: Month of the year (1 to 12).
  - `Nota Limpeza`: Cleanliness score for the month.
  - `Média Limpezas Realizadas`: Average number of cleanings per room.

### 2. `df_faxina`
- **Description**: Detailed cleaning data for each staff member. Used to analyze the correlation between working days and cleaning performance.
- **Columns**:
  - `Mes`: Month of the year (1 to 12).
  - `Faxineiro`: Identifier for the cleaning staff member.
  - `Dias Trabalhados`: Number of unique days worked by the staff member.
  - `Média Faxinas/Dia`: Average number of rooms cleaned per day.

### 3. `media_por_funcionario`
- **Description**: Average number of cleanings per day for each staff member. Used for boxplot visualization of daily cleaning averages.
- **Columns**:
  - `Faxineiro`: Identifier for the cleaning staff member.
  - `Média Faxinas/Dia`: Average number of rooms cleaned per day.

### 4. `customensal`
- **Description**: Monthly fixed and variable cleaning costs. Used for comparing cost options for different cleaning strategies.
- **Columns**:
  - `Mes`: Month of the year (1 to 12).
  - `Fixo Mensal`: Total fixed monthly cost.
  - `Custo p/ Quarto`: Total variable cost per room cleaned.

### Curiosities

A unique aspect of this study is the detailed examination of the correlation between room cleanliness scores and the number of cleanings performed. This analysis helped us understand whether increasing cleaning frequency would effectively improve guest satisfaction.

### Objectives

This case study not only addresses the immediate issue of cleanliness complaints but also provides a data-driven approach to optimizing cleaning operations, aiming to enhance guest experiences while managing operational costs effectively.

### License

This project is licensed under the MIT License.

### Contact

For questions or support, please contact [anacarolina.cartola@gmail.com](mailto:anacarolina.cartola@gmail.com).

## Português

### Introdução

No nosso renomado ApartHotel, a satisfação dos hóspedes é primordial. Ultimamente, no entanto, ouvimos murmúrios de descontentamento em relação à frequência das limpezas dos quartos. À medida que essas preocupações crescem, a administração enfrenta uma decisão crítica: devemos contratar mais funcionários para limpeza ou podemos otimizar nossas operações atuais?

Este estudo de caso utiliza análise de dados para fornecer insights sobre as operações de limpeza, utilizando várias bibliotecas e ferramentas Python para facilitar uma avaliação abrangente.

### Ferramentas e Bibliotecas Utilizadas

- **Pandas**: Utilizado para manipulação e análise de dados, permitindo o tratamento e a transformação eficiente de dados do Excel.
- **Matplotlib e Seaborn**: Usados para criar visualizações informativas, com o Seaborn adicionando gráficos estatísticos esteticamente agradáveis.
- **Plotly Express**: Visualização de dados aprimorada com gráficos interativos e de alta qualidade.
- **NumPy e SciPy**: Empregados para cálculos numéricos e análise estatística.

### Curiosidades

Um aspecto único deste estudo é o exame detalhado da correlação entre as pontuações de limpeza dos quartos e o número de limpezas realizadas. Esta análise nos ajudou a entender se aumentar a frequência de limpeza melhoraria efetivamente a satisfação dos hóspedes.

### Objetivos

Este estudo de caso não só aborda a questão imediata das reclamações de limpeza, mas também fornece uma abordagem baseada em dados para otimizar as operações de limpeza, visando melhorar as experiências dos hóspedes enquanto gerencia eficazmente os custos operacionais.

### Licença

Este projeto está licenciado sob a Licença MIT.

### Contato

Para perguntas ou suporte, entre em contato com [anacarolina.cartola@gmail.com](mailto:anacarolina.cartola@gmail.com).
