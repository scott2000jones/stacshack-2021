from textgenrnn import textgenrnn

nn = textgenrnn('./weights/loverboy.hdf5')
# if you want to reset the weights to zero --> nn.reset()
nn.train_from_file('./datasets/loverboy.txt', num_epochs=100)
# nn.save('./weights/loverboy.hdf5')
v = nn.generate(return_as_list=True, max_gen_length=300)[0]
print('train-net> ' + str(v))