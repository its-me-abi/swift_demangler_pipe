### swift demangler python library

what is mangling/demangling
```
mangling means symbouls are  converted to another form.
so demangling/normalizing is needed to programmatically access it or  understand it visually.
this is needed in reverse engineering executable binary .
for example 
   to understand api calls in macho binary of IOS we should demangle it.
```

### usage
```
name = demangler().get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print ( "normalized = " , name )
```




