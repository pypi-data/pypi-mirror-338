# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# import warnings
# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Input,Embedding,Flatten,Dot,Dense,Concatenate
#
# warnings.filterwarnings("ignore")
# ratings = pd.read_csv("ratings.csv")
# ratings.info()
# num_users = ratings['userId'].nunique()
# num_movies = ratings['movieId'].nunique()
# user_ids = ratings['userId'].unique()
# movie_ids = ratings['movieId'].unique()
# user_to_index = {user_id: idx for idx,user_id in enumerate(user_ids)}
# movie_to_index = {movie_id: idx for idx,movie_id in enumerate(movie_ids)}
# ratings['user_index'] = ratings['userId'].map(user_to_index)
# ratings['movie_index']=ratings['movieId'].map(movie_to_index)
# x = ratings[['user_index','movie_index']]
# y=ratings['rating']
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
#
# def build_model(num_users,num_movies,embedding_size=50):
#     user_input = Input(shape=(1,))
#     user_embedding=Embedding(input_dim=num_users,output_dim=embedding_size)(user_input)
#     user_vec = Flatten()(user_embedding)
#     movie_input = Input(shape=(1,))
#     movie_embedding=Embedding(input_dim=num_movies,output_dim=embedding_size)(movie_input)
#     movie_vec = Flatten()(movie_embedding)
#     dot_product = Dot(axes=1)([user_vec,movie_vec])
#     output = Dense(1,activation='linear')(dot_product)
# model = Model(inputs=[user_input,movie_input],outputs = output)
# model.compile(optimizer='adam',loss='mean_squared_error')
# return model
# model = build_model(num_users,num_movies)
# history=model.fit([x_train['user_index'],x_train['movie_index']],y_train,epochs=
# 10,batch_size=64,validation_data=([x_test['user_index'],x_test['movie_index']],y_test))
# model.summary()
# loss = model.evaluate([x_test['user_index'],x_test['movie_index']],y_test)
# print(f'Test Loss:{loss}')
# import numpy as np
# user_index = 0
# movie_index = 0
# predicted_rating = model.predict([np.array([user_index]),np.array([movie_index])])
# print(f'Predicted Rating : {predicted_rating[0][0]}')