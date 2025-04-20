from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import agentops

# Charger la clé API si stockée dans un fichier .env
load_dotenv()


def flatten_messages(messages: list[dict[str, str]]) -> str:
    """Convertit une liste de messages chat en un prompt unique pour LLM."""
    prompt = ""
    for msg in messages:
        role = msg["role"]
        content = msg["content"]
        if role == "system":
            prompt += f"[System]\n{content}\n\n"
        elif role == "user":
            prompt += f"[User]\n{content}\n\n"
        elif role == "assistant":
            prompt += f"[Assistant]\n{content}\n\n"
    return prompt.strip()


class COTLLM(LLM):
    def call(self, messages: list[dict[str, str]], **kwargs) -> str:
        from test_strategie_decoding_COT import decoding_cot_pipeline  # ton script réutilisé

        prompt = flatten_messages(messages)

        print(f"\n🚀 Pipeline COT lancé sur le prompt : {prompt}")
        final_answer = decoding_cot_pipeline(prompt, k=3)

        return (
            f"Thought: I reasoned through several possible answers using a CoT strategy.\n"
            f"Final Answer: {final_answer}"
        )


agent = Agent(
    role="Assistant en orthographe",
    goal="Répondre avec pertinence aux questions d'orthographe",
    backstory="",
    llm=COTLLM(
        model="gpt-4o",  # utilisé par l’API interne
        temperature=0.0  # pas utilisé dans ton decoding
    ),
    allow_delegation=False
)

task = Task(
    description="Combien de R dans le mot Strawberry ?",
    expected_output="Une phrase simple.",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task], verbose=True)

if __name__ == "__main__":
    session_agentops = agentops.init(default_tags=["test wrapper"])
    result = crew.kickoff()
    print("\n=== Résultat final ===")
    print(result)


#${env:AGENTOPS_API_KEY} = "eda5a49a-9491-40eb-aaa6-45c962ad5cae"