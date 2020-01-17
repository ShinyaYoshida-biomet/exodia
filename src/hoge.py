import exodia
import inspect
from collections import defaultdict

array = []
hoge = defaultdict()
for name, member in inspect.getmembers(exodia):
    if name != "Duel" :
        hoge[member.name] = member
    if inspect.isclass(member):
        array.append("%s" % name)

array
from exodia import  *
hoge = defaultdict()
for k in array :
    hoge[f"{k}.name"] = k.name

hoge
exodia.Duel.name
