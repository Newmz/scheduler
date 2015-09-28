README

1. Commentary on design decisions

On Python:
	Python is a very.. interesting language. The language itself does not explicitly define many data
	structures and there is no restriction in terms of making class variables private or inaccessible.
	I tried to keep my seperate classes, well, seperate, by including variable accessors and not
	directly accessing the variables themselves. Furthermore, there is not any explicit passing of
	parameters by reference or by value - Python has its own peculiar way of handling its function 
	parameters. It calls them "by object-reference"... Essentially, Python is a strongly-typed 
	language, and each of its types isn't necesarily a type - every variable is really a pointer to 
	some object that knows its type. What this means, in conjunction with public classes,
	is that any function I write for one class can work directly with the parameters and members 
	or any other class that I include. Which scares me. I tried to keep them more or less seperate.
	more reading: 
	https://www.jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/

	If I was working in, say, c++, the list of shifts for an employee would have been a stack, and 
	instead of the shift having a member that is the name of its employee, I merely would have 
	added a pointer to an Employee object which would be the person assigned to that shift. My 
	decision to write this application in Python coincides with my mentoring of a course taught in 
	Python; I am more comfortable working in the context of a statically-typed, lower-level language
	like c++ or c. This has been an informative project so far in learning how classes and "variables"
	interact in python. If everything continues to go smoothly, I will add (or try to add) a UI so 
	that it is much easier for someone to use this application. That will be a hefty project but 
	also an invaluable experience.

