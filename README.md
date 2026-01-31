# RSafe: Incentivizing Proactive Reasoning to Build Effective and Robust LLM Safeguards [NeurIPS 2025]

<!-- This repository contains the implementation for **RSafe**, an adaptive reasoning-based safeguard framework that enhances the safety alignment of large language models (LLMs) through **guided reasoning** and **reinforcement learning (RL)**. RSafe improves out-of-distribution generalization and provides interpretable, step-by-step safety assessments on both prompts and responses. -->

<!-- ## 🧠 Project Overview

Large Language Models (LLMs) remain vulnerable to producing harmful or policy-violating content, particularly under adversarial or unseen conditions. Existing safety guard methods often rely on static heuristics or extensive annotated datasets, limiting their generalizability. RSafe addresses these limitations by:

- Incentivizing **step-by-step safety reasoning**.
- Applying **reinforcement learning** to internalize safety paths.
- Supporting **dual-stage moderation** (prompt-level and response-level).
- Reducing dependency on large-scale labeled data. -->

![intro](intro.png)

RSafe, an adaptive reasoning-based safeguard designed to provide robust and interpretable safety moderation for Large Language Models (LLMs). RSafe operates through two principal stages: Guided Reasoning and Reinforced Alignment. During the first stage, it analyzes potential safety risks through policy-guided, step-by-step reasoning to internalize safety principles. In the second stage, rule-based reinforcement learning (RL) is employed to optimize these reasoning paths, ensuring they align with accurate safety predictions. Specifically, RSafe bridges the gap in out-of-distribution generalization, enabling effective protection against emerging harmful categories and jailbreak attacks while providing human-readable explanations for its safety judgments. [Read our paper](https://arxiv.org/pdf/2506.07736)

## 🚀 Getting Started

### 1. Build the Environment

We implement our code on the base of [verl](https://github.com/volcengine/verl?tab=readme-ov-file)

### 2. Data Generation

Before training, prepare training data for both prompt- and response-level moderation tasks:

```bash
python examples/data_preprocess/RSafe_prompt_data_generation.py
python examples/data_preprocess/RSafe_response_data_generation.py
```

### 3. Training

To start training:

```bash
bash examples/RSafe_Training/run_training.sh
```

### 3. Inference

After training, run inference with the saved checkpoint:

```bash
bash evaluate/inference/evaluation.sh
```
