import numpy
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def main(params,label):
    dataset = numpy.genfromtxt('voice.csv',delimiter=",",names=True,dtype=None)
    lista = []
    lista_nazw = []
    for i in range(len(dataset)):
        new_elem = []
        new_elem.append(dataset[i][0])
        new_elem.append(dataset[i][1])
        new_elem.append(dataset[i][2])
        new_elem.append(dataset[i][3])
        new_elem.append(dataset[i][4])
        new_elem.append(dataset[i][5])
        new_elem.append(dataset[i][6])
        new_elem.append(dataset[i][7])
        new_elem.append(dataset[i][10])
        lista_nazw.append(dataset[i][-1])
        lista.append(new_elem)
    print(lista[0])
    lista = numpy.asarray(lista)
    lista_nazw = numpy.asarray(lista_nazw)
    test_size = 0.33
    seed = 7
    X_tr, X_te, Y_tr, Y_te = train_test_split(lista,lista_nazw, test_size=test_size,random_state = seed)
    model = XGBClassifier()
    model.fit(lista,lista_nazw)
    params2 = []
    params2.append(params)
    params = numpy.asarray(params2)
    y_pred = model.predict(params)
    print(y_pred)
    print(label)
    # predictions = [value for value in y_pred]
    #
    # accuracy = accuracy_score(Y_te,predictions)
    # print(accuracy*100)

if __name__ == '__main__':
    main()