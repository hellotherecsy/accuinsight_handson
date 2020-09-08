from tensorflow import keras
import argparse
import numpy as np
from filestorage import custom_module

### Argument parser를 통해 하이퍼파라미터 설정
parser = argparse.ArgumentParser()
parser.add_argument('--num_nodes', type=int, default=128)
parser.add_argument('--learning_rate', type=float, default=0.01)
parser.add_argument('--batch_size', type=int, default=128)
args = parser.parse_args()

### 모델 실행에 필요한 데이터를 filestorage 폴더에 위치
train_images = np.load('filestorage/train_images.npy')
valid_images = np.load('filestorage/valid_images.npy')
train_labels = np.load('filestorage/train_labels.npy')
valid_labels = np.load('filestorage/valid_labels.npy')

train_images = train_images / 255.0
valid_images = valid_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(args.num_nodes, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

Adam = keras.optimizers.Adam(lr=args.learning_rate)

model.compile(optimizer=Adam,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, batch_size=args.batch_size, epochs=5)

test_loss, test_acc = model.evaluate(valid_images, valid_labels, verbose=2)

### AutoDL에서 평가 지표를 수집할 수 있도록 Metrics Collector의 metricsFormat에 맞추어 평가 지표를 출력
print('test_acc={:.4f}'.format(test_acc))