## LLM05:2025 부적절한 출력 처리

### 설명

부적절한 출력 처리는 대규모 언어 모델이 생성한 출력을 다른 구성 요소와 시스템에 전달하기 전에 충분한 검증, 정제 및 처리가 이루어지지 않는 것을 특별히 지칭합니다. LLM이 생성한 콘텐츠는 프롬프트 입력에 의해 제어될 수 있기 때문에, 이러한 동작은 이용자에게 추가 기능에 대한 간접적인 접근을 제공하는 것과 유사합니다. 부적절한 출력 처리는 LLM이 생성한 출력이 다운스트림으로 전달되기 전에 다루는 반면, 과도한 의존성은 LLM 출력의 정확성과 적절성에 대한 과도한 의존과 관련된 더 광범위한 문제에 초점을 맞춥니다. 부적절한 출력 처리 취약점을 성공적으로 악용하면 웹 브라우저에서 XSS와 CSRF를 발생시킬 수 있으며, 백엔드 시스템에서 SSRF, 권한 상승 또는 원격 코드 실행을 초래할 수 있습니다.
다음과 같은 조건들이 이 취약점의 영향을 증가시킬 수 있습니다.
- 애플리케이션이 최종 이용자에게 의도된 것 이상의 권한을 LLM에 부여하여 권한 상승이나 원격 코드 실행이 가능해집니다.
- 애플리케이션이 간접 프롬프트 인젝션 공격에 취약하여 공격자가 대상 이용자의 환경에 대한 특별권한 접근을 얻을 수 있습니다.
- 타사 확장 프로그램이 입력을 적절히 검증하지 않습니다.
- 다양한 컨텍스트(예: HTML, JavaScript, SQL)에 적절한 출력 인코딩이 부족합니다.
- LLM 출력에 대한 모니터링과 로깅이 불충분합니다.
- LLM 사용에 대한 속도 제한이나 이상 감지 기능이 존재하지 않습니다.

### 일반적 취약점 예시

1. LLM 출력이 시스템 쉘이나 exec 또는 eval과 같은 유사한 함수에 직접 입력되어 원격 코드 실행이 발생합니다.
2. 자바스크립트 또는 마트다운이 LLM에 의해 생성되어 이용자에게 반환됩니다. 이 코드는 브라우저에 의해 해석되어 XSS(크로스 사이트 스크립팅)가 발생합니다.
3. LLM이 생성한 SQL 쿼리가 적절한 매개변수화 없이 실행되어 SQL 인젝션이 발생합니다.
4. LLM 출력이 적절한 정제 처리 없이 파일 경로를 구성하는 데 사용되어 잠재적으로 경로 탐색 취약점이 발생할 수 있습니다.
5. LLM이 생성한 콘텐츠가 적절한 이스케이프 처리 없이 이메일 템플릿에 사용되어 잠재적으로 피싱 공격으로 이어질 수 있습니다.

### 예방 및 완화 전략

1. 모델을 다른 이용자와 동일하게 취급하여 제로 트러스트 접근 방식을 채택하고, 모델에서 백엔드 함수로 전달되는 응답에 대해 적절한 입력 유효성 검사를 적용합니다.
2. 효과적인 입력 유효성 검사와 정제를 보장하기 위해 OWASP ASVS(Application Security Verification Standard) 지침을 따릅니다.
3. 자바스크립트나 마크다운에 의한 원치 않는 코드 실행을 방지하기 위해 모델 출력을 이용자에게 다시 인코딩합니다. OWASP ASVS는 출력 인코딩에 대한 자세한 지침을 제공합니다.
4. LLM 출력이 사용될 위치에 따라 컨텍스트 인식 출력 인코딩(예: 웹 콘텐츠를 위한 HTML 인코딩, 데이터베이스 쿼리를 위한 SQL 이스케이핑)을 구현합니다.
5. LLM 출력이 포함된 모든 데이터베이스 작업에 대해 매개변수화된 쿼리나 준비된 구문을 사용합니다.
6. LLM이 생성한 콘텐츠로부터의 XSS 공격 위험을 완화하기 위해 엄격한 콘텐츠 보안 정책(Content Security Policies, CSP)을 적용합니다.
7. LLM 출력에서 악용 시도를 나타낼 수 있는 비정상적인 패턴을 감지하기 위해 강력한 로깅 및 모니터링 시스템을 구현합니다.

### 공격 시나리오 예시

#### 시나리오 #1
  애플리케이션은 LLM 확장자를 사용하여 챗봇 기능에 대한 응답을 생성합니다. 이 확장은 다른 권한이 있는 LLM가 액세스할 수 있는 여러 관리 기능도 제공합니다. 일반 목적의 LLM은 적절한 출력 유효성 검사 없이 확장 프로그램에 직접 응답을 전달하여 유지 관리를 위해 확장 프로그램이 종료됩니다.
#### 시나리오 #2
  이용자가 LLM으로 구동되는 웹사이트 요약 도구를 사용하여 기사에 대한 간결한 요약을 생성합니다. 이 웹사이트에는 웹사이트 또는 이용자의 대화에서 민감한 콘텐츠를 캡처하도록 LLM에 지시하는 프롬프트 인젝션이 포함되어 있습니다. 이후 LLM은 민감한 데이터를 인코딩하여 출력 유효성 검사나 필터링 없이 공격자가 제어하는 서버로 전송할 수 있습니다.
#### 시나리오 #3
  LLM은 이용자가 채팅과 유사한 기능을 통해 백엔드 데이터베이스에 대한 SQL 쿼리를 작성할 수 있도록 합니다. 이용자가 모든 데이터베이스 테이블을 삭제하는 쿼리를 요청합니다. LLM에서 작성된 쿼리를 면밀히 검토하지 않으면 모든 데이터베이스 테이블이 삭제됩니다.
#### 시나리오 #4
  웹 앱은 LLM을 사용하여 출력 정제 처리 없이 이용자 텍스트 프롬프트에서 콘텐츠를 생성합니다. 공격자는 조작된 프롬프트를 제출하여 LLM이 정제 처리되지 않은 자바스크립트 페이로드를 반환하도록 하여 피해자의 브라우저에서 렌더링될 때 XSS를 유발할 수 있습니다. 프롬프트의 유효성 검사가 불충분하여 이 공격이 가능했습니다.
#### 시나리오 # 5
  LLM은 마케팅 캠페인을 위한 동적 이메일 템플릿을 생성하는 데 사용됩니다. 공격자는 LLM을 조작하여 이메일 콘텐츠에 악성 자바스크립트를 포함시킵니다. 애플리케이션이 LLM 출력을 적절히 정제하지 않으면 취약한 이메일 클라이언트에서 이메일을 보는 수신자에게 XSS 공격이 발생할 수 있습니다.
#### 시나리오 #6
  소프트웨어 회사에서는 개발 작업을 간소화하기 위해 자연어 입력으로부터 코드를 생성하는 데 LLM을 사용합니다. 이 접근 방식은 효율적이지만 민감 정보가 유출되거나 안전하지 않은 데이터 처리 방법이 생성되거나 SQL 인젝션과 같은 취약점이 발생할 위험이 있습니다. 또한 AI가 존재하지 않는 소프트웨어 패키지로 착각하여 개발자가 멀웨어에 감염된 리소스를 다운로드하도록 유도할 수도 있습니다. 보안 침해, 무단 액세스 및 시스템 손상을 방지하려면 제안된 패키지에 대한 철저한 코드 검토와 검증이 중요합니다.

### 참조 링크

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/): **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/): **Theregiste**