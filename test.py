from textgenrnn import textgenrnn

nn = textgenrnn()
v = nn.generate(return_as_list=True, max_gen_length=300)[0]

print('test> ' + str(v))