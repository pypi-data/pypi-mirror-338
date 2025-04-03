# DBT - AutomateDV ERD generator

This Python project scans an AutomateDV local repository of SQL templates, extracts metadata (e.g., keys, tags, structure), and can automatically generate:

- A basis Entity-Relationship Diagram (ERD) as a `.png`
- A SQL query framework joining an ensemble (hub / sat / link) together

Ensembles are identified by the tags in the AutomateDV templates

# Setup
First, install Graphviz from https://graphviz.org/
Second, install Graphviz package: pip install graphviz
Finally, install OVM_ERD: pip install ovm-erd

Test the installation by running: python -m ovm_erd --help

# Execution
## CLI
    python -m ovm_erd graphviz --path C:/Local_repository --ensemble example

    python -m ovm_erd sql --path C:/Local_repository --ensemble example

## API
    from ovm_erd.erd_sql import erd_sql
    erd_sql(path="...", ensemble="...")
    
    
    from ovm_erd import erd_graphviz
    erd_graphviz(path="...", ensemble="...")



