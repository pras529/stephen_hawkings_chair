import tensorflow as tf
from tensorflow.keras import layers, models

def create_model():
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(64,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, data, labels):
    model.fit(data, labels, epochs=10)

if __name__ == "__main__":
    model = create_model()
    # Example data
    data = tf.random.normal([100, 64])
    labels = tf.random.uniform([100], maxval=10, dtype=tf.int32)
    labels = tf.one_hot(labels, 10)
    train_model(model, data, labels)
