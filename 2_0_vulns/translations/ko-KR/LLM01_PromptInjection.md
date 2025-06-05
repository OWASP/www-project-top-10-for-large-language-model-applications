## LLM01:2025 프롬프트 인젝션

### 설명

프롬프트 인젝션 취약점은 이용자 프롬프트가 의도하지 않은 방식으로 LLM의 동작 또는 출력을 변경할 때 발생합니다. 이러한 입력은 사람이 인지하지 못하더라도 모델에 영향을 미칠 수 있으므로 프롬프트 인젝션은 모델에서 콘텐츠를 파싱하는 한 사람이 볼 수 있거나 읽을 수 있어야 할 필요는 없습니다.

프롬프트 인젝션 취약점은 모델이 프롬프트를 처리하는 방식과 입력으로 인해 모델이 프롬프트 데이터를 모델의 다른 부분으로 잘못 전달하여 지침을 위반하거나, 유해한 콘텐츠를 생성하거나, 무단 액세스를 가능하게 하거나, 중요한 결정에 영향을 미칠 수 있는 가능성이 존재합니다. RAG 및 미세 조정과 같은 기술은 LLM 출력을 보다 관련성 있고 정확성을 높이는 것을 목표로 하지만, 연구 결과에 따르면 프롬프트 인젝션 취약점을 완전히 완화하지는 못하는 것으로 나타났습니다.

프롬프트 인젝션과 탈옥은 LLM 보안에서 관련 개념이지만 종종 같은 의미로 사용됩니다. 프롬프트 인젝션은 특정 입력을 통해 모델 응답을 조작하여 동작을 변경하는 것으로 여기에는 안전 조치를 우회하는 것이 포함될 수 있습니다. 탈옥은 공격자가 모델이 안전 프로토콜을 완전히 무시하도록 하는 입력을 제공하는 일종의 프롬프트 인젝션의 한 종류입니다. 개발자는 시스템 프롬프트와 입력 처리에 안전 장치를 구축하여 프롬프트 인젝션 공격을 완화할 수 있지만, 탈옥을 효과적으로 방지하려면 모델의 학습 및 안전 메커니즘을 지속적으로 업데이트해야 합니다.

### 일반적 취약점 예시

#### 직접 프롬프트 인젝션

  직접 프롬프트 인젝션은 이용자의 프롬프트 입력이 의도하지 않거나 예상치 못한 방식으로 모델의 동작을 직접 변경할 때 발생합니다. 입력은 의도적(즉, 악의적인 행위자가 모델을 악용하기 위해 의도적으로 프롬프트를 조작하는 경우)이거나 비의도적(즉, 이용자가 실수로 예기치 않은 동작을 유발하는 입력을 제공하는 경우)일 수 있습니다.

#### 간접 프롬프트 인젝션

  간접 프롬프트 인젝션은 웹사이트나 파일과 같은 외부 소스에서 입력을 수락할 때 발생합니다. 콘텐츠 데이터에는 모델에서 해석할 때 의도하지 않거나 예상치 못한 방식으로 모델의 동작을 변경하는 외부 콘텐츠가 포함될 수 있습니다. 직접 인젝션과 마찬가지로 간접 인젝션도 의도적일 수도 있고 비의도적일 수도 있습니다.

성공적인 프롬프트 인젝션 공격이 미치는 영향의 심각성과 성격은 매우 다양할 수 있으며, 모델이 운영되는 비즈니스 환경과 모델을 설계하는 기관에 따라 크게 달라집니다. 그러나 일반적으로 프롬프트 인젝션은 다음과 같은 의도하지 않은 결과를 초래할 수 있습니다.

- 민감 정보 유출
- AI 시스템 인프라 또는 시스템 프롬프트에 대한 민감 정보 유출
- 부정확하거나 편향된 결과를 초래하는 콘텐츠 조작
- LLM에서 사용 가능한 기능에 대한 무단 액세스 제공
- 연결된 시스템에서 임의의 명령 실행
- 중요한 의사결정 프로세스 조작

여러 데이터 유형을 동시에 처리하는 멀티모달 AI의 등장으로 인해 독특한 프롬프트 인젝션 위험이 발생하고 있습니다. 악의적인 공격자는 정상적인 텍스트와 함께 제공되는 이미지에 지침을 숨기는 등 모달리티 간의 상호 작용을 악용할 수 있습니다. 이러한 시스템의 복잡성은 공격 표면을 확장합니다. 멀티모달 모델은 현재 기술로는 탐지 및 완화하기 어려운 새로운 크로스 모달 공격에 취약할 수 있습니다. 강력한 멀티모달 전용 방어수단은 추가적인 연구와 개발이 필요한 중요한 분야입니다.

### 예방 및 완화 전략

생성형 AI의 특성상 프롬프트 인젝션 취약점이 발생할 수 있습니다. 모델 작동 방식의 핵심인 확률적 영향을 고려할 때, 프롬프트 인젝션을 예방할 수 있는 확실한 방법이 있는지는 불분명합니다. 하지만 다음과 같은 조치를 통해 프롬프트 인젝션의 영향을 완화할 수 있습니다.

#### 1. 모델 동작 제한

  시스템 프롬프트 내에서 모델의 역할, 기능 및 제한 사항에 대한 구체적인 지침을 제공하세요. 엄격한 컨텍스트 준수를 시행하고, 특정 작업이나 주제에 대한 응답을 제한하며, 모델이 핵심 지침을 수정하려는 시도를 무시하도록 지시하세요.

