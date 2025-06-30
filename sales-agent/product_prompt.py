KNOWLEDGE_BASE = {
    "health_score": """
    Product: Health Score
    Includes: Lab-test based analysis, personalized report on overall health and biological age.
    How it works: You get a kit, do a blood test, results are analyzed.
    Value: Helps understand lifestyle impact, provides actionable insights.
    Pricing: Rs. 2299.
    Test Requirements: Blood sample.
    Scientific Credibility: Based on extensive scientific research and medical guidelines.
    """,

    "alcohol_risk_assessment": """
    Product: Alcohol Risk Assessment
    Includes: Behavioral and lab-based evaluation of alcohol-related health risks.
    How it works: Involves a questionnaire and specific blood tests.
    Value: Offers personalized insights into your alcohol-related health risks and guidance for healthier choices.
    Pricing: Rs. 10999.
    Test Requirements: Questionnaire and blood tests.
    Scientific Credibility: Based on extensive medical research.
    """,

    "stress_impact_assessment": """
    Product: Stress Impact Assessment
    Includes: Multi-input measure of physical and emotional stress load.
    How it works: Uses a combination of wearable data (optional) and self-reported information.
    Value: Helps identify sources of stress and provides actionable strategies for managing physical and emotional well-being.
    Pricing: Rs. 1999.
    Test Requirements: Self-reported info, optional wearable data.
    Scientific Credibility: Developed by stress physiology experts.
    """,

    "refund_policy": """
    Refund Policy: You can receive a full refund within 14 days of purchase if no lab tests have been initiated.
    For specific refund scenarios, please refer to our full FAQ on our website, or I can connect you to our care team.
    """,

    "data_safety": """
    Data Safety: Your data privacy and security are our top priorities. We use industry-standard encryption and strict data handling protocols to ensure your information is protected. We never share your data with third parties without your explicit consent.
    """,
    
    "worth_it": """
    Is it worth it?: Many users find our insights incredibly valuable for informed health decisions. Investing in your health with actionable data is highly beneficial.
    """
}

# Combine all knowledge into a single string
COMBINED_KNOWLEDGE = "\n\n--- KNOWLEDGE BASE START ---\n\n" + \
                     "\n\n---\n\n".join(KNOWLEDGE_BASE.values()) + \
                     "\n\n--- KNOWLEDGE BASE END ---\n"