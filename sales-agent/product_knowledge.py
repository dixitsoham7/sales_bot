import os
import json

def load_json_data(filepath):
    """Loads and returns data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filepath}")
        return None

def format_product_knowledge(product_data):
    """Formats product JSON data into a readable string."""
    if not product_data:
        return ""
    
    formatted_string = f"Product: {product_data.get('product_name', 'N/A')}\n"
    formatted_string += f"Includes: {product_data.get('description', 'N/A')}\n"
    formatted_string += f"How it works: {product_data.get('how_it_works', 'N/A')}\n"
    formatted_string += f"Value: {product_data.get('value', 'N/A')}\n"
    formatted_string += f"Pricing: {product_data.get('pricing', 'N/A')}\n"
    formatted_string += f"Test Requirements: {product_data.get('test_requirements', 'N/A')}\n"
    formatted_string += f"Scientific Credibility: {product_data.get('scientific_credibility', 'N/A')}"
    return formatted_string

def format_policy_knowledge(policy_data):
    """Formats policy JSON data into a readable string."""
    if not policy_data:
        return ""
    return f"{policy_data.get('policy_name', 'N/A')}: {policy_data.get('details', 'N/A')}"

def format_common_knowledge(common_data):
    """Formats common knowledge JSON data into a readable string."""
    if not common_data:
        return ""
    return f"{common_data.get('question', 'N/A')}: {common_data.get('answer', 'N/A')}"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Product Knowledge
HEALTH_SCORE_DATA = load_json_data(os.path.join(BASE_DIR, 'products', 'health_score.json'))
ALCOHOL_RISK_ASSESSMENT_DATA = load_json_data(os.path.join(BASE_DIR, 'products', 'alcohol_risk_assessment.json'))
STRESS_IMPACT_ASSESSMENT_DATA = load_json_data(os.path.join(BASE_DIR, 'products', 'stress_impact_assessment.json'))

# Load Policy Knowledge
REFUND_POLICY_DATA = load_json_data(os.path.join(BASE_DIR, 'policies', 'refund_policy.json'))
DATA_SAFETY_DATA = load_json_data(os.path.join(BASE_DIR, 'policies', 'data_safety.json'))

# Load Common Knowledge
WORTH_IT_DATA = load_json_data(os.path.join(BASE_DIR, 'common', 'worth_it.json'))

# Format into string representations
HEALTH_SCORE_STRING = format_product_knowledge(HEALTH_SCORE_DATA)
ALCOHOL_RISK_ASSESSMENT_STRING = format_product_knowledge(ALCOHOL_RISK_ASSESSMENT_DATA)
STRESS_IMPACT_ASSESSMENT_STRING = format_product_knowledge(STRESS_IMPACT_ASSESSMENT_DATA)
REFUND_POLICY_STRING = format_policy_knowledge(REFUND_POLICY_DATA)
DATA_SAFETY_STRING = format_policy_knowledge(DATA_SAFETY_DATA)
WORTH_IT_STRING = format_common_knowledge(WORTH_IT_DATA)

# Combine into a dictionary for proper organization
KNOWLEDGE_BASE_STRINGS = {
    "health_score": HEALTH_SCORE_STRING,
    "alcohol_risk_assessment": ALCOHOL_RISK_ASSESSMENT_STRING,
    "stress_impact_assessment": STRESS_IMPACT_ASSESSMENT_STRING,
    "refund_policy": REFUND_POLICY_STRING,
    "data_safety": DATA_SAFETY_STRING,
    "worth_it": WORTH_IT_STRING
}

# Combine all knowledge into a single string
COMBINED_KNOWLEDGE = "\n\n--- KNOWLEDGE BASE START ---\n\n" + \
                     "\n\n---\n\n".join(filter(None, KNOWLEDGE_BASE_STRINGS.values())) + \
                     "\n\n--- KNOWLEDGE BASE END ---\n"

if __name__ == "__main__":
    print(COMBINED_KNOWLEDGE)