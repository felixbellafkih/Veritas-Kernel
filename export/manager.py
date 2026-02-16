import json

class ExportManager:
    def generate_markdown(self, data):
        """
        Génère un rapport Markdown lisible pour l'humain.
        """
        content = f"# ROOT ANALYSIS: {data['root']}\n"
        content += f"## Arabic: {data['arabic']}\n"
        content += f"**Logic Function:** {data['logic_function']}\n\n"
        content += f"### Description\n{data['description']}\n"
        
        if data.get('binary_pair'):
            content += f"\n**Binary Pair:** {data['binary_pair']}\n"
            
        return f"{data['root']}_report.md", content

    def generate_json(self, data):
        """
        Génère un dump JSON brut pour la machine.
        """
        # On retourne une string JSON formatée
        return json.dumps(data, indent=4, ensure_ascii=False)
