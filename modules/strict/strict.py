if command.endswith("stk"):
	print(crayons.yellow("warning: stack usage may cause buffer overflows!"))

if command == "callmacro":
	print(crayons.yellow("warning: macro may have unchecked errors!"))