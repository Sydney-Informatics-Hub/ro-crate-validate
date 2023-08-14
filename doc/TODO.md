# RO-Crate validation notes


Spec https://www.researchobject.org/ro-crate/1.1/


## Structure 1

1.a ro-crate-metadata.json

MUST

* be called ro-crate-metadata.json
* be json-ld. // parse it
* be flattened
* be compacted

SHOULD

* have a context

the JSON-LD MUST

* have a root element 
* have an RO-Crate metadata file descriptor which is about -> root element

the root data entity MUST 

* MUST be a Dataset
* MUST have an id ending with /
* SHOULD have an id of ./
* SHOULD have an unambigious name
* SHOULD have a description
* datePublished - MUST have an ISO8610
* SHOULD link to a ContextualEntity
* MAY have a license URL

RO-Crate contents (ie the filesystem of the directory)

* not all contents need to be in the RO-Crate
* directories should be DataEntities of type Dataset
* files should be DataEntities of type File
* files and directories must have @ids which are relative or absolute paths

extra level of validation - check that files and directories exist, that encodings
and PRONOMs are correct

linting - check that the graph is internally consistent