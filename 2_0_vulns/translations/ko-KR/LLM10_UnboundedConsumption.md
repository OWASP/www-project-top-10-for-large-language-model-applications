## LLM10:2025 무제한 소비

### 설명

무제한 소비는 LLM이 입력 쿼리 또는 프롬프트에 기반하여 출력을 생성하는 과정을 의미합니다. LLM의 추론 기능은 학습된 패턴과 지식을 적용하여 관련 응답이나 예측을 생성하는 핵심적인 역할을 합니다.

서비스를 방해하거나, 대상의 재정 자원을 고갈시키거나, 심지어 모델의 동작을 복제하여 지적 재산을 탈취하려는 공격은 모두 공통적인 보안 취약점을 악용하여 성공합니다. 무제한 소비는 LLM 애플리케이션이 이용자의 과도하고 통제되지 않은 추론을 허용할 때 발생하며, 이는 서비스 거부, 경제적 손실, 모델 도용, 서비스 성능 저하 등의 위험을 초래할 수 있습니다. 특히, 클라우드 환경에서 LLM의 높은 연산 요구량은 리소스 악용 및 무단 사용의 표적이 되기 쉬우며, 이러한 취약점이 공격자에게 악용될 경우 심각한 보안 문제가 발생할 수 있습니다.

### 일반적 취약점 예시

#### 1. 가변 길이 입력 플러딩

  공격자가 다양한 길이의 입력을 대량으로 전송하여 LLM의 처리 효율성을 악용합니다. 이로 인해 시스템 리소스가 소진되거나 응답 불가능한 상태에 빠질 수 있으며, 서비스 가용성에 심각한 영향을 미칠 수 있습니다.

#### 2. 지갑 거부 공격 (Denial of Wallet, DoW)

  공격자가 대량의 연산 작업을 수행하도록 유도하여 클라우드 기반 AI 서비스의 종량제 비용 모델을 악용합니다. 이로 인해 서비스 제공자가 감당할 수 없는 재정적 부담을 떠안게 되며, 심각한 경제적 손실을 초래할 수 있습니다.

#### 3. 지속적 입력 오버플로우

  LLM의 컨텍스트 윈도우를 초과하는 입력을 지속적으로 보내 과도한 컴퓨팅 자원 소비를 유발할 수 있습니다. 결과적으로 서비스 성능이 저하되거나 운영에 차질이 발생할 수 있습니다.

#### 4. 자원 집약적 쿼리

  복잡한 문장 구조나 정교한 언어 패턴을 포함하는 과도하게 높은 연산 비용이 필요한 쿼리를 제출하여 시스템 리소스를 소모시키고 처리 속도를 저하시킬 수 있습니다. 최악의 경우 시스템 장애를 초래할 수도 있습니다.

#### 5. API를 통한 모델 추출

  공격자가 정교하게 설계된 입력과 프롬프트 인젝션 기법을 활용하여 모델 API를 통해 충분한 출력을 수집함으로써 기존 모델의 일부를 복제하거나 그림자 모델을 생성할 수 있습니다. 이는 지적 재산권 침해 위험뿐만 아니라 원본 모델의 무결성을 훼손할 수 있습니다.

#### 6. 기능적 모델 복제

  공격자가 대상 모델을 활용하여 합성 훈련 데이터를 생성한 후, 이를 기반으로 또 다른 기본 모델을 미세 조정하여 기존 모델과 기능적으로 동일한 모델을 제작할 수 있습니다. 이는 전통적인 쿼리 기반 추출 방법을 우회하여 독점 모델 및 기술에 대한 심각한 보안 위협을 초래할 수 있습니다.

#### 7. 부채널 공격

  악의적인 공격자가 LLM의 입력 필터링 기법을 악용하여 부채널 공격을 수행할 수 있습니다. 이를 통해 모델 가중치 및 아키텍처 정보를 추출할 수 있으며, 결국 모델의 보안이 위협받고 추가적인 악용 가능성이 커질 수 있습니다.

### 예방 및 완화 전략

#### 1. 입력 검증

  엄격한 입력 유효성 검사를 구현하여 입력이 합리적인 크기 제한을 초과하지 않도록 합니다.

#### 2. Logits 및 Logprobs 노출 제한

  API 응답에서 logit_bias 및 logprobs 의 노출을 제한하거나 난독화합니다. 자세한 확률을 공개하지 않고 필요한 정보만 제공하세요.

#### 3. 속도 제한

  속도 제한 및 사용자 할당량을 적용하여 단일 소스 엔터티가 주어진 기간 동안 요청할 수 있는 요청 수를 제한합니다.

#### 4. 자원 할당 관리

  자원 할당을 동적으로 모니터링하고 관리하여 단일 사용자나 요청이 과도한 리소스를 소비하지 않도록 방지하세요.

