import sys
from textgenrnn import textgenrnn

# Script to train neural network on data in given weights file with given training data, specified in command line args (see usage comment)
if len(sys.argv) != 3:
    print('Usage:')
    print('python3 train-net.py <weights-file> <dataset-file>')
    print('Be careful! The given weights file *will* be overwritten!')
    exit()

# Open a textgenrnn using the given weights file
nn = textgenrnn(str(sys.argv[1])) 

# If you want to reset the weights to zero --> nn.reset()
# But be careful! This will overwrite the weights in the file given above

# Train the nn on given dataset for given epoch number
# Weights are saved after each epoch, so don't worry about terminating early
nn.train_from_file(str(sys.argv[2]), num_epochs=100)

# Optional force save --> nn.save('./weights/loverboy.hdf5')

# Example use case of generating a result from a trained network:
# v = nn.generate(return_as_list=True, max_gen_length=300)[0]
# print('train-net> ' + str(v))