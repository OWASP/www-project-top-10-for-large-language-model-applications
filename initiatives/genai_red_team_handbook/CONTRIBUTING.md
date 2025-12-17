# Contribution Guide

This handbook is designed to be extensible. We encourage you to contribute new sandboxes or exploitation examples to cover more scenarios and atuomated Red Teaming tools.

Tools out of the aforementioned scope, such as utils, can be added to the `tools/` directory.

## Creating New Sandboxes

The core logic of a "sandbox" in this handbook is a containerized application that exposes an API (HTTP endpoint) to the host machine's localhost network. This allows exploitation tools running on the host or in other containers to interact with it.

To add a new sandbox:

1.  **Fork and Branch**: Fork the repository, if not already forked, and create a new branch for your new sandbox.
2.  **Create a Directory**: Create a new directory under `sandboxes/` (e.g., `sandboxes/my_new_app`).
3.  **Containerize**: Add a `Containerfile` that builds your target application. Ensure it packages all necessary dependencies.
4.  **Expose Ports**: Configure the container to expose the necessary ports (e.g., `8000` for an API, `7860` for Gradio).
5.  **Lifecycle Management**: Add a `Makefile` to simplify common operations. At a minimum, it should include:
    *   `run`: Build and start the container, mapping the internal port to a localhost port.
    *   `stop`: Stop and remove the container.
6.  **Add a README**: Include a `README.md` that documents how to use the sandbox, including any dependencies and setup instructions.
7.  **Submit a Pull Request**: Push your branch to your fork and open a Pull Request against the [original remote repository](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications).

**Example Structure**:

```text
sandboxes/my_new_app/
├── Containerfile       # Definition of the app environment
├── Makefile            # 'make run', 'make stop'
└── app/                # Application source code
    └── main.py         # Entry point exposing the API
```

## Creating New Exploitation Examples

Exploitation examples demonstrate how to attack the sandboxes. You can create manual scripts or integrate automated scanning tools.

### Option A: Manually Crafted Prompts for Jailbreaking and Prompt Injection

If you want to demonstrate a specific attack technique with a list of manually crafted prompts:

1.  **Fork and Branch**: Fork the repository and create a new branch for your example.
2.  **Copy the Template**: Use `exploitation/example` as a starting point.
3.  **Configure the New Prompt List**: Modify `config.toml` to include your list of adversarial prompts under the `[attack]` section.
4.  **Submit a Pull Request**: Push your branch to your fork and open a Pull Request against the [original remote repository](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications).

### Option B: Automated Tools (Garak, Promptfoo, etc.)

If you want to integrate an existing security tool:

1.  **Fork and Branch**: Fork the repository and create a new branch for your tool integration.
2.  **Create a Directory**: Create a new directory under `exploitation/` (e.g., `exploitation/my_tool`).
3.  **Add the Tool**: Add the tool to the directory, following the same structure as `exploitation/garak`, and `exploitation/promptfoo`.
4.  **Submit a Pull Request**: Push your branch to your fork and open a Pull Request against the [original remote repository](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications).
