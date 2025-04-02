import ast
import logging
import os
import re

import cv2
import numpy as np
import requests
import tifffile as tiff
from sklearn.metrics import (accuracy_score, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                     MaxPooling2D)
from tensorflow.keras.models import Sequential, load_model
from tqdm import tqdm

logging.getLogger("tifffile").setLevel(logging.CRITICAL)


class PickShot:

    """
    Class for processing images and making predictions using a loaded model.

    Attributes:
        name (str): The name of the model.
        model_storage: The loaded model used for predictions.
        _image_shape (tuple): The target shape to which images will be resized before prediction.
    """

    def __init__(self, name: str, model, target_size: tuple):
        self.name = name
        self.model_storage = model
        self._image_shape = target_size

    @classmethod
    def load(cls, file_path):
        """
        Loads a model from a file.

        Parameters:
            file_path (str): The path to the file containing the model.

        Returns:
            PickShot: A new PickShot object with the loaded model.

        Exceptions:
            FileNotFoundError: Raised if the file cannot be found at the specified path.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found!")

        tmp_model = load_model(file_path)

        basename = os.path.splitext(os.path.basename(file_path))[0]

        name = re.sub("_CNN.*", "", basename)

        target_size = re.sub(".*CNN_", "", basename)
        target_size = ast.literal_eval(target_size)

        return cls(name, tmp_model, target_size)

    @classmethod
    def download(cls, url: str, path_to_save=None):
        """
        Downloads a model from the internet and saves it to disk.

        Parameters:
            url (str): The URL from which the model will be downloaded.
            path_to_save (str, optional): The directory where the file will be saved (defaults to the current working directory).

        Returns:
            PickShot: A new PickShot object with the downloaded model.

        Exceptions:
            requests.exceptions.RequestException: Raised if an error occurs while downloading the file.
        """

        if path_to_save is None:
            path_to_save = os.getcwd()

        filename = os.path.join(path_to_save, os.path.basename(url))

        try:
            response = requests.get(url, stream=True, timeout=180)
            response.raise_for_status()

            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            tmp_model = load_model(filename)

            basename = os.path.splitext(os.path.basename(filename))[0]

            name = re.sub("_CNN.*", "", basename)

            target_size = re.sub(".*CNN_", "", basename)
            target_size = ast.literal_eval(target_size)

            return cls(name, tmp_model, target_size)

        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")

    def _load_and_preprocess_image(self, img_path):
        ext = os.path.splitext(img_path)[-1].lower()

        if ext in [".tif", ".tiff"]:
            img = tiff.imread(img_path)
        elif ext in [".jpg", ".jpeg", ".png", ".bmp"]:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            raise ValueError(f"Unsupported image format: {ext}")

        if len(img.shape) == 3 and img.shape[-1] > 3:
            img = img[:, :, :3]
        elif len(img.shape) == 2:
            img = np.stack([img] * 3, axis=-1)

        img_resized = cv2.resize(img, self._image_shape)

        img_resized = img_resized / 255.0

        return np.expand_dims(img_resized, axis=0)

    def predict(self, path_to_images: str, ident_part: str, pred_value: float = 0.7):
        """
        Makes predictions for images in a given directory based on a part of their filenames.

        Parameters:
            path_to_images (str): The path to the directory containing the images.
            ident_part (str): A part of the filename used to identify relevant images.
            pred_value (float, optional): The threshold for the prediction (default is 0.7).

        Returns:
            dict: A dictionary containing image IDs and their corresponding predictions ("pass" or "drop").
        """

        img_list = os.listdir(path_to_images)

        img_list = [x for x in img_list if ident_part.upper() in x.upper()]

        img_list = [os.path.join(path_to_images, file) for file in img_list]

        images_dict = {"images_ids": [], "prediciton": []}

        for file in tqdm(img_list):
            img = self._load_and_preprocess_image(file)

            prediction = self.model_storage.predict(img)[0][0]

            images_dict["images_ids"].append(
                int(re.sub("_.*", "", os.path.basename(file)))
            )

            images_dict["prediciton"].append(
                "pass" if prediction > pred_value else "drop"
            )

        return images_dict


class TrainingModel:

    """
    Class for training a convolutional neural network model for image classification.

    Attributes:
        _image_shape (tuple): Target shape for input images (default (50, 50)).
        _drop_images (list): List of image paths to be excluded from training.
        _save_images (list): List of image paths to be included in training.
        _train_paths (list): Paths of training images.
        _train_labels (list): Labels for training images.
        _test_paths (list): Paths of testing images.
        _test_labels (list): Labels for testing images.
        test_size_val (float): Proportion of data used for testing (default 0.2).
        activation (str): Activation function used in the model (default 'relu').
        model_storage: The trained model.
        epochs_val (int): Number of training epochs (default 10).
        batch_size_val (int): Batch size used during training (default 32).
        model_stats (dict): Dictionary holding performance metrics.
    """

    def __init__(self):
        self._image_shape = (50, 50)
        self._drop_images = []
        self._save_images = []
        self._train_paths = []
        self._train_labels = []
        self._test_paths = []
        self._test_labels = []
        self.test_size_val = 0.2
        self.activation = "relu"
        self.model_storage = None
        self.epochs_val = 10
        self.batch_size_val = 32
        self.model_stats = {
            "Accuracy": None,
            "Precision": None,
            "Recall": None,
            "F1-Score": None,
        }

    @property
    def image_shape(self):
        """
        Returns the shape of the input images.
        """

        return self._image_shape

    @image_shape.setter
    def image_shape(self, value):
        """
        Sets the shape of the input images.

        Parameters:
            value (tuple): Shape of the images.

        Raises:
            ValueError: If value is not a tuple.
        """

        if not isinstance(value, tuple):
            raise ValueError("Image_shape must be a tuple eg. (50,50)")
        self._image_shape = value

    @property
    def test_size(self):
        """
        Returns the test size for splitting data.
        """

        return self._image_shape

    @test_size.setter
    def test_size(self, value):
        """
        Sets the test size for splitting data.

        Parameters:
            value (float): Test size as a float.

        Raises:
            ValueError: If value is not a float.
        """

        if not isinstance(value, float):
            raise ValueError("Test_size must be a float")
        self.test_size_val = value

    @property
    def activation_fun(self):
        """
        Returns the activation function used in the model.
        """

        return self.activation

    @activation_fun.setter
    def activation_fun(self, value):
        """
        Sets the activation function.

        Parameters:
            value (str): Name of the activation function.

        Raises:
            ValueError: If value is not a string.
        """

        if not isinstance(value, str):
            raise ValueError("Activation function must be a string")
        self.activation = value

    @property
    def epochs(self):
        """
        Returns the number of epochs for training.
        """

        return self.epochs_val

    @epochs.setter
    def epochs(self, value):
        """
        Sets the number of epochs for training.

        Parameters:
            value (int): Number of epochs.

        Raises:
            ValueError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise ValueError("Epochs must be an integer")
        self.epochs_val = value

    @property
    def batch_size(self):
        """
        Returns the batch size used during training.
        """

        return self.batch_size_val

    @batch_size.setter
    def batch_size(self, value):
        """
        Sets the batch size for training.

        Parameters:
            value (int): Batch size.

        Raises:
            ValueError: If value is not an integer.
        """

        if not isinstance(value, int):
            raise ValueError("Batch size must be an integer")
        self.batch_size_val = value

    def get_notes(self):
        """
        Prints and returns the model's performance metrics.

        Returns:
            dict: A dictionary of the model's performance metrics (Accuracy, Precision, Recall, F1-Score).
        """

        print(f"Accuracy: {self.model_stats['Accuracy']:.4f}")
        print(f"Precision: {self.model_stats['Precision']:.4f}")
        print(f"Recall: {self.model_stats['Recall']:.4f}")
        print(f"F1-Score: {self.model_stats['F1-Score']:.4f}")

        return self.model_stats

    def images_paths(self, images_to_drop: list, images_to_save: list):
        """
        Validates and sets the paths for images to be dropped and saved for training.

        Parameters:
            images_to_drop (list): List of image paths to exclude.
            images_to_save (list): List of image paths to include.
        """

        images_to_drop_exist = []
        images_to_save_exist = []

        for p in images_to_drop:
            if os.path.isfile(p):
                images_to_drop_exist.append(p)
            else:
                print(f"The path {p} does not exist. It was removed for analysis!")

        for p in images_to_save:
            if os.path.isfile(p):
                images_to_save_exist.append(p)
            else:
                print(f"The path {p} does not exist. It was removed for analysis!")

        self._drop_images = images_to_drop_exist
        self._save_images = images_to_save_exist

    def _load_and_preprocess_image(self, img_path):
        ext = os.path.splitext(img_path)[-1].lower()

        if ext in [".tif", ".tiff"]:
            img = tiff.imread(img_path)
        elif ext in [".jpg", ".jpeg", ".png", ".bmp"]:
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            raise ValueError(f"Unsupported image format: {ext}")

        if len(img.shape) == 3 and img.shape[-1] > 3:
            img = img[:, :, :3]
        elif len(img.shape) == 2:
            img = np.stack([img] * 3, axis=-1)

        img_resized = cv2.resize(img, self._image_shape)

        img_resized = img_resized / 255.0

        return np.expand_dims(img_resized, axis=0)

    def _model_create(self):
        model = Sequential()

        model.add(
            Conv2D(
                32,
                (3, 3),
                activation=self.activation,
                input_shape=(self._image_shape[0], self._image_shape[1], 3),
            )
        )
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3), activation=self.activation))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(128, (3, 3), activation=self.activation))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())

        model.add(Dense(128, activation=self.activation))
        model.add(Dropout(0.5))
        model.add(Dense(1, activation="sigmoid"))

        model.compile(
            optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
        )

        self.model_storage = model

    def _data_prepare(self):
        image_paths = self._drop_images + self._save_images
        labels = len(self._drop_images) * [0] + len(self._save_images) * [1]

        train_paths, test_paths, train_labels, test_labels = train_test_split(
            image_paths, labels, test_size=self.test_size_val, random_state=42
        )

        self._train_paths = train_paths
        self._train_labels = train_labels
        self._test_paths = test_paths
        self._test_labels = test_labels

    def _train_model(self):
        train_images = np.vstack(
            [self._load_and_preprocess_image(path) for path in self._train_paths]
        )
        train_labels = np.array(self._train_labels)

        self.model_storage.fit(
            train_images,
            train_labels,
            epochs=self.epochs_val,
            batch_size=self.batch_size_val,
        )

    def _model_note(self):
        test_images = np.vstack(
            [self._load_and_preprocess_image(path) for path in self._test_paths]
        )
        test_labels = np.array(self._test_labels)

        test_predictions = self.model_storage.predict(test_images)
        test_predictions = (test_predictions > 0.5).astype(int)

        self.model_stats["Accuracy"] = accuracy_score(test_labels, test_predictions)
        self.model_stats["Precision"] = precision_score(test_labels, test_predictions)
        self.model_stats["Recall"] = recall_score(test_labels, test_predictions)
        self.model_stats["F1-Score"] = f1_score(test_labels, test_predictions)

    def train(self):
        """
        Runs the entire model training process.
        """

        self._model_create()
        self._data_prepare()
        self._train_model()
        self._model_note()

    def save_model(self, name: str, path=os.getcwd()):
        """
        Saves the trained model to a file.

        Parameters:
            name (str): The name for the saved model file.
            path (str): Directory path to save the model (defaults to current working directory).
        """

        model_path = os.path.join(
            path, f"{name}_CNN_{re.sub(' ', '', str(self._image_shape))}.h5"
        )
        self.model_storage.save(model_path)
