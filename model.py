import tensorflow as tf
import json
class Meta(object):
    def __init__(self):
        self.num_train_examples = None
        self.num_val_examples = None
        self.num_test_examples = None

    def save(self, path_to_json_file):
        with open(path_to_json_file, 'w') as f:
            content = {
                'num_examples': {
                    'train': self.num_train_examples,
                    'val': self.num_val_examples,
                    'test': self.num_test_examples
                }
            }
            json.dump(content, f)

    def load(self, path_to_json_file):
        with open(path_to_json_file, 'r') as f:
            content = json.load(f)
            self.num_train_examples = content['num_examples']['train']
            self.num_val_examples = content['num_examples']['val']
            self.num_test_examples = content['num_examples']['test']
class Donkey(object):
    @staticmethod
    def _preprocess(image,downsampling=54):
        image = tf.image.convert_image_dtype(image, dtype=tf.float32)
        image = tf.multiply(tf.subtract(image, 0.5), 2)
        image = tf.reshape(image, [64, 64, 3])
        image = tf.random_crop(image, [downsampling, downsampling, 3])
        return image

    @staticmethod
    def _read_and_decode(filename_queue,digit_size=5):
        reader = tf.TFRecordReader()
        _, serialized_example = reader.read(filename_queue)
        features = tf.parse_single_example(
            serialized_example,
            features={
                'image': tf.FixedLenFeature([], tf.string),
                'length': tf.FixedLenFeature([], tf.int64),
                'digits': tf.FixedLenFeature([digit_size], tf.int64)
            })

        image = Donkey._preprocess(tf.decode_raw(features['image'], tf.uint8))
        length = tf.cast(features['length'], tf.int32)
        digits = tf.cast(features['digits'], tf.int32)
        return image, length, digits

    @staticmethod
    def build_batch(path_to_tfrecords_file, num_examples, batch_size, shuffled):
        assert tf.gfile.Exists(path_to_tfrecords_file), '%s not found' % path_to_tfrecords_file

        filename_queue = tf.train.string_input_producer([path_to_tfrecords_file], num_epochs=None)
        image, length, digits = Donkey._read_and_decode(filename_queue)

        min_queue_examples = int(0.4 * num_examples)
        if shuffled:
            image_batch, length_batch, digits_batch = tf.train.shuffle_batch([image, length, digits],
                                                                             batch_size=batch_size,
                                                                             num_threads=2,
                                                                             capacity=min_queue_examples + 3 * batch_size,
                                                                             min_after_dequeue=min_queue_examples)
        else:
            image_batch, length_batch, digits_batch = tf.train.batch([image, length, digits],
                                                                     batch_size=batch_size,
                                                                     num_threads=2,
                                                                     capacity=min_queue_examples + 3 * batch_size)
            print image_batch
            print length_batch
            print digits_batch
        return image_batch, length_batch, digits_batch
    
