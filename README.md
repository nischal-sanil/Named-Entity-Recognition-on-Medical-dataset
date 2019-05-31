# Named-Entity-Recognition-on-Medical-dataset

This repository is a part of an assignment submitted to SahiCareers.

The [scrap.py](https://github.com/nischal-sanil/Named-Entity-Recognition-on-Medical-dataset/blob/master/scrap.py) generates a dataset of patients queries which then can be used to perform named entity recognition for extracting key insights of the treatment such as medication name, dosage, etc.
Also, This repository implements a Named entity recognition using a CNN-LSTM model trained using the i2b2 dataset, which can be found [here](https://www.i2b2.org/). However, The dataset is not present in the repository as I2B2 has a strict Data use policy, but can be accessed by contacting and signing a Data use agreement. I2B2 are very quick with their response. 


![CNN-LSTM](https://github.com/nischal-sanil/Named-Entity-Recognition-on-Medical-dataset/blob/master/Named-Entity-Recognition-BidirectionalLSTM-CNN-CoNLL/model.png)


The data from the I2B2 has to be converted suitable for LSTM model, which is done by the [parser.ipynb](https://github.com/nischal-sanil/Named-Entity-Recognition-on-Medical-dataset/blob/master/i2b2_2009-to-CoNLL/parser.ipynb), present in the [i2b2_2009-to-CoNLL](https://github.com/nischal-sanil/Named-Entity-Recognition-on-Medical-dataset/tree/master/i2b2_2009-to-CoNLL) directory.
After 30 epochs of training the model has achieved [84.69%](https://github.com/nischal-sanil/Named-Entity-Recognition-on-Medical-dataset/blob/master/Named-Entity-Recognition-BidirectionalLSTM-CNN-CoNLL/30_0.5_0.25_200_3_0.0105_Nadam.txt), which can be further improved by hyperparameter tuning.
The annotations Include:
1. medication name and its offset (marker “m”)
2. dosage and its offset (marker “do”)
3. mode/route of administration and its offset (marker “mo”)
4. frequency and its offset (marker “f”)
5. duration and its offset (marker “du”)
6. reason and its offset (marker “r”)
7. event (marker “e”)
8. temporal marker (marker “t”)
9. certainty (marker “c”)
10. found in list/narrative of the text (marker “ln”)

The training logs and sample output is present in the [LSTM.ipynb](https://github.com/nischal-sanil/Named-Entity-Recognition-on-Medical-dataset/blob/master/Named-Entity-Recognition-BidirectionalLSTM-CNN-CoNLL/LSTM.ipynb). 
