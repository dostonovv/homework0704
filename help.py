from parse import parse

# "/u/id/name" -> "/u/1/aa" -> id = 1, name = aa


parsed = parse("/u/{id}/{name}", "/")

print(parsed)