import numpy as np
import pandas as pd
import series_predictor
import csv
import utils
from matplotlib import pyplot as plt

def split_data(data, separator):
	train = data[:separator] 
	test = data[separator:]
	return train, test

def main():
	"""
		Main del proyecto, este archivo no es necesario, puede ser personalizado o incluso crear uno nuevo, este es simplemente el estilo del creador de este proyecto

		contiene la interacción de un usuario final con el proyecto. Mediante este archivo se leen los datos de un archivo .csv, se inicializan los hyperparámetros para la ejecución
		se invoca al proyecto para que entrene y realice las predicciones y se grafican los resultados


		#### Models ids ####
		# 0 -> LSTM
		# 1 -> Random Forest....................(only available for 1 time step)
		# 2 -> AdaBoost.........................(only available for 1 time step)
		# 3 -> SVM..............................(only available for 1 time step)
		# 4 -> Arima............................(only available for 1 time step)
	
		Se manjean 12 hyperparámetros principales
		- model -- Entero, el id del modelo que se va a utilizar (ver ids arriba)
		- parameters -- Booleano, indica si se va a hacer optimzación de parámetros
		- select -- Booleano, indica si se va a hacer selección de variables
		- original -- Booleano, indica si se va a entrenar con las variables originales o con las variables seleccionadas, True es con las originales (si select es True este es False automaticamente)
		- time_steps -- Entero, número de tiempos en el futuro que se van a predecir
		- max_vars -- Entero, número máximo de variables a ser seleccionadas por el algoritmo de selección de variables, si select es False, este parámetro no importa
		- verbosity -- Entero, número que indica el nivel de verbosidad de la ejecución, hasta 2 muestra gráficas, de ahí para arriba muestra *logs* de la ejecución
		- parameters_file_name -- String, nombre del archivo donde se va a guardar o cargar el modelo entrenado, si este parámetro es None, se utilizan los parámetros por *default*
		- MAX_EVALS -- Entero, número de iteraciones de la optimización bayesiana, si parameters es False este parámetro no importa
		- saved_model -- Booleano, indica si se desea entrenar el modelo o cargar uno guardado. Si True se carga un modelo guardado, si False se entrena un nuevo modelo.
		- model_file_name -- String, nombre del archivo donde se va a guardar y/o cargar el modelo entrenado, si saved_model es False este parámetro solo importa para guardar el modelo
		- returns -- Booleano, indica si se está trabajando con retornos o no (serie diferenciada). True es que si se trabaja con retornos.

		Hay 1 hyperparámetro adicional que es:
		- predicting -- Entero, id de la columna dentro del dataframe de la variable objetivo a predecir, para que en el caso que esta no sea la posición 0, se intercambie

	"""

	# Parameters
	model = 0 # id of model to use
	parameters = 0 # Set to True for performing bayes optimization looking for best parameters
	select = 1 # set to True for performing feature selection
	original = 0 # set to True for training with original data (not feature selected)
	time_steps = 5 # number of periods in the future to predict
	max_vars = 200 # maximum number of variables for taking in count for variable selection
	verbosity = 0 # level of logs
	parameters_file_name = 'parameters/camilo.pars' # 'parameters/default_lstm_%dtimesteps.pars' % time_steps
	MAX_EVALS = 50
	saved_model = False
	model_file_name = None # 'models/lstm-noSW-prueba.h5'
	returns = True
	# 0: algoritmo genetico, 1: simulated annealing, 2: stepwise selection
	variable_selection_method = 2

	# input_file_name = 'data/forecast-competition-complete.csv'
	# input_file_name = 'data/data_16_11_2018_differentiated.csv'
	input_file_name = 'data/data_16_11_2018.csv'
	# input_file_name = 'data/data_returns.csv'
	dataframe = pd.read_csv(input_file_name, header=0, index_col=0)
	df = pd.DataFrame()
	# output_file_name = 'results/salida_' + str(time_steps) + '_periodos.csv'
	output_file_name = 'results/salida_' + str(time_steps) + '_periodos_SPTR.csv'

	# choose the feature to predict
	predicting = 0
	cols = dataframe.columns
	predicting = cols[predicting]
	cols = set(cols)
	cols.remove(predicting)
	cols = [predicting] + list(cols)
	dataframe = dataframe[cols]

	out = dataframe.columns[0]
	mini = min(dataframe.loc[:,out].values)
	maxi = max(dataframe.loc[:,out].values)
	rango = maxi - mini

	p = []
	ini = 200
	fin = 225
	step = 1 # time_steps

	train, _ = split_data(dataframe.values, ini)

	predictor = series_predictor.Predictor(dataframe.values, model, original, time_steps, train, cols, parameters, select, max_vars, verbosity, parameters_file_name, MAX_EVALS, saved_model, model_file_name, returns, variable_selection_method)

	for i in range(ini, fin, step):
		print(i)
		train, test = split_data(dataframe.values, i)

		pred = predictor.predict(train[[-1]])

		actual = test[0:time_steps, 0]

		print('prediction:', pred)
		print('observation:', actual, end='\n\n')
		df = df.append(pd.Series([pred]), ignore_index=True)
		p.append(pred)
	
	datos = dataframe.values[ini:fin+min(step*2, 20)]
	# datos = dataframe.values[ini-time_steps:fin-time_steps]
	preds = np.array(p).ravel()
	tam = min(len(preds), len(datos))
	print('real rmse: ', utils.calculate_rmse(datos[:tam, 0], preds[:tam]))
	if(returns):
		print('real direction accuracy: %f%%' % (utils.get_returns_direction_accuracy(datos[:tam, 0], preds[:tam])*100))
	else:
		print('real direction accuracy: %f%%' % (utils.get_direction_accuracy(datos[:tam, 0], preds[:tam])*100))
	plt.plot(datos[:, 0], label='observations', lw=10, color='red')
	if(time_steps > 1):
		for i in range(len(p)):
			pad = [None for j in range(i*step)]
			plt.plot(pad + list(p[i]))#, color='blue')
	else:
		plt.plot(p, label='predictions')
		plt.legend()
	if(returns): plt.plot(np.zeros(len(datos)), color='black')
	plt.suptitle('Predictions vs Observations', fontsize=16)
	plt.show()

	df.columns=[out]
	df.to_csv(output_file_name)


if __name__ == '__main__':
	main()