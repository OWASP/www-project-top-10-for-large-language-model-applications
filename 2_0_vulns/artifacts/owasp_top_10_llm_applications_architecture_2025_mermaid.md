graph LR
    %% Core Flow
    Client["Client/malicious actor<br>inputs (prompt + context)<br>CRUD operations"] --> Internet1[("Untrusted medium<br>(IE Internet)")]
    Internet1 --> Inference

    %% Main Application Flow
    Inference --> Ingress
    Ingress --> AppServices["Application Services"]
    AppServices --> LLMAutomation["LLM Automation<br>(Agents)"]
    LLMAutomation --> LLMModel["LLM Model"]
    LLMModel --> ProdServices["LLM Production Services"]
    ProdServices --> ServerFuncs["Server-side Functions"]

    %% Data Store Connections
    LLMModel --- VectorDB[("Vector DB")]
    LLMModel --- PrivateData[("Private Data<br>(RAG)")]

    %% Training Flow
    ExternalData["External Data Sources"] --> Internet2[("Untrusted medium")]
    ExternalData --> FinetuningData[("Fine-tuning Data")]
    FinetuningData --> TrainingData[("Training Data")]

    %% Human Actors
    Engineer["ML Engineer"] -.-> AppServices
    DataScientist["Data Scientist"] -.-> ExternalData

    %% Vulnerabilities
    LLM01["LLM01-Prompt Injection<br>CWE-20,77<br>APL-T0051"] -.-> Ingress
    LLM02["LLM02-Info Disclosure<br>CWE-200,201<br>APL-T0024"] -.-> AppServices
    LLM03["LLM03-Misalignment<br>APL-T0094"] -.-> Inference
    LLM04["LLM04-Data Poisoning<br>CWE-20,125<br>APL-T0058"] -.-> ExternalData
    LLM05["LLM05-Supply Chain<br>CWE-937,1104<br>APL-T0030"] -.-> ExternalData
    LLM06["LLM06-Output Handling<br>CWE-113<br>APL-T0095"] -.-> AppServices
    LLM07["LLM07-Prompt Leakage<br>APL-T0096"] -.-> AppServices
    LLM08["LLM08-Excessive Agency<br>CWE-285,732<br>APL-T0093"] -.-> LLMModel
    LLM09["LLM09-Weaknesses<br>APL-T0095"] -.-> PrivateData
    LLM10["LLM10-Consumption<br>APL-T0029,58,59"] -.-> Inference

    %% Trust Boundaries
    subgraph TB1 [" "]
        VectorDB
        PrivateData
    end

    subgraph TB2 [" "]
        FinetuningData
        TrainingData
    end

    %% Styling
    classDef vulnerability fill:#ffcccb,stroke:#ff0000
    classDef external fill:#f0f0f0,stroke-dasharray: 5 5
    classDef datastore fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef human fill:#e6f3ff,stroke:#0066cc

    class LLM01,LLM02,LLM03,LLM04,LLM05,LLM06,LLM07,LLM08,LLM09,LLM10 vulnerability
    class Internet1,Internet2,ExternalData external
    class VectorDB,PrivateData,TrainingData,FinetuningData datastore
    class Engineer,DataScientist human