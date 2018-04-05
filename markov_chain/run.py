from markov_python.cc_markov import MarkovChain as mc

mc_first = MarkovChain()

f = mc.add_file("test_text.rtf")

g = generate_text(f)

print (g)