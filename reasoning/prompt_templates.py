SCENE_REASONING_PROMPT = """
You are an autonomous driving safety system.

Traffic Knowledge:
{context}

Scene Information:
{scene}

Based on the scene and the traffic knowledge, analyze the situation.

Respond strictly in JSON:

{{
"scene_description": "...",
"risk_level": "low | medium | high",
"main_risk": "...",
"recommended_action": "..."
}}
""" 