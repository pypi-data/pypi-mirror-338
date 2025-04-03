from ovm_erd.repository_reader import (
    read_repository,
    build_metadata_dict
)

def generate_sql_query(metadata: dict, ensemble: str) -> str:
    """
    Genereert een SQL-query op basis van metadata voor een specifieke ensemble/tag.
    Verbindt hubs met sats en links via INNER JOINs.

    :param metadata: De volledige (gefilterde) metadata dictionary
    :param ensemble: De tag waarvoor de SQL-query gegenereerd wordt
    :return: Een SQL-query als string
    """
    filtered = {
        fn: d for fn, d in metadata.items()
        if ensemble in d.get("tags", [])
    }

    if not filtered:
        return f"-- ⚠️ No tables found for ensemble: {ensemble}"

    from_clause = []
    joins = []
    added = set()
    used_links = set()

    for data in filtered.values():
        name = data["table_name"]
        pattern = data.get("pattern", "")
        pk = data.get("pk", "")
        fk_list = data.get("fk", [])

        if pattern == "hub":
            from_clause.append(name)
            added.add(name)

            # JOIN met sats
            for sat_data in filtered.values():
                if sat_data.get("pattern") == "sat" and sat_data.get("pk") == pk:
                    sat = sat_data["table_name"]
                    joins.append(f"INNER JOIN {sat} ON {sat}.{pk} = {name}.{pk}")
                    added.add(sat)

            # JOIN met links (maar max 1x per link!)
            for link_data in filtered.values():
                if link_data.get("pattern") == "link" and pk in link_data.get("fk", []):
                    link = link_data["table_name"]
                    if link not in used_links:
                        joins.append(f"INNER JOIN {link} ON {link}.{pk} = {name}.{pk}")
                        used_links.add(link)
                        added.add(link)

    tables_used = from_clause + [j.split()[2] for j in joins]
    select_clause = ",\n    ".join([f"{t}.*" for t in tables_used])

    query = f"SELECT\n    {select_clause}\nFROM\n    {from_clause[0]}\n"
    if joins:
        query += "\n" + "\n".join(joins)

    return query



def erd_sql(path, ensemble, output_file="ovm_erd/output/sql_output.sql"):
    """
    Eén-regel functie voor CLI en Python om SQL-query te genereren uit metadata + ensemble.
    """
    files = read_repository(path)
    metadata = build_metadata_dict(files)

    sql = generate_sql_query(metadata, ensemble)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(sql)

    print(f"✅ SQL-query voor ensemble '{ensemble}' opgeslagen in: {output_file}")
