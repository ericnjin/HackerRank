sex =["C","CPP","JAVA","PYTHON","PERL","PHP","RUBY","CSHARP","HASKELL","CLOJURE","BASH","SCALA","ERLANG","CLISP","LUA","BRAINFUCK","JAVASCRIPT","GO","D","OCAML","R","PASCAL","SBCL","DART","GROOVY","OBJECTIVEC"]
n = int(raw_input())
for i in range(n):
  s,y = [j for j in raw_input().split()]
  if y in sex:
    print "VALID"
  else:
    print "INVALID"
