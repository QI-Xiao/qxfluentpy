import pickle
import nester

man=['3432',23432,'dfsawerdrg']
try:
    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man,man_file)
except IOError as err:
    print('error'+ err)
except pickle.PickleError as perr:
    print('perror'+ str(perr))

new_man = []
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('file error' + err)
except pickle.PickleError as perr:
    print('pickling error' + str(perr))

nester.judge(new_man)


