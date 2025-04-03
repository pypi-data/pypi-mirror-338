from ovm_erd.erd_sql import erd_sql

erd_sql(path="C:/Temp/datavault-layer", ensemble="activity")


from ovm_erd import erd_graphviz

a= "C:/Temp/datavault-layer"

erd_graphviz(path=a, ensemble="activity")


# python -m ovm_erd sql --path C:/Temp/datavault-layer --ensemble activity
# python -m ovm_erd graphviz --path C:/Temp/datavault-layer --ensemble ferry