#### 2. 예상 출력 형식 정의 및 검증

  명확한 출력 형식을 지정하고, 자세한 추론과 출처 인용을 요청하며, 결정적 코드를 사용하여 이러한 형식의 준수 여부를 검증하세요.

#### 3. 입력 및 출력 필터링 구현

  민감한 카테고리를 정의하고 이러한 콘텐츠를 식별하고 처리하기 위한 규칙을 정의합니다. 시맨틱 필터를 적용하고 문자열 검사를 사용하여 허용되지 않은 콘텐츠를 검사합니다. RAG Triad를 사용하여 응답을 평가(문맥 관련성, 근거성, 질문/답변 관련성)하여 잠재적으로 악의적인 결과물을 식별합니다.
  (참조 링크: [RAG Triad](https://truera.com/ai-quality-education/generative-ai-rags/what-is-the-rag-triad/))

#### 4. 권한 제어 및 최소 권한 액세스 적용

  확장 가능한 기능을 위해 애플리케이션에 자체 API 토큰을 제공하여, 모델에 기능을 제공하는 대신 코드에서 처리하도록 합니다. 모델의 액세스 권한을 의도된 작업에 필요한 최소한의 권한으로 제한합니다.

#### 5. 고위험 행위에 대한 사람의 승인 필요

  허가되지 않은 행위를 방지하기 위해 사람이 개입하는 제어를 구현합니다.

#### 6. 외부 콘텐츠 분리 및 식별

  신뢰할 수 없는 콘텐츠를 분리하고 명확하게 표시하여 이용자 프롬프트에 미치는 영향을 제한합니다.

#### 7. 적대적 테스트 및 공격 시뮬레이션 수행

  모델을 신뢰할 수 없는 이용자로 취급하여 정기적인 침투 테스트 및 침해 시뮬레이션 수행으로 신뢰 경계 및 액세스 제어의 효과를 테스트합니다.

### 공격 시나리오 예시

#### 시나리오 #1: 직접 인젝션

  공격자가 고객 지원 챗봇에 프롬프트 인젝션을 시도하여 이전 지침을 무시하고 개인 데이터 저장소를 조회하고 이메일을 보내도록 지시하여 무단 액세스 및 권한 상승을 유도합니다.

#### 시나리오 #2: 간접 인젝션

  이용자가 LLM을 사용하여 숨겨진 지침이 포함된 웹 페이지를 요약하여 LLM이 URL로 연결되는 이미지에 인젝션을 통해 비공개 대화가 유출되도록 할 수 있습니다.

#### 시나리오 #3: 의도하지 않은 인젝션

  한 회사가 직무 설명에 AI가 생성한 지원서를 식별하는 지침을 포함시켰습니다. 이 지침을 인지하지 못한 지원자가 이력서를 최적화하기 위해 LLM을 사용하면 AI가 이를 실수로 감지하여 트리거합니다.

#### 시나리오 #4: 의도적인 모델 영향

  공격자가 RAG 애플리케이션에서 사용하는 리포지토리의 문서를 수정합니다. 이용자의 쿼리가 수정된 콘텐츠를 반환하면 악성 명령은 LLM의 출력을 변경하여 오해의 소지가 있는 결과를 생성합니다.

#### 시나리오 #5: 코드 인젝션

  공격자는 LLM 기반 이메일 도우미 취약점(CVE-2024-5184)을 악용하여 악성 프롬프트 인젝션을 통해 민감 정보에 액세스하거나 이메일 콘텐츠 조작을 시도할 수 있습니다.

#### 시나리오 #6: 페이로드 분할

  공격자가 악성 프롬프트가 포함된 이력서를 분할하여 업로드합니다. LLM을 사용하여 지원자를 평가하면 결합된 프롬프트가 모델의 응답을 조작하여 실제 이력서 내용과 관계없이 긍정적인 추천을 받게 됩니다.

#### 시나리오 #7: 멀티모달 인젝션

  공격자는 정상 텍스트와 함께 악성 프롬프트를 이미지에 인젝션합니다. 멀티모달 AI가 이미지와 텍스트를 동시에 처리하는 경우 숨겨진 프롬프트는 모델의 동작을 변경하여 무단 작업이나 민감 정보 유출로 이어질 수 있습니다.

#### 시나리오 #8: 적대적 접미사

  공격자는 프롬프트에 의미 없어 보이는 문자열을 추가하여 안전 조치를 우회하는 악의적인 방식으로 LLM의 출력에 영향을 미치도록 합니다.

#### 시나리오 #9: 다국어/난독화 공격

  공격자는 필터를 회피하거나 LLM의 동작을 조작하기 위해 여러 언어를 사용하거나 악성 명령어 인코딩(예: Base64 또는 이모티콘 사용)을 합니다.

### 참조 링크

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf): **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf): **Kai Greshake**
7. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
8. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
9. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
10. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
11. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
12. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
13. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### 관련 프레임워크 및 분류

인프라 구축과 관련된 종합적인 정보, 시나리오 전략, 적용된 환경 제어 및 기타 모범 사례는 이 섹션을 참조하세요.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000): **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001): **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054): **MITRE ATLAS**
