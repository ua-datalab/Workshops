# Time Series Forecasting 
Time Series Forecasting teaching material for data-lab worksop series.

![Example of financial data forcasting](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/lstm_output.png "LSTM output example")

# Presentation - [Click Here](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/presentation/timeseries-forecasting.pptx)

# Zoom Link - Pending

# Problem Illustration
Given a sequence of data-points, we must predict what comes next.

![problem illustration](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/problem_illustration.png "Problem Illustration")

# Problem Formalization
Let us look at how we formalize this problem with some notations. 

![problem formalization](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/problem_formalization.png "Problem Formalization")

# Prediction Accuracy
It is important to calculate how well your model is doing by messauring the error.
Several specific ways can be used with the most common being MAPE(Mean Absolute Prediction Error) and MSPE(Mean Square Prediction Error).

![Prediction error](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/accuray1.png "prediction errors")

# Landscape of forecasting models
We can divide these models into 2 broad types - linear and non-linear. 
Linear model comprise of techniques like auto-regression while neural network based approaches make up non-linear methods.

![Model landscape](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/forecasting_options.png "forecasting options")

* LASSO - Form of penalized regression. Least Absolute Shrinkage and Selection Operator
* RNN - Recurrent Neural Networks
* LSTM - Long-Short Term Memory Networks.
* GRU - Gate Recurrent Unit

# RNN vs Feed-Forward networks
RNN use information from the previous interation in the current iteration. Loop for the cyclic connections.

![rnn_vs_feedforward](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/feedforward_vs_rnn.png "RNN vs feed foarward")

# Annotated LSTM

![annotated LSTM](https://github.com/nextgensh/datalab-teaching-timeseries/blob/bbc3935b1b618e6034261af665ea0fce0f59d75c/figures/annotated_lstm.png "Annotated LSTM")

# Further Reading 

* (Probabilistic time series forecasting with transformers and hugging face. State of the Art)[https://huggingface.co/blog/time-series-transformers]
* (IBM - RNN explaination)[https://www.ibm.com/topics/recurrent-neural-networks]
* (Complete technical explaination of LSTM)[https://medium.com/analytics-vidhya/lstms-explained-a-complete-technically-accurate-conceptual-guide-with-keras-2a650327e8f2]
* (InDepth blog on developing LSTM networks for time-series forecasting)[https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/]
* (Masini, Ricardo P., Marcelo C. Medeiros, and Eduardo F. Mendes. "Machine learning advances for time series forecasting." Journal of economic surveys 37.1 (2023): 76-111.)[https://onlinelibrary.wiley.com/doi/abs/10.1111/joes.12429]
