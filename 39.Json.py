#****************** Json**************use to creat API********
#**************maily use to storing and transferring data b/w brower and the server.
#*********** json support string, number, boolean, null, object, array
import json
dr={"name":"anil","mobile":"8954060915"}
f=json.dumps(dr)
print(f)
print(type(f))