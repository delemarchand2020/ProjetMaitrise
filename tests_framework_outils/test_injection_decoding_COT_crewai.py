from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import agentops

# Charger la clé API si stockée dans un fichier .env
load_dotenv()

class COTLLM(LLM):
    def call(self, messages: list[dict[str, str]], **kwargs) -> str:
        from test_strategie_decoding_COT import decoding_cot_pipeline  # ton script réutilisé

        # 🔍 Trouver le dernier message utilisateur
        prompt = None
        for msg in reversed(messages):
            if msg["role"] == "user":
                prompt = msg["content"]
                break

        if not prompt:
            raise ValueError("No user prompt found in messages")

        print(f"\n🚀 Pipeline COT lancé sur le prompt : {prompt}")
        final_answer = decoding_cot_pipeline(prompt, k=3)

        return (
            f"Thought: I reasoned through several possible answers using a CoT strategy.\n"
            f"Final Answer: {final_answer}"
        )


agent = Agent(
    role="Explorateur raisonnement",
    goal="Répondre avec un raisonnement COT optimisé",
    backstory="Un assistant IA curieux qui explore plusieurs chemins de réponse.",
    llm=COTLLM(
        model="gpt-4o",  # utilisé par l’API interne
        temperature=0.0  # pas utilisé dans ton decoding
    ),
    allow_delegation=False
)

task = Task(
    description="Combien de R dans le mot Strawberry ?",
    expected_output="Une phrase réponse (sujet verbe complément)",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task], verbose=True)

if __name__ == "__main__":
    session_agentops = agentops.init(default_tags=["test wrapper"])
    result = crew.kickoff()
    print("\n=== Résultat final ===")
    print(result)


#${env:AGENTOPS_API_KEY} = "eda5a49a-9491-40eb-aaa6-45c962ad5cae"