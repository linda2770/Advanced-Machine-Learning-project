train.py is python file for training model
model.py includes the methods to convert data to tensorflow format and preprocessing as well as model
ourtext_database.py contains all the outcome data
graphics.ipynb shows the graphs of outcome
AML-project.pdf is our final report

Because we trained our model on the terminal, we only show the best model structure here. The comparison between models can be
found in graphics.ipynb

Dataset:
Download SVHN Dataset format 1 (http://ufldl.stanford.edu/housenumbers/)
Extract them to data folder

Usage:
1.Convert to TFRecords format
python model.py --data_dir ./data

2.Train
python train.py --data_dir ./data --train_logdir ./logs/train