class Model(object):               
    @staticmethod
    def inference(x, drop_rate):       
        [f1,f2,f3,f4,f5,f6,f7]=[48,64,128,160,192,192,192]
        [k1,k2,k3,k4,k51,k52,k61,k62,k71,k72,k73]=[5,5,5,5,5,5,5,5,5,5,5]
        [p1,p2,p3,p4,p5,p6,p7]=[2,2,2,2,2,2,2]
        [ps1,ps2,ps3,ps4,ps5,ps6,ps7]=[2,1,2,1,2,1,2]
        dmf=4
        with tf.variable_scope('hidden1'):
            conv = tf.layers.conv2d(x, filters=f1, kernel_size=[k1, k1], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation, pool_size=[p1, p1], strides=ps1, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden1 = dropout
            print hidden1.get_shape()

        with tf.variable_scope('hidden2'):
            conv = tf.layers.conv2d(hidden1, filters=f2, kernel_size=[k2, k2], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation, pool_size=[p2, p2], strides=ps2, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden2 = dropout
            print hidden2.get_shape()

        with tf.variable_scope('hidden3'):
            conv = tf.layers.conv2d(hidden2, filters=f3, kernel_size=[k3, k3], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation, pool_size=[p3, p3], strides=ps3, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden3 = dropout
            print hidden3.get_shape()

        with tf.variable_scope('hidden4'):
            conv = tf.layers.conv2d(hidden3, filters=f4, kernel_size=[k4, k4], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation, pool_size=[p4, p4], strides=ps4, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden4 = dropout
            print hidden4.get_shape()

        with tf.variable_scope('hidden5'):
            conv = tf.layers.conv2d(hidden4, filters=f5, kernel_size=[k51, k51], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            conv = tf.layers.conv2d(activation, filters=f5, kernel_size=[k52, k52], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation1 = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation1, pool_size=[p5, p5], strides=ps5, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden5 = dropout
            print hidden5.get_shape()

        with tf.variable_scope('hidden6'):
            conv = tf.layers.conv2d(hidden5, filters=f6, kernel_size=[k61, k61], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            conv = tf.layers.conv2d(activation, filters=f6, kernel_size=[k62, k62], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation1 = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation1, pool_size=[p6, p6], strides=ps6, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden6 = dropout
            print hidden6.get_shape()

        with tf.variable_scope('hidden7'):
            conv = tf.layers.conv2d(hidden6, filters=f7, kernel_size=[k71, k71], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation = tf.nn.relu(norm)
            conv = tf.layers.conv2d(activation, filters=f7, kernel_size=[k72, k72], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation1 = tf.nn.relu(norm)
            conv = tf.layers.conv2d(activation1, filters=f7, kernel_size=[k73, k73], padding='same')
            norm = tf.layers.batch_normalization(conv)
            activation2 = tf.nn.relu(norm)
            pool = tf.layers.max_pooling2d(activation2, pool_size=[p7, p7], strides=ps7, padding='same')
            dropout = tf.layers.dropout(pool, rate=drop_rate)
            hidden7 = dropout
            print hidden7.get_shape()
            
        flatten = tf.reshape(hidden7, [-1, dmf * dmf * f7])
        with tf.variable_scope('hidden10'):
            dense = tf.layers.dense(flatten, units=3072, activation=tf.nn.relu)
            hidden10 = dense

        with tf.variable_scope('hidden11'):
            dense = tf.layers.dense(flatten, units=3072, activation=tf.nn.relu)
            hidden11 = dense

        with tf.variable_scope('digit_length'):
            dense = tf.layers.dense(hidden11, units=7)
            length = dense

        with tf.variable_scope('digit1'):
            dense = tf.layers.dense(hidden11, units=11)
            digit1 = dense

        with tf.variable_scope('digit2'):
            dense = tf.layers.dense(hidden11, units=11)
            digit2 = dense

        with tf.variable_scope('digit3'):
            dense = tf.layers.dense(hidden11, units=11)
            digit3 = dense

        with tf.variable_scope('digit4'):
            dense = tf.layers.dense(hidden11, units=11)
            digit4 = dense

        with tf.variable_scope('digit5'):
            dense = tf.layers.dense(hidden11, units=11)
            digit5 = dense

        length_logits, digits_logits = length, tf.stack([digit1, digit2, digit3, digit4, digit5], axis=1)
        return length_logits, digits_logits

    @staticmethod
    def loss(length_logits, digits_logits, length_labels, digits_labels):
        length_cross_entropy = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(labels=length_labels, logits=length_logits))
        digit1_cross_entropy = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(labels=digits_labels[:, 0], logits=digits_logits[:, 0, :]))
        digit2_cross_entropy = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(labels=digits_labels[:, 1], logits=digits_logits[:, 1, :]))
        digit3_cross_entropy = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(labels=digits_labels[:, 2], logits=digits_logits[:, 2, :]))
        digit4_cross_entropy = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(labels=digits_labels[:, 3], logits=digits_logits[:, 3, :]))
        digit5_cross_entropy = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(labels=digits_labels[:, 4], logits=digits_logits[:, 4, :]))
        loss = length_cross_entropy + digit1_cross_entropy + digit2_cross_entropy + digit3_cross_entropy + digit4_cross_entropy + digit5_cross_entropy
        return loss

class Evaluator(object):
    def __init__(self, path_to_eval_log_dir):
        self.summary_writer = tf.summary.FileWriter(path_to_eval_log_dir)

    def evaluate(self, path_to_checkpoint, path_to_tfrecords_file, num_examples, global_step):
        batch_size = 128
        num_batches = num_examples / batch_size
        needs_include_length = False

        with tf.Graph().as_default():
            image_batch, length_batch, digits_batch = Donkey.build_batch(path_to_tfrecords_file,
                                                                         num_examples=num_examples,
                                                                         batch_size=batch_size,
                                                                         shuffled=False)
            length_logits, digits_logits = Model.inference(image_batch, drop_rate=0.0)
            length_predictions = tf.argmax(length_logits, axis=1)
            digits_predictions = tf.argmax(digits_logits, axis=2)

            if needs_include_length:
                labels = tf.concat([tf.reshape(length_batch, [-1, 1]), digits_batch], axis=1)
                predictions = tf.concat([tf.reshape(length_predictions, [-1, 1]), digits_predictions], axis=1)
            else:
                labels = digits_batch
                predictions = digits_predictions

            labels_string = tf.reduce_join(tf.as_string(labels), axis=1)
            predictions_string = tf.reduce_join(tf.as_string(predictions), axis=1)

            accuracy, update_accuracy = tf.metrics.accuracy(
                labels=labels_string,
                predictions=predictions_string
            )

            tf.summary.image('image', image_batch)
            tf.summary.scalar('accuracy', accuracy)
            tf.summary.histogram('variables',
                                 tf.concat([tf.reshape(var, [-1]) for var in tf.trainable_variables()], axis=0))
            summary = tf.summary.merge_all()

            with tf.Session() as sess:
                sess.run([tf.global_variables_initializer(), tf.local_variables_initializer()])
                coord = tf.train.Coordinator()
                threads = tf.train.start_queue_runners(sess=sess, coord=coord)

                restorer = tf.train.Saver()
                restorer.restore(sess, path_to_checkpoint)

                for _ in xrange(num_batches):
                    sess.run(update_accuracy)

                accuracy_val, summary_val = sess.run([accuracy, summary])
                self.summary_writer.add_summary(summary_val, global_step=global_step)

                coord.request_stop()
                coord.join(threads)

        return accuracy_val
