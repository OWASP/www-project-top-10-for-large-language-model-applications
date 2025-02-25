## LLM04: 데이터 및 모델 오염

### 설명

데이터 오염은 사전 학습, 미세 조정 또는 임베딩 데이터가 조작되어 취약점, 백도어 또는 편향성이 발생하는 경우를 말합니다. 이러한 조작은 모델의 보안, 성능 또는 윤리적 행동을 손상시켜 유해한 출력이나 기능 저하를 초래할 수 있습니다. 일반적인 위험에는 모델 성능 저하, 편향되거나 유해한 콘텐츠 생성, 그리고 다운스트림 시스템의 악용이 포함됩니다.

데이터 오염은 LLM 수명 주기의 여러 단계를 대상으로 할 수 있습니다. 여기에는 사전 학습(일반 데이터로부터의 학습), 미세 조정(특정 작업에 모델 적응), 임베딩(텍스트를 수치 벡터로 변환) 등이 포함됩니다. 이러한 단계들을 이해하면 취약점이 발생할 수 있는 지점을 파악하는 데 도움이 됩니다. 데이터 오염은 학습 데이터를 조작하여 모델의 정확한 예측 능력에 영향을 미치므로 무결성 공격으로 간주됩니다. 특히 검증되지 않거나 악의적인 콘텐츠를 포함할 수 있는 외부 데이터 소스를 사용할 때 위험이 높습니다.

또한, 공유 저장소나 오픈소스 플랫폼을 통해 배포되는 모델은 악성 피클링과 같은 기술을 통해 인젝션된 멀웨어 등 데이터 오염을 넘어선 위험을 가질 수 있으며, 이는 모델이 로드될 때 유해한 코드를 실행할 수 있습니다. 또한 오염을 통해 백도어가 구현될 수 있다는 점도 고려해야 합니다. 이러한 백도어는 특정 트리거가 발생하기 전까지는 모델의 동작을 그대로 유지할 수 있습니다. 이로 인해 이러한 변화를 테스트하고 감지하기 어려워질 수 있으며, 결과적으로 모델이 잠복 에이전트가 될 수 있는 기회를 만들 수 있습니다.

### 일반적 취약점 예시

1. 악의적인 행위자들이 학습 과정에서 유해한 데이터를 인젝션하여 편향된 출력을 유도합니다. "분할보기 데이터 오염(Split-View Data Poisoning)" 또는 "프론트런닝 오염(Frontrunning Poisoning)"과 같은 기술들은 모델 학습 동적을 악용하여 이를 달성합니다.
  (참조 링크: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (참조 링크: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. 공격자들은 학습 과정에 유해한 콘텐츠를 직접 인젝션하여 모델의 출력 품질을 손상시킬 수 있습니다.
3. 이용자들이 상호작용 중에 민감하거나 독점적인 정보를 무의식적으로 인젝션할 수 있으며, 이는 후속 출력에서 유출될 수 있습니다.
4. 검증되지 않은 학습 데이터는 편향되거나 잘못된 출력의 위험을 증가시킵니다.
5. 리소스 접근 제한의 부재로 인해 안전하지 않은 데이터의 유입이 허용될 수 있으며, 이는 편향된 출력을 초래할 수 있습니다.

### 예방 및 완화 전략

1. OWASP CycloneDX나 ML-BOM과 같은 도구를 사용하여 데이터의 출처와 변환을 추적하고, Dyana와 같은 도구를 활용하여 타사 소프트웨어의 동적 분석을 수행하세요. 모든 모델 개발 단계에서 데이터의 정당성을 검증하세요.
2. 데이터 공급업체를 엄격하게 검증하고, 신뢰할 수 있는 소스와 모델 출력을 비교하여 오염의 징후를 감지합니다.
3. 엄격한 샌드박싱을 구현하여 검증되지 않은 데이터 소스에 대한 모델 유출을 제한합니다. 이상 징후 탐지 기술을 사용하여 적대적 데이터를 필터링합니다.
4. 미세 조정을 위해 특정 데이터셋을 사용하여 다양한 사용 사례에 맞게 모델을 조정합니다. 이렇게 하면 정의된 목표에 기반하여 더 정확한 출력을 생성하는 데 도움이 됩니다.
5. 모델이 의도하지 않은 데이터 소스에 접근하는 것을 방지하기 위해 인프라를 충분히 제어해야 합니다.
6. 데이터 버전 제어(DVC)를 사용하여 데이터셋의 변경 사항을 추적하고 조작을 감지합니다. 버전 관리는 모델 무결성 유지에 중요합니다.
7. 이용자가 제공한 정보를 벡터 데이터베이스에 저장하여 전체 모델을 다시 학습시키지 않고도 조정할 수 있게 합니다.
8. 레드팀 캠페인과 연합 학습과 같은 적대적 기술을 사용하여 모델 견고성을 테스트하여 데이터 간섭의 영향을 완화할 수 있습니다.
9. 학습 손실을 모니터링하고 오염의 징후에 대한 모델 동작을 분석합니다. 임계값을 사용하여 비정상적인 출력을 감지합니다.
10. 추론 단계에 RAG와 그라운딩 기술을 통합하여 환각(hallucinations)의 위험을 줄입니다.

### 공격 시나리오 예시

#### 시나리오 #1
  공격자가 학습 데이터를 조작하거나 프롬프트 인젝션 기술을 사용하여 모델의 출력을 편향시켜 잘못된 정보를 확산시킵니다.
#### 시나리오 #2
  적절한 필터링 없이 유해한 데이터가 사용되면 유해하거나 편향된 출력이 발생하여 위험한 정보가 전파될 수 있습니다.
#### 시나리오 # 3
  악의적인 행위자나 경쟁자가 학습용 위조 문서를 생성하여, 이러한 부정확성이 모델 출력에 반영되는 결과를 초래합니다.
#### 시나리오 #4
  부적절한 필터링으로 인해 공격자가 프롬프트 인젝션을 통해 오해의 소지가 있는 데이터를 인젝션할 수 있어 손상된 출력이 발생합니다.
#### 시나리오 #5
  공격자가 오염 기술을 사용하여 모델에 백도어 트리거를 인젝션합니다. 이로 인해 인증 우회, 데이터 유출 또는 숨겨진 명령 실행에 취약해질 수 있습니다.

### 참조 링크

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target): **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/): **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/): **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training): **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models): **Cobalt**

### 관련 프레임워크 및 분류

인프라 구축과 관련된 종합적인 정보, 시나리오 전략, 적용된 환경 제어 및 기타 모범 사례는 이 섹션을 참조하세요.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018): **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**