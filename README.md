### swift demangler python library using pipe (incomplete)

laurie wired wrote ghidra script but it is a slow approach because it starts new process for every demangling
so a faster approach is needed .compiling only demangler from swiftsource is not documented anywhere.
so swift forum suggested a pipe based method.this is it.

#### what is mangling/demangling
```
mangling means symbols are  converted to another form.
so demangling/normalizing is needed to programmatically access it or  understand it visually.
this is needed in reverse engineering executable binary .
```

### usage
```
import swiftdemangle
name = swiftdemangle.demangler().get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print ( "normalized = " , name )
```




