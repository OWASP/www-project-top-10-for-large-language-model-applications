## Letter from the Project Leads - Lettre des chefs de projet

Le projet "OWASP Top 10 for Large Language Model Application" a débuté en 2023 en tant qu'effort communautaire ayant pour objectif de de mettre en lumière et adresser les problématiques de sécurités liées à l'utilisation de l'IA et plus spécifiquement des LLMs. A partir de là, la technologie n'a cessé de s'implanter dans une multitude de secteurs et d'applications, et donc apporte avec elle, son lot de risques. Au fur et à mesure de cette intégration toujours plus profonde des LLMs dans la vie de tout les jours jusqu'au opérations internes, les développeurs et les spécialistes de la sécurités découvrent de nouvelles vulnérabilités ainsi que de nouveaux moyens de les contrer.

The OWASP Top 10 for Large Language Model Applications started in 2023 as a community-driven effort to highlight and address security issues specific to AI applications. Since then, the technology has continued to spread across industries and applications, and so have the associated risks. As LLMs are embedded more deeply in everything from customer interactions to internal operations, developers and security professionals are discovering new vulnerabilities—and ways to counter them.

La liste de 2023 a eu un grand succès et a ainsi permis de sensibiliser et construire une base pour sécuriser les usages liés aux LLM, néanmoins, l'histoire n'était qu'à son début et nous avons appris encore plus de choses depuis. Dans cette nouvelle version de 2025, nous avons travaillé avec un plus grand nombre et une plus grande diversité de contributeurs à travers le monde à l'élaboration de cette liste. Le processus a impliqué des sessions de brainstorming, du vote et des retours d'expériences de professionnels aguerris dans le milieu de la sécurité applicative de LLM, tant dans la contribution que dans son amélioration. Chaque voix entendue a été déterminante dans la création, rédaction et utilisabilité de cette nouvelle parution.

The 2023 list was a big success in raising awareness and building a foundation for secure LLM usage, but we've learned even more since then. In this new 2025 version, we’ve worked with a larger, more diverse group of contributors worldwide who have all helped shape this list. The process involved brainstorming sessions, voting, and real-world feedback from professionals in the thick of LLM application security, whether by contributing or refining those entries through feedback. Each voice was critical to making this new release as thorough and practical as possible.

### What’s New in the 2025 Top 10 - Quoi de neuf dans le Top 10 2025

La liste de 2025 permet une meilleur compréhension des risques existant et introduit des avancées majeures sur la manière dont les LLms sont réellement utilisés. Par exemple **Consommation démesurée** ajoute que les attaques par déni de service (DDoS) qui déjà pouvait inclure des risques autour de la gestion des ressources peut tout aussi bien engendrer des coûts supplémentaires non prévu qui peut s'avérer très problématique dans le cas de déploiement de large LLMs.

The 2025 list reflects a better understanding of existing risks and introduces critical updates on how LLMs are used in real-world applications today. For instance, **Unbounded Consumption** expands on what was previously Denial of Service to include risks around resource management and unexpected costs—a pressing issue in large-scale LLM deployments.

L'article **Vecteurs et Intégration** répond à la demande de la communauté de savoir comment pouvoir sécuriser les Retriaval-Augmented Generation (RAF) ainsi que les autres méthodes d’intégrations qui sont dorénavant des pratiques clés pour garantir une génération cohérente des modèles.

The **Vector and Embeddings** entry responds to the community’s requests for guidance on securing Retrieval-Augmented Generation (RAG) and other embedding-based methods, now core practices for grounding model outputs.

Nous avons aussi ajouté **Fuite dans le système de prompt** qui adresse frontalement les exploitations de vulnérabilités, ce qui était également grandement demandé par la communauté. De nombreuses applications pensaient que les prompts étaient isolées de manière sécurisée, mais des incidents récents ont démontré que les développeurs ne peuvent pas garantir que les informations des prompts demeurent secrètes.

We’ve also added **System Prompt Leakage** to address an area with real-world exploits that were highly requested by the community. Many applications assumed prompts were securely isolated, but recent incidents have shown that developers cannot safely assume that information in these prompts remains secret.

**Abus d'agencement** a été aussi modifié au vue de l’accroissement du nombre d'architectures avec agent qui permettent aux LLM d'avoir plus d'autonomie. Avec les LLMs agissant en tant qu'agent ou en tant que plugins, des permissions non vérifiées peuvent induire à des actions non voulues ou risquées, mettant alors cet problématique plus critique que jamais. 

**Excessive Agency** has been expanded, given the increased use of agentic architectures that can give the LLM more autonomy. With LLMs acting as agents or in plug-in settings, unchecked permissions can lead to unintended or risky actions, making this entry more critical than ever.

### Moving Forward - Aller plus loin 

Tout comme la technologie elle-même, cette liste est un produit de l'expérience et de la connaissance de la communauté opensource. Elle a été construite par les contributions de développeurs, data scientists, et d'experts de la sécurité de divers secteurs, tous dans la même optique de mettre en place une utilisation plus sécurisée de L'IA. Nous sommes fiers de partager cette nouvelle version de 2025 avec vous, nous espérons qu'elle vous donnera les outils et la connaissance pour sécuriser vos LLMs efficacement.

Like the technology itself, this list is a product of the open-source community’s insights and experiences. It has been shaped by contributions from developers, data scientists, and security experts across sectors, all committed to building safer AI applications. We’re proud to share this 2025 version with you, and we hope it provides you with the tools and knowledge to secure LLMs effectively.

Merci à tout ceux qui ont contribué et ceux qui continuent d'utiliser et d'améliorer ces articles. Nous sommes très reconnaissants de faire partie de cette aventure à vos côtés.

Thank you to everyone who helped bring this together and those who continue to use and improve it. We’re grateful to be part of this work with you.

#### Steve Wilson

Project Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: <https://www.linkedin.com/in/wilsonsd/>

#### Ads Dawson

Technical Lead & Vulnerability Entries Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: <https://www.linkedin.com/in/adamdawson0/>

#### Équipe de traduction française

Milly VAILLANT
LinkedIn: <https://www.linkedin.com/in/milly-vaillant/>