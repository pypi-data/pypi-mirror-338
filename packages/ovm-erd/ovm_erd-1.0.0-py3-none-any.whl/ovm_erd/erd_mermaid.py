def generate_mermaid(metadata: dict, output_file="ovm_erd/output/erd_diagram.mmd"):
    """
    Genereert een ERD in Mermaid-syntax op basis van de metadata dictionary.

    :param metadata: Dict met entity-informatie
    :param output_file: Pad naar het bestand waarin de Mermaid-code wordt opgeslagen
    """
    mermaid_lines = ["```mermaid", "graph TD"]

    # Mermaid nodes
    for data in metadata.values():
        name = data["table_name"]
        pattern = data.get("pattern", "")

        if pattern == "sat":
            style = 'fill:#fffacc,stroke:#333,stroke-width:1px'
        elif pattern == "link":
            style = 'fill:#cfe2ff,stroke:#333,stroke-width:1px'
        else:  # hub of default
            style = 'fill:#ffffff,stroke:#333,stroke-width:1px'

        mermaid_lines.append(f'{name}["{name}"]')
        mermaid_lines.append(f'style {name} {style}')

    # Relaties
    for data in metadata.values():
        table = data["table_name"]
        pattern = data.get("pattern", "")
        pk = data.get("pk", "")
        fk_list = data.get("fk", [])

        if pattern == "sat":
            for hub in metadata.values():
                if hub.get("pattern") == "hub" and hub.get("pk") == pk:
                    mermaid_lines.append(f'{hub["table_name"]} --> {table}')
        elif pattern == "link":
            for fk in fk_list:
                for hub in metadata.values():
                    if hub.get("pattern") == "hub" and hub.get("pk") == fk:
                        mermaid_lines.append(f'{hub["table_name"]} --> {table}')

    mermaid_lines.append("```")

def generate_mermaid_markdown(metadata: dict, output_file="ovm_erd/output/erd_diagram.md", title="ERD Diagram"):
    """
    Genereert een volledige Markdown file met ingesloten Mermaid-diagram.

    :param metadata: Dict met metadata (eventueel gefilterd op ensemble)
    :param output_file: Pad naar de .md file
    :param title: Titel bovenaan de Markdown-bestand
    """
    mermaid_lines = ["```mermaid", "graph TD"]

    for data in metadata.values():
        name = data["table_name"]
        pattern = data.get("pattern", "")

        if pattern == "sat":
            style = 'fill:#fffacc,stroke:#333,stroke-width:1px'
        elif pattern == "link":
            style = 'fill:#cfe2ff,stroke:#333,stroke-width:1px'
        else:
            style = 'fill:#ffffff,stroke:#333,stroke-width:1px'

        mermaid_lines.append(f'{name}["{name}"]')
        mermaid_lines.append(f'style {name} {style}')

    for data in metadata.values():
        table = data["table_name"]
        pattern = data.get("pattern", "")
        pk = data.get("pk", "")
        fk_list = data.get("fk", [])

        if pattern == "sat":
            for hub in metadata.values():
                if hub.get("pattern") == "hub" and hub.get("pk") == pk:
                    mermaid_lines.append(f'{hub["table_name"]} --> {table}')
        elif pattern == "link":
            for fk in fk_list:
                for hub in metadata.values():
                    if hub.get("pattern") == "hub" and hub.get("pk") == fk:
                        mermaid_lines.append(f'{hub["table_name"]} --> {table}')

    mermaid_lines.append("```")

    # Markdown met titel + Mermaid
    markdown = [f"# {title}", "", *mermaid_lines]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown))

    print(f"✅ Markdown met Mermaid ERD opgeslagen in: {output_file}")


    # Save
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(mermaid_lines))

    print(f"✅ Mermaid ERD opgeslagen in: {output_file}")
