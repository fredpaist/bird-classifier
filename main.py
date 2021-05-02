# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

from app.service.classifier_service import ClassifierService

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Disable Tensorflow logging

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    classifier = ClassifierService()
    classifier.main(start_time)
    print('Time spent: %s' % (time.time() - start_time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
