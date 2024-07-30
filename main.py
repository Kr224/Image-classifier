import tensorflow as tf
from utils.data_loader import load_data
from models.cnn_model import create_cnn_model
import matplotlib.pyplot as plt

# Load data
(train_images, train_labels), (test_images, test_labels) = load_data()

# Create model
model = create_cnn_model()

# Compile model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train model
history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))

# Evaluate model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print("\nTest accuracy:", test_acc)

# Plot training & validation accuracy values
plt.figure(figsize=(12, 8))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch', fontsize=14)
plt.ylabel('Accuracy', fontsize=14)
plt.ylim([0, 1])
plt.legend(loc='lower right', fontsize=12)
plt.title('Training and Validation Accuracy', fontsize=16)
plt.grid(True)
plt.savefig('training_validation_accuracy.png', dpi=300)  # Save with high resolution
plt.show()
