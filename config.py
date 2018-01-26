import os


GOAL = 30
DELAY = 4

VISION_W = 1  # less than 7
VISION_F = 21  # less than 70
VISION_B = 14  # less than 30

VISUALENABLED = False
DLAGENTENABLED = True

CONSTANT_PENALTY = 0  # 0.00005

EMERGENCY_BRAKE_MAX_SPEED_DIFF = 20
EMERGENCY_BRAKE_PENALTY = 0

MISMATCH_ACTION_PENALTY = 0

MAX_MEM = 1000000
MAX_EPISODE = 3  # 2000
MAX_FRAME_COUNT = 1000 * DELAY
TESTING_EPISODE = 3  # 200

LEARNING_RATE = float(os.environ.get('LEARNING_RATE', 5e-5))
BATCH_SIZE = int(os.environ.get('BATCH_SIZE', 32))
EPSILON_GREEDY_START_PROB = 1.0
EPSILON_GREEDY_END_PROB = 0.1
EPSILON_GREEDY_MAX_STATES = 1000 * 2000
EPSILON_GREEDY_TEST_PROB = 0.05
TARGET_NETWORK_UPDATE_FREQUENCY = 10000
LEARN_START = 32  # 100000

ROUND = int(os.environ.get('ROUND', 1))

IDENTIFIER = os.environ.get('IDENTIFIER', 'CV')

MODEL_NAME = '{}_R{}__DQN__lr={}_input=36-3_conv=2_FC=2_nn=100-5_batch={}'\
    .format(IDENTIFIER, ROUND, LEARNING_RATE, BATCH_SIZE)

ROAD_VIEW_OFFSET = 1010
INPUT_VIEW_OFFSET_X = 1405
INPUT_VIEW_OFFSET_Y = 480