#### 5. 타임아웃 및 조절

  자원을 많이 사용하는 작업에 대해 타임아웃을 설정하고, 처리 속도를 조절하여 과도한 자원 소비를 방지합니다.

#### 6.샌드박스 기술

  LLM의 네트워크 자원, 내부 서비스 및 API에 대한 LLM의 액세스를 제한합니다. 이는 내부자 위험과 위협을 포괄하기 때문에 모든 일반적인 시나리오에서 특히 중요합니다. 또한 LLM 애플리케이션의 데이터 및 리소스 접근 범위를 관리하여 부채널 공격을 완화하거나 방지하는 중요한 제어 메커니즘으로 작용합니다.

#### 7. 포괄적인 로깅, 모니터링 및 이상 징후 탐지

  자원 사용량을 지속적으로 모니터링하고 로깅을 구현하여 비정상적인 자원 소비 패턴을 감지하고 대응하세요.

#### 8. 워터마킹

  LLM 출력물의 무단 사용을 감지하고 방지할 수 있도록 워터마킹 프레임워크를 구현합니다.

#### 9. 단계적 성능 저하

  과부하가 걸렸을 때 시스템이 정상적으로 작동하도록 설계하여 완전한 장애가 아닌 부분적인 기능을 유지합니다.

#### 10. 대기열 처리 제한 및 확장성 확보

  대기 중인 작업 수와 총 작업에 대한 제한을 구현하는 동시에 동적 확장 및 로드 밸런싱을 통합하여 다양한 요구를 처리하고 일관된 시스템 성능을 보장하세요.

#### 11. 적대적 견고성 훈련

  적대적 쿼리 및 추출 시도를 탐지하고 완화할 수 있도록 모델을 훈련합니다.

#### 12. 글리치 토큰 필터링

  알려진 글리치 토큰의 목록을 구축하고, 이를 모델의 컨텍스트 윈도우에 추가하기 전에 필터링합니다.

#### 13. 접근 통제

  역할 기반 접근 제어(RBAC) 및 최소 권한 원칙을 적용하여, LLM 모델 저장소 및 훈련 환경에 대한 무단 접근을 제한합니다.

#### 14. 중앙 집중형 ML 모델 인벤토리

  프로덕션에 사용되는 모델에 중앙 집중식 ML 모델 인벤토리 또는 레지스트리를 사용하여 적절한 거버넌스 및 액세스 제어를 보장합니다.

#### 15. 자동화된 MLOps 배포

  거버넌스, 추적, 승인 워크플로우를 포함한 자동화된 MLOps 배포를 구현하여, 인프라 내에서 모델 접근 및 배포 통제를 강화합니다.

### 공격 시나리오 예시

#### 시나리오 #1: 통제되지 않은 입력 크기

  공격자가 LLM 애플리케이션에 비정상적으로 큰 입력을 제출하여, 과도한 메모리 사용과 CPU 부하를 유발합니다. 이로 인해 시스템이 다운되거나 서비스 속도가 심각하게 저하될 수 있습니다.

#### 시나리오 #2: 반복 요청

  공격자가 LLM API에 대량의 요청을 전송하여 계산 리소스를 과도하게 소모하고 정상적인 사용자가 서비스를 사용할 수 없게 만듭니다.

#### 시나리오 #3: 자원 집약적 쿼리

  공격자는 LLM의 가장 계산 비용이 많이 드는 프로세스를 트리거하도록 설계된 특정 입력을 조작하여 CPU 사용 시간을 연장하고 잠재적인 시스템 오류를 유발합니다.

#### 시나리오 #4: 지갑 거부 공격

  공격자는 클라우드 기반 AI 서비스의 사용량 기반 유료 모델을 악용하기 위해 과도한 작업을 생성하여 서비스 제공업체에 지속 불가능한 비용을 초래합니다.

#### 시나리오 #5: 기능적 모델 복제

  공격자는 LLM의 API를 사용하여 합성 학습 데이터를 생성하고 다른 모델을 미세 조정하여 기능적으로 동등한 모델을 생성하고 기존 모델 추출의 제한을 우회합니다.

#### 시나리오 #6: 시스템 입력 필터링 우회

  악의적인 공격자는 입력 필터링 기술과 LLM의 프리앰블을 우회하여 부채널 공격을 수행하고 모델 정보를 자신의 통제하에 있는 원격 제어 리소스로 가져옵니다.

### 참조 링크

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/): **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634): **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463): **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**

### 관련 프레임워크 및 분류

인프라 구축과 관련된 종합적인 정보, 시나리오 전략, 적용된 환경 제어 및 기타 모범 사례는 이 섹션을 참조하세요.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html): **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024): **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029): **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034): **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025): **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html): **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/): **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/): **OWASP Secure Coding Practices**
