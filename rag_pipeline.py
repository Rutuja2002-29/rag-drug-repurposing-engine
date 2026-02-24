class MedicalKnowledgeBase:

    def __init__(self):
        self.data = {
            "diabetes": {
                "medicines": ["Metformin", "Insulin", "Glipizide"],
                "drug_value": "High effectiveness in blood sugar control",
                "harmful": "Overdose may cause hypoglycemia",
                "side_effects": ["Nausea", "Weight gain", "Low blood sugar"]
            },
            "lung cancer": {
                "medicines": ["Cisplatin", "Paclitaxel", "Pembrolizumab"],
                "drug_value": "Used in chemotherapy and immunotherapy",
                "harmful": "May weaken immune system",
                "side_effects": ["Hair loss", "Fatigue", "Nausea"]
            },
            "alzheimer": {
                "medicines": ["Donepezil", "Memantine"],
                "drug_value": "Helps manage symptoms",
                "harmful": "May cause dizziness",
                "side_effects": ["Confusion", "Headache"]
            }
        }

    def get_info(self, disease):
        disease = disease.lower()
        return self.data.get(disease, {"error": "Disease not found in database"